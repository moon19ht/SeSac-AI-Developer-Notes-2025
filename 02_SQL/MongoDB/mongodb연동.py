# pip install pymongo
from pymongo import MongoClient
from typing import Optional

class MongoDBConnection:
    def __init__(self, host: str = "127.0.0.1", port: int = 27017, 
                 username: str = "test", password: str = "1234", 
                 database: str = "mydb"):
        """MongoDB 연결을 위한 초기화"""
        self.connection_string = f"mongodb://{username}:{password}@{host}:{port}/"
        self.database_name = database
        self.client: Optional[MongoClient] = None
        self.db = None
    
    def connect(self):
        """MongoDB에 연결"""
        try:
            self.client = MongoClient(self.connection_string)
            self.db = self.client[self.database_name]
            return True
        except Exception as e:
            print(f"Connection failed: {e}")
            return False
    
    def get_all_persons(self):
        """person 컬렉션의 모든 문서 조회"""
        if not self.db:
            print("Database not connected")
            return []
        
        try:
            return list(self.db.person.find())
        except Exception as e:
            print(f"Query failed: {e}")
            return []
    
    def close(self):
        """MongoDB 연결 종료"""
        if self.client:
            self.client.close()

def main():
    """메인 실행 함수"""
    mongo = MongoDBConnection()
    
    # MongoDB 연결 시도
    if mongo.connect():
        # 모든 person 데이터 조회
        persons = mongo.get_all_persons()
        
        # 결과 출력
        for person in persons:
            print(person)
            # print(person['_id'], person['name'], person['gender'])  # 특정 필드만 출력
    
    # 연결 종료
    mongo.close()

if __name__ == "__main__":
    main()
