# 🧩 파이썬(Python) 심화; SQL 연결

##### 🗓️ 2025.05.28
##### 📝 Writer : Moon19ht

---

## 📚 목차

- [1. SQLAlchemy 정의](#1-sqlalchemy-정의)
- [2. 설치](#2-설치)
- [3. 연결 설정하기](#3-연결-설정하기)
- [4. 트랜잭션과 쿼리 실행하기](#4-트랜잭션과-쿼리-실행하기)
- [5. 데이터베이스 메타데이터로 작업하기](#5-데이터베이스-메타데이터로-작업하기)
- [6. Core와 ORM 방식으로 행 조회하기](#6-core와-orm-방식으로-행-조회하기)
- [7. Core 방식으로 행 삽입하기](#7-core-방식으로-행-삽입하기)
- [8. Core 방식으로 행 수정 및 삭제하기](#8-core-방식으로-행-수정-및-삭제하기)
- [9. ORM 방식으로 데이터 조작하기](#9-orm-방식으로-데이터-조작하기)
- [10. ORM으로 관련 개체 작업하기](#10-orm으로-관련-개체-작업하기)

---

# SQLAlchemy 가이드 (MySQL 기준)

이 문서는 SQLAlchemy를 활용하여 MySQL 데이터베이스를 다루는 방법을 Core와 ORM 방식을 중심으로 정리한 가이드입니다. 각 항목은 설명과 함께 Python 코드 예제 및 MySQL에 맞는 SQL 표현으로 제공됩니다.

## 1. SQLAlchemy 정의
SQLAlchemy는 파이썬에서 데이터베이스를 효율적으로 다룰 수 있도록 도와주는 라이브러리로, 두 가지 주요 접근 방식을 제공합니다:

- **SQLAlchemy Core**: SQL 표현식 언어를 사용해 SQL에 가깝게 다루는 방식.
- **SQLAlchemy ORM**: 클래스 객체와 매핑을 통해 데이터베이스를 객체지향적으로 다루는 방식.

장점:
- 다양한 DB 백엔드 지원 (MySQL, PostgreSQL, SQLite 등)
- SQL과 ORM의 유연한 결합
- 높은 확장성과 유지보수성

## 2. 설치
SQLAlchemy와 MySQL을 연동하기 위해 `pymysql` 드라이버를 함께 설치합니다.

```bash
pip install sqlalchemy pymysql
```

## 3. 연결 설정하기
MySQL 데이터베이스에 연결을 설정하는 기본적인 방법입니다.

```python
from sqlalchemy import create_engine

# 'mysql+pymysql://username:password@host:port/dbname'
engine = create_engine("mysql+pymysql://root:password@localhost:3306/testdb", echo=True)
```

- `echo=True`는 실행되는 SQL을 콘솔에 출력하게 해줍니다.

## 4. 트랜잭션과 쿼리 실행하기

### 연결 얻기
```python
conn = engine.connect()
```

### 변경 사항 커밋하기 (트랜잭션 수동 제어)
```python
trans = conn.begin()
try:
    conn.execute(text("INSERT INTO users (name) VALUES (:name)"), {"name": "Alice"})
    trans.commit()
except:
    trans.rollback()
```

### 명령문 실행의 기초
```python
from sqlalchemy import text

result = conn.execute(text("SELECT * FROM users"))
for row in result:
    print(row)
```

### 쿼리에 매개변수 전달하기
```python
result = conn.execute(text("SELECT * FROM users WHERE name = :name"), {"name": "Alice"})
```

### ORM Session으로 실행
```python
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()
```

- ORM을 사용하는 경우 대부분의 DB 작업은 Session을 통해 이루어집니다.

## 5. 데이터베이스 메타데이터로 작업하기

SQLAlchemy Core는 테이블 정의를 위한 `MetaData` 객체를 통해 스키마 정보를 관리합니다.

### 테이블 객체를 만들고 메타데이터에 담기
```python
from sqlalchemy import Table, Column, Integer, String, MetaData

metadata = MetaData()
users = Table(
    "users", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False),
)
metadata.create_all(engine)  # 실제 DB에 테이블 생성
```

### 단순 제약 선언하기
```python
Column("email", String(100), unique=True, nullable=False)
```

### ORM 방식으로 테이블 메타데이터 정의하기
```python
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
```

### 기존 데이터베이스의 테이블을 ORM 객체로 불러오기
```python
from sqlalchemy.ext.automap import automap_base

Base = automap_base()
Base.prepare(engine, reflect=True)
User = Base.classes.users
```

## 6. Core와 ORM 방식으로 행 조회하기

### select()를 통한 SQL 표현식 구성
```python
from sqlalchemy import select

stmt = select(users)
result = conn.execute(stmt)
for row in result:
    print(row)
```

### FROM 절과 컬럼 세팅하기
```python
stmt = select(users.c.id, users.c.name)
```

### WHERE 절
```python
stmt = select(users).where(users.c.name == "Alice")
```

### ORDER BY, GROUP BY, HAVING
```python
stmt = select(users).order_by(users.c.name)
```

### 별칭 사용하기
```python
from sqlalchemy.orm import aliased

user_alias = aliased(User)
session.query(user_alias).filter(user_alias.name == "Alice")
```

### 서브쿼리와 CTE
```python
subq = select(users.c.id).where(users.c.name == "Alice").subquery()
stmt = select(users).where(users.c.id.in_(subq))
```

### 스칼라 서브 쿼리, 상호연관 쿼리
```python
scalar_subq = select(users.c.name).where(users.c.id == 1).scalar_subquery()
```

### UNION, UNION ALL 연산자들
```python
stmt1 = select(users).where(users.c.name == "Alice")
stmt2 = select(users).where(users.c.name == "Bob")
union_stmt = stmt1.union(stmt2)
```

### EXISTS 서브쿼리들
```python
from sqlalchemy import exists

stmt = select(users).where(exists(select(users.c.id).where(users.c.name == "Alice")))
```

### SQL 함수 다뤄보기
```python
from sqlalchemy import func

stmt = select(func.count(users.c.id))
```

## 7. Core 방식으로 행 삽입하기

### insert() 를 통한 SQL 표현식 구성
```python
from sqlalchemy import insert

stmt = insert(users).values(name="Bob")
```

### 명령문 실행
```python
conn.execute(stmt)
```

### Connection.execute() 에 INSERT 매개변수 전달하기
```python
conn.execute(insert(users), [{"name": "Alice"}, {"name": "Bob"}])
```

### Insert.from_select()
```python
stmt = insert(users).from_select(["name"], select(users.c.name))
```

### Insert.returning()
```python
stmt = insert(users).values(name="Charlie").returning(users.c.id)
```

## 8. Core 방식으로 행 수정 및 삭제하기

### update() 를 통한 SQL 표현식 구성
```python
from sqlalchemy import update

stmt = update(users).where(users.c.name == "Alice").values(name="Alicia")
```

### delete() 를 통한 SQL 표현식 구성
```python
from sqlalchemy import delete

stmt = delete(users).where(users.c.name == "Bob")
```

### UPDATE, DELETE에서 영향을 받는 행 수 얻기
```python
result = conn.execute(stmt)
print(result.rowcount)
```

### UPDATE, DELETE와 함께 RETURNING 사용하기
```python
stmt = update(users).where(users.c.name == "Alicia").values(name="Alice").returning(users.c.id)
```

## 9. ORM 방식으로 데이터 조작하기

### ORM으로 행 삽입하기
```python
new_user = User(name="Diana")
session.add(new_user)
session.commit()
```

### ORM 객체 UPDATE하기
```python
user = session.query(User).filter_by(name="Diana").first()
user.name = "Diane"
session.commit()
```

### ORM 객체를 삭제하기
```python
session.delete(user)
session.commit()
```

### Rolling Back
```python
session.rollback()
```

### Session 종료하기
```python
session.close()
```

## 10. ORM으로 관련 개체 작업하기

### 관계된 객체 사용하기
```python
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Address(Base):
    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="addresses")

User.addresses = relationship("Address", back_populates="user", cascade="all, delete")
```

### Session에 객체 캐스케이딩
```python
user = User(name="Emma", addresses=[Address()])
session.add(user)
session.commit()
```

### 관계 로드
```python
from sqlalchemy.orm import joinedload

user = session.query(User).options(joinedload(User.addresses)).first()
```

### 쿼리에서 relationship 사용하기
```python
session.query(Address).join(Address.user).filter(User.name == "Emma")
```

### Loading relationship의 종류
- `select`: 기본값, 필요한 시점에 개별 쿼리
- `joined`: 즉시 조인하여 함께 로드
- `subquery`: 서브쿼리로 로드
- `dynamic`: 쿼리 객체 반환하여 지연 실행
