"""MNIST 숫자 이미지 예측 API 모듈

이 모듈은 업로드된 이미지에서 MNIST 숫자를 예측하는 FastAPI 라우터를 제공합니다.
"""

import os
import shutil
from datetime import datetime
from typing import Optional, Dict, Any, Tuple

import torch
import torch.nn as nn
from torch.nn import functional as F
import torchvision.transforms as transforms
from PIL import Image

from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

from database import Database 

class PredictionResponse(BaseModel):
    """예측 결과 응답 모델"""
    message: str
    predicted_class: Optional[int] = None
    probability: Optional[float] = None
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
    prefix="/predict",
    tags=["predict"],
    responses={404: {"description": "Not found"}}
)


class ImageClassifier(nn.Module):
    """MNIST 숫자 분류를 위한 간단한 신경망 모델"""
    
    def __init__(self, input_size: int = 28*28, hidden_size: int = 500, num_classes: int = 10):
        """모델 초기화
        
        Args:
            input_size: 입력 크기 (기본값: 784 = 28*28)
            hidden_size: 은닉층 크기 (기본값: 500)
            num_classes: 출력 클래스 수 (기본값: 10)
        """
        super(ImageClassifier, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, num_classes)
        self.dropout = nn.Dropout(0.2)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """순전파 수행
        
        Args:
            x: 입력 텐서
            
        Returns:
            예측 결과 텐서
        """
        # 이미지를 1차원 벡터로 평탄화
        x = x.reshape(-1, 28*28)
        x = self.fc1(x)
        x = self.relu(x)
        x = self.dropout(x)
        x = self.fc2(x)
        return x 
    
def _load_model(model_path: str = "mnist.pth") -> ImageClassifier:
    """훈련된 모델 로드
    
    Args:
        model_path: 모델 파일 경로
        
    Returns:
        로드된 모델
        
    Raises:
        HTTPException: 모델 파일을 찾을 수 없는 경우
    """
    try:
        model = ImageClassifier()
        model.load_state_dict(torch.load(model_path, map_location='cpu'))
        model.eval()
        return model
    except FileNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Model file '{model_path}' not found"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to load model: {str(e)}"
        )


def _preprocess_image(image: Image.Image) -> torch.Tensor:
    """이미지 전처리
    
    Args:
        image: PIL 이미지
        
    Returns:
        전처리된 텐서
    """
    transform = transforms.Compose([
        transforms.Resize((28, 28)),
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])
    
    image_tensor = transform(image)
    return image_tensor.unsqueeze(0)  # 배치 차원 추가


def _validate_image_file(file: UploadFile) -> None:
    """업로드된 이미지 파일 유효성 검사
    
    Args:
        file: 업로드된 파일
        
    Raises:
        HTTPException: 파일이 유효하지 않은 경우
    """
    if not file or not file.filename:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No file uploaded"
        )
    
    # 파일 크기 제한 (5MB)
    MAX_FILE_SIZE = 5 * 1024 * 1024
    if file.size and file.size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail="File size too large. Maximum 5MB allowed."
        )
    
    # 허용된 이미지 확장자
    ALLOWED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp'}
    file_ext = os.path.splitext(file.filename)[1].lower()
    if file_ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"File type not allowed. Allowed types: {', '.join(ALLOWED_EXTENSIONS)}"
        )


def predict_image(image_path: str) -> Tuple[int, float]:
    """이미지에서 MNIST 숫자 예측
    
    Args:
        image_path: 이미지 파일 경로
        
    Returns:
        예측된 클래스와 확률의 튜플
        
    Raises:
        HTTPException: 이미지 로드 또는 예측 실패 시
    """
    try:
        # 모델 로드
        model = _load_model()
        
        # 이미지 로드 및 전처리
        image = Image.open(image_path).convert('L')  # 흑백 변환
        image_tensor = _preprocess_image(image)
        
        # 예측 수행
        with torch.no_grad():
            output = model(image_tensor)
            probabilities = F.softmax(output, dim=1)
            predicted_class = torch.argmax(probabilities, dim=1)
            predicted_prob = probabilities[0][predicted_class].item()
            
        return predicted_class.item(), predicted_prob
        
    except FileNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Image file not found: {image_path}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Prediction failed: {str(e)}"
        )


