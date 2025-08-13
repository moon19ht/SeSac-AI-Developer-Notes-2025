from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# FastAPI 애플리케이션 초기화
app = FastAPI(title="Sample FastAPI", version="1.0.0")

# CORS(Cross-Origin Resource Sharing) 설정
# React 개발 서버(localhost:3000 등)와 통신하기 위해 필요합니다.
origins = [
    "http://127.0.0.1:5173",
    "http://localhost:5173",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용 (GET, POST, PUT, DELETE 등)
    allow_headers=["*"],  # 모든 HTTP 헤더 허용
)


@app.get("/", tags=["health"])  # 간단한 헬스체크 및 환영 메시지
def index():
    return {"message": "Hello FastAPI"}

#값받기 
# http://127.0.0.1:8000/add?x=4&y=8
@app.get("/add", tags=["math"])  # 쿼리 파라미터 이용
def add_query(x: int, y: int):
    return {"x": x, "y": y, "result": x + y}

# http://127.0.0.1:8000/add2/x/y
@app.get("/add2/{x}/{y}", tags=["math"])  # 경로 파라미터 이용
def add_path(x: int, y: int):
    return {"x": x, "y": y, "result": x + y}


# ====== 점수 도메인 스키마 ======

class ScoreIn(BaseModel):
    name: str = Field(..., min_length=1, description="이름")
    kor: int = Field(..., ge=0, le=100, description="국어 (0~100)")
    eng: int = Field(..., ge=0, le=100, description="영어 (0~100)")
    mat: int = Field(..., ge=0, le=100, description="수학 (0~100)")


class Score(ScoreIn):
    total: int
    avg: float


class ScoreListResponse(BaseModel):
    scoreList: List[Score]


def _compute_score(data: ScoreIn) -> Score:
    total = data.kor + data.eng + data.mat
    avg = total / 3

    # pydantic v1(dict) / v2(model_dump) 호환 처리
    def _to_dict(model: BaseModel) -> dict:
        return model.model_dump() if hasattr(model, "model_dump") else model.dict()

    return Score(**_to_dict(data), total=total, avg=avg)


# 더미데이터 (인메모리 저장)
score_list: List[Score] = [
    Score(name="홍길동", kor=100, eng=100, mat=100, total=300, avg=100),
    Score(name="임꺽정", kor=90, eng=90, mat=90, total=270, avg=90),
    Score(name="장길산", kor=80, eng=80, mat=80, total=240, avg=80),
]

@app.get("/scoreList", response_model=ScoreListResponse, tags=["scores"])  # 응답 스키마 명시
def get_score_list():
    # 디비에서 읽어오는 로직으로 대체 가능
    return {"scoreList": score_list}

@app.post("/score/insert", response_model=Score, tags=["scores"])  # 입력 스키마 사용 및 검증
def score_insert(payload: ScoreIn):
    score = _compute_score(payload)
    score_list.append(score)
    return score




# 실행방법 (예시)
# conda activate backend
# python -m uvicorn main:app --reload
# http://127.0.0.1:8000/docs

