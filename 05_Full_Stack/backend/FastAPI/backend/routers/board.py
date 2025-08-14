from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from database import Database

router = APIRouter(
    prefix="/board",
    tags=["board"],
    responses={404: {"description": "Not found"}}
)


@router.get("/")
def board_index():
    """게시판 메인 페이지"""
    return {"msg": "게시판입니다"}


@router.get("/list")
def board_list():
    """게시판 목록 조회"""
    try:
        with Database() as db_mgr:
            sql = "SELECT * FROM tb_board ORDER BY id DESC"
            results = db_mgr.executeAll(sql)
        return {"list": results}
    except SQLAlchemyError as e:
        return JSONResponse(
            status_code=500,
            content={"msg": "게시판 목록 조회 실패", "error": str(e)}
        )


@router.post("/insert")
def board_insert(
    title: str = Body(..., description="게시글 제목"),
    writer: str = Body(..., description="작성자"),
    contents: str = Body(..., description="게시글 내용")
):
    """게시글 등록"""
    sql = """
        INSERT INTO tb_board (title, writer, contents, wdate, hit)
        VALUES (:title, :writer, :contents, NOW(), 0)
    """
    params = {"title": title, "writer": writer, "contents": contents}
    
    try:
        with Database() as db_mgr:
            db_mgr.execute(sql, params)
        return {"msg": "등록성공"}
    except SQLAlchemyError as e:
        return JSONResponse(
            status_code=500,
            content={"msg": "데이터 등록 실패", "error": str(e)}
        )
