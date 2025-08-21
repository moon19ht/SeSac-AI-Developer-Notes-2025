import sqlalchemy
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Connection
from typing import Any, Dict, List, Optional


class Database:
    """데이터베이스 연결 및 쿼리 실행을 위한 클래스"""
    
    def __init__(self, url: str = "mysql+pymysql://root:1234@localhost/mydb"):
        """
        데이터베이스 객체 초기화
        
        Args:
            url (str): 데이터베이스 연결 URL
        """
        self.url = url
        self.engine = create_engine(self.url)
        self.connection: Optional[Connection] = None

    def __enter__(self) -> 'Database':
        """
        컨텍스트 매니저 진입 시 데이터베이스 연결 생성
        
        Returns:
            Database: 현재 인스턴스
        """
        try:
            self.connection = self.engine.connect()
            print("DB 연결 성공")
            return self
        except sqlalchemy.exc.SQLAlchemyError as e:
            print("DB 연결 실패:", e)
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        """컨텍스트 매니저 종료 시 데이터베이스 연결 해제"""
        if self.connection:
            self.connection.close()
            print("DB 연결 종료")

    def execute(self, query: str, args: dict = None) -> None:
        """
        쿼리 실행 (결과 반환 없음)
        
        Args:
            query (str): 실행할 SQL 쿼리
            args (dict, optional): 쿼리 파라미터
        """
        with self.connection.begin():
            self.connection.execute(text(query), args or {})

    def execute_one(self, query: str, args: dict = None) -> Optional[Dict[str, Any]]:
        """
        쿼리 실행 후 단일 결과 반환
        
        Args:
            query (str): 실행할 SQL 쿼리
            args (dict, optional): 쿼리 파라미터
            
        Returns:
            Optional[Dict[str, Any]]: 첫 번째 행의 결과 또는 None
        """
        result = self.connection.execute(text(query), args or {})
        row = result.fetchone()
        return dict(row._mapping) if row else None

    def execute_all(self, query: str, args: dict = None) -> List[Dict[str, Any]]:
        """
        쿼리 실행 후 모든 결과 반환
        
        Args:
            query (str): 실행할 SQL 쿼리
            args (dict, optional): 쿼리 파라미터
            
        Returns:
            List[Dict[str, Any]]: 모든 행의 결과 리스트
        """
        result = self.connection.execute(text(query), args or {})
        return [dict(row._mapping) for row in result.fetchall()]
