# MySQL 계정 만들기

## 기본 명령어

```bash
cd 경로명 
mysql -u root -p mydb < emp_dept_sample.sql
Enter your password : 1234 
```

## 새로운 계정 만들기

기본적으로 MySQL은 로컬에서만 접근 가능합니다.
- 로컬에서만 가능하다는 말은 DB서버(MySQL84)와 DB클라이언트(mysql, workbench, dbeavor, sqlgate, heidsql..)가 동일 컴퓨터에 존재할 때 접근 가능함을 의미합니다.
- 클라이언트가 다른 컴퓨터에 있을 때 접근 가능한 계정을 별도로 만들어줘야 합니다.
- 실무에서는 보통 phpMyAdmin이라는 웹사이트를 설치하여 이 사이트를 통해 접근합니다.

### 로컬 접근 계정 만들기

```sql
-- 기본 구문
CREATE USER '계정명'@'localhost' IDENTIFIED BY '패스워드';

-- 예시
CREATE USER 'user01'@'localhost' IDENTIFIED BY '1234';
```

### 권한 부여

root 계정이 생성된 사용자 계정에게 DB에 접근할 권한을 부여해야 특정 DB에 접근할 권한이 생깁니다.

```sql
GRANT ALL PRIVILEGES ON mydb.* TO user01@localhost;
```

## 테이블 구조 확인

```sql
-- 테이블의 구조를 확인하는 명령어
DESC 테이블명;
DESC emp;
DESC dept;
```

## 데이터 타입

열을 필드라고 부릅니다. Type 데이터 타입이 존재합니다: `SMALLINT`, `INT`, `BIGINT` 등

### CHAR
- **고정길이 문자열** (1000 byte 이내)
- 예: `gender CHAR(10)`에서 `gender='Y'`일 때
- `Y _ _ _ _ _ _ _ _ _` (10개의 메모리를 다 차지)
- 주의사항:
  - `WHERE gender='y'`와 `WHERE gender='Y'`는 다른 DBMS마다 다름
  - 대부분은 데이터에서 한해서 대소문자 구분을 하는데 MySQL은 못함
  - Oracle의 경우: `WHERE gender='y         '` 또는 `WHERE TRIM(gender)='y'`
- **사용 용도**: 데이터의 길이가 정해져 있을 때 (사번, 학번, 성별, 연도, 주민번호, 우편번호 등)

### VARCHAR
- **가변길이 문자열** (variant char의 약자)
- 용량을 지정해도 실제 데이터만큼만 사용
- 예: `VARCHAR(100)`에 `'y'`가 들어가면 실제 데이터 길이 1만 차지
- 2000byte까지, 앞부분에 데이터 길이를 별도로 저장
- **사용 용도**: 사용자 아이디, 게시글 타이틀 등

### TEXT
- `TEXT`, `LONG TEXT` - 2G까지 (게시판 게시글 등)

## 테이블 구조 예시

```
+--------+-------------+------+-----+---------+-------+
| Field  | Type        | Null | Key | Default | Extra |
+--------+-------------+------+-----+---------+-------+
| DEPTNO | int         | NO   | PRI | NULL    |       |
| DNAME  | varchar(14) | YES  |     | NULL    |       |
| LOC    | varchar(13) | YES  |     | NULL    |       |
+--------+-------------+------+-----+---------+-------+
```

### 필드 설명
- **Null**: 널 허용 여부
- **Key**: 
  - `PRI` - Primary Key: 중복불가, null불가 조건을 만족해야 함
- **Default**: 특별한 값을 입력하지 않았을 때 기본값으로 저장

## SQL 언어 분류

### DCL (Data Control Language)
- **권한 관련 명령어**
- `GRANT` (권한 주는 명령어)
- `REVOKE` (권한 뺏는 명령어)

### DML (Data Manipulation Language)
- **데이터 조작어**
- `INSERT`, `DELETE`, `UPDATE`, `SELECT` (조회 - 애매함)

### DDL (Data Definition Language)
- **데이터 정의어**
- `CREATE`, `DROP`, `ALTER`, `TRUNCATE` 등

## 다음 단계

조회 명령어인 `SELECT` 명령어 사용법을 배우겠습니다. 