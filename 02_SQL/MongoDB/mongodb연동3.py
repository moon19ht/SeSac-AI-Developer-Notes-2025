import pymongo
from pymongo import MongoClient 
from pymongo.collection import ReturnDocument

def connect_to_database():
    """MongoDB 데이터베이스에 연결"""
    try:
        conn = MongoClient("mongodb://test:1234@127.0.0.1:27017/")
        db = conn.mydb
        return db
    except Exception as e:
        print(f"데이터베이스 연결 실패: {e}")
        return None

def initialize_sequence_collection(db):
    """시퀀스 컬렉션 초기화 (필요한 경우에만)"""
    # 시퀀스 컬렉션이 존재하지 않으면 생성
    if "customSequences" not in db.list_collection_names():
        db.customSequences.insert_one({"_id": "guestbook", "seq": 0})

def get_next_sequence(db, sequence_name):
    """다음 시퀀스 번호 가져오기"""
    try:
        document = db.customSequences.find_one_and_update(
            {"_id": sequence_name}, 
            {"$inc": {"seq": 1}}, 
            return_document=ReturnDocument.AFTER,
            upsert=True  # 문서가 없으면 생성
        )
        return document['seq']
    except Exception as e:
        print(f"시퀀스 생성 실패: {e}")
        return None

def insert_guestbook_entry(db, title, contents, writer, age):
    """방명록 항목 추가"""
    try:
        # 다음 ID 가져오기
        next_id = get_next_sequence(db, 'guestbook')
        if next_id is None:
            return False
            
        # 방명록 컬렉션 가져오기
        guestbook = db.guestbook
        
        # 현재 날짜 가져오기
        from datetime import datetime
        current_date = datetime.now().strftime('%Y-%m-%d')
        
        # 문서 삽입
        entry = {
            'id': str(next_id),
            'title': title,
            'contents': contents,
            'writer': writer,
            'wdate': current_date,
            'age': age
        }
        
        result = guestbook.insert_one(entry)
        print(f"방명록 항목 추가 완료: {result.inserted_id}")
        return True
        
    except Exception as e:
        print(f"방명록 항목 추가 실패: {e}")
        return False

def display_all_guestbook_entries(db):
    """모든 방명록 항목 출력"""
    try:
        rows = db.guestbook.find()
        print("\n=== 방명록 목록 ===")
        for row in rows:
            print(f"ID: {row.get('id')}, 제목: {row.get('title')}, "
                  f"작성자: {row.get('writer')}, 날짜: {row.get('wdate')}")
        print("==================\n")
    except Exception as e:
        print(f"방명록 조회 실패: {e}")

def main():
    """메인 실행 함수"""
    # 데이터베이스 연결
    db = connect_to_database()
    if db is None:
        return
    
    # 시퀀스 컬렉션 초기화
    initialize_sequence_collection(db)
    
    # 샘플 데이터 추가
    sample_id = get_next_sequence(db, 'guestbook')
    if sample_id:
        insert_guestbook_entry(
            db, 
            title=f'제목{sample_id}',
            contents=f'내용{sample_id}',
            writer=f'홍길동{sample_id}',
            age=23
        )
    
    # 모든 항목 출력
    display_all_guestbook_entries(db)

if __name__ == "__main__":
    main()
