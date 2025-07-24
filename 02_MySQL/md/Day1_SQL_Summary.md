# 🚀 Day 1: SQL 기초 및 환경 설정

##### 📅 학습 기간: 2025.05.14 ~ 2025.05.16 (3일)
##### 🎯 학습 목표: MySQL 환경 구축 + SQL 기본 개념 마스터
##### 📝 Writer : Moon19ht

---

## 📋 Day 1 학습 체크리스트

- [x] MySQL 설치 및 초기 설정 완료
- [x] Workbench 또는 DBeaver 연결 확인
- [x] SQL 기본 개념 이해
- [x] 데이터 타입 7가지 이상 암기
- [x] 기본 테이블 생성 및 데이터 삽입 실습
- [x] SELECT 문 기본 문법 5가지 이상 실습

---

## 🔧 STEP 1: MySQL 환경 설정 (30분)

### 1.1 MySQL 설치

#### 📥 Windows 설치
```bash
# 1. MySQL 공식 사이트 접속
https://dev.mysql.com/downloads/installer/

# 2. MySQL Installer 다운로드
- "Windows (x86, 32-bit), MSI Installer" 선택
- "mysql-installer-web-community" 또는 "mysql-installer-community" 다운로드

# 3. 설치 옵션 선택
- Developer Default (개발용 모든 도구 포함) ✅ 권장
- Custom (선택적 설치)
```

#### ⚙️ 초기 설정
```sql
-- 설치 과정에서 설정할 항목들
Port Number: 3306 (기본값 유지)
Root Password: ******** (강력한 비밀번호 설정)
Authentication Method: "Use Strong Password Encryption" 선택
Windows Service: MySQL80 (자동 시작 설정)
```

#### 🔍 설치 확인
```bash
# 명령 프롬프트에서 확인
mysql --version

# 또는 MySQL 서비스 상태 확인
services.msc 에서 MySQL80 서비스 확인
```

### 1.2 GUI 도구 설정

#### 🛠️ MySQL Workbench 연결
```sql
-- 연결 설정
Connection Name: Local MySQL
Hostname: localhost (또는 127.0.0.1)
Port: 3306
Username: root
Password: [설치 시 설정한 비밀번호]

-- 연결 테스트
Test Connection 클릭하여 연결 확인
```

#### 🔧 대안 도구: DBeaver (선택사항)
```bash
# DBeaver 설치 (무료)
https://dbeaver.io/download/

# 연결 설정
Driver: MySQL
Server Host: localhost
Port: 3306
Database: (비워둠)
Username: root
Password: [MySQL root 비밀번호]
```

---

## 📚 STEP 2: SQL 기본 개념 이해 (45분)

### 2.1 SQL이란?

#### 🔍 정의
**SQL (Structured Query Language)**
- 관계형 데이터베이스의 표준 언어
- 데이터의 생성, 조회, 수정, 삭제를 위한 언어
- ANSI/ISO 표준으로 대부분 DBMS에서 공통 사용

#### 🗂️ SQL 명령어 4가지 분류
| 분류 | 전체 이름 | 주요 명령어 | 역할 | 실무 빈도 |
|------|-----------|-------------|------|----------|
| **DDL** | Data Definition Language | `CREATE`, `ALTER`, `DROP` | 테이블 구조 정의 | ⭐⭐⭐ |
| **DML** | Data Manipulation Language | `SELECT`, `INSERT`, `UPDATE`, `DELETE` | 데이터 조작 | ⭐⭐⭐⭐⭐ |
| **DCL** | Data Control Language | `GRANT`, `REVOKE` | 권한 제어 | ⭐⭐ |
| **TCL** | Transaction Control Language | `COMMIT`, `ROLLBACK` | 트랜잭션 제어 | ⭐⭐⭐⭐ |

### 2.2 관계형 데이터베이스 구조

#### 📊 기본 구성 요소
```
데이터베이스 (Database)
    └── 테이블 (Table) - 엑셀의 시트와 유사
        ├── 행 (Row/Record) - 하나의 데이터 레코드
        └── 열 (Column/Field) - 데이터의 속성
```

#### 🏢 실무 예시: 회사 직원 관리 시스템
```sql
-- 회사 데이터베이스 구조 예시
company_db
├── employees (직원 테이블)
│   ├── id (직원번호)
│   ├── name (이름)
│   ├── department (부서)
│   └── salary (급여)
├── departments (부서 테이블)
│   ├── dept_id (부서번호)
│   ├── dept_name (부서명)
│   └── location (위치)
└── projects (프로젝트 테이블)
    ├── project_id (프로젝트번호)
    ├── project_name (프로젝트명)
    └── deadline (마감일)
```

---

## 🎯 STEP 3: 데이터 타입 완전 정복 (30분)