@router.get("/", response_model=MessageResponse)
def predict_index() -> MessageResponse:
    """예측 API 상태 확인 엔드포인트"""
    return MessageResponse(msg="MNIST 숫자 예측 API")

@router.post("/upload", response_model=PredictionResponse)
def upload_and_predict(
    file: UploadFile = File(..., description="MNIST 숫자 이미지 파일"),
    title: str = Form(..., description="게시글 제목"),
    writer: str = Form(..., description="작성자"),
    contents: str = Form(..., description="게시글 내용"),
    settings: Dict[str, Any] = Depends(get_settings)
) -> PredictionResponse:
    """이미지 업로드 및 MNIST 숫자 예측
    
    Args:
        file: 업로드할 이미지 파일
        title: 게시글 제목
        writer: 작성자
        contents: 게시글 내용
        settings: 애플리케이션 설정
        
    Returns:
        예측 결과 및 파일 정보
    """
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
    
    # 파일 유효성 검사
    _validate_image_file(file)
    
    # 고유 파일명 생성
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_ext = os.path.splitext(file.filename)[1]
    unique_filename = f"{timestamp}_{file.filename}"
    
    file_location = os.path.join(settings["UPLOAD_DIRECTORY"], unique_filename)
    image_url = f"static/{unique_filename}"
    
    # 업로드 디렉터리 확인
    os.makedirs(settings["UPLOAD_DIRECTORY"], exist_ok=True)
    
    predicted_class = None
    predicted_prob = None
    
    try:
        # 파일 저장
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # 이미지 예측 수행
        predicted_class, predicted_prob = predict_image(file_location)
        
        # 데이터베이스에 저장
        sql = """
            INSERT INTO tb_board (title, writer, contents, filename, image_url, wdate, hit)
            VALUES (:title, :writer, :contents, :filename, :image_url, NOW(), 0)
        """
        
        with Database() as db_mgr:
            data = [{
                "title": title,
                "writer": writer,
                "contents": contents,
                "filename": unique_filename,
                "image_url": image_url
            }]
            db_mgr.execute(sql, data)
        
        return PredictionResponse(
            message="업로드 및 예측 완료",
            predicted_class=predicted_class,
            probability=round(predicted_prob, 4),
            filename=unique_filename,
            image_url=image_url
        )
        
    except Exception as e:
        # 에러 발생 시 업로드된 파일 정리
        if os.path.exists(file_location):
            os.remove(file_location)
        
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Upload and prediction failed: {str(e)}"
        )


@router.post("/predict-only", response_model=Dict[str, Any])
def predict_only(
    file: UploadFile = File(..., description="MNIST 숫자 이미지 파일")
) -> Dict[str, Any]:
    """이미지 예측만 수행 (데이터베이스 저장 없음)
    
    Args:
        file: 업로드할 이미지 파일
        
    Returns:
        예측 결과만 포함된 응답
    """
    _validate_image_file(file)
    
    # 임시 파일로 저장
    temp_filename = f"temp_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{file.filename}"
    temp_location = os.path.join("/tmp", temp_filename)
    
    try:
        with open(temp_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        predicted_class, predicted_prob = predict_image(temp_location)
        
        return {
            "predicted_class": predicted_class,
            "probability": round(predicted_prob, 4),
            "message": f"예측 결과: 숫자 {predicted_class} (확률: {predicted_prob:.4f})"
        }
        
    finally:
        # 임시 파일 정리
        if os.path.exists(temp_location):
            os.remove(temp_location)



