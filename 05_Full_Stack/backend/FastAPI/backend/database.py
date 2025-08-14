from sqlalchemy import create_engine, text
from sqlalchemy.engine import Connection
from sqlalchemy.exc import SQLAlchemyError
from typing import Any, Dict, List, Optional, Union


class Database:
    """데이터베이스 연결 및 쿼리 실행을 담당하는 클래스"""
    
    DEFAULT_URL = "mysql+pymysql://root:1234@localhost/mydb"
    
    def __init__(self, url: str = "") -> None:
        """데이터베이스 연결 초기화
        
        Args:
            url: 데이터베이스 연결 URL (기본값: DEFAULT_URL 사용)
        """
        self.url = url if url else self.DEFAULT_URL
        self.engine = create_engine(self.url)
        self.connection: Optional[Connection] = None

    def __enter__(self) -> 'Database':
        """with 구문 진입 시 데이터베이스 연결"""
        try:
            self.connection = self.engine.connect()
            print("DB연결성공")
            return self
        except SQLAlchemyError as e:
            print(f"연결실패: {e}")
            raise

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """with 구문 종료 시 데이터베이스 연결 해제"""
        if self.connection:
            self.connection.close()
            self.connection = None
            print("데이터베이스 연결 종료")

    def execute(self, query: str, params: Optional[Union[Dict, List[Dict]]] = None) -> None:
        """INSERT, UPDATE, DELETE 쿼리 실행
        
        Args:
            query: 실행할 SQL 쿼리
            params: 쿼리 파라미터
        """
        if not self.connection:
            raise RuntimeError("데이터베이스 연결이 없습니다")
            
        with self.connection.begin():
            self.connection.execute(text(query), params)

    def executeOne(self, query: str, params: Optional[Union[Dict, List[Dict]]] = None) -> Optional[Dict[str, Any]]:
        """단일 결과 반환 쿼리 실행
        
        Args:
            query: 실행할 SQL 쿼리
            params: 쿼리 파라미터
            
        Returns:
            쿼리 결과 딕셔너리 또는 None
        """
        if not self.connection:
            raise RuntimeError("데이터베이스 연결이 없습니다")
            
        result = self.connection.execute(text(query), params)
        row = result.fetchone()
        return dict(row._mapping) if row else None

    def executeAll(self, query: str, params: Optional[Union[Dict, List[Dict]]] = None) -> List[Dict[str, Any]]:
        """다중 결과 반환 쿼리 실행
        
        Args:
            query: 실행할 SQL 쿼리
            params: 쿼리 파라미터
            
        Returns:
            쿼리 결과 딕셔너리 리스트
        """
        if not self.connection:
            raise RuntimeError("데이터베이스 연결이 없습니다")
            
        result = self.connection.execute(text(query), params)
        return [dict(row._mapping) for row in result.fetchall()]
