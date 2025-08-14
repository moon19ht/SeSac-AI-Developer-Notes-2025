from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from database import Database

router = APIRouter(
    prefix="/score",
    tags=["score"],
    responses={404: {"description": "Not found"}}
)


@router.get("/scoreList")
def get_score_list():
    """성적 목록 조회"""
    try:
        with Database() as db_mgr:
            sql = "SELECT * FROM tb_score ORDER BY id DESC"
            results = db_mgr.executeAll(sql)
        return {"scoreList": results}
    except SQLAlchemyError as e:
        return JSONResponse(
            status_code=500,
            content={"msg": "성적 목록 조회 실패", "error": str(e)}
        )


@router.post("/score/insert")
def score_insert(
    name: str = Body(..., description="학생 이름"),
    kor: int = Body(..., description="국어 점수"),
    eng: int = Body(..., description="영어 점수"),
    mat: int = Body(..., description="수학 점수")
):
    """성적 등록"""
    total = kor + eng + mat
    avg = round(total / 3, 2)
    
    sql = """
        INSERT INTO tb_score (name, kor, eng, mat, total, avg)
        VALUES (:name, :kor, :eng, :mat, :total, :avg)
    """
    params = {
        "name": name,
        "kor": kor,
        "eng": eng,
        "mat": mat,
        "total": total,
        "avg": avg
    }
    
    try:
        with Database() as db_mgr:
            db_mgr.execute(sql, params)
        return {"msg": "등록성공", "data": params}
    except SQLAlchemyError as e:
        return JSONResponse(
            status_code=500,
            content={"msg": "성적 등록 실패", "error": str(e)}
        )
