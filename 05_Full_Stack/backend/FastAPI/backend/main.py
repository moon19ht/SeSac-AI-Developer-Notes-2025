from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import board, score

# FastAPI 애플리케이션 초기화
app = FastAPI(
    title="Board API",
    description="게시판 및 성적 관리 API 서버",
    version="1.0.0"
)

# CORS 허용 도메인 설정
ALLOWED_ORIGINS = [
    "http://127.0.0.1:5173",
    "http://localhost:5173",
    "http://www.sessac.com:5173"
]

# CORS 미들웨어 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(board.router)
app.include_router(score.router)


@app.get("/", tags=["health"])
def health_check():
    """서버 상태 확인 엔드포인트"""
    return {"message": "서버가 정상적으로 실행 중입니다", "status": "healthy"}


@app.get("/info", tags=["info"])
def get_server_info():
    """서버 정보 반환"""
    return {
        "server": "FastAPI Backend",
        "version": "1.0.0",
        "available_endpoints": [
            "/board/list - 게시판 목록 조회",
            "/board/insert - 게시글 등록",
            "/score/scoreList - 성적 목록 조회",
            "/score/score/insert - 성적 등록"
        ]
    }

# 실행 방법:
# conda activate backend
# python -m uvicorn main:app --reload --port 8000
