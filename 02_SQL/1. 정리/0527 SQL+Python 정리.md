# 🧩 파이썬(Python) 심화; SQL 연결

##### 🗓️ 2025.05.27
##### 📝 Writer : Moon19ht

---

## 📚 목차

- [1. pymysql로 MySQL 연결](#1-pymysql로-mysql-연결)
- [2. SQLAlchemy로 ORM 연결](#2-sqlalchemy로-orm-연결)
- [3. SQLAlchemy 커넥션 풀](#3-sqlalchemy-커넥션-풀)
- [4. Python 연산자 중복 (Operator Overloading)](#4-python-연산자-중복-operator-overloading)

---

# Python과 SQL 연동 가이드 (예제 포함)

Python에서 SQL과 연동하는 다양한 방법과 고급 기능들을 예제와 함께 설명합니다.

## 1. pymysql로 MySQL 연결

`pymysql`은 MySQL에 직접 연결하는 드라이버입니다.

### 예제: 간단한 SELECT 쿼리

```python
import pymysql

# 데이터베이스 연결
conn = pymysql.connect(
    host='localhost',
    user='user',
    password='password',
    db='test_db',
    charset='utf8mb4'
)

try:
    with conn.cursor() as cursor:
        sql = "SELECT id, name FROM users"
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}")
finally:
    conn.close()
```

---

## 2. SQLAlchemy로 ORM 연결

`sqlalchemy`는 ORM(Object Relational Mapping)을 제공하여 Python 객체로 DB를 다룰 수 있게 해줍니다.

### 예제: 사용자 정보 추가 및 조회

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://user:password@localhost/test_db", echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# 사용자 추가
user1 = User(name='이몽룡')
user2 = User(name='성춘향')
session.add_all([user1, user2])
session.commit()

# 사용자 조회
for user in session.query(User).all():
    print(f"ID: {user.id}, Name: {user.name}")
```

---

## 3. SQLAlchemy 커넥션 풀

성능 최적화를 위해 커넥션 풀을 설정할 수 있습니다.

### 예제: 풀 옵션 설정

```python
engine = create_engine(
    "mysql+pymysql://user:password@localhost/test_db",
    pool_size=5,          # 기본 커넥션 수
    max_overflow=10,      # 초과 허용 커넥션 수
    pool_timeout=15,      # 커넥션 요청 대기 시간 (초)
    pool_recycle=3600     # 커넥션 재활용 주기 (초)
)
```

---

## 4. Python 연산자 중복 (Operator Overloading)

클래스에 연산자를 오버로딩하면 직관적인 코드 작성이 가능합니다.

### 예제: 벡터 클래스

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(1, 5)

print("덧셈:", v1 + v2)    # Vector(3, 8)
print("뺄셈:", v1 - v2)    # Vector(1, -2)
print("스칼라곱:", v1 * 3) # Vector(6, 9)
```

---

## 참고

- [PyMySQL 공식 문서](https://pymysql.readthedocs.io/)
- [SQLAlchemy 공식 문서](https://docs.sqlalchemy.org/)
