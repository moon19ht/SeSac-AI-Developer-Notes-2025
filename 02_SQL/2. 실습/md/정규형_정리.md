# 데이터베이스 정규화 완벽 가이드

---

## 목차

1. [정규화 개요](#1-정규화-개요)
2. [제1정규형 (1NF)](#2-제1정규형-1nf)
3. [제2정규형 (2NF)](#3-제2정규형-2nf)
4. [제3정규형 (3NF)](#4-제3정규형-3nf)
5. [보이스-코드 정규형 (BCNF)](#5-보이스-코드-정규형-bcnf)
6. [정규화 요약](#6-정규화-요약)
7. [트랜잭션과 ACID](#7-트랜잭션과-acid)
8. [실습 예제](#8-실습-예제)

---

# 1. 정규화 개요

## 1.1 정규화란?

### 정의
**정규화(Normalization)는 데이터베이스 설계 시 중복을 줄이고, 데이터의 일관성과 무결성을 유지하기 위한 과정**

### 목적
- **데이터 중복 최소화**: 동일한 데이터가 여러 곳에 저장되는 것을 방지
- **데이터 일관성 유지**: 데이터 변경 시 모든 곳에서 일관되게 반영
- **저장 공간 효율성**: 불필요한 데이터 중복으로 인한 공간 낭비 방지
- **이상 현상 방지**: 삽입, 삭제, 갱신 시 발생할 수 있는 문제 해결

### 정규화 과정
주어진 데이터를 일련의 정규형(1NF → 2NF → 3NF → BCNF)으로 단계적으로 분해

## 1.2 이상 현상 (Anomaly)

### 삽입 이상 (Insertion Anomaly)
- 새로운 데이터를 삽입할 때 불필요한 데이터도 함께 삽입해야 하는 문제
- 예: 새로운 과목을 추가하려면 반드시 학생 정보도 함께 입력해야 함

### 삭제 이상 (Deletion Anomaly)
- 특정 데이터를 삭제할 때 필요한 다른 데이터까지 함께 삭제되는 문제
- 예: 학생을 삭제하면 해당 과목 정보도 함께 사라짐

### 갱신 이상 (Update Anomaly)
- 데이터를 수정할 때 중복된 데이터를 모두 수정하지 않으면 일관성이 깨지는 문제
- 예: 학생 정보 변경 시 여러 곳에 있는 동일한 정보를 모두 수정해야 함

---

# 2. 제1정규형 (1NF)

## 2.1 정의
**테이블의 모든 속성이 원자값(Atomic Value)을 가져야 함**

### 조건
- 각 속성은 단일 값만 가져야 함
- 반복되는 그룹이나 배열 형태의 데이터가 없어야 함
- 각 행은 고유해야 함

## 2.2 1NF 위반 예시

### ❌ 1NF 위반 테이블
| 학생ID | 학생명 | 수강과목 |
|--------|--------|----------|
| 001 | 김철수 | 수학, 영어, 과학 |
| 002 | 이영희 | 국어, 영어 |
| 003 | 박민수 | 수학, 과학 |

**문제점**: `수강과목` 컬럼에 여러 값이 저장됨 (반복 속성)

### ✅ 1NF 준수 테이블
| 학생ID | 학생명 | 수강과목 |
|--------|--------|----------|
| 001 | 김철수 | 수학 |
| 001 | 김철수 | 영어 |
| 001 | 김철수 | 과학 |
| 002 | 이영희 | 국어 |
| 002 | 이영희 | 영어 |
| 003 | 박민수 | 수학 |
| 003 | 박민수 | 과학 |

**해결**: 각 행이 하나의 원자값만 가지도록 분리

## 2.3 1NF 적용 방법

### 방법 1: 행 분리
```sql
-- 원래 테이블
CREATE TABLE student_subjects_bad (
    student_id VARCHAR(10),
    student_name VARCHAR(50),
    subjects VARCHAR(200)  -- '수학,영어,과학' 형태
);

-- 1NF 적용 후
CREATE TABLE student_subjects_1nf (
    student_id VARCHAR(10),
    student_name VARCHAR(50),
    subject VARCHAR(50)
);
```

### 방법 2: 테이블 분리
```sql
-- 학생 테이블
CREATE TABLE students (
    student_id VARCHAR(10) PRIMARY KEY,
    student_name VARCHAR(50)
);

-- 수강 테이블
CREATE TABLE enrollments (
    student_id VARCHAR(10),
    subject VARCHAR(50),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);
```

---

# 3. 제2정규형 (2NF)

## 3.1 정의
**1NF를 만족하면서 부분 함수 종속을 제거한 형태**

### 조건
- 1NF를 만족해야 함
- 기본키가 아닌 모든 속성이 기본키에 완전 함수 종속되어야 함
- 부분 함수 종속이 없어야 함

### 함수 종속성
- **완전 함수 종속**: 기본키 전체에 종속
- **부분 함수 종속**: 기본키의 일부분에만 종속

## 3.2 2NF 위반 예시

### ❌ 2NF 위반 테이블
| 학생ID | 과목코드 | 학생명 | 과목명 | 성적 | 교수명 |
|--------|----------|--------|--------|------|--------|
| 001 | CS101 | 김철수 | 컴퓨터과학 | A | 박교수 |
| 001 | MA101 | 김철수 | 수학 | B+ | 이교수 |
| 002 | CS101 | 이영희 | 컴퓨터과학 | A- | 박교수 |

**기본키**: (학생ID, 과목코드)

**문제점**:
- `학생명`은 `학생ID`에만 종속 (부분 함수 종속)
- `과목명`, `교수명`은 `과목코드`에만 종속 (부분 함수 종속)

### ✅ 2NF 준수 테이블

#### 학생 테이블
| 학생ID | 학생명 |
|--------|--------|
| 001 | 김철수 |
| 002 | 이영희 |

#### 과목 테이블
| 과목코드 | 과목명 | 교수명 |
|----------|--------|--------|
| CS101 | 컴퓨터과학 | 박교수 |
| MA101 | 수학 | 이교수 |

#### 수강 테이블
| 학생ID | 과목코드 | 성적 |
|--------|----------|------|
| 001 | CS101 | A |
| 001 | MA101 | B+ |
| 002 | CS101 | A- |

## 3.3 2NF 적용 SQL

```sql
-- 2NF 위반 테이블
CREATE TABLE enrollment_bad (
    student_id VARCHAR(10),
    subject_code VARCHAR(10),
    student_name VARCHAR(50),
    subject_name VARCHAR(100),
    professor VARCHAR(50),
    grade VARCHAR(5),
    PRIMARY KEY (student_id, subject_code)
);

-- 2NF 적용: 테이블 분리
CREATE TABLE students (
    student_id VARCHAR(10) PRIMARY KEY,
    student_name VARCHAR(50)
);

CREATE TABLE subjects (
    subject_code VARCHAR(10) PRIMARY KEY,
    subject_name VARCHAR(100),
    professor VARCHAR(50)
);

CREATE TABLE enrollments (
    student_id VARCHAR(10),
    subject_code VARCHAR(10),
    grade VARCHAR(5),
    PRIMARY KEY (student_id, subject_code),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (subject_code) REFERENCES subjects(subject_code)
);
```

---

# 4. 제3정규형 (3NF)

## 4.1 정의
**2NF를 만족하면서 이행 함수 종속을 제거한 형태**

### 조건
- 2NF를 만족해야 함
- 기본키가 아닌 속성들 간에 이행 함수 종속이 없어야 함

### 이행 함수 종속
- A → B이고, B → C이면, A → C가 성립
- 이때 C는 A에 이행적으로 종속

## 4.2 3NF 위반 예시

### ❌ 3NF 위반 테이블
| 학생ID | 학생명 | 학과코드 | 학과명 | 학과장 |
|--------|--------|----------|--------|--------|
| 001 | 김철수 | CS | 컴퓨터과학과 | 박교수 |
| 002 | 이영희 | MA | 수학과 | 이교수 |
| 003 | 박민수 | CS | 컴퓨터과학과 | 박교수 |

**기본키**: 학생ID

**이행 함수 종속**:
- 학생ID → 학과코드 → 학과명
- 학생ID → 학과코드 → 학과장

**문제점**: `학과명`, `학과장`이 `학생ID`에 이행적으로 종속

### ✅ 3NF 준수 테이블

#### 학생 테이블
| 학생ID | 학생명 | 학과코드 |
|--------|--------|----------|
| 001 | 김철수 | CS |
| 002 | 이영희 | MA |
| 003 | 박민수 | CS |

#### 학과 테이블
| 학과코드 | 학과명 | 학과장 |
|----------|--------|--------|
| CS | 컴퓨터과학과 | 박교수 |
| MA | 수학과 | 이교수 |

## 4.3 3NF 적용 SQL

```sql
-- 3NF 위반 테이블
CREATE TABLE student_dept_bad (
    student_id VARCHAR(10) PRIMARY KEY,
    student_name VARCHAR(50),
    dept_code VARCHAR(10),
    dept_name VARCHAR(100),
    dept_head VARCHAR(50)
);

-- 3NF 적용: 테이블 분리
CREATE TABLE students (
    student_id VARCHAR(10) PRIMARY KEY,
    student_name VARCHAR(50),
    dept_code VARCHAR(10),
    FOREIGN KEY (dept_code) REFERENCES departments(dept_code)
);

CREATE TABLE departments (
    dept_code VARCHAR(10) PRIMARY KEY,
    dept_name VARCHAR(100),
    dept_head VARCHAR(50)
);
```

---

# 5. 보이스-코드 정규형 (BCNF)

## 5.1 정의
**3NF보다 더 엄격한 정규형으로, 모든 결정자가 후보키인 형태**

### 조건
- 3NF를 만족해야 함
- 모든 결정자(determinant)가 후보키(candidate key)여야 함

### 주요 개념
- **결정자**: 다른 속성을 함수적으로 결정하는 속성
- **후보키**: 기본키가 될 수 있는 모든 키

## 5.2 BCNF 위반 예시

### ❌ BCNF 위반 테이블
| 학생ID | 과목 | 교수 |
|--------|------|------|
| 001 | 데이터베이스 | 김교수 |
| 001 | 운영체제 | 이교수 |
| 002 | 데이터베이스 | 김교수 |
| 003 | 운영체제 | 박교수 |

**후보키**: (학생ID, 과목), (학생ID, 교수)

**함수 종속성**:
- (학생ID, 과목) → 교수
- (학생ID, 교수) → 과목
- 교수 → 과목 (한 교수는 한 과목만 담당)

**문제점**: `교수 → 과목`에서 `교수`가 결정자이지만 후보키가 아님

### ✅ BCNF 준수 테이블

#### 수강 테이블
| 학생ID | 교수 |
|--------|------|
| 001 | 김교수 |
| 001 | 이교수 |
| 002 | 김교수 |
| 003 | 박교수 |

#### 담당 테이블
| 교수 | 과목 |
|------|------|
| 김교수 | 데이터베이스 |
| 이교수 | 운영체제 |
| 박교수 | 운영체제 |

## 5.3 BCNF 적용 SQL

```sql
-- BCNF 위반 테이블
CREATE TABLE student_subject_prof_bad (
    student_id VARCHAR(10),
    subject VARCHAR(50),
    professor VARCHAR(50),
    PRIMARY KEY (student_id, subject)
);

-- BCNF 적용: 테이블 분리
CREATE TABLE student_professor (
    student_id VARCHAR(10),
    professor VARCHAR(50),
    PRIMARY KEY (student_id, professor)
);

CREATE TABLE professor_subject (
    professor VARCHAR(50) PRIMARY KEY,
    subject VARCHAR(50)
);
```

---

# 6. 정규화 요약

## 6.1 정규형 비교표

| 정규형 | 조건 | 제거하는 문제 | 핵심 포인트 |
|--------|------|---------------|-------------|
| **1NF** | 원자값만 허용 | 반복 속성 | 각 셀에 하나의 값만 |
| **2NF** | 1NF + 완전 함수 종속 | 부분 함수 종속 | 기본키 전체에 종속 |
| **3NF** | 2NF + 이행 종속 제거 | 이행 함수 종속 | 간접적 종속 제거 |
| **BCNF** | 3NF + 모든 결정자가 후보키 | 결정자 이상 | 모든 결정자가 키 |

## 6.2 정규화 단계별 진행

```
비정규형 테이블
    ↓ (반복 속성 제거)
1NF (제1정규형)
    ↓ (부분 함수 종속 제거)
2NF (제2정규형)
    ↓ (이행 함수 종속 제거)
3NF (제3정규형)
    ↓ (결정자 이상 제거)
BCNF (보이스-코드 정규형)
```

## 6.3 정규화의 장단점

### ✅ 장점
- **데이터 중복 최소화**: 저장 공간 효율성
- **데이터 일관성 보장**: 갱신 이상 방지
- **데이터 무결성 향상**: 삽입/삭제 이상 방지
- **유지보수 용이성**: 구조가 명확하고 변경이 쉬움

### ❌ 단점
- **조인 연산 증가**: 여러 테이블을 조인해야 함
- **성능 저하 가능성**: 복잡한 쿼리로 인한 속도 저하
- **설계 복잡성**: 초기 설계가 복잡해짐

---

# 7. 트랜잭션과 ACID

## 7.1 트랜잭션 정의

### 개념
**트랜잭션(Transaction)은 데이터베이스에서 하나의 작업 단위로 처리되는 일련의 연산 묶음**

### 특징
- **All or Nothing**: 모든 연산이 성공하면 COMMIT, 하나라도 실패하면 ROLLBACK
- **데이터 무결성 보장**: 일관성 있는 데이터 상태 유지
- **동시성 제어**: 여러 사용자가 동시에 접근할 때 데이터 일관성 보장

## 7.2 ACID 속성

### A - 원자성 (Atomicity)
- **정의**: 트랜잭션의 모든 연산이 완전히 수행되거나 전혀 수행되지 않아야 함
- **예시**: 계좌 이체 시 출금과 입금이 모두 성공하거나 모두 실패

### C - 일관성 (Consistency)
- **정의**: 트랜잭션 실행 전후에 데이터베이스가 일관된 상태를 유지해야 함
- **예시**: 잔액은 항상 0 이상이어야 한다는 제약조건 유지

### I - 독립성 (Isolation)
- **정의**: 동시에 실행되는 트랜잭션들이 서로 영향을 주지 않아야 함
- **예시**: 두 사용자가 동시에 같은 계좌에 접근해도 서로 간섭하지 않음

### D - 지속성 (Durability)
- **정의**: 성공적으로 완료된 트랜잭션의 결과는 영구적으로 반영되어야 함
- **예시**: 시스템 장애가 발생해도 커밋된 데이터는 보존됨

## 7.3 트랜잭션 제어 명령어

### 기본 구문
```sql
-- 트랜잭션 시작
START TRANSACTION;
-- 또는
BEGIN;

-- 트랜잭션 확정 (영구 반영)
COMMIT;

-- 트랜잭션 취소 (되돌리기)
ROLLBACK;

-- 저장점 설정
SAVEPOINT savepoint_name;

-- 특정 저장점으로 롤백
ROLLBACK TO savepoint_name;
```

### 실제 예제
```sql
-- 계좌 이체 트랜잭션
START TRANSACTION;

-- 출금 계좌에서 차감
UPDATE accounts 
SET balance = balance - 100000 
WHERE account_id = 'A001';

-- 잔액 확인
SELECT balance FROM accounts WHERE account_id = 'A001';

-- 입금 계좌에 추가
UPDATE accounts 
SET balance = balance + 100000 
WHERE account_id = 'A002';

-- 모든 작업이 성공하면 커밋
COMMIT;

-- 문제가 발생하면 롤백
-- ROLLBACK;
```

---

# 8. 실습 예제

## 8.1 정규화 실습

### 시나리오: 도서관 관리 시스템

#### 원본 테이블 (비정규형)
```sql
CREATE TABLE library_records (
    record_id INT PRIMARY KEY,
    book_title VARCHAR(200),
    authors VARCHAR(300),        -- '김작가,이작가,박작가'
    publisher VARCHAR(100),
    pub_address VARCHAR(200),
    member_name VARCHAR(50),
    member_phone VARCHAR(20),
    borrow_date DATE,
    return_date DATE,
    librarian VARCHAR(50)
);
```

#### 1NF 적용
```sql
-- 작가 정보를 별도 테이블로 분리
CREATE TABLE books (
    book_id INT PRIMARY KEY,
    book_title VARCHAR(200),
    publisher VARCHAR(100),
    pub_address VARCHAR(200)
);

CREATE TABLE authors (
    author_id INT PRIMARY KEY,
    author_name VARCHAR(50)
);

CREATE TABLE book_authors (
    book_id INT,
    author_id INT,
    PRIMARY KEY (book_id, author_id)
);

CREATE TABLE borrowing_records (
    record_id INT PRIMARY KEY,
    book_id INT,
    member_name VARCHAR(50),
    member_phone VARCHAR(20),
    borrow_date DATE,
    return_date DATE,
    librarian VARCHAR(50)
);
```

#### 2NF 적용
```sql
-- 회원 정보 분리 (member_phone이 member_name에 종속)
CREATE TABLE members (
    member_id INT PRIMARY KEY,
    member_name VARCHAR(50),
    member_phone VARCHAR(20)
);

-- 대출 기록 테이블 수정
CREATE TABLE borrowing_records (
    record_id INT PRIMARY KEY,
    book_id INT,
    member_id INT,
    borrow_date DATE,
    return_date DATE,
    librarian VARCHAR(50)
);
```

#### 3NF 적용
```sql
-- 출판사 정보 분리 (pub_address가 publisher에 종속)
CREATE TABLE publishers (
    publisher_id INT PRIMARY KEY,
    publisher_name VARCHAR(100),
    pub_address VARCHAR(200)
);

-- 도서 테이블 수정
CREATE TABLE books (
    book_id INT PRIMARY KEY,
    book_title VARCHAR(200),
    publisher_id INT,
    FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
);

-- 사서 정보 분리
CREATE TABLE librarians (
    librarian_id INT PRIMARY KEY,
    librarian_name VARCHAR(50)
);

-- 대출 기록 테이블 최종
CREATE TABLE borrowing_records (
    record_id INT PRIMARY KEY,
    book_id INT,
    member_id INT,
    librarian_id INT,
    borrow_date DATE,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES books(book_id),
    FOREIGN KEY (member_id) REFERENCES members(member_id),
    FOREIGN KEY (librarian_id) REFERENCES librarians(librarian_id)
);
```

## 8.2 트랜잭션 실습

### 시나리오: 온라인 쇼핑몰 주문 처리

```sql
-- 주문 처리 트랜잭션
START TRANSACTION;

-- 1. 재고 확인
SELECT stock_quantity 
FROM products 
WHERE product_id = 'P001';

-- 2. 재고 차감
UPDATE products 
SET stock_quantity = stock_quantity - 2
WHERE product_id = 'P001' AND stock_quantity >= 2;

-- 3. 주문 생성
INSERT INTO orders (order_id, customer_id, order_date, total_amount)
VALUES ('O001', 'C001', NOW(), 50000);

-- 4. 주문 상세 생성
INSERT INTO order_details (order_id, product_id, quantity, unit_price)
VALUES ('O001', 'P001', 2, 25000);

-- 5. 고객 포인트 차감
UPDATE customers 
SET points = points - 1000
WHERE customer_id = 'C001' AND points >= 1000;

-- 모든 작업이 성공하면 커밋
COMMIT;

-- 실패 시 롤백 예제
-- ROLLBACK;
```

### 저장점을 활용한 트랜잭션
```sql
START TRANSACTION;

-- 첫 번째 작업
UPDATE accounts SET balance = balance - 10000 WHERE account_id = 'A001';
SAVEPOINT sp1;

-- 두 번째 작업
UPDATE accounts SET balance = balance + 10000 WHERE account_id = 'A002';
SAVEPOINT sp2;

-- 세 번째 작업 (실패할 수 있음)
UPDATE accounts SET balance = balance - 5000 WHERE account_id = 'A003';

-- 세 번째 작업만 취소하고 첫 번째, 두 번째 작업은 유지
ROLLBACK TO sp2;

-- 최종 커밋
COMMIT;
```

---

# 9. 정규화 vs 비정규화

## 9.1 비정규화 (Denormalization)

### 정의
**성능 향상을 위해 의도적으로 정규화 규칙을 위반하여 중복을 허용하는 것**

### 비정규화가 필요한 경우
- **조회 성능이 중요한 경우**: OLAP, 데이터 웨어하우스
- **조인 비용이 큰 경우**: 대용량 데이터에서 복잡한 조인
- **실시간 응답이 필요한 경우**: 웹 서비스의 빠른 응답

### 비정규화 기법
```sql
-- 계산된 컬럼 추가 (주문 총액을 미리 계산하여 저장)
CREATE TABLE orders (
    order_id VARCHAR(10) PRIMARY KEY,
    customer_id VARCHAR(10),
    order_date DATE,
    total_amount DECIMAL(10,2),  -- 비정규화: 계산값 저장
    item_count INT               -- 비정규화: 주문 항목 수
);

-- 중복 컬럼 추가 (자주 조회되는 고객명을 주문 테이블에 중복 저장)
CREATE TABLE orders (
    order_id VARCHAR(10) PRIMARY KEY,
    customer_id VARCHAR(10),
    customer_name VARCHAR(50),   -- 비정규화: customers 테이블과 중복
    order_date DATE,
    total_amount DECIMAL(10,2)
);
```

## 9.2 정규화 vs 비정규화 선택 기준

| 구분 | 정규화 | 비정규화 |
|------|--------|----------|
| **데이터 무결성** | 높음 | 낮음 |
| **저장 공간** | 효율적 | 비효율적 |
| **조회 성능** | 낮을 수 있음 | 높음 |
| **갱신 성능** | 높음 | 낮을 수 있음 |
| **유지보수** | 쉬움 | 어려움 |
| **적용 분야** | OLTP 시스템 | OLAP, 데이터 웨어하우스 |

---

# 10. 실전 팁과 베스트 프랙티스

## 10.1 정규화 설계 팁

### ✅ 해야 할 것
- **단계적 정규화**: 1NF → 2NF → 3NF 순서로 진행
- **함수 종속성 분석**: 어떤 속성이 어떤 속성을 결정하는지 명확히 파악
- **업무 규칙 반영**: 실제 비즈니스 로직을 고려한 설계
- **성능 테스트**: 정규화 후 성능 영향 확인

### ❌ 하지 말아야 할 것
- **과도한 정규화**: 실용성을 무시한 지나친 분해
- **성능 무시**: 조회 성능을 전혀 고려하지 않는 설계
- **업무 특성 무시**: 비즈니스 요구사항을 반영하지 않는 설계

## 10.2 트랜잭션 설계 팁

### ✅ 베스트 프랙티스
```sql
-- 1. 트랜잭션을 가능한 짧게 유지
START TRANSACTION;
-- 필요한 작업만 수행
UPDATE accounts SET balance = balance - 1000 WHERE id = 1;
INSERT INTO transactions (from_account, amount) VALUES (1, 1000);
COMMIT;

-- 2. 적절한 격리 수준 설정
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

-- 3. 데드락 방지를 위한 일관된 순서
-- 항상 작은 ID부터 큰 ID 순으로 락 획득
```

### ❌ 피해야 할 것
```sql
-- 1. 너무 긴 트랜잭션 (피해야 함)
START TRANSACTION;
-- 수많은 작업들...
-- 사용자 입력 대기...
-- 복잡한 계산...
COMMIT;  -- 너무 늦은 커밋

-- 2. 트랜잭션 내에서 사용자 상호작용 (피해야 함)
START TRANSACTION;
UPDATE products SET stock = stock - 1 WHERE id = 1;
-- 사용자에게 확인 메시지 표시하고 응답 대기... (위험!)
COMMIT;
```

---

# 11. 요약 및 체크리스트

## 11.1 정규화 체크리스트

### 1NF 체크사항
- [ ] 모든 속성이 원자값인가?
- [ ] 반복되는 그룹이나 배열이 없는가?
- [ ] 각 행이 고유한가?

### 2NF 체크사항
- [ ] 1NF를 만족하는가?
- [ ] 복합 기본키가 있는가?
- [ ] 모든 비키 속성이 기본키 전체에 종속되는가?
- [ ] 부분 함수 종속이 없는가?

### 3NF 체크사항
- [ ] 2NF를 만족하는가?
- [ ] 이행 함수 종속이 있는가?
- [ ] 비키 속성들 간의 종속성이 없는가?

### BCNF 체크사항
- [ ] 3NF를 만족하는가?
- [ ] 모든 결정자가 후보키인가?
- [ ] 키가 아닌 결정자가 있는가?

## 11.2 트랜잭션 체크리스트

### ACID 속성 확인
- [ ] **원자성**: 모든 작업이 성공하거나 모두 실패하는가?
- [ ] **일관성**: 제약조건을 위반하지 않는가?
- [ ] **독립성**: 동시 실행되는 다른 트랜잭션과 간섭하지 않는가?
- [ ] **지속성**: 커밋된 결과가 영구적으로 보존되는가?

### 성능 최적화
- [ ] 트랜잭션이 가능한 짧은가?
- [ ] 불필요한 락을 오래 유지하지 않는가?
- [ ] 데드락 가능성을 고려했는가?
- [ ] 적절한 격리 수준을 선택했는가?

---

**💡 핵심 포인트**

1. **정규화는 단계적으로**: 1NF → 2NF → 3NF → BCNF 순서 준수
2. **함수 종속성 이해**: 어떤 속성이 어떤 속성을 결정하는지 파악
3. **비즈니스 요구사항 고려**: 이론적 완벽함보다 실용성 중시
4. **성능과 무결성의 균형**: 정규화와 비정규화의 적절한 조합
5. **트랜잭션은 ACID 준수**: 데이터 일관성과 무결성 보장

이 가이드를 통해 데이터베이스 정규화와 트랜잭션의 개념을 체계적으로 이해하고 실무에 적용해보시기 바랍니다! 🚀 