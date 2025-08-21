"""
FastAPI 백엔드 서버

필수 의존성:
pip install python-multipart
pip install fastapi
pip install uvicorn
pip install pymysql sqlalchemy 
"""

import os
import shutil
from typing import Optional

from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from routers import board, predict


class GlobalSettings:
    """전역 애플리케이션 설정 컨테이너"""
    
    def __init__(self):
        self.API_KEY = "1203ue"
        self.DB_URL = ""
        self.UPLOAD_DIRECTORY = "./upload_files"
        self.ALLOWED_ORIGINS = [
            "http://127.0.0.1:5173",
            "http://localhost:5173",
            "http://www.sessac.com:5173"
        ]


def create_upload_directory(directory_path: str) -> None:
    """업로드 디렉토리가 존재하지 않으면 생성"""
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"업로드 디렉토리 생성: {directory_path}")


def setup_cors_middleware(app: FastAPI, allowed_origins: list) -> None:
    """CORS 미들웨어를 설정하여 교차 출처 요청을 허용"""
    app.add_middleware(
        CORSMiddleware,
        allow_origins=allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],  # 모든 HTTP 메서드 허용 (GET, POST, PUT, DELETE 등)
        allow_headers=["*"],  # 모든 HTTP 헤더 허용
    )


def setup_static_files(app: FastAPI, upload_directory: str) -> None:
    """업로드된 파일을 제공하기 위한 정적 파일 디렉토리 마운트"""
    app.mount(
        "/static", 
        StaticFiles(directory=upload_directory), 
        name="static"
    )


def configure_routers(app: FastAPI, settings: dict) -> None:
    """의존성 주입을 통해 애플리케이션 라우터 구성 및 포함"""
    # 설정에 대한 의존성 주입
    board.settings_container["settings"] = settings
    predict.settings_container["settings"] = settings
    
    # 라우터 포함
    app.include_router(board.router)
    app.include_router(predict.router)


def create_app() -> FastAPI:
    """FastAPI 애플리케이션을 생성하고 구성하는 팩토리 함수"""
    # FastAPI 애플리케이션 초기화
    app = FastAPI(
        title="SeSac AI 백엔드 API",
        description="AI 개발자 과정용 백엔드 API",
        version="1.0.0"
    )
    
    # 전역 설정 초기화
    settings = GlobalSettings()
    
    # 업로드 디렉토리 생성
    create_upload_directory(settings.UPLOAD_DIRECTORY)
    
    # 미들웨어 및 정적 파일 설정
    setup_cors_middleware(app, settings.ALLOWED_ORIGINS)
    setup_static_files(app, settings.UPLOAD_DIRECTORY)
    
    # 라우터 주입을 위해 설정을 딕셔너리로 변환
    settings_dict = {
        "api_key": settings.API_KEY,
        "db_url": settings.DB_URL,
        "UPLOAD_DIRECTORY": settings.UPLOAD_DIRECTORY
    }
    
    # 라우터 구성
    configure_routers(app, settings_dict)
    
    return app


# FastAPI 애플리케이션 인스턴스 생성
app = create_app()


@app.get("/", tags=["루트"])
def root():
    """루트 엔드포인트 - 상태 확인"""
    return {
        "message": "Hello FastAPI",
        "status": "running",
        "docs": "/docs"
    }


@app.get("/health", tags=["상태확인"])
def health_check():
    """상태 확인 엔드포인트"""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )

"""
애플리케이션 실행:

1. conda 환경 활성화:
   conda activate backend

2. 의존성 설치:
   conda install pymysql sqlalchemy python-multipart

3. 서버 실행:
   python -m uvicorn main:app --reload --port 8000
   
   또는 간단히:
   python main.py

4. 엔드포인트 접근:
   - API: http://127.0.0.1:8000
   - 문서: http://127.0.0.1:8000/docs
   - 정적 파일: http://127.0.0.1:8000/static/{filename}

5. 관리자 권한 (Windows):
   명령어 실행 전에 CMD를 관리자 권한으로 실행
"""