import os
import shutil
from typing import Optional, List, Dict, Any
from datetime import datetime

from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from database import Database


class BoardResponse(BaseModel):
    """게시판 아이템 응답 모델"""
    id: int
    title: str
    writer: str
    wdate: str
    hit: int
    filename: Optional[str] = None
    image_url: Optional[str] = None
    contents: Optional[str] = None


class FileUploadResponse(BaseModel):
    """파일 업로드 응답 모델"""
    message: str
    filename: Optional[str] = None
    image_url: Optional[str] = None


class MessageResponse(BaseModel):
    """일반 메시지 응답 모델"""
    msg: str


# 의존성 주입을 위한 설정 컨테이너
settings_container = {}


def get_settings() -> Dict[str, Any]:
    """애플리케이션 설정 가져오기"""
    settings = settings_container.get("settings")
    if not settings:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Settings not configured"
        )
    return settings


router = APIRouter(
    prefix="/board",
    tags=["board"],
    responses={404: {"description": "Not found"}}
)

@router.get("/", response_model=MessageResponse)
def board_index() -> MessageResponse:
    """게시판 API 상태 확인 엔드포인트"""
    return MessageResponse(msg="접속성공")


@router.get("/list", response_model=Dict[str, List[BoardResponse]])
def get_board_list() -> Dict[str, List[BoardResponse]]:
    """모든 게시판 글 목록 가져오기"""
    sql = """
        SELECT id, title, writer, DATE_FORMAT(wdate, '%Y-%m-%d') as wdate,
               hit, filename, image_url 
        FROM tb_board
        ORDER BY id DESC
    """
    
    try:
        with Database() as db_mgr:
            results = db_mgr.executeAll(sql)
        
        if not results:
            return {"data": []}
            
        return {"data": results}
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )

def _validate_file(file: UploadFile) -> None:
    """업로드된 파일 유효성 검사"""
    # 파일 크기 검증 (10MB 제한)
    MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
    
    # 허용된 파일 확장자
    ALLOWED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'}
    
    if file.size and file.size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail="File size too large. Maximum 10MB allowed."
        )
    
    if file.filename:
        file_ext = os.path.splitext(file.filename.lower())[1]
        if file_ext not in ALLOWED_EXTENSIONS:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"File type not allowed. Allowed types: {', '.join(ALLOWED_EXTENSIONS)}"
            )


def _save_uploaded_file(file: UploadFile, upload_dir: str) -> tuple[str, str]:
    """업로드된 파일 저장 후 파일명과 이미지 URL 반환"""
    if not file or not file.filename:
        return "", ""
    
    # 파일 유효성 검사
    _validate_file(file)
    
    # 충돌 방지를 위한 고유 파일명 생성
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_ext = os.path.splitext(file.filename)[1]
    unique_filename = f"{timestamp}_{file.filename}"
    
    file_location = os.path.join(upload_dir, unique_filename)
    
    # 업로드 디렉터리가 존재하는지 확인
    os.makedirs(upload_dir, exist_ok=True)
    
    try:
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        return unique_filename, f"static/{unique_filename}"
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to save file: {str(e)}"
        )


@router.post("/insert", response_model=MessageResponse)
def create_board_post(
    title: str = Form(..., description="Post title"),
    writer: str = Form(..., description="Post writer"),
    contents: str = Form(..., description="Post contents"),
    file: Optional[UploadFile] = File(None, description="Optional image file"),
    settings: Dict[str, Any] = Depends(get_settings)
) -> MessageResponse:
    """선택적 파일 업로드와 함께 새 게시판 글 작성"""
    
    # 입력값 검증
    if not title.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Title cannot be empty"
        )
    
    if not writer.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Writer cannot be empty"
        )
    
    # 파일 업로드 처리
    filename, image_url = _save_uploaded_file(file, settings["UPLOAD_DIRECTORY"])
    
    # 데이터베이스에 삽입
    sql = """
        INSERT INTO tb_board (title, writer, contents, filename, image_url, wdate, hit)
        VALUES (:title, :writer, :contents, :filename, :image_url, NOW(), 0)
    """
    
    try:
        with Database() as db_mgr:
            data = [{
                "title": title.strip(),
                "writer": writer.strip(),
                "contents": contents.strip(),
                "filename": filename,
                "image_url": image_url
            }]
            db_mgr.execute(sql, data)
        
        return MessageResponse(msg="등록성공")
    
    except Exception as e:
        # 데이터베이스 삽입 실패 시 업로드된 파일 정리
        if filename:
            file_path = os.path.join(settings["UPLOAD_DIRECTORY"], filename)
            if os.path.exists(file_path):
                os.remove(file_path)
        
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to create post: {str(e)}"
        )


@router.get("/view/{post_id}", response_model=Dict[str, List[BoardResponse]])
def get_board_post(post_id: int) -> Dict[str, List[BoardResponse]]:
    """ID로 특정 게시판 글 가져오기"""
    if post_id <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid post ID"
        )
    
    sql = """
        SELECT id, title, writer, DATE_FORMAT(wdate, '%Y-%m-%d') as wdate,
               hit, filename, image_url, contents
        FROM tb_board
        WHERE id = :id
    """
    
    try:
        with Database() as db_mgr:
            data = [{"id": post_id}]
            results = db_mgr.executeAll(sql, data)
        
        if not results:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Post not found"
            )
        
        return {"data": results}
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )


@router.patch("/view/{post_id}/hit")
def increment_post_hit(post_id: int) -> MessageResponse:
    """게시글 조회수 증가"""
    if post_id <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid post ID"
        )
    
    sql = """
        UPDATE tb_board 
        SET hit = hit + 1 
        WHERE id = :id
    """
    
    try:
        with Database() as db_mgr:
            data = [{"id": post_id}]
            affected_rows = db_mgr.execute(sql, data)
        
        if affected_rows == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Post not found"
            )
        
        return MessageResponse(msg="조회수 증가 성공")
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )
