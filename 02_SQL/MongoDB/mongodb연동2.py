import pymongo
from pymongo import MongoClient

def connect_to_mongodb():
    """MongoDB에 연결하고 데이터베이스 객체를 반환합니다."""
    connection_string = "mongodb://test:1234@127.0.0.1:27017/"
    client = MongoClient(connection_string)
    return client.mydb

def display_collection_data(collection, title="데이터 조회"):
    """컬렉션의 모든 문서를 출력합니다."""
    print(f"\n=== {title} ===")
    documents = collection.find()
    for doc in documents:
        print(doc)

def insert_sample_data(guestbook_collection):
    """방명록에 샘플 데이터를 삽입합니다."""
    sample_data = [
        {'id': 1, 'title': '제목1', 'contents': '내용1', 'writer': '홍길동', 'wdate': '2019-03-15', 'age': 23},
        {'id': 2, 'title': '제목2', 'contents': '내용2', 'writer': '임꺽정', 'wdate': '2019-03-16', 'age': 33},
        {'id': 3, 'title': '제목3', 'contents': '내용3', 'writer': '장길산', 'wdate': '2019-03-17', 'age': 42},
        {'id': 4, 'title': '제목4', 'contents': '내용4', 'writer': '홍경래', 'wdate': '2019-03-18', 'age': 53},
        {'id': 5, 'title': '제목5', 'contents': '내용5', 'writer': '장승업', 'wdate': '2019-04-12', 'age': 34}
    ]
    
    # 여러 문서를 한 번에 삽입
    guestbook_collection.insert_many(sample_data)
    print("샘플 데이터가 삽입되었습니다.")

def delete_document(guestbook_collection, doc_id):
    """지정된 ID의 문서를 삭제합니다."""
    result = guestbook_collection.delete_one({'id': doc_id})
    if result.deleted_count > 0:
        print(f"ID {doc_id} 문서가 삭제되었습니다.")
    else:
        print(f"ID {doc_id} 문서를 찾을 수 없습니다.")

def update_document(guestbook_collection, doc_id, update_data):
    """지정된 ID의 문서를 업데이트합니다."""
    result = guestbook_collection.update_one(
        {'id': doc_id}, 
        {'$set': update_data}
    )
    if result.modified_count > 0:
        print(f"ID {doc_id} 문서가 수정되었습니다.")
    else:
        print(f"ID {doc_id} 문서를 찾을 수 없거나 수정되지 않았습니다.")

def search_by_age(guestbook_collection, min_age):
    """지정된 나이 이상의 문서를 검색합니다."""
    print(f"\n=== {min_age}세 이상 검색 결과 ===")
    results = guestbook_collection.find({'age': {'$gte': min_age}})
    for result in results:
        print(result)

def main():
    """메인 실행 함수"""
    # MongoDB 연결
    db = connect_to_mongodb()
    
    # 기존 person 컬렉션 데이터 조회
    if 'person' in db.list_collection_names():
        display_collection_data(db.person, "Person 컬렉션 데이터")
    
    # 방명록 컬렉션 생성 (컬렉션이 없으면 자동 생성됨)
    guestbook = db.guestbook
    
    # 기존 데이터 삭제 (테스트를 위해)
    guestbook.drop()
    print("기존 guestbook 컬렉션이 삭제되었습니다.")
    
    # 샘플 데이터 삽입
    insert_sample_data(guestbook)
    
    # 전체 데이터 조회
    display_collection_data(guestbook, "삽입 후 전체 데이터")
    
    # 문서 삭제 (ID는 정수형으로 검색)
    delete_document(guestbook, 1)
    
    # 문서 수정
    update_document(guestbook, 2, {'title': '제목을 수정합니다'})
    
    # 수정 후 전체 데이터 조회
    display_collection_data(guestbook, "수정/삭제 후 전체 데이터")
    
    # 조건 검색 (30세 이상)
    search_by_age(guestbook, 30)
    
    # 컬렉션 제거
    guestbook.drop()
    print("\nguestbook 컬렉션이 제거되었습니다.")

if __name__ == "__main__":
    main()
