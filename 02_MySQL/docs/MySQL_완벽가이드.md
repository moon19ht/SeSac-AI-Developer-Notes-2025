# MySQL 완벽 가이드

## 목차

1. [MySQL 소개](#1-mysql-소개)
2. [설치 및 환경 설정](#2-설치-및-환경-설정)
3. [데이터베이스 기본 개념](#3-데이터베이스-기본-개념)
4. [데이터 타입](#4-데이터-타입)
5. [SQL 기본 문법](#5-sql-기본-문법)
6. [고급 기능](#6-고급-기능)
7. [성능 최적화](#7-성능-최적화)
8. [백업 및 복구](#8-백업-및-복구)
9. [보안](#9-보안)
10. [실무 팁과 베스트 프랙티스](#10-실무-팁과-베스트-프랙티스)

---

## 1. MySQL 소개

### 1.1 MySQL이란?

MySQL은 세계에서 가장 인기 있는 오픈 소스 관계형 데이터베이스 관리 시스템(RDBMS) 중 하나입니다.

**주요 특징:**
- **오픈 소스**: GPL 라이선스로 무료 사용 가능
- **고성능**: 빠른 읽기/쓰기 성능
- **확장성**: 작은 임베디드 애플리케이션부터 대용량 웹사이트까지 지원
- **안정성**: 수년간 검증된 안정적인 시스템
- **크로스 플랫폼**: Windows, Linux, macOS 등 다양한 운영체제 지원

### 1.2 MySQL vs 다른 DBMS

| 특징 | MySQL | PostgreSQL | Oracle | SQL Server |
|------|-------|------------|---------|------------|
| 라이선스 | GPL/Commercial | BSD | Commercial | Commercial |
| 성능 | 읽기 최적화 | 복잡한 쿼리 우수 | 고성능 | 높은 성능 |
| 확장성 | 우수 | 우수 | 매우 우수 | 우수 |
| 비용 | 무료/유료 | 무료 | 높음 | 높음 |

### 1.3 MySQL 버전별 특징

**MySQL 8.0 (최신 버전)**
- JSON 지원 강화
- Window Functions
- CTE (Common Table Expressions)
- 향상된 보안 기능
- 성능 개선

**MySQL 5.7**
- JSON 데이터 타입 도입
- Generated Columns
- 성능 스키마 개선

---

## 2. 설치 및 환경 설정

### 2.1 Windows 설치

**방법 1: MySQL Installer 사용**
1. MySQL 공식 웹사이트에서 MySQL Installer 다운로드
2. mysql-installer-community-8.0.x.x.msi 실행
3. Setup Type에서 "Developer Default" 선택
4. Root 패스워드 설정
5. MySQL Server 구성 완료

**방법 2: ZIP 아카이브 설치**
```bash
# 환경 변수 설정
Path에 C:\mysql\bin 추가

# MySQL 서비스 설치
mysqld --install MySQL80 --defaults-file="C:\mysql\my.ini"

# 서비스 시작
net start MySQL80
```

### 2.2 Linux 설치

**Ubuntu/Debian:**
```bash
# 패키지 업데이트
sudo apt update

# MySQL 서버 설치
sudo apt install mysql-server

# 보안 설정
sudo mysql_secure_installation

# 서비스 상태 확인
sudo systemctl status mysql
```

**CentOS/RHEL:**
```bash
# MySQL 리포지토리 추가
sudo yum install mysql-server

# 서비스 시작 및 활성화
sudo systemctl start mysqld
sudo systemctl enable mysqld

# 초기 패스워드 확인
sudo grep 'temporary password' /var/log/mysqld.log
```

### 2.3 기본 설정

**my.cnf 설정 파일 (Linux) / my.ini (Windows)**
```ini
[mysql]
default-character-set = utf8mb4

[mysqld]
# 기본 설정
port = 3306
socket = /var/run/mysqld/mysqld.sock
datadir = /var/lib/mysql

# 문자셋 설정
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci

# 성능 설정
innodb_buffer_pool_size = 128M
max_connections = 151
query_cache_size = 16M

# 로그 설정
general_log = 1
general_log_file = /var/log/mysql/mysql.log
slow_query_log = 1
slow_query_log_file = /var/log/mysql/slow.log
long_query_time = 2
```

### 2.4 접속 및 기본 명령어

```sql
-- MySQL 접속
mysql -u root -p

-- 버전 확인
SELECT VERSION();

-- 현재 사용자 확인
SELECT USER();

-- 데이터베이스 목록 확인
SHOW DATABASES;

-- 현재 날짜/시간 확인
SELECT NOW();

-- 도움말
HELP;

-- MySQL 종료
EXIT; 또는 QUIT;
```

---

## 3. 데이터베이스 기본 개념

### 3.1 관계형 데이터베이스 개념

**데이터베이스 (Database)**
- 관련된 데이터의 집합
- 하나의 MySQL 서버에 여러 데이터베이스 존재 가능

**테이블 (Table)**
- 데이터베이스 내의 데이터 저장 구조
- 행(Row)과 열(Column)로 구성

**스키마 (Schema)**
- MySQL에서는 데이터베이스와 스키마가 동의어
- 테이블들의 논리적 그룹

### 3.2 데이터베이스 생성과 관리

```sql
-- 데이터베이스 생성
CREATE DATABASE company_db
    DEFAULT CHARACTER SET utf8mb4
    DEFAULT COLLATE utf8mb4_unicode_ci;

-- 데이터베이스 선택
USE company_db;

-- 현재 선택된 데이터베이스 확인
SELECT DATABASE();

-- 데이터베이스 삭제
DROP DATABASE company_db;

-- 데이터베이스 정보 확인
SHOW CREATE DATABASE company_db;
```

### 3.3 테이블 구조

```sql
-- 테이블 생성 예제
CREATE TABLE employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    hire_date DATE,
    salary DECIMAL(10,2),
    department_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 테이블 구조 확인
DESCRIBE employees;
-- 또는
SHOW COLUMNS FROM employees;

-- 테이블 생성 문 확인
SHOW CREATE TABLE employees;
```

---

## 4. 데이터 타입

### 4.1 숫자 데이터 타입

**정수형**
| 타입 | 크기 | 범위 (Signed) | 범위 (Unsigned) |
|------|------|---------------|----------------|
| TINYINT | 1 byte | -128 ~ 127 | 0 ~ 255 |
| SMALLINT | 2 bytes | -32,768 ~ 32,767 | 0 ~ 65,535 |
| MEDIUMINT | 3 bytes | -8,388,608 ~ 8,388,607 | 0 ~ 16,777,215 |
| INT | 4 bytes | -2,147,483,648 ~ 2,147,483,647 | 0 ~ 4,294,967,295 |
| BIGINT | 8 bytes | -9,223,372,036,854,775,808 ~ 9,223,372,036,854,775,807 | 0 ~ 18,446,744,073,709,551,615 |

```sql
-- 정수형 예제
CREATE TABLE numbers_example (
    tiny_num TINYINT,
    small_num SMALLINT,
    medium_num MEDIUMINT,
    int_num INT,
    big_num BIGINT,
    unsigned_int INT UNSIGNED
);
```

**실수형**
```sql
-- 실수형 타입
CREATE TABLE decimal_example (
    price DECIMAL(10,2),  -- 전체 10자리, 소수점 2자리
    ratio FLOAT,          -- 단정밀도 부동소수점
    percentage DOUBLE     -- 배정밀도 부동소수점
);

-- 예제 데이터
INSERT INTO decimal_example VALUES 
(999999.99, 3.14159, 99.999999999);
```

### 4.2 문자열 데이터 타입

```sql
-- 문자열 타입 예제
CREATE TABLE string_example (
    fixed_char CHAR(10),        -- 고정 길이 (10바이트)
    variable_char VARCHAR(100), -- 가변 길이 (최대 100자)
    tiny_text TINYTEXT,         -- 최대 255자
    normal_text TEXT,           -- 최대 65,535자
    medium_text MEDIUMTEXT,     -- 최대 16,777,215자
    long_text LONGTEXT,         -- 최대 4,294,967,295자
    binary_data BLOB            -- 이진 데이터
);

-- CHAR vs VARCHAR 차이점
INSERT INTO string_example (fixed_char, variable_char) VALUES 
('Hello', 'Hello');  -- CHAR은 'Hello     '로 저장 (공백 패딩)
```

### 4.3 날짜와 시간 데이터 타입

```sql
-- 날짜/시간 타입 예제
CREATE TABLE datetime_example (
    birth_date DATE,                    -- YYYY-MM-DD
    work_time TIME,                     -- HH:MM:SS
    created_datetime DATETIME,          -- YYYY-MM-DD HH:MM:SS
    updated_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    birth_year YEAR                     -- YYYY
);

-- 날짜/시간 데이터 삽입
INSERT INTO datetime_example VALUES 
('1990-05-15', '09:30:00', '2024-01-15 14:30:00', NOW(), 2024);

-- 날짜 함수 예제
SELECT 
    NOW(),                    -- 현재 날짜/시간
    CURDATE(),               -- 현재 날짜
    CURTIME(),               -- 현재 시간
    DATE('2024-01-15 14:30:00'),  -- 날짜 부분 추출
    TIME('2024-01-15 14:30:00'),  -- 시간 부분 추출
    YEAR(NOW()),             -- 연도 추출
    MONTH(NOW()),            -- 월 추출
    DAY(NOW());              -- 일 추출
```

### 4.4 JSON 데이터 타입 (MySQL 5.7+)

```sql
-- JSON 타입 예제
CREATE TABLE user_profile (
    user_id INT PRIMARY KEY,
    profile JSON,
    preferences JSON
);

-- JSON 데이터 삽입
INSERT INTO user_profile VALUES 
(1, '{"name": "김철수", "age": 30, "city": "서울"}', 
    '{"theme": "dark", "language": "ko", "notifications": true}');

-- JSON 데이터 조회
SELECT 
    user_id,
    JSON_EXTRACT(profile, '$.name') AS name,
    JSON_EXTRACT(profile, '$.age') AS age,
    profile->'$.city' AS city,      -- 단축 문법
    profile->>'$.name' AS name_unquoted  -- 따옴표 제거
FROM user_profile;

-- JSON 함수들
SELECT 
    JSON_VALID('{"name": "test"}'),           -- JSON 유효성 검사
    JSON_TYPE('{"name": "test"}'),            -- JSON 타입 반환
    JSON_LENGTH('{"a": 1, "b": 2}'),          -- JSON 요소 개수
    JSON_KEYS('{"a": 1, "b": 2}');            -- JSON 키 목록
```

---

## 5. SQL 기본 문법

### 5.1 DDL (Data Definition Language)

**CREATE 문**
```sql
-- 테이블 생성
CREATE TABLE departments (
    dept_id INT AUTO_INCREMENT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL UNIQUE,
    manager_id INT,
    budget DECIMAL(12,2) DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_dept_name (dept_name),
    FOREIGN KEY (manager_id) REFERENCES employees(emp_id)
);

-- 인덱스 생성
CREATE INDEX idx_employee_name ON employees(last_name, first_name);
CREATE UNIQUE INDEX idx_employee_email ON employees(email);

-- 뷰 생성
CREATE VIEW employee_details AS
SELECT 
    e.emp_id, 
    CONCAT(e.first_name, ' ', e.last_name) AS full_name,
    e.email, 
    d.dept_name,
    e.salary
FROM employees e
JOIN departments d ON e.department_id = d.dept_id;
```

**ALTER 문**
```sql
-- 컬럼 추가
ALTER TABLE employees 
ADD COLUMN phone VARCHAR(20) AFTER email,
ADD COLUMN status ENUM('active', 'inactive') DEFAULT 'active';

-- 컬럼 수정
ALTER TABLE employees 
MODIFY COLUMN salary DECIMAL(12,2) NOT NULL,
CHANGE COLUMN hire_date employment_date DATE;

-- 컬럼 삭제
ALTER TABLE employees 
DROP COLUMN phone;

-- 인덱스 추가/삭제
ALTER TABLE employees 
ADD INDEX idx_salary (salary),
DROP INDEX idx_employee_email;

-- 제약조건 추가
ALTER TABLE employees 
ADD CONSTRAINT fk_dept 
FOREIGN KEY (department_id) REFERENCES departments(dept_id);
```

**DROP 문**
```sql
-- 테이블 삭제
DROP TABLE IF EXISTS temp_table;

-- 인덱스 삭제
DROP INDEX idx_salary ON employees;

-- 뷰 삭제
DROP VIEW IF EXISTS employee_details;

-- 데이터베이스 삭제
DROP DATABASE IF EXISTS test_db;
```

### 5.2 DML (Data Manipulation Language)

**INSERT 문**
```sql
-- 단일 행 삽입
INSERT INTO employees (first_name, last_name, email, hire_date, salary, department_id)
VALUES ('김', '철수', 'kim.cs@company.com', '2024-01-15', 5000000, 1);

-- 다중 행 삽입
INSERT INTO employees (first_name, last_name, email, hire_date, salary, department_id)
VALUES 
    ('이', '영희', 'lee.yh@company.com', '2024-01-16', 4500000, 2),
    ('박', '민수', 'park.ms@company.com', '2024-01-17', 5500000, 1),
    ('최', '수진', 'choi.sj@company.com', '2024-01-18', 4800000, 3);

-- 서브쿼리를 이용한 삽입
INSERT INTO high_earners (emp_id, full_name, salary)
SELECT 
    emp_id, 
    CONCAT(first_name, ' ', last_name), 
    salary
FROM employees 
WHERE salary > 5000000;

-- 중복 시 업데이트 (UPSERT)
INSERT INTO employees (emp_id, first_name, last_name, salary)
VALUES (1, '김', '철수', 5500000)
ON DUPLICATE KEY UPDATE 
    salary = VALUES(salary),
    updated_at = NOW();
```

**SELECT 문**
```sql
-- 기본 조회
SELECT * FROM employees;

-- 특정 컬럼 조회
SELECT first_name, last_name, salary FROM employees;

-- 조건부 조회
SELECT * FROM employees 
WHERE salary BETWEEN 4000000 AND 6000000
AND department_id IN (1, 2, 3)
AND hire_date >= '2024-01-01';

-- 정렬
SELECT * FROM employees 
ORDER BY salary DESC, hire_date ASC;

-- 제한
SELECT * FROM employees 
ORDER BY salary DESC 
LIMIT 5 OFFSET 10;  -- 11번째부터 5개

-- 그룹화
SELECT 
    department_id,
    COUNT(*) AS employee_count,
    AVG(salary) AS avg_salary,
    MAX(salary) AS max_salary,
    MIN(salary) AS min_salary
FROM employees 
GROUP BY department_id
HAVING AVG(salary) > 5000000;

-- 조인
SELECT 
    e.first_name,
    e.last_name,
    d.dept_name,
    e.salary
FROM employees e
INNER JOIN departments d ON e.department_id = d.dept_id
WHERE e.salary > 5000000
ORDER BY e.salary DESC;
```

**UPDATE 문**
```sql
-- 단일 행 업데이트
UPDATE employees 
SET salary = 5500000, updated_at = NOW()
WHERE emp_id = 1;

-- 조건부 업데이트
UPDATE employees 
SET salary = salary * 1.1  -- 10% 인상
WHERE department_id = 1 
AND hire_date < '2024-01-01';

-- 조인을 이용한 업데이트
UPDATE employees e
JOIN departments d ON e.department_id = d.dept_id
SET e.salary = e.salary * 1.05
WHERE d.dept_name = 'IT';

-- CASE를 이용한 조건부 업데이트
UPDATE employees 
SET salary = CASE 
    WHEN department_id = 1 THEN salary * 1.15
    WHEN department_id = 2 THEN salary * 1.10
    WHEN department_id = 3 THEN salary * 1.12
    ELSE salary * 1.08
END
WHERE hire_date < '2024-01-01';
```

**DELETE 문**
```sql
-- 조건부 삭제
DELETE FROM employees 
WHERE status = 'inactive' 
AND hire_date < '2020-01-01';

-- 조인을 이용한 삭제
DELETE e FROM employees e
JOIN departments d ON e.department_id = d.dept_id
WHERE d.dept_name = 'Temp Department';

-- 안전한 삭제 (백업 후)
CREATE TABLE employees_backup AS 
SELECT * FROM employees WHERE status = 'inactive';

DELETE FROM employees WHERE status = 'inactive';
```

### 5.3 DCL (Data Control Language)

**사용자 관리**
```sql
-- 사용자 생성
CREATE USER 'developer'@'localhost' IDENTIFIED BY 'secure_password123!';
CREATE USER 'app_user'@'%' IDENTIFIED BY 'app_password456!';

-- 사용자 목록 확인
SELECT User, Host FROM mysql.user;

-- 사용자 삭제
DROP USER 'old_user'@'localhost';
```

**권한 관리**
```sql
-- 권한 부여
GRANT SELECT, INSERT, UPDATE ON company_db.* TO 'developer'@'localhost';
GRANT ALL PRIVILEGES ON company_db.employees TO 'hr_manager'@'localhost';

-- 읽기 전용 권한
GRANT SELECT ON company_db.* TO 'readonly_user'@'%';

-- 특정 컬럼에만 권한 부여
GRANT SELECT (emp_id, first_name, last_name) ON company_db.employees TO 'limited_user'@'localhost';

-- 권한 확인
SHOW GRANTS FOR 'developer'@'localhost';

-- 권한 회수
REVOKE INSERT, UPDATE ON company_db.* FROM 'developer'@'localhost';

-- 권한 적용
FLUSH PRIVILEGES;
```

---

## 6. 고급 기능

### 6.1 인덱스 (Index)

**인덱스 종류와 특징**
```sql
-- 일반 인덱스
CREATE INDEX idx_last_name ON employees(last_name);

-- 복합 인덱스
CREATE INDEX idx_name_salary ON employees(last_name, first_name, salary);

-- 유니크 인덱스
CREATE UNIQUE INDEX idx_email ON employees(email);

-- 전문 검색 인덱스
CREATE FULLTEXT INDEX idx_fulltext ON articles(title, content);

-- 인덱스 정보 확인
SHOW INDEX FROM employees;

-- 인덱스 사용 확인
EXPLAIN SELECT * FROM employees WHERE last_name = '김';
```

**인덱스 최적화 팁**
```sql
-- 좋은 인덱스 예제
SELECT * FROM employees 
WHERE last_name = '김' AND first_name = '철수';
-- 인덱스: (last_name, first_name)

-- 나쁜 인덱스 사용 예제
SELECT * FROM employees 
WHERE UPPER(last_name) = '김';  -- 함수 사용으로 인덱스 사용 불가

-- 올바른 방법
SELECT * FROM employees 
WHERE last_name = '김';  -- 인덱스 사용 가능
```

### 6.2 뷰 (View)

```sql
-- 단순 뷰
CREATE VIEW active_employees AS
SELECT emp_id, first_name, last_name, email, salary
FROM employees
WHERE status = 'active';

-- 복잡한 뷰
CREATE VIEW department_summary AS
SELECT 
    d.dept_name,
    COUNT(e.emp_id) AS employee_count,
    AVG(e.salary) AS avg_salary,
    SUM(e.salary) AS total_salary
FROM departments d
LEFT JOIN employees e ON d.dept_id = e.department_id
WHERE e.status = 'active'
GROUP BY d.dept_id, d.dept_name;

-- 뷰 사용
SELECT * FROM department_summary 
WHERE employee_count > 5;

-- 업데이트 가능한 뷰
CREATE VIEW employee_basic_info AS
SELECT emp_id, first_name, last_name, email
FROM employees
WHERE status = 'active';

-- 뷰를 통한 업데이트
UPDATE employee_basic_info 
SET email = 'new.email@company.com'
WHERE emp_id = 1;

-- 뷰 수정
ALTER VIEW active_employees AS
SELECT emp_id, first_name, last_name, email, salary, hire_date
FROM employees
WHERE status = 'active' AND hire_date >= '2024-01-01';
```

### 6.3 스토어드 프로시저 (Stored Procedure)

```sql
-- 기본 스토어드 프로시저
DELIMITER $$
CREATE PROCEDURE GetEmployeeInfo(IN emp_id_param INT)
BEGIN
    SELECT 
        emp_id,
        CONCAT(first_name, ' ', last_name) AS full_name,
        email,
        salary,
        hire_date
    FROM employees
    WHERE emp_id = emp_id_param;
END$$
DELIMITER ;

-- 프로시저 호출
CALL GetEmployeeInfo(1);

-- 매개변수가 있는 프로시저
DELIMITER $$
CREATE PROCEDURE UpdateSalary(
    IN emp_id_param INT,
    IN increase_percent DECIMAL(5,2),
    OUT old_salary DECIMAL(10,2),
    OUT new_salary DECIMAL(10,2)
)
BEGIN
    DECLARE current_salary DECIMAL(10,2);
    
    -- 현재 급여 조회
    SELECT salary INTO current_salary
    FROM employees
    WHERE emp_id = emp_id_param;
    
    SET old_salary = current_salary;
    SET new_salary = current_salary * (1 + increase_percent / 100);
    
    -- 급여 업데이트
    UPDATE employees
    SET salary = new_salary
    WHERE emp_id = emp_id_param;
END$$
DELIMITER ;

-- OUT 매개변수를 사용한 호출
CALL UpdateSalary(1, 10.0, @old_sal, @new_sal);
SELECT @old_sal AS 'Old Salary', @new_sal AS 'New Salary';

-- 조건문과 반복문이 있는 프로시저
DELIMITER $$
CREATE PROCEDURE ProcessYearEndBonus()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE emp_id_var INT;
    DECLARE salary_var DECIMAL(10,2);
    DECLARE bonus DECIMAL(10,2);
    
    DECLARE emp_cursor CURSOR FOR
        SELECT emp_id, salary FROM employees WHERE status = 'active';
    
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    
    OPEN emp_cursor;
    
    emp_loop: LOOP
        FETCH emp_cursor INTO emp_id_var, salary_var;
        IF done THEN
            LEAVE emp_loop;
        END IF;
        
        -- 급여에 따른 보너스 계산
        IF salary_var >= 8000000 THEN
            SET bonus = salary_var * 0.15;
        ELSEIF salary_var >= 5000000 THEN
            SET bonus = salary_var * 0.12;
        ELSE
            SET bonus = salary_var * 0.10;
        END IF;
        
        -- 보너스 테이블에 삽입
        INSERT INTO bonuses (emp_id, bonus_amount, bonus_year)
        VALUES (emp_id_var, bonus, YEAR(NOW()));
        
    END LOOP;
    
    CLOSE emp_cursor;
END$$
DELIMITER ;
```

### 6.4 함수 (Function)

```sql
-- 사용자 정의 함수
DELIMITER $$
CREATE FUNCTION CalculateAge(birth_date DATE) 
RETURNS INT
READS SQL DATA
DETERMINISTIC
BEGIN
    RETURN TIMESTAMPDIFF(YEAR, birth_date, CURDATE());
END$$
DELIMITER ;

-- 함수 사용
SELECT 
    first_name,
    last_name,
    birth_date,
    CalculateAge(birth_date) AS age
FROM employees;

-- 문자열 처리 함수
DELIMITER $$
CREATE FUNCTION FormatPhoneNumber(phone VARCHAR(20))
RETURNS VARCHAR(20)
DETERMINISTIC
BEGIN
    DECLARE formatted_phone VARCHAR(20);
    
    -- 숫자만 추출
    SET formatted_phone = REGEXP_REPLACE(phone, '[^0-9]', '');
    
    -- 형식 적용
    IF LENGTH(formatted_phone) = 11 THEN
        SET formatted_phone = CONCAT(
            SUBSTRING(formatted_phone, 1, 3), '-',
            SUBSTRING(formatted_phone, 4, 4), '-',
            SUBSTRING(formatted_phone, 8, 4)
        );
    END IF;
    
    RETURN formatted_phone;
END$$
DELIMITER ;
```

### 6.5 트리거 (Trigger)

```sql
-- 삽입 후 트리거
DELIMITER $$
CREATE TRIGGER employee_audit_insert
AFTER INSERT ON employees
FOR EACH ROW
BEGIN
    INSERT INTO employee_audit (
        action_type,
        emp_id,
        action_date,
        user_name,
        old_values,
        new_values
    ) VALUES (
        'INSERT',
        NEW.emp_id,
        NOW(),
        USER(),
        NULL,
        CONCAT('Name: ', NEW.first_name, ' ', NEW.last_name, 
               ', Salary: ', NEW.salary)
    );
END$$
DELIMITER ;

-- 업데이트 전 트리거
DELIMITER $$
CREATE TRIGGER employee_salary_update
BEFORE UPDATE ON employees
FOR EACH ROW
BEGIN
    -- 급여 감소 방지
    IF NEW.salary < OLD.salary * 0.9 THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = '급여는 10% 이상 감소할 수 없습니다.';
    END IF;
    
    -- 자동으로 업데이트 시간 설정
    SET NEW.updated_at = NOW();
END$$
DELIMITER ;

-- 삭제 후 트리거
DELIMITER $$
CREATE TRIGGER employee_delete_backup
AFTER DELETE ON employees
FOR EACH ROW
BEGIN
    INSERT INTO deleted_employees (
        original_emp_id,
        first_name,
        last_name,
        email,
        salary,
        deleted_at,
        deleted_by
    ) VALUES (
        OLD.emp_id,
        OLD.first_name,
        OLD.last_name,
        OLD.email,
        OLD.salary,
        NOW(),
        USER()
    );
END$$
DELIMITER ;

-- 트리거 정보 확인
SHOW TRIGGERS LIKE 'employees';

-- 트리거 삭제
DROP TRIGGER IF EXISTS employee_audit_insert;
```

---

## 7. 성능 최적화

### 7.1 쿼리 최적화

**EXPLAIN을 이용한 실행 계획 분석**
```sql
-- 기본 EXPLAIN
EXPLAIN SELECT * FROM employees WHERE salary > 5000000;

-- 상세 정보
EXPLAIN FORMAT=JSON 
SELECT e.first_name, e.last_name, d.dept_name
FROM employees e
JOIN departments d ON e.department_id = d.dept_id
WHERE e.salary > 5000000;

-- 실제 실행 통계
EXPLAIN ANALYZE
SELECT * FROM employees 
WHERE last_name = '김' AND salary > 4000000;
```

**쿼리 최적화 기법**
```sql
-- 1. 인덱스 활용
-- 나쁜 예
SELECT * FROM employees WHERE YEAR(hire_date) = 2024;

-- 좋은 예
SELECT * FROM employees 
WHERE hire_date >= '2024-01-01' AND hire_date < '2025-01-01';

-- 2. LIMIT 사용
-- 나쁜 예
SELECT * FROM employees ORDER BY salary DESC;

-- 좋은 예
SELECT * FROM employees ORDER BY salary DESC LIMIT 10;

-- 3. 필요한 컬럼만 선택
-- 나쁜 예
SELECT * FROM employees WHERE department_id = 1;

-- 좋은 예
SELECT emp_id, first_name, last_name FROM employees WHERE department_id = 1;

-- 4. EXISTS vs IN 성능 비교
-- EXISTS 사용 (일반적으로 더 빠름)
SELECT * FROM employees e
WHERE EXISTS (
    SELECT 1 FROM departments d 
    WHERE d.dept_id = e.department_id AND d.budget > 1000000
);

-- 5. 조인 최적화
-- 나쁜 예 (카르테시안 곱)
SELECT * FROM employees, departments 
WHERE employees.department_id = departments.dept_id;

-- 좋은 예
SELECT * FROM employees e
INNER JOIN departments d ON e.department_id = d.dept_id;
```

### 7.2 인덱스 최적화

```sql
-- 인덱스 사용 통계 확인
SELECT 
    table_schema,
    table_name,
    index_name,
    cardinality,
    seq_in_index,
    column_name
FROM information_schema.statistics
WHERE table_schema = 'company_db'
ORDER BY table_name, index_name, seq_in_index;

-- 사용되지 않는 인덱스 찾기
SELECT 
    object_schema,
    object_name,
    index_name
FROM performance_schema.table_io_waits_summary_by_index_usage
WHERE index_name IS NOT NULL
AND count_star = 0
AND object_schema = 'company_db';

-- 복합 인덱스 순서 최적화
-- 좋은 복합 인덱스 순서: 카디널리티가 높은 순서
CREATE INDEX idx_employee_search ON employees(department_id, status, last_name);

-- 인덱스 힌트 사용
SELECT * FROM employees 
USE INDEX (idx_employee_search)
WHERE department_id = 1 AND status = 'active';

-- 인덱스 강제 사용
SELECT * FROM employees 
FORCE INDEX (idx_salary)
WHERE salary > 5000000;
```

### 7.3 설정 최적화

```sql
-- 현재 설정 확인
SHOW VARIABLES LIKE 'innodb_buffer_pool_size';
SHOW VARIABLES LIKE 'query_cache%';
SHOW VARIABLES LIKE 'max_connections';

-- 버퍼 풀 히트율 확인
SELECT 
    (1 - (Innodb_buffer_pool_reads / Innodb_buffer_pool_read_requests)) * 100 
    AS buffer_pool_hit_rate
FROM 
    (SELECT variable_value AS Innodb_buffer_pool_reads FROM information_schema.global_status WHERE variable_name = 'Innodb_buffer_pool_reads') AS reads,
    (SELECT variable_value AS Innodb_buffer_pool_read_requests FROM information_schema.global_status WHERE variable_name = 'Innodb_buffer_pool_read_requests') AS requests;

-- 슬로우 쿼리 로그 분석
-- my.cnf에 설정
/*
slow_query_log = 1
slow_query_log_file = /var/log/mysql/slow.log
long_query_time = 1
log_queries_not_using_indexes = 1
*/

-- 슬로우 쿼리 확인
SELECT 
    schema_name,
    digest_text,
    count_star,
    avg_timer_wait/1000000 as avg_time_ms,
    sum_timer_wait/1000000 as total_time_ms
FROM performance_schema.events_statements_summary_by_digest
WHERE schema_name = 'company_db'
ORDER BY avg_timer_wait DESC
LIMIT 10;
```

---

## 8. 백업 및 복구

### 8.1 논리적 백업 (mysqldump)

```bash
# 전체 데이터베이스 백업
mysqldump -u root -p --all-databases > full_backup.sql

# 특정 데이터베이스 백업
mysqldump -u root -p company_db > company_backup.sql

# 테이블 구조만 백업
mysqldump -u root -p --no-data company_db > structure_only.sql

# 데이터만 백업
mysqldump -u root -p --no-create-info company_db > data_only.sql

# 특정 테이블만 백업
mysqldump -u root -p company_db employees departments > specific_tables.sql

# 압축 백업
mysqldump -u root -p company_db | gzip > company_backup.sql.gz

# 원격 서버 백업
mysqldump -h remote_host -u username -p database_name > remote_backup.sql
```

**고급 백업 옵션**
```bash
# 일관성 있는 백업 (InnoDB)
mysqldump -u root -p --single-transaction --routines --triggers company_db > consistent_backup.sql

# 바이너리 로그 정보 포함
mysqldump -u root -p --master-data=2 --single-transaction company_db > backup_with_binlog.sql

# 대용량 데이터베이스 백업
mysqldump -u root -p --single-transaction --quick --lock-tables=false company_db > large_db_backup.sql
```

### 8.2 물리적 백업

```bash
# 서비스 중지 후 데이터 디렉토리 복사
sudo systemctl stop mysql
sudo cp -R /var/lib/mysql /backup/mysql_physical_backup
sudo systemctl start mysql

# 핫 백업 (MySQL Enterprise Backup 또는 Percona XtraBackup)
xtrabackup --backup --target-dir=/backup/mysql_hot_backup
```

### 8.3 복구

```bash
# 전체 복구
mysql -u root -p < full_backup.sql

# 특정 데이터베이스 복구
mysql -u root -p company_db < company_backup.sql

# 압축 파일 복구
gunzip < company_backup.sql.gz | mysql -u root -p company_db

# 부분 복구 (특정 테이블)
mysql -u root -p company_db -e "source /path/to/specific_tables.sql"
```

**Point-in-Time 복구**
```sql
-- 바이너리 로그를 이용한 특정 시점 복구
-- 1. 기본 백업 복구
mysql -u root -p company_db < base_backup.sql

-- 2. 바이너리 로그 적용
mysqlbinlog --start-datetime="2024-01-15 09:00:00" \
            --stop-datetime="2024-01-15 10:30:00" \
            mysql-bin.000001 | mysql -u root -p company_db
```

### 8.4 자동화된 백업

```bash
#!/bin/bash
# backup_script.sh

DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/backup/mysql"
DB_NAME="company_db"
RETENTION_DAYS=30

# 백업 실행
mysqldump -u backup_user -p$BACKUP_PASSWORD \
    --single-transaction \
    --routines \
    --triggers \
    $DB_NAME > $BACKUP_DIR/${DB_NAME}_$DATE.sql

# 압축
gzip $BACKUP_DIR/${DB_NAME}_$DATE.sql

# 오래된 백업 삭제
find $BACKUP_DIR -name "*.sql.gz" -mtime +$RETENTION_DAYS -delete

# 로그 기록
echo "$(date): Backup completed for $DB_NAME" >> /var/log/mysql_backup.log
```

**Cron 설정**
```bash
# 매일 새벽 2시에 백업 실행
0 2 * * * /path/to/backup_script.sh
```

---

## 9. 보안

### 9.1 사용자 보안

```sql
-- 강력한 비밀번호 정책 설정
INSTALL COMPONENT 'file://component_validate_password';

-- 비밀번호 정책 확인
SHOW VARIABLES LIKE 'validate_password%';

-- 비밀번호 정책 설정
SET GLOBAL validate_password.length = 12;
SET GLOBAL validate_password.mixed_case_count = 1;
SET GLOBAL validate_password.number_count = 2;
SET GLOBAL validate_password.special_char_count = 1;

-- 안전한 사용자 생성
CREATE USER 'secure_user'@'localhost' 
IDENTIFIED BY 'StrongPass123!' 
PASSWORD EXPIRE INTERVAL 90 DAY
FAILED_LOGIN_ATTEMPTS 3 
PASSWORD_LOCK_TIME 2;

-- 계정 잠금 확인
SELECT user, host, account_locked FROM mysql.user;

-- 계정 잠금 해제
ALTER USER 'secure_user'@'localhost' ACCOUNT UNLOCK;
```

### 9.2 접속 보안

```sql
-- SSL 연결 강제
ALTER USER 'secure_user'@'localhost' REQUIRE SSL;

-- 특정 IP에서만 접속 허용
CREATE USER 'app_user'@'192.168.1.100' IDENTIFIED BY 'password123!';

-- 역할 기반 권한 관리 (MySQL 8.0+)
CREATE ROLE 'app_read', 'app_write', 'app_admin';

GRANT SELECT ON company_db.* TO 'app_read';
GRANT INSERT, UPDATE, DELETE ON company_db.* TO 'app_write';
GRANT ALL PRIVILEGES ON company_db.* TO 'app_admin';

-- 사용자에게 역할 할당
GRANT 'app_read', 'app_write' TO 'developer'@'localhost';

-- 기본 역할 설정
ALTER USER 'developer'@'localhost' DEFAULT ROLE 'app_read';
```

### 9.3 데이터 보안

```sql
-- 데이터 암호화
-- 1. 투명한 데이터 암호화 (TDE) 설정
ALTER INSTANCE ROTATE INNODB MASTER KEY;

-- 2. 컬럼 레벨 암호화
CREATE TABLE sensitive_data (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    ssn VARBINARY(255),  -- 암호화된 주민번호
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 데이터 암호화 함수 사용
INSERT INTO sensitive_data (name, ssn) 
VALUES ('김철수', AES_ENCRYPT('123456-1234567', 'encryption_key'));

-- 복호화
SELECT 
    name,
    AES_DECRYPT(ssn, 'encryption_key') AS decrypted_ssn
FROM sensitive_data;

-- 3. 해시 함수를 이용한 비밀번호 저장
CREATE TABLE user_accounts (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    password_hash VARCHAR(255),  -- SHA2 해시
    salt VARCHAR(32),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 비밀번호 해시 생성
INSERT INTO user_accounts (username, password_hash, salt)
VALUES ('user1', SHA2(CONCAT('user_password', 'random_salt'), 256), 'random_salt');
```

### 9.4 감사 로그

```sql
-- 감사 로그 플러그인 설치 (MySQL Enterprise)
INSTALL PLUGIN audit_log SONAME 'audit_log.so';

-- 감사 설정
SET GLOBAL audit_log_policy = 'ALL';
SET GLOBAL audit_log_format = 'JSON';

-- 일반 로그 활성화
SET GLOBAL general_log = 'ON';
SET GLOBAL general_log_file = '/var/log/mysql/general.log';

-- 접속 이력 확인
SELECT 
    event_time,
    user_host,
    thread_id,
    server_id,
    command_type,
    argument
FROM mysql.general_log 
WHERE command_type IN ('Connect', 'Query')
ORDER BY event_time DESC 
LIMIT 100;
```

---

## 10. 실무 팁과 베스트 프랙티스

### 10.1 명명 규칙

```sql
-- 테이블명: 복수형, 소문자, 언더스코어
CREATE TABLE employees (
    -- 컬럼명: 소문자, 언더스코어, 의미있는 이름
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email_address VARCHAR(100) UNIQUE,
    hire_date DATE,
    annual_salary DECIMAL(10,2),
    department_id INT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 인덱스명: idx_테이블명_컬럼명
CREATE INDEX idx_employees_last_name ON employees(last_name);
CREATE INDEX idx_employees_dept_salary ON employees(department_id, annual_salary);

-- 외래키명: fk_테이블명_참조테이블명
ALTER TABLE employees 
ADD CONSTRAINT fk_employees_departments 
FOREIGN KEY (department_id) REFERENCES departments(department_id);
```

### 10.2 데이터 모델링 베스트 프랙티스

```sql
-- 1. 정규화 예제
-- 비정규화된 테이블 (나쁜 예)
CREATE TABLE orders_bad (
    order_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    customer_email VARCHAR(100),
    customer_phone VARCHAR(20),
    product_name VARCHAR(100),
    product_price DECIMAL(10,2),
    quantity INT,
    order_date DATE
);

-- 정규화된 테이블 (좋은 예)
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    total_amount DECIMAL(12,2),
    status ENUM('pending', 'processing', 'shipped', 'delivered', 'cancelled') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    subtotal DECIMAL(12,2) GENERATED ALWAYS AS (quantity * unit_price) STORED,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
```

### 10.3 성능 모니터링

```sql
-- 1. 현재 실행 중인 쿼리 확인
SELECT 
    id,
    user,
    host,
    db,
    command,
    time,
    state,
    info
FROM information_schema.processlist
WHERE command != 'Sleep'
ORDER BY time DESC;

-- 2. 테이블 크기 확인
SELECT 
    table_schema AS 'Database',
    table_name AS 'Table',
    ROUND(((data_length + index_length) / 1024 / 1024), 2) AS 'Size (MB)',
    table_rows AS 'Rows'
FROM information_schema.tables
WHERE table_schema = 'company_db'
ORDER BY (data_length + index_length) DESC;

-- 3. 인덱스 효율성 확인
SELECT 
    t.table_schema,
    t.table_name,
    s.index_name,
    s.column_name,
    s.cardinality,
    ROUND(s.cardinality / t.table_rows * 100, 2) AS selectivity_percent
FROM information_schema.statistics s
JOIN information_schema.tables t ON s.table_schema = t.table_schema 
    AND s.table_name = t.table_name
WHERE t.table_schema = 'company_db'
    AND t.table_rows > 0
ORDER BY selectivity_percent DESC;

-- 4. 자주 사용되는 쿼리 패턴 분석
SELECT 
    digest_text,
    count_star AS execution_count,
    ROUND(avg_timer_wait / 1000000, 2) AS avg_time_ms,
    ROUND(sum_timer_wait / 1000000, 2) AS total_time_ms
FROM performance_schema.events_statements_summary_by_digest
WHERE schema_name = 'company_db'
ORDER BY count_star DESC
LIMIT 20;
```

### 10.4 트랜잭션 관리

```sql
-- 1. 명시적 트랜잭션 사용
START TRANSACTION;

-- 여러 관련된 작업을 하나의 트랜잭션으로 묶기
INSERT INTO orders (customer_id, order_date, total_amount)
VALUES (1, CURDATE(), 150000);

SET @order_id = LAST_INSERT_ID();

INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES 
    (@order_id, 1, 2, 50000),
    (@order_id, 2, 1, 50000);

-- 재고 업데이트
UPDATE products SET stock_quantity = stock_quantity - 2 WHERE product_id = 1;
UPDATE products SET stock_quantity = stock_quantity - 1 WHERE product_id = 2;

-- 모든 작업이 성공하면 커밋
COMMIT;

-- 2. 에러 처리가 있는 트랜잭션
DELIMITER $$
CREATE PROCEDURE ProcessOrder(
    IN p_customer_id INT,
    IN p_product_id INT,
    IN p_quantity INT
)
BEGIN
    DECLARE v_stock INT;
    DECLARE v_price DECIMAL(10,2);
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    
    -- 재고 확인
    SELECT stock_quantity, price INTO v_stock, v_price
    FROM products 
    WHERE product_id = p_product_id
    FOR UPDATE;  -- 행 잠금
    
    IF v_stock < p_quantity THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = '재고가 부족합니다.';
    END IF;
    
    -- 주문 생성
    INSERT INTO orders (customer_id, order_date, total_amount)
    VALUES (p_customer_id, CURDATE(), p_quantity * v_price);
    
    SET @order_id = LAST_INSERT_ID();
    
    INSERT INTO order_items (order_id, product_id, quantity, unit_price)
    VALUES (@order_id, p_product_id, p_quantity, v_price);
    
    -- 재고 감소
    UPDATE products 
    SET stock_quantity = stock_quantity - p_quantity
    WHERE product_id = p_product_id;
    
    COMMIT;
END$$
DELIMITER ;
```

### 10.5 일반적인 문제 해결

```sql
-- 1. 데드락 확인 및 해결
-- 데드락 정보 확인
SHOW ENGINE INNODB STATUS;

-- 데드락 방지를 위한 쿼리 순서 통일
-- 나쁜 예: 서로 다른 순서로 테이블 액세스
-- 세션 1: UPDATE table_a, UPDATE table_b
-- 세션 2: UPDATE table_b, UPDATE table_a

-- 좋은 예: 항상 같은 순서로 테이블 액세스
-- 세션 1: UPDATE table_a, UPDATE table_b
-- 세션 2: UPDATE table_a, UPDATE table_b

-- 2. 잠금 대기 확인
SELECT 
    r.trx_id waiting_trx_id,
    r.trx_mysql_thread_id waiting_thread,
    r.trx_query waiting_query,
    b.trx_id blocking_trx_id,
    b.trx_mysql_thread_id blocking_thread,
    b.trx_query blocking_query
FROM information_schema.innodb_lock_waits w
INNER JOIN information_schema.innodb_trx b ON b.trx_id = w.blocking_trx_id
INNER JOIN information_schema.innodb_trx r ON r.trx_id = w.requesting_trx_id;

-- 3. 테이블 복구
-- 테이블 검사
CHECK TABLE employees;

-- 테이블 복구
REPAIR TABLE employees;

-- 테이블 분석 (통계 정보 업데이트)
ANALYZE TABLE employees;

-- 테이블 최적화
OPTIMIZE TABLE employees;

-- 4. 연결 수 관리
-- 현재 연결 수 확인
SHOW STATUS LIKE 'Threads_connected';
SHOW STATUS LIKE 'Max_used_connections';

-- 최대 연결 수 설정
SET GLOBAL max_connections = 200;

-- 연결 프로세스 확인
SHOW PROCESSLIST;

-- 특정 연결 종료
KILL 123;  -- 프로세스 ID
```

### 10.6 데이터 마이그레이션

```sql
-- 1. 안전한 대용량 데이터 업데이트
-- 나쁜 예: 한 번에 모든 데이터 업데이트
UPDATE large_table SET status = 'processed' WHERE status = 'pending';

-- 좋은 예: 배치 단위로 처리
DELIMITER $$
CREATE PROCEDURE BatchUpdateStatus()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE batch_size INT DEFAULT 1000;
    DECLARE affected_rows INT;
    
    REPEAT
        UPDATE large_table 
        SET status = 'processed' 
        WHERE status = 'pending' 
        LIMIT batch_size;
        
        SET affected_rows = ROW_COUNT();
        
        -- 다른 트랜잭션에게 기회 제공
        SELECT SLEEP(0.1);
        
    UNTIL affected_rows < batch_size END REPEAT;
END$$
DELIMITER ;

-- 2. 테이블 스키마 변경 (대용량 테이블)
-- 온라인 DDL 사용 (MySQL 5.6+)
ALTER TABLE large_table 
ADD COLUMN new_column VARCHAR(100) DEFAULT 'default_value',
ALGORITHM=INPLACE, LOCK=NONE;

-- 3. 데이터 동기화
CREATE TABLE data_sync_log (
    sync_id INT AUTO_INCREMENT PRIMARY KEY,
    table_name VARCHAR(100),
    operation_type ENUM('INSERT', 'UPDATE', 'DELETE'),
    record_id INT,
    sync_status ENUM('pending', 'completed', 'failed') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP NULL
);
```

---

## 마무리

이 가이드는 MySQL의 핵심 개념부터 고급 기능까지 포괄적으로 다루고 있습니다. 각 섹션의 예제들을 직접 실행해보면서 MySQL의 다양한 기능들을 익혀보세요.

**추가 학습 리소스:**
- MySQL 공식 문서: https://dev.mysql.com/doc/
- MySQL Performance Blog: https://www.percona.com/blog/
- MySQL Tutorial: https://www.mysqltutorial.org/

**실무에서 기억할 점:**
1. 항상 백업을 먼저 수행하세요
2. 프로덕션 환경에서는 신중하게 쿼리를 실행하세요
3. 성능 모니터링을 정기적으로 수행하세요
4. 보안 설정을 정기적으로 검토하세요
5. 최신 버전의 보안 패치를 적용하세요

MySQL 마스터가 되는 길은 지속적인 학습과 실습에 있습니다. 이 가이드가 여러분의 MySQL 여정에 도움이 되기를 바랍니다! 