### 3.1 숫자형 데이터 타입

| 타입 | 크기 | 범위 | 실무 용도 | 예시 |
|------|------|------|----------|------|
| `TINYINT` | 1바이트 | -128 ~ 127 | 나이, 등급 | `age TINYINT` |
| `INT` | 4바이트 | -21억 ~ 21억 | ID, 수량 | `employee_id INT` |
| `BIGINT` | 8바이트 | 매우 큰 수 | 전화번호, 계좌번호 | `phone_number BIGINT` |
| `DECIMAL(p,s)` | 가변 | 정확한 소수 | 금액, 평점 | `salary DECIMAL(10,2)` |
| `FLOAT` | 4바이트 | 근사 소수 | 측정값 | `height FLOAT` |

#### 💡 실무 팁
```sql
-- 금액은 반드시 DECIMAL 사용 (정확한 계산 필요)
price DECIMAL(10,2)  -- 최대 99,999,999.99까지 저장

-- ID는 대부분 INT 또는 BIGINT
user_id INT AUTO_INCREMENT PRIMARY KEY

-- 불린값은 TINYINT(1) 또는 BOOLEAN
is_active BOOLEAN DEFAULT TRUE
```

### 3.2 문자형 데이터 타입

| 타입 | 특징 | 최대 길이 | 실무 용도 | 예시 |
|------|------|----------|----------|------|
| `CHAR(n)` | 고정 길이 | 255자 | 코드, 상태 | `gender CHAR(1)` |
| `VARCHAR(n)` | 가변 길이 | 65,535자 | 이름, 이메일 | `name VARCHAR(50)` |
| `TEXT` | 긴 문자열 | 65,535자 | 설명, 내용 | `description TEXT` |
| `LONGTEXT` | 매우 긴 문자열 | 4GB | 게시글, 로그 | `content LONGTEXT` |

#### 💡 길이 설정 가이드
```sql
-- 일반적인 길이 설정
name VARCHAR(50)        -- 한국 이름: 10자 이내
email VARCHAR(100)      -- 이메일: 50-100자
phone VARCHAR(20)       -- 전화번호: 15자 내외
address VARCHAR(200)    -- 주소: 100-200자
```

### 3.3 날짜/시간 데이터 타입

| 타입 | 형식 | 범위 | 실무 용도 |
|------|------|------|----------|
| `DATE` | YYYY-MM-DD | 1000-01-01 ~ 9999-12-31 | 생년월일, 입사일 |
| `TIME` | HH:MM:SS | -838:59:59 ~ 838:59:59 | 근무시간, 경과시간 |
| `DATETIME` | YYYY-MM-DD HH:MM:SS | 1000년 ~ 9999년 | 생성일시, 수정일시 |
| `TIMESTAMP` | YYYY-MM-DD HH:MM:SS | 1970년 ~ 2038년 | 로그 시간 (UTC) |

#### 💡 실무 활용
```sql
-- 자동 시간 입력
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP

-- 날짜 계산 예시
SELECT DATEDIFF(NOW(), hire_date) AS days_worked FROM employees;
```

---

## 🏗️ STEP 4: 첫 번째 데이터베이스 만들기 (60분)

### 4.1 데이터베이스 생성

```sql
-- 1. 데이터베이스 생성
CREATE DATABASE my_first_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 2. 데이터베이스 선택
USE my_first_db;

-- 3. 생성된 데이터베이스 확인
SHOW DATABASES;
```

### 4.2 실습용 테이블 생성

