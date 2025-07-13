# MySQL 튜닝 완벽 가이드

**강사**: 백현숙  
**자료 위치**: https://url.kr/jtmlkw

---

## 목차

1. [MySQL 개요](#1-mysql-개요)
2. [MySQL 설치 및 환경설정](#2-mysql-설치-및-환경설정)
3. [SQL 튜닝 기초](#3-sql-튜닝-기초)
4. [데이터베이스 구조 이해](#4-데이터베이스-구조-이해)
5. [인덱스 최적화](#5-인덱스-최적화)
6. [쿼리 최적화](#6-쿼리-최적화)
7. [실행계획 분석](#7-실행계획-분석)
8. [물리적 튜닝](#8-물리적-튜닝)

---

# 1. MySQL 개요

## 1.1 MySQL의 특징

### 장점
- **오픈 소스** (현재는 Oracle 소유로 유료화)
- **다양한 운영체제 지원**: Windows, Linux, macOS
- **높은 성능과 확장성**: 대용량 데이터 처리 시에도 빠른 쿼리 실행
- **표준 SQL 지원**: 널리 알려진 표준 SQL 형식 사용
- **강력한 보안 기능**: 사용자 권한 관리 및 데이터 암호화
- **풍부한 기능**: 스토어드 프로시저, 트리거, 커서, 업데이트 가능한 뷰

## 1.2 MySQL vs MariaDB 비교

| 구분 | MySQL | MariaDB |
|------|-------|---------|
| **라이선스** | Oracle 소유, 상용/오픈소스 혼재 | 완전한 GPL 오픈소스 |
| **지원** | Oracle 상용 지원 | 커뮤니티 주도 개발 |
| **스토리지 엔진** | InnoDB, MyISAM 등 제한적 | 더 많은 스토리지 엔진 지원 |
| **성능** | 트랜잭션 처리와 데이터 무결성 중시 | 병렬 쿼리, 대규모 데이터 처리에 유리 |
| **개발 속도** | 안정성 중심의 정기 업데이트 | 빠른 기능 추가 및 성능 개선 |

---

# 2. MySQL 설치 및 환경설정

## 2.1 MariaDB 설치

### 다운로드 및 설치
```bash
# 다운로드 위치
https://downloads.mariadb.com/MariaDB/mariadb-10.5.8/

# 설치 과정
1. C:\mariadb에 압축 해제
2. CMD를 관리자 권한으로 실행
3. cd /mariadb/bin
4. mysql_install_db --datadir=C:\mariadb\data --service=mariaDBZip --port=3306 --password=1234
```

### 환경변수 설정
1. 내 PC → 마우스 오른쪽 → 속성
2. 고급 시스템 설정 → 환경변수
3. 시스템 변수 → Path 편집
4. 새로 만들기 → `C:\mariadb\bin` 추가

### 서비스 시작 및 접속
```bash
# 서비스 시작 (Windows 서비스에서 MariaDB 시작)

# 데이터베이스 접속
mysql -u root -p --port=3306
# 패스워드: 1234

# 데이터베이스 생성
create database mydb default character set utf8 collate utf8_general_ci;

# 사용자 계정 생성
create user 'user01'@'localhost' identified by '1234';
grant all privileges on mydb.* TO user01@localhost;
```

## 2.2 MySQL 설치

### 다운로드 및 설치
```bash
# 다운로드 위치
https://dev.mysql.com/downloads/mysql
# 8.4.3 안정화 버전 권장

# 워크벤치 다운로드
https://dev.mysql.com/downloads/workbench/

# 설치 시 주의사항
- 기존 MySQL/MariaDB가 있을 경우 포트 번호 변경 (기본: 3306)
- 패스워드: 1234
- 샘플 데이터베이스 선택 (Sakila, World Database)
```

### 설치 확인
```sql
-- 접속 확인
mysql -u root -p

-- 데이터베이스 확인
show databases;

-- Sakila 데이터베이스 사용
use sakila;
show tables;

-- 테이블 구조 확인
desc actor;
```

## 2.3 튜닝 준비 작업

### 데모 데이터 설치
```bash
# demobld.sql 파일 실행
cd C:\내자료\MYSQL\SQLtune-main\SQLtune-main\
mysql -u root -p < demobld.sql

# data_setting.sql 파일 실행
mysql -u root -p < data_setting.sql

# 데이터 확인
mysql -u root -p
show databases;
use tuning;
show tables;
select count(1) from 사원;
```

### 패스워드 분실 시 복구
```bash
net stop mysql80                                    # MySQL 서비스 종료
mysqld --skip-grant-tables --skip-networking        # 안전모드 로그온
mysql -u root
ALTER USER 'root'@'localhost' IDENTIFIED BY '1234';
FLUSH PRIVILEGES;
```

---

# 3. SQL 튜닝 기초

## 3.1 SQL 튜닝이란?

### 정의
**최소한의 CPU-IO-메모리를 사용하여 최대한 빠른 시간 내에 원하는 데이터 작업을 수행하도록 만드는 것**

### 주요 용어
- **데이터베이스**: 데이터들의 집합체
- **DBMS**: Database Management System (Oracle, MS-SQL, MySQL 등)
- **SQL**: Structured Query Language (데이터베이스 조작 언어)

## 3.2 SQL 튜닝의 필요성

### 문제점
1. **개발자 역량 차이**: 모든 개발자가 일정 수준 이상의 SQL 구사 능력을 갖지 못함
2. **환경 차이**: 개발환경과 운영환경의 데이터량 및 구성 차이
3. **성능 저하**: SQL 역량 부족으로 인한 비효율적인 쿼리 작성

### 해결 방안
- 단위/통합 테스트에서 성능 문제 SQL 식별
- 최적화된 SQL로 개선하여 성능 향상
- 실행계획 분석을 통한 사전 검증

## 3.3 SQL 튜닝 시점

### 분석 및 설계 단계
- 사용자 데이터 처리 및 조회 패턴 분석
- 중요 업무 화면의 SQL 성능 최적화 고려
- 업무 성격에 따른 최적화된 데이터 모델링
- 최적의 실행계획을 위한 DBMS 파라미터 설정

### 개발 및 구현 단계
- 테스트를 통한 병목현상 모니터링 및 최적화
- 개발환경과 운영환경의 차이점 고려

### 운영 단계
- 예상치 못한 데이터 및 사용량 증가에 따른 성능 저하 대응

---

# 4. 데이터베이스 구조 이해

## 4.1 관계형 데이터베이스 구조

### 기본 구성요소
- **테이블(Table)**: 2차원 표 형태의 데이터 저장 공간
- **행(Row)**: 하나의 개체를 구성하는 값들의 가로 집합
- **열(Column)**: 데이터의 공통 특성을 정의하는 세로 집합
- **인덱스(Index)**: 데이터 검색 속도 향상을 위한 색인
- **뷰(View)**: 하나 이상의 테이블에서 파생된 가상 테이블

## 4.2 제약조건 (Constraints)

### Primary Key (기본키)
```sql
-- Primary Key 추가
ALTER TABLE 테이블명 ADD PRIMARY KEY(필드명);

-- Primary Key 삭제
ALTER TABLE 테이블명 DROP PRIMARY KEY;

-- 예시
ALTER TABLE emp ADD PRIMARY KEY(empno);
SHOW INDEX FROM emp;
```

**특징**:
- NULL 값 허용하지 않음
- 중복 값 허용하지 않음
- 테이블당 하나만 존재 가능
- 자동으로 인덱스 생성
- MySQL에서 auto_increment 사용 시 반드시 필요

### Foreign Key (외부키)
```sql
-- Foreign Key 추가
ALTER TABLE [자식테이블] ADD CONSTRAINT [제약조건명] 
FOREIGN KEY(컬럼명) REFERENCES [부모테이블](PK컬럼명);

-- Foreign Key 삭제
ALTER TABLE [테이블명] DROP FOREIGN KEY [제약조건명];

-- 예시
ALTER TABLE dept ADD CONSTRAINT PRIMARY KEY (deptno);
ALTER TABLE emp ADD CONSTRAINT fk_emp_dept 
FOREIGN KEY(deptno) REFERENCES dept(deptno);
```

---

# 5. 인덱스 최적화

## 5.1 인덱스 개념

### 정의
**데이터베이스에서 키값으로 실제 데이터 위치를 식별하고 데이터 접근 속도를 높이기 위해 생성되는 키 기준으로 정렬된 객체**

### 인덱스 vs Full Table Scan
- **순차검색**: 처음부터 차례대로 찾는 방식 (느림)
- **인덱스 검색**: 색인을 통해 빠르게 찾는 방식 (빠름)

## 5.2 인덱스 종류

### 1) Primary Index (기본키 인덱스)
```sql
-- Primary Key 지정 시 자동 생성
ALTER TABLE emp ADD PRIMARY KEY(empno);
```
- 테이블당 하나만 존재
- 자동으로 클러스터링 인덱스 생성
- 데이터를 인덱스 순서대로 물리적 정렬

### 2) Unique Index (고유 인덱스)
```sql
-- Unique 제약조건 추가 후 인덱스 생성
ALTER TABLE 테이블명 ADD CONSTRAINT 제약조건명 UNIQUE(필드);
CREATE UNIQUE INDEX idx_users_email ON users(email);
```
- 중복값 허용하지 않음
- NULL 값 허용 가능
- Primary Key와 유사하지만 NULL 허용

### 3) 일반 Index (보조 인덱스)
```sql
CREATE INDEX idx_users_name ON users(name);
```
- 중복값 허용
- 검색 속도 향상이 주 목적
- WHERE, ORDER BY, JOIN 절에 사용되는 컬럼에 적합

### 4) Fulltext Index (전문 검색 인덱스)
```sql
CREATE FULLTEXT INDEX idx_post_content ON posts(content);
SELECT * FROM posts WHERE MATCH(content) AGAINST('MySQL');
```
- 긴 텍스트에서 빠른 검색
- LIKE 대신 MATCH() AGAINST() 사용
- '%단어%' 형태의 LIKE보다 효율적

### 5) Composite Index (복합 인덱스)
```sql
CREATE INDEX idx_users_name_email ON users(name, email);
```
- 여러 컬럼을 묶어서 하나의 인덱스 생성
- 왼쪽 컬럼부터 순서대로 사용해야 효과적
- WHERE 조건에서 여러 컬럼 동시 검색 시 유용

### 6) 함수 기반 인덱스 (MySQL 8.0+)
```sql
-- Generated Column + 인덱스
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    lower_name VARCHAR(255) GENERATED ALWAYS AS (LOWER(name)) STORED,
    INDEX idx_lower_name (lower_name)
);
```

## 5.3 인덱스 사용이 부적절한 경우

### 1) 데이터가 너무 적은 경우
- 작은 테이블에서는 인덱스 탐색 비용이 오히려 더 큼
- MySQL이 자동으로 Full Table Scan 선택

### 2) 결과 집합이 너무 큰 경우
- 전체 데이터의 대부분을 조회하는 경우
- 예: 성별 검색 (남/여 중 하나 선택 시 50% 데이터 조회)

### 3) 인덱스가 너무 많거나 비효율적인 경우
- INSERT, UPDATE, DELETE 성능 저하
- 불필요한 인덱스로 인한 공간 낭비

---

# 6. 쿼리 최적화

## 6.1 기본 SELECT 문

### 구문 구조
```sql
SELECT 필드1, 필드2, 필드3, ...
FROM 테이블명
WHERE 조건절
ORDER BY 필드1 [ASC|DESC];
```

### 별칭(Alias) 사용
```sql
-- AS 키워드 사용
SELECT ename AS 사원명, sal AS 급여 FROM emp;

-- 한글 별칭 (공백이나 특수문자 시 따옴표 필요)
SELECT ename AS "사원 이름", sal AS "월 급여" FROM emp;

-- 문자열 연결
SELECT CONCAT(ename, '님의 급여는 ', sal, '입니다') AS 급여정보 FROM emp;
```

## 6.2 조건절 최적화

### 비교 연산자
```sql
-- 기본 비교
SELECT * FROM emp WHERE sal = 3000;
SELECT * FROM emp WHERE sal > 2000;
SELECT * FROM emp WHERE hiredate < '1982-01-01';
```

### 범위 조건
```sql
-- BETWEEN AND
SELECT * FROM emp WHERE sal BETWEEN 2000 AND 3000;
SELECT * FROM emp WHERE hiredate BETWEEN '1981-01-01' AND '1981-12-31';
```

### IN 연산자 (매우 중요!)
```sql
-- 여러 값 중 하나와 일치
SELECT * FROM emp WHERE empno IN (7369, 7566, 7900);

-- NOT IN
SELECT * FROM emp WHERE empno NOT IN (7369, 7566, 7900);
```

### LIKE 연산자와 와일드카드
```sql
-- % : 여러 글자 대체
SELECT * FROM emp WHERE ename LIKE 'F%';     -- F로 시작
SELECT * FROM emp WHERE ename LIKE '%A%';    -- A 포함
SELECT * FROM emp WHERE ename LIKE '%N';     -- N으로 끝남

-- _ : 한 글자 대체
SELECT * FROM emp WHERE ename LIKE '_A%';    -- 두 번째 글자가 A
SELECT * FROM emp WHERE ename LIKE '__A%';   -- 세 번째 글자가 A
```

### NULL 처리
```sql
-- NULL 검색
SELECT * FROM emp WHERE comm IS NULL;
SELECT * FROM emp WHERE comm IS NOT NULL;

-- NULL 값 처리
SELECT ename, sal, IFNULL(comm, 0) AS commission FROM emp;
SELECT ename, sal * 12 + IFNULL(comm, 0) AS 연봉 FROM emp;
```

## 6.3 조인 최적화

### 조인 종류
```sql
-- INNER JOIN
SELECT e.empno, e.ename, d.dname
FROM emp e
INNER JOIN dept d ON e.deptno = d.deptno;

-- LEFT JOIN
SELECT e.empno, e.ename, d.dname
FROM emp e
LEFT JOIN dept d ON e.deptno = d.deptno;

-- RIGHT JOIN
SELECT e.empno, e.ename, d.dname
FROM emp e
RIGHT JOIN dept d ON e.deptno = d.deptno;
```

### 드라이빙 테이블 선택 전략

#### 드라이빙 테이블 선택 조건
1. **필터 조건이 많은 테이블** (WHERE 조건이 많은 테이블)
2. **선택도가 높은 테이블** (조건에 해당하는 비율이 낮은 테이블)
3. **작은 테이블** (특히 중간 결과가 클 때)
4. **인덱스가 있는 테이블을 드리븐으로**

#### 조인 방식

**1) 중첩 루프 조인 (Nested Loop Join)**
```sql
-- 드라이빙 테이블의 각 행마다 드리븐 테이블 검색
SELECT * FROM emp e JOIN dept d ON e.deptno = d.deptno;
```

**2) 해시 조인 (MySQL 8.0.18+)**
```sql
-- 대용량 테이블 간 조인에 효율적
SET optimizer_switch = 'hash_join=on';
SELECT /*+ HASH_JOIN(d) */ * FROM emp e JOIN dept d ON e.deptno = d.deptno;
```

## 6.4 서브쿼리 최적화

### 서브쿼리 종류
```sql
-- 스칼라 서브쿼리 (결과가 1개 값)
SELECT ename, sal, (SELECT AVG(sal) FROM emp) AS 평균급여 FROM emp;

-- 다중행 서브쿼리
SELECT * FROM emp WHERE deptno IN (SELECT deptno FROM dept WHERE loc = 'NEW YORK');

-- 상관 서브쿼리
SELECT * FROM emp e1 
WHERE sal > (SELECT AVG(sal) FROM emp e2 WHERE e2.deptno = e1.deptno);
```

## 6.5 페이징 최적화

### LIMIT 사용
```sql
-- 기본 페이징
SELECT * FROM emp LIMIT 0, 10;    -- 1페이지 (0~9)
SELECT * FROM emp LIMIT 10, 10;   -- 2페이지 (10~19)
SELECT * FROM emp LIMIT 20, 10;   -- 3페이지 (20~29)

-- 정렬과 함께 사용
SELECT * FROM emp ORDER BY empno LIMIT 0, 10;
```

---

# 7. 실행계획 분석

## 7.1 실행계획 기본

### EXPLAIN 명령어
```sql
-- 기본 실행계획
EXPLAIN SELECT * FROM emp WHERE empno = 7369;

-- 상세 실행계획
EXPLAIN FORMAT=TRADITIONAL SELECT * FROM emp WHERE empno = 7369;
```

## 7.2 실행계획 주요 컬럼

### type 컬럼 (성능 순서)

| Type | 성능 | 설명 | 예시 |
|------|------|------|------|
| **system** | 최고 | 레코드가 1건 또는 0건인 테이블 | MyISAM, MEMORY 엔진 |
| **const** | 최고 | PK나 Unique로 1건 조회 | `WHERE id = 1` |
| **eq_ref** | 우수 | 조인에서 PK/Unique 사용 | JOIN 시 1:1 매칭 |
| **ref** | 좋음 | 일반 인덱스로 동등 조건 검색 | `WHERE name = 'John'` |
| **ref_or_null** | 좋음 | ref + NULL 비교 | `WHERE name = 'John' OR name IS NULL` |
| **range** | 보통 | 인덱스 범위 검색 | `WHERE id BETWEEN 1 AND 100` |
| **index** | 나쁨 | 인덱스 풀 스캔 | ORDER BY만 있는 경우 |
| **ALL** | 최악 | 테이블 풀 스캔 | 인덱스를 전혀 사용하지 않음 |

### 실행계획 예시 분석

#### 1) 최적화된 쿼리 (type: const)
```sql
-- Primary Key 사용
EXPLAIN SELECT * FROM 사원 WHERE 사원번호 = 100000;
```
**결과**: type=const, rows=1 (최고 성능)

#### 2) 인덱스 사용 (type: ref)
```sql
-- 일반 인덱스 사용
EXPLAIN SELECT * FROM 사원 WHERE 입사일자 = '1989-08-24';
```
**결과**: type=ref, 인덱스를 통한 빠른 검색

#### 3) 범위 검색 (type: range)
```sql
-- 범위 조건
EXPLAIN SELECT * FROM 사원 WHERE 사원번호 < 100000;
```
**결과**: type=range, 인덱스 범위 스캔

#### 4) 풀 테이블 스캔 (type: ALL)
```sql
-- 인덱스가 없는 컬럼 검색
EXPLAIN SELECT * FROM 사원 WHERE 사원번호 = 100000;  -- 인덱스 없을 때
```
**결과**: type=ALL, rows=전체데이터수 (최악 성능)

## 7.3 실행계획 최적화 실습

### 인덱스 생성 전후 비교
```sql
-- 1. 인덱스 삭제
ALTER TABLE 사원 DROP PRIMARY KEY;
ALTER TABLE 사원 DROP INDEX I_입사일자;

-- 2. 인덱스 없을 때 실행계획
EXPLAIN SELECT * FROM 사원 WHERE 사원번호 = 10000;
-- 결과: type=ALL (풀 테이블 스캔)

-- 3. Primary Key 추가
ALTER TABLE 사원 ADD PRIMARY KEY (사원번호);

-- 4. 인덱스 있을 때 실행계획
EXPLAIN SELECT * FROM 사원 WHERE 사원번호 = 10000;
-- 결과: type=const (최적화됨)

-- 5. 일반 인덱스 추가
ALTER TABLE 사원 ADD INDEX I_입사일자(입사일자);

-- 6. 일반 인덱스 사용 확인
EXPLAIN SELECT * FROM 사원 WHERE 입사일자 = '1989-08-24';
-- 결과: type=ref
```

---

# 8. 물리적 튜닝

## 8.1 인덱스 최적화

### 인덱스 종류별 특성
```sql
-- B-Tree 인덱스 (기본)
CREATE INDEX idx_name ON users(name);

-- Hash 인덱스 (MEMORY 엔진 전용)
CREATE TABLE temp_table (
    id INT,
    name VARCHAR(50),
    INDEX USING HASH (id)
) ENGINE=MEMORY;

-- Fulltext 인덱스
CREATE FULLTEXT INDEX idx_content ON posts(content);

-- Spatial 인덱스 (GIS 데이터)
CREATE TABLE locations (
    id INT PRIMARY KEY,
    coordinates POINT NOT NULL,
    SPATIAL INDEX(coordinates)
);
```

## 8.2 스토리지 엔진 선택

### 주요 스토리지 엔진
| 엔진 | 특징 | 사용 사례 |
|------|------|-----------|
| **InnoDB** | ACID 보장, 트랜잭션, 외래키 지원 | 대부분의 경우 (권장) |
| **MyISAM** | 빠른 읽기, 트랜잭션 없음 | 읽기 전용, 로그 데이터 |
| **MEMORY** | 메모리 저장, 휘발성 | 임시 데이터, 캐시 |
| **ARCHIVE** | 압축 저장, 검색 성능 낮음 | 대량 저장용 |

## 8.3 테이블 파티셔닝

### 파티셔닝 예시
```sql
-- 날짜별 파티셔닝
CREATE TABLE sales (
    id INT,
    sale_date DATE,
    amount DECIMAL(10,2)
)
PARTITION BY RANGE(YEAR(sale_date)) (
    PARTITION p2023 VALUES LESS THAN (2024),
    PARTITION p2024 VALUES LESS THAN (2025),
    PARTITION p2025 VALUES LESS THAN (2026)
);
```

**장점**:
- 큰 테이블을 물리적으로 분할
- 분산 처리로 검색 성능 향상
- 특정 파티션만 백업/복구 가능

## 8.4 서버 설정 최적화

### 주요 설정 파라미터
```sql
-- InnoDB 버퍼 풀 크기 (전체 메모리의 60~70%)
SET innodb_buffer_pool_size = '4G';

-- 임시 테이블 크기
SET tmp_table_size = '256M';
SET max_heap_table_size = '256M';

-- 쿼리 캐시 (MySQL 5.7까지)
SET query_cache_size = '128M';

-- 배치 키 액세스 활성화
SET optimizer_switch = 'batched_key_access=on';

-- 해시 조인 활성화 (MySQL 8.0.18+)
SET optimizer_switch = 'hash_join=on';
```

## 8.5 디스크 I/O 최적화

### 하드웨어 최적화
- **SSD 사용**: HDD보다 훨씬 빠른 I/O
- **RAID 구성**: 성능과 안정성 강화
- **파일 분리**: 데이터 파일과 로그 파일을 다른 디스크에 분리

### 테이블 압축
```sql
-- InnoDB 압축 테이블
CREATE TABLE compressed_table (
    id INT PRIMARY KEY,
    data TEXT
) ENGINE=InnoDB ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
```

---

# 9. SQL 문제 유형 및 해결방안

## 9.1 인덱스 관련 문제

### 문제 유형
- 조건절에서 비교하는 컬럼에 인덱스가 없는 경우
- 조인 조건으로 사용된 컬럼에 인덱스가 없는 경우
- 조건절에서 사용한 컬럼의 변형으로 인덱스를 사용할 수 없는 경우
- LIKE에서 앞에 '%' 사용으로 인덱스를 사용할 수 없는 경우

### 해결방안
```sql
-- 나쁜 예: 함수 사용으로 인덱스 사용 불가
SELECT * FROM emp WHERE UPPER(ename) = 'SMITH';

-- 좋은 예: 조건 변경으로 인덱스 사용
SELECT * FROM emp WHERE ename = 'SMITH';

-- 나쁜 예: 앞에 % 사용
SELECT * FROM emp WHERE ename LIKE '%ITH';

-- 좋은 예: 뒤에 % 사용
SELECT * FROM emp WHERE ename LIKE 'SM%';
```

## 9.2 조인 관련 문제

### 문제 유형
- 드라이빙 테이블을 잘못 선정하여 비용이 증가한 경우
- 비효율적인 조인 순서로 비용이 증가한 경우
- 조인 후 GROUP BY 수행으로 비용이 증가한 경우

### 해결방안
```sql
-- 작은 테이블을 드라이빙 테이블로 사용
SELECT /*+ USE_INDEX(e, idx_deptno) */ 
       e.ename, d.dname
FROM emp e
JOIN dept d ON e.deptno = d.deptno
WHERE e.sal > 2000;  -- 필터 조건이 있는 테이블을 드라이빙으로
```

---

# 10. 실전 튜닝 체크리스트

## 10.1 쿼리 작성 시 체크사항

### ✅ 기본 체크리스트
- [ ] WHERE 절에 사용되는 컬럼에 인덱스가 있는가?
- [ ] 조인 조건에 사용되는 컬럼에 인덱스가 있는가?
- [ ] LIKE 사용 시 앞에 '%'를 피했는가?
- [ ] 함수를 조건절에 사용하지 않았는가?
- [ ] NULL 비교 시 IS NULL/IS NOT NULL을 사용했는가?
- [ ] 서브쿼리보다 조인이 더 효율적이지 않은가?

### ✅ 성능 체크리스트
- [ ] 실행계획에서 type이 ALL(풀 스캔)이 아닌가?
- [ ] 예상 rows 수가 적절한가?
- [ ] 불필요한 컬럼을 SELECT하지 않았는가?
- [ ] ORDER BY, GROUP BY에 필요한 인덱스가 있는가?
- [ ] LIMIT을 사용하여 불필요한 데이터 조회를 피했는가?

## 10.2 튜닝 우선순위

### 1순위: 실행계획 분석
```sql
EXPLAIN SELECT * FROM 테이블명 WHERE 조건;
```

### 2순위: 인덱스 최적화
```sql
-- 필요한 인덱스 추가
CREATE INDEX idx_컬럼명 ON 테이블명(컬럼명);

-- 불필요한 인덱스 제거
DROP INDEX idx_불필요인덱스 ON 테이블명;
```

### 3순위: 쿼리 재작성
```sql
-- 서브쿼리를 조인으로 변경
-- EXISTS 사용 고려
-- UNION 대신 OR 조건 사용 검토
```

### 4순위: 물리적 튜닝
- 서버 설정 최적화
- 하드웨어 업그레이드
- 파티셔닝 적용

---

# 11. 참고자료

## 공식 문서
- [MySQL 8.0 Reference Manual](https://dev.mysql.com/doc/refman/8.0/en/)
- [MySQL Performance Schema](https://dev.mysql.com/doc/refman/8.0/en/performance-schema.html)

## 유용한 블로그 및 자료
- [MySQL 실행계획 분석](https://velog.io/@ddongh1122/MySQL-%EC%8B%A4%ED%96%89%EA%B3%84%ED%9A%8D2-EXPLAIN)
- [SQL 튜닝 용어 정리](https://velog.io/@mj3242/SQL-%ED%8A%9C%EB%8B%9D-%EC%9A%A9%EC%96%B4-%EC%A7%81%EA%B4%80%EC%A0%81-%EC%9D%B4%ED%95%B4-%EA%B0%9C%EB%85%90%EC%A0%81%EC%9D%B8-%ED%8A%9C%EB%8B%9D-%EC%9A%A9%EC%96%B4)
- [MySQL JOIN 이해하기](https://velog.io/@youjung/g/MySQL-JOIN)

## 실습 환경
- **자료 다운로드**: https://url.kr/jtmlkw
- **MySQL 공식 다운로드**: https://dev.mysql.com/downloads/
- **MariaDB 다운로드**: https://downloads.mariadb.com/

---

**💡 핵심 포인트**
1. **실행계획을 항상 확인하라** - EXPLAIN은 튜닝의 시작점
2. **인덱스를 적절히 활용하라** - 하지만 너무 많으면 오히려 독
3. **작은 테이블부터 조인하라** - 드라이빙 테이블 선택이 중요
4. **쿼리를 단순하게 작성하라** - 복잡한 쿼리는 최적화가 어려움
5. **정기적으로 통계정보를 갱신하라** - 옵티마이저의 정확한 판단을 위해

이 가이드를 통해 MySQL 튜닝의 기초부터 고급 기법까지 체계적으로 학습하고 실무에 적용해보시기 바랍니다! 