#### 👥 직원 테이블 생성
```sql
CREATE TABLE employees (
    -- 기본키: 자동 증가하는 직원 ID
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    
    -- 필수 정보
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    
    -- 선택 정보
    department VARCHAR(30),
    position VARCHAR(50),
    salary DECIMAL(10,2),
    hire_date DATE,
    
    -- 시스템 정보
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

#### 🏢 부서 테이블 생성
```sql
CREATE TABLE departments (
    dept_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(50) NOT NULL UNIQUE,
    location VARCHAR(100),
    manager_name VARCHAR(50),
    budget DECIMAL(15,2),
    established_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### 📋 프로젝트 테이블 생성
```sql
CREATE TABLE projects (
    project_id INT PRIMARY KEY AUTO_INCREMENT,
    project_name VARCHAR(100) NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    status VARCHAR(20) DEFAULT 'Planning',
    budget DECIMAL(12,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 4.3 테이블 구조 확인

```sql
-- 테이블 구조 확인 (3가지 방법)
DESC employees;
DESCRIBE employees;
SHOW CREATE TABLE employees;

-- 모든 테이블 목록 보기
SHOW TABLES;
```

---

## 📝 STEP 5: 데이터 입력 및 기본 조회 (45분)

### 5.1 기본 데이터 입력

#### 👥 직원 데이터 입력
```sql
-- 단일 행 입력
INSERT INTO employees (name, email, department, position, salary, hire_date)
VALUES ('김철수', 'kim@company.com', '개발팀', 'Senior Developer', 5500000, '2024-01-15');

-- 여러 행 동시 입력
INSERT INTO employees (name, email, department, position, salary, hire_date)
VALUES 
    ('이영희', 'lee@company.com', '마케팅팀', 'Marketing Manager', 4800000, '2024-02-01'),
    ('박민수', 'park@company.com', '개발팀', 'Junior Developer', 3800000, '2024-02-15'),
    ('최지은', 'choi@company.com', '디자인팀', 'UI Designer', 4200000, '2024-03-01'),
    ('정호석', 'jung@company.com', '영업팀', 'Sales Manager', 5200000, '2024-01-20'),
    ('한미라', 'han@company.com', '인사팀', 'HR Specialist', 4000000, '2024-03-10');
```

#### 🏢 부서 데이터 입력
```sql
INSERT INTO departments (dept_name, location, manager_name, budget, established_date)
VALUES 
    ('개발팀', '서울 강남', '김철수', 50000000, '2020-01-01'),
    ('마케팅팀', '서울 홍대', '이영희', 30000000, '2020-06-01'),
    ('디자인팀', '서울 성수', '최지은', 20000000, '2021-01-01'),
    ('영업팀', '서울 명동', '정호석', 40000000, '2019-12-01'),
    ('인사팀', '서울 여의도', '한미라', 15000000, '2020-03-01');
```

#### 📋 프로젝트 데이터 입력
```sql
INSERT INTO projects (project_name, description, start_date, end_date, status, budget)
VALUES 
    ('쇼핑몰 리뉴얼', 'E-commerce 사이트 전면 개편', '2024-01-01', '2024-06-30', 'In Progress', 80000000),
    ('모바일 앱 개발', '신규 모바일 어플리케이션 개발', '2024-02-01', '2024-08-31', 'Planning', 120000000),
    ('브랜드 리뉴얼', '회사 브랜드 아이덴티티 개선', '2024-03-01', '2024-05-31', 'In Progress', 30000000),
    ('CRM 시스템 구축', '고객관리시스템 구축', '2024-04-01', '2024-12-31', 'Planning', 150000000);
```

### 5.2 기본 SELECT 문 마스터

#### 🔍 전체 조회
```sql
-- 모든 직원 정보 조회
SELECT * FROM employees;

-- 모든 부서 정보 조회
SELECT * FROM departments;
```

#### 🎯 특정 열만 조회
```sql
-- 직원 이름과 급여만 조회
SELECT name, salary FROM employees;

-- 부서 이름과 위치만 조회
SELECT dept_name, location FROM departments;
```

#### 📊 조건부 조회
```sql
-- 급여가 500만원 이상인 직원
SELECT name, salary, department FROM employees WHERE salary >= 5000000;

-- 개발팀 직원들만 조회
SELECT * FROM employees WHERE department = '개발팀';

-- 2024년 2월 이후 입사자
SELECT name, hire_date, department FROM employees WHERE hire_date >= '2024-02-01';
```

#### 📈 정렬
```sql
-- 급여 높은 순으로 정렬
SELECT name, salary, department FROM employees ORDER BY salary DESC;

-- 입사일 순으로 정렬
SELECT name, hire_date, department FROM employees ORDER BY hire_date ASC;

-- 부서별, 급여순 정렬
SELECT name, department, salary FROM employees ORDER BY department, salary DESC;
```

#### 🔢 개수 제한
```sql
-- 상위 3명만 조회
SELECT name, salary FROM employees ORDER BY salary DESC LIMIT 3;

-- 2번째부터 3개 조회 (페이징)
SELECT name, salary FROM employees ORDER BY salary DESC LIMIT 1, 3;
```

#### 🚫 중복 제거
```sql
-- 중복 없는 부서 목록
SELECT DISTINCT department FROM employees;

-- 중복 없는 직급 목록  
SELECT DISTINCT position FROM employees;
```

---

## 🎯 STEP 6: 실전 연습 문제 (30분)

### 💪 기본 연습 문제

#### 문제 1: 조건 조회
```sql
-- Q1. 급여가 400만원 이상 500만원 이하인 직원을 조회하세요
-- 💡 힌트: BETWEEN 사용

SELECT name, salary, department 
FROM employees 
WHERE salary BETWEEN 4000000 AND 5000000;
```

#### 문제 2: 패턴 검색
```sql
-- Q2. 이름에 '김'이 포함된 직원을 조회하세요
-- 💡 힌트: LIKE 사용

SELECT name, department, position 
FROM employees 
WHERE name LIKE '%김%';
```

#### 문제 3: 복합 조건
```sql
-- Q3. 개발팀이면서 급여가 400만원 이상인 직원을 조회하세요
-- 💡 힌트: AND 사용

SELECT name, salary, position 
FROM employees 
WHERE department = '개발팀' AND salary >= 4000000;
```

### 🏆 도전 문제

#### 문제 4: 집계 함수
```sql
-- Q4. 전체 직원 수와 평균 급여를 구하세요
-- 💡 힌트: COUNT(), AVG() 사용

SELECT 
    COUNT(*) AS total_employees,
    AVG(salary) AS average_salary
FROM employees;
```

#### 문제 5: 그룹 분석
```sql
-- Q5. 부서별 직원 수를 구하세요
-- 💡 힌트: GROUP BY 사용

SELECT 
    department,
    COUNT(*) AS employee_count
FROM employees 
GROUP BY department;
```

---

## 📚 STEP 7: 오늘의 핵심 정리 (15분)

### ✅ 완료 체크리스트
- [ ] MySQL 설치 및 연결 성공
- [ ] 기본 데이터베이스 생성 완료
- [ ] 테이블 3개 생성 (employees, departments, projects)
- [ ] 각 테이블에 데이터 삽입 완료
- [ ] SELECT 문 7가지 패턴 실습 완료

### 🎯 핵심 문법 요약

#### 필수 암기 문법
```sql
-- 1. 데이터베이스 관련
CREATE DATABASE db_name;
USE db_name;
SHOW DATABASES;

-- 2. 테이블 관련
CREATE TABLE table_name (column_definitions);
DROP TABLE table_name;
DESC table_name;

-- 3. 데이터 조작
INSERT INTO table_name (columns) VALUES (values);
SELECT columns FROM table_name WHERE conditions;
UPDATE table_name SET column=value WHERE conditions;
DELETE FROM table_name WHERE conditions;

-- 4. 조회 옵션
ORDER BY column ASC/DESC;
LIMIT number;
DISTINCT column;
```

### 💡 실무 팁 정리

1. **테이블 설계 시 주의사항**
   - 항상 PRIMARY KEY 설정
   - 문자열 길이 여유있게 설정
   - 날짜는 DATETIME보다 DATE 먼저 고려

2. **데이터 입력 시 주의사항**
   - 문자열은 반드시 따옴표로 감싸기
   - 날짜 형식은 'YYYY-MM-DD' 준수
   - NULL과 빈 문자열('')은 다름

3. **쿼리 작성 시 습관**
   - WHERE 절 없는 UPDATE/DELETE 금지
   - SELECT * 대신 필요한 컬럼만 명시
   - 정렬이 필요하면 ORDER BY 명시

---

## 🚀 내일 학습 예고: Day 2

### 📅 Day 2 학습 내용 (0517-0519)
- **고급 SELECT 문**: 복잡한 조건, 서브쿼리
- **데이터 수정 및 삭제**: UPDATE, DELETE 심화
- **제약조건**: FOREIGN KEY, CHECK, UNIQUE
- **기본 함수**: 문자열, 날짜, 수학 함수

### 🎯 준비사항
- [ ] 오늘 생성한 테이블과 데이터 유지
- [ ] 연습 문제 5개 모두 해결
- [ ] 기본 문법 7가지 복습

---

## ❓ FAQ

**Q1. MySQL이 시작되지 않아요**
```bash
# Windows 서비스에서 MySQL80 서비스 수동 시작
services.msc → MySQL80 → 시작

# 또는 명령어로 시작
net start mysql80
```

**Q2. 한글이 깨져요**
```sql
-- 데이터베이스 생성 시 utf8mb4 사용
CREATE DATABASE db_name CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

**Q3. 비밀번호를 잊었어요**
```bash
# MySQL 비밀번호 재설정 (관리자 권한 필요)
mysqld --skip-grant-tables
mysql -u root
ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';
```

**Q4. Workbench 연결이 안 돼요**
- 방화벽 설정 확인
- MySQL 서비스 상태 확인
- 호스트명, 포트, 비밀번호 재확인

---

## 📖 추가 학습 자료

### 🌐 온라인 자료
- [MySQL 공식 문서](https://dev.mysql.com/doc/)
- [W3Schools SQL Tutorial](https://www.w3schools.com/sql/)
- [프로그래머스 SQL 고득점 Kit](https://programmers.co.kr/learn/challenges?tab=sql_practice_kit)

### 📚 추천 도서
- "SQL 첫걸음" - 아사이 아츠시
- "Learning SQL" - Alan Beaulieu
- "MySQL로 배우는 데이터베이스 개론과 실습" - 박우창

---

💪 **첫날 고생하셨습니다! 내일은 더 재미있는 JOIN과 서브쿼리가 기다리고 있어요!** 🚀 