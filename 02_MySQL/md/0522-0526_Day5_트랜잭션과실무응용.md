# 🚀 Day 5: 트랜잭션과 실무응용 마스터

##### 📅 학습 기간: 2025.05.22 ~ 2025.05.26 (5일)
##### 🎯 학습 목표: 트랜잭션 + 성능 최적화 + 실무 프로젝트 완성
##### 📝 Writer : Moon19ht

---

## 📋 Day 5 학습 체크리스트

- [x] ACID 원칙 완전 이해
- [x] 트랜잭션 격리 수준 4가지 실습
- [x] 교착상태(Deadlock) 해결
- [x] 인덱스 최적화 전략 수립
- [x] 쿼리 성능 튜닝 10가지 기법
- [x] 실무 프로젝트: 완전한 ERP 시스템 구축
- [x] 데이터베이스 백업/복원 실습

---

## 🔒 STEP 1: 트랜잭션 완전 정복 (90분)

### 1.1 ACID 원칙 실습

#### ⚛️ Atomicity (원자성) - 모두 성공 또는 모두 실패
```sql
-- 계좌 이체 시나리오 (원자성 보장)
-- 테스트용 계좌 테이블 생성
CREATE TABLE bank_accounts (
    account_id INT PRIMARY KEY AUTO_INCREMENT,
    account_number VARCHAR(20) UNIQUE NOT NULL,
    customer_name VARCHAR(50) NOT NULL,
    balance DECIMAL(15,2) NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chk_balance CHECK (balance >= 0)
);

-- 계좌 이체 로그 테이블
CREATE TABLE transfer_log (
    transfer_id INT PRIMARY KEY AUTO_INCREMENT,
    from_account VARCHAR(20),
    to_account VARCHAR(20),
    amount DECIMAL(15,2),
    transfer_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) DEFAULT 'PENDING',
    error_message TEXT
);

-- 샘플 계좌 생성
INSERT INTO bank_accounts (account_number, customer_name, balance) VALUES
('1001-001', '김철수', 1000000),
('1001-002', '이영희', 500000),
('1001-003', '박민수', 750000);

-- 원자성 보장 계좌 이체 프로시저
DELIMITER //
CREATE PROCEDURE TransferMoney(
    IN from_account_num VARCHAR(20),
    IN to_account_num VARCHAR(20),
    IN transfer_amount DECIMAL(15,2),
    OUT result_code INT,
    OUT result_message VARCHAR(200)
)
BEGIN
    DECLARE from_balance DECIMAL(15,2);
    DECLARE transfer_id INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        -- 오류 발생 시 롤백
        ROLLBACK;
        SET result_code = -1;
        SET result_message = 'ERROR: 이체 처리 중 오류가 발생했습니다.';
        UPDATE transfer_log SET status = 'FAILED', error_message = 'Transaction failed' 
        WHERE transfer_log.transfer_id = transfer_id;
    END;
    
    -- 트랜잭션 시작
    START TRANSACTION;
    
    -- 이체 로그 기록
    INSERT INTO transfer_log (from_account, to_account, amount) 
    VALUES (from_account_num, to_account_num, transfer_amount);
    SET transfer_id = LAST_INSERT_ID();
    
    -- 출금 계좌 잔액 확인
    SELECT balance INTO from_balance 
    FROM bank_accounts 
    WHERE account_number = from_account_num FOR UPDATE;
    
    IF from_balance < transfer_amount THEN
        SET result_code = -2;
        SET result_message = 'ERROR: 잔액이 부족합니다.';
        UPDATE transfer_log SET status = 'FAILED', error_message = 'Insufficient balance' 
        WHERE transfer_log.transfer_id = transfer_id;
        ROLLBACK;
    ELSE
        -- 출금 처리
        UPDATE bank_accounts 
        SET balance = balance - transfer_amount 
        WHERE account_number = from_account_num;
        
        -- 입금 처리
        UPDATE bank_accounts 
        SET balance = balance + transfer_amount 
        WHERE account_number = to_account_num;
        
        -- 성공 로그 업데이트
        UPDATE transfer_log SET status = 'COMPLETED' 
        WHERE transfer_log.transfer_id = transfer_id;
        
        SET result_code = 0;
        SET result_message = CONCAT('SUCCESS: ', transfer_amount, '원이 성공적으로 이체되었습니다.');
        
        COMMIT;
    END IF;
END //
DELIMITER ;

-- 이체 테스트
SET @code = 0;
SET @msg = '';
CALL TransferMoney('1001-001', '1001-002', 100000, @code, @msg);
SELECT @code AS result_code, @msg AS result_message;
SELECT * FROM bank_accounts;
SELECT * FROM transfer_log;
```

#### 🔄 Consistency (일관성) - 제약조건 유지
```sql
-- 일관성 검증 프로시저
DELIMITER //
CREATE PROCEDURE ValidateAccountConsistency()
BEGIN
    DECLARE total_balance DECIMAL(15,2);
    DECLARE total_transfers DECIMAL(15,2);
    DECLARE balance_diff DECIMAL(15,2);
    
    -- 현재 총 잔액
    SELECT SUM(balance) INTO total_balance FROM bank_accounts;
    
    -- 성공한 이체의 총액 (순증감 확인)
    SELECT 
        SUM(CASE WHEN status = 'COMPLETED' THEN amount ELSE 0 END) - 
        SUM(CASE WHEN status = 'COMPLETED' THEN amount ELSE 0 END)
    INTO total_transfers 
    FROM transfer_log;
    
    -- 초기 잔액과 현재 잔액 비교 (일관성 확인)
    SELECT 
        total_balance AS current_total_balance,
        1500000 AS initial_total_balance,  -- 초기 총 잔액
        total_balance - 1500000 AS balance_difference,
        CASE 
            WHEN ABS(total_balance - 1500000) < 0.01 THEN 'CONSISTENT'
            ELSE 'INCONSISTENT'
        END AS consistency_status;
END //
DELIMITER ;

CALL ValidateAccountConsistency();
```

### 1.2 격리 수준 (Isolation Levels)

#### 🔐 4가지 격리 수준 실습
```sql
-- 현재 격리 수준 확인
SELECT @@transaction_isolation;

-- 격리 수준별 테스트용 세션 설정
-- SESSION 1 (터미널 1에서 실행)
SET SESSION TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
START TRANSACTION;
UPDATE bank_accounts SET balance = balance + 1000000 WHERE account_number = '1001-001';
-- 아직 COMMIT 하지 않음

-- SESSION 2 (터미널 2에서 실행)
SET SESSION TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
START TRANSACTION;
SELECT * FROM bank_accounts WHERE account_number = '1001-001';  -- Dirty Read 발생 가능

-- READ COMMITTED 테스트
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
START TRANSACTION;
SELECT * FROM bank_accounts WHERE account_number = '1001-001';  -- 커밋된 데이터만 읽음

-- REPEATABLE READ 테스트 (MySQL 기본값)
SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ;
START TRANSACTION;
SELECT * FROM bank_accounts WHERE account_number = '1001-001';
-- 다른 세션에서 UPDATE 후 COMMIT
SELECT * FROM bank_accounts WHERE account_number = '1001-001';  -- 동일한 결과

-- SERIALIZABLE 테스트 (가장 엄격)
SET SESSION TRANSACTION ISOLATION LEVEL SERIALIZABLE;
START TRANSACTION;
SELECT * FROM bank_accounts WHERE account_number = '1001-001';
-- 다른 세션의 수정 작업이 대기됨
```

### 1.3 교착상태(Deadlock) 해결

#### ⚔️ 교착상태 시뮬레이션 및 해결
```sql
-- 교착상태 모니터링 테이블
CREATE TABLE deadlock_log (
    log_id INT PRIMARY KEY AUTO_INCREMENT,
    session_id VARCHAR(50),
    query_text TEXT,
    lock_wait_time DECIMAL(10,3),
    deadlock_occurred BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 교착상태 방지 프로시저 (일관된 락 순서)
DELIMITER //
CREATE PROCEDURE SafeTransferBetweenAccounts(
    IN account1 VARCHAR(20),
    IN account2 VARCHAR(20),
    IN amount1 DECIMAL(15,2),
    IN amount2 DECIMAL(15,2)
)
BEGIN
    DECLARE first_account VARCHAR(20);
    DECLARE second_account VARCHAR(20);
    DECLARE first_amount DECIMAL(15,2);
    DECLARE second_amount DECIMAL(15,2);
    
    -- 교착상태 방지를 위한 일관된 락 순서 (계좌번호 순서대로)
    IF account1 < account2 THEN
        SET first_account = account1;
        SET second_account = account2;
        SET first_amount = amount1;
        SET second_amount = amount2;
    ELSE
        SET first_account = account2;
        SET second_account = account1;
        SET first_amount = amount2;
        SET second_amount = amount1;
    END IF;
    
    START TRANSACTION;
    
    -- 일관된 순서로 락 획득
    UPDATE bank_accounts SET balance = balance + first_amount 
    WHERE account_number = first_account;
    
    UPDATE bank_accounts SET balance = balance + second_amount 
    WHERE account_number = second_account;
    
    COMMIT;
END //
DELIMITER ;

-- 교착상태 감지 쿼리
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
```

---

## 📈 STEP 2: 인덱스 최적화 전략 (75분)

### 2.1 인덱스 분석 및 최적화

#### 🔍 현재 인덱스 현황 분석
```sql
-- 인덱스 사용 현황 분석
SELECT 
    t.TABLE_NAME,
    t.TABLE_ROWS,
    ROUND(((t.DATA_LENGTH + t.INDEX_LENGTH) / 1024 / 1024), 2) AS 'Table Size (MB)',
    ROUND((t.INDEX_LENGTH / 1024 / 1024), 2) AS 'Index Size (MB)',
    ROUND((t.INDEX_LENGTH / (t.DATA_LENGTH + t.INDEX_LENGTH)) * 100, 2) AS 'Index Ratio (%)',
    s.INDEX_NAME,
    s.COLUMN_NAME,
    s.CARDINALITY
FROM information_schema.TABLES t
LEFT JOIN information_schema.STATISTICS s ON t.TABLE_NAME = s.TABLE_NAME
WHERE t.TABLE_SCHEMA = DATABASE()
  AND t.TABLE_TYPE = 'BASE TABLE'
ORDER BY t.TABLE_NAME, s.SEQ_IN_INDEX;

-- 인덱스 효율성 분석
SELECT 
    INDEX_NAME,
    TABLE_NAME,
    COLUMN_NAME,
    CARDINALITY,
    CASE 
        WHEN CARDINALITY IS NULL THEN 'No statistics'
        WHEN CARDINALITY < 10 THEN 'Low selectivity - Consider removal'
        WHEN CARDINALITY > 1000 THEN 'High selectivity - Good'
        ELSE 'Medium selectivity'
    END AS selectivity_assessment
FROM information_schema.STATISTICS 
WHERE TABLE_SCHEMA = DATABASE()
ORDER BY CARDINALITY DESC;
```

#### 🚀 복합 인덱스 최적화
```sql
-- 쿼리 패턴 분석을 위한 복합 인덱스 생성
-- 1. 부서 + 급여 조회 패턴
CREATE INDEX idx_dept_salary_hire ON employees(department, salary, hire_date);

-- 2. 프로젝트 + 직원 + 날짜 패턴
CREATE INDEX idx_project_emp_dates ON project_assignments(project_id, emp_id, start_date, end_date);

-- 3. 급여 이력 조회 패턴
CREATE INDEX idx_salary_emp_date ON salary_history(emp_id, change_date);

-- 인덱스 사용 효과 비교
EXPLAIN FORMAT=JSON
SELECT e.name, e.salary, e.hire_date
FROM employees e
WHERE e.department = '개발팀' 
  AND e.salary > 4000000
  AND e.hire_date >= '2024-01-01'
ORDER BY e.salary DESC;

-- 커버링 인덱스 생성 (데이터까지 포함)
CREATE INDEX idx_covering_employee_summary ON employees(department, salary, name, hire_date);

-- 커버링 인덱스 효과 확인
EXPLAIN FORMAT=JSON
SELECT name, salary, hire_date
FROM employees
WHERE department = '개발팀' AND salary > 4000000;
```

### 2.2 실행 계획 분석

#### 📊 쿼리 성능 분석 도구
```sql
-- 1. 실행 계획 상세 분석
EXPLAIN FORMAT=JSON
SELECT 
    e.name,
    d.dept_name,
    p.project_name,
    pa.allocation_percent
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id
INNER JOIN project_assignments pa ON e.emp_id = pa.emp_id
INNER JOIN projects p ON pa.project_id = p.project_id
WHERE e.salary > 4500000
  AND p.status = 'In Progress'
ORDER BY e.salary DESC
LIMIT 10;

-- 2. 쿼리 프로파일링 활성화
SET profiling = 1;

-- 분석할 쿼리 실행
SELECT COUNT(*) FROM employees e
WHERE EXISTS (
    SELECT 1 FROM project_assignments pa 
    WHERE pa.emp_id = e.emp_id
);

-- 프로파일 결과 확인
SHOW PROFILES;
SHOW PROFILE FOR QUERY 1;

-- 3. 성능 스키마 활용
SELECT 
    EVENT_NAME,
    COUNT_STAR,
    SUM_TIMER_WAIT/1000000000000 AS total_time_sec,
    AVG_TIMER_WAIT/1000000000000 AS avg_time_sec
FROM performance_schema.events_statements_summary_by_event_name
WHERE EVENT_NAME LIKE 'statement/sql/%'
ORDER BY SUM_TIMER_WAIT DESC
LIMIT 10;
```

### 2.3 인덱스 힌트와 최적화

#### 🎯 인덱스 힌트 활용
```sql
-- 1. 특정 인덱스 강제 사용
SELECT /*+ USE_INDEX(employees, idx_dept_salary_hire) */
    name, department, salary
FROM employees
WHERE department = '개발팀' AND salary > 4000000;

-- 2. 인덱스 무시 (테스트 목적)
SELECT /*+ IGNORE_INDEX(employees, idx_dept_salary_hire) */
    name, department, salary
FROM employees
WHERE department = '개발팀' AND salary > 4000000;

-- 3. 조인 순서 최적화
SELECT /*+ STRAIGHT_JOIN */
    e.name, d.dept_name, p.project_name
FROM departments d
INNER JOIN employees e ON d.dept_id = e.dept_id
INNER JOIN project_assignments pa ON e.emp_id = pa.emp_id
INNER JOIN projects p ON pa.project_id = p.project_id
WHERE d.budget > 30000000;
```

---

## ⚡ STEP 3: 쿼리 성능 튜닝 (90분)

### 3.1 성능 튜닝 10가지 기법

#### 🔧 1. SELECT 절 최적화
```sql
-- ❌ 비효율적인 쿼리
SELECT * FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id
WHERE e.salary > 4000000;

-- ✅ 최적화된 쿼리
SELECT e.name, e.salary, d.dept_name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id
WHERE e.salary > 4000000;
```

#### 🔧 2. WHERE 절 최적화
```sql
-- ❌ 함수 사용으로 인덱스 무효화
SELECT * FROM employees WHERE YEAR(hire_date) = 2024;

-- ✅ 범위 조건으로 인덱스 활용
SELECT * FROM employees 
WHERE hire_date >= '2024-01-01' AND hire_date < '2025-01-01';

-- ❌ OR 조건으로 인덱스 효율성 저하
SELECT * FROM employees WHERE department = '개발팀' OR department = '디자인팀';

-- ✅ IN 조건으로 최적화
SELECT * FROM employees WHERE department IN ('개발팀', '디자인팀');
```

#### 🔧 3. JOIN 최적화
```sql
-- 작은 테이블부터 조인하는 최적화된 쿼리
EXPLAIN FORMAT=JSON
SELECT 
    d.dept_name,
    COUNT(e.emp_id) as employee_count,
    AVG(e.salary) as avg_salary
FROM departments d  -- 작은 테이블부터
LEFT JOIN employees e ON d.dept_id = e.dept_id
WHERE d.budget > 25000000  -- 선택적 조건 먼저
GROUP BY d.dept_id, d.dept_name
HAVING COUNT(e.emp_id) > 0
ORDER BY avg_salary DESC;
```

#### 🔧 4. 서브쿼리 vs EXISTS 최적화
```sql
-- 성능 비교용 대용량 데이터 생성 프로시저
DELIMITER //
CREATE PROCEDURE GenerateLargeDataset()
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE random_dept INT;
    DECLARE random_salary INT;
    
    -- 대용량 테스트 테이블 생성
    DROP TABLE IF EXISTS large_employees;
    CREATE TABLE large_employees (
        emp_id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(50),
        department VARCHAR(30),
        salary DECIMAL(10,2),
        hire_date DATE,
        INDEX idx_dept (department),
        INDEX idx_salary (salary)
    );
    
    WHILE i <= 100000 DO
        SET random_dept = FLOOR(RAND() * 5) + 1;
        SET random_salary = FLOOR(RAND() * 5000000) + 3000000;
        
        INSERT INTO large_employees (name, department, salary, hire_date)
        VALUES (
            CONCAT('Employee_', i),
            CASE random_dept
                WHEN 1 THEN '개발팀'
                WHEN 2 THEN '마케팅팀'
                WHEN 3 THEN '디자인팀'
                WHEN 4 THEN '영업팀'
                ELSE '인사팀'
            END,
            random_salary,
            DATE_ADD('2020-01-01', INTERVAL FLOOR(RAND() * 1500) DAY)
        );
        
        SET i = i + 1;
    END WHILE;
END //
DELIMITER ;

-- CALL GenerateLargeDataset();  -- 실행 시 시간이 오래 걸림

-- 서브쿼리 vs EXISTS 성능 비교
-- ❌ 느린 서브쿼리 (IN 사용)
SELECT name, salary FROM large_employees
WHERE department IN (
    SELECT dept_name FROM departments WHERE budget > 30000000
);

-- ✅ 빠른 EXISTS 사용
SELECT name, salary FROM large_employees le
WHERE EXISTS (
    SELECT 1 FROM departments d 
    WHERE d.dept_name = le.department AND d.budget > 30000000
);
```

### 3.2 분할(Partitioning) 전략

#### 🗂️ 테이블 파티셔닝
```sql
-- 날짜 기반 파티셔닝 (급여 이력 테이블)
CREATE TABLE salary_history_partitioned (
    history_id INT AUTO_INCREMENT,
    emp_id INT NOT NULL,
    old_salary DECIMAL(10,2),
    new_salary DECIMAL(10,2),
    change_date DATE NOT NULL,
    change_reason VARCHAR(100),
    PRIMARY KEY (history_id, change_date)
) PARTITION BY RANGE (YEAR(change_date)) (
    PARTITION p2020 VALUES LESS THAN (2021),
    PARTITION p2021 VALUES LESS THAN (2022),
    PARTITION p2022 VALUES LESS THAN (2023),
    PARTITION p2023 VALUES LESS THAN (2024),
    PARTITION p2024 VALUES LESS THAN (2025),
    PARTITION p_future VALUES LESS THAN MAXVALUE
);

-- 파티션 정보 확인
SELECT 
    PARTITION_NAME,
    TABLE_ROWS,
    PARTITION_EXPRESSION,
    PARTITION_DESCRIPTION
FROM information_schema.PARTITIONS
WHERE TABLE_NAME = 'salary_history_partitioned';

-- 파티션 프루닝 효과 확인
EXPLAIN PARTITIONS
SELECT * FROM salary_history_partitioned
WHERE change_date BETWEEN '2024-01-01' AND '2024-12-31';
```

---

## 🏗️ STEP 4: 실무 종합 프로젝트 - ERP 시스템 (180분)

### 4.1 완전한 ERP 데이터베이스 설계

#### 🏢 통합 비즈니스 시스템 구축
```sql
-- 1. 회사 조직 관리
CREATE TABLE companies (
    company_id INT PRIMARY KEY AUTO_INCREMENT,
    company_name VARCHAR(100) NOT NULL,
    business_number VARCHAR(20) UNIQUE,
    ceo_name VARCHAR(50),
    address TEXT,
    phone VARCHAR(20),
    email VARCHAR(100),
    established_date DATE,
    capital DECIMAL(15,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE departments (
    dept_id INT PRIMARY KEY AUTO_INCREMENT,
    company_id INT,
    dept_code VARCHAR(10) UNIQUE,
    dept_name VARCHAR(50) NOT NULL,
    parent_dept_id INT,
    manager_id INT,
    location VARCHAR(100),
    budget DECIMAL(15,2),
    cost_center VARCHAR(20),
    established_date DATE,
    FOREIGN KEY (company_id) REFERENCES companies(company_id),
    FOREIGN KEY (parent_dept_id) REFERENCES departments(dept_id)
);

-- 2. 인사 관리 시스템
CREATE TABLE positions (
    position_id INT PRIMARY KEY AUTO_INCREMENT,
    position_code VARCHAR(10) UNIQUE,
    position_name VARCHAR(50),
    level_order INT,
    min_salary DECIMAL(10,2),
    max_salary DECIMAL(10,2)
);

CREATE TABLE employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_number VARCHAR(20) UNIQUE,
    name VARCHAR(50) NOT NULL,
    english_name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    dept_id INT,
    position_id INT,
    manager_id INT,
    hire_date DATE,
    employment_type ENUM('정규직', '계약직', '인턴', '파견'),
    status ENUM('재직', '휴직', '퇴직') DEFAULT '재직',
    salary DECIMAL(10,2),
    birth_date DATE,
    gender ENUM('M', 'F'),
    address TEXT,
    emergency_contact VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id),
    FOREIGN KEY (position_id) REFERENCES positions(position_id),
    FOREIGN KEY (manager_id) REFERENCES employees(emp_id)
);

-- 3. 프로젝트 관리 시스템
CREATE TABLE project_categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(50),
    description TEXT
);

CREATE TABLE projects (
    project_id INT PRIMARY KEY AUTO_INCREMENT,
    project_code VARCHAR(20) UNIQUE,
    project_name VARCHAR(100) NOT NULL,
    category_id INT,
    client_company VARCHAR(100),
    project_manager_id INT,
    start_date DATE,
    end_date DATE,
    status ENUM('기획', '진행중', '완료', '중단', '보류') DEFAULT '기획',
    budget DECIMAL(15,2),
    actual_cost DECIMAL(15,2) DEFAULT 0,
    description TEXT,
    priority ENUM('높음', '보통', '낮음') DEFAULT '보통',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES project_categories(category_id),
    FOREIGN KEY (project_manager_id) REFERENCES employees(emp_id)
);

-- 4. 재무 관리 시스템
CREATE TABLE accounts (
    account_id INT PRIMARY KEY AUTO_INCREMENT,
    account_code VARCHAR(20) UNIQUE,
    account_name VARCHAR(100),
    account_type ENUM('자산', '부채', '자본', '수익', '비용'),
    parent_account_id INT,
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (parent_account_id) REFERENCES accounts(account_id)
);

CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    transaction_date DATE,
    description VARCHAR(200),
    reference_number VARCHAR(50),
    total_amount DECIMAL(15,2),
    created_by INT,
    approved_by INT,
    status ENUM('작성', '승인', '완료') DEFAULT '작성',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (created_by) REFERENCES employees(emp_id),
    FOREIGN KEY (approved_by) REFERENCES employees(emp_id)
);

CREATE TABLE transaction_details (
    detail_id INT PRIMARY KEY AUTO_INCREMENT,
    transaction_id INT,
    account_id INT,
    debit_amount DECIMAL(15,2) DEFAULT 0,
    credit_amount DECIMAL(15,2) DEFAULT 0,
    description VARCHAR(200),
    FOREIGN KEY (transaction_id) REFERENCES transactions(transaction_id),
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);
```

### 4.2 비즈니스 로직 구현

#### 💼 급여 계산 시스템
```sql
DELIMITER //

-- 월급여 계산 프로시저
CREATE PROCEDURE CalculateMonthlyPayroll(
    IN payroll_year INT,
    IN payroll_month INT,
    IN dept_id_filter INT DEFAULT NULL
)
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE emp_id INT;
    DECLARE base_salary DECIMAL(10,2);
    DECLARE overtime_hours DECIMAL(5,2);
    DECLARE bonus_amount DECIMAL(10,2);
    DECLARE deduction_amount DECIMAL(10,2);
    
    -- 급여 계산 결과 테이블
    DROP TEMPORARY TABLE IF EXISTS payroll_results;
    CREATE TEMPORARY TABLE payroll_results (
        emp_id INT,
        emp_name VARCHAR(50),
        dept_name VARCHAR(50),
        base_salary DECIMAL(10,2),
        overtime_pay DECIMAL(10,2),
        bonus DECIMAL(10,2),
        gross_pay DECIMAL(10,2),
        tax_deduction DECIMAL(10,2),
        insurance_deduction DECIMAL(10,2),
        total_deduction DECIMAL(10,2),
        net_pay DECIMAL(10,2)
    );
    
    -- 급여 대상자 커서
    DECLARE payroll_cursor CURSOR FOR
        SELECT e.emp_id, e.salary
        FROM employees e
        WHERE e.status = '재직'
          AND (dept_id_filter IS NULL OR e.dept_id = dept_id_filter);
    
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    
    OPEN payroll_cursor;
    
    payroll_loop: LOOP
        FETCH payroll_cursor INTO emp_id, base_salary;
        
        IF done THEN
            LEAVE payroll_loop;
        END IF;
        
        -- 초과근무 시간 조회 (별도 테이블에서)
        SET overtime_hours = FLOOR(RAND() * 20);  -- 시뮬레이션
        
        -- 성과급 계산
        SET bonus_amount = CASE 
            WHEN base_salary >= 6000000 THEN base_salary * 0.1
            WHEN base_salary >= 4000000 THEN base_salary * 0.05
            ELSE 0
        END;
        
        -- 세금 및 보험료 계산
        SET deduction_amount = base_salary * 0.15;  -- 15% 공제
        
        -- 결과 삽입
        INSERT INTO payroll_results
        SELECT 
            e.emp_id,
            e.name,
            d.dept_name,
            base_salary,
            overtime_hours * (base_salary / 240),  -- 시간당 급여
            bonus_amount,
            base_salary + (overtime_hours * (base_salary / 240)) + bonus_amount,
            deduction_amount * 0.6,  -- 세금
            deduction_amount * 0.4,  -- 보험료
            deduction_amount,
            base_salary + (overtime_hours * (base_salary / 240)) + bonus_amount - deduction_amount
        FROM employees e
        INNER JOIN departments d ON e.dept_id = d.dept_id
        WHERE e.emp_id = emp_id;
        
    END LOOP;
    
    CLOSE payroll_cursor;
    
    -- 급여 명세서 출력
    SELECT * FROM payroll_results ORDER BY dept_name, emp_name;
    
    -- 부서별 급여 요약
    SELECT 
        dept_name,
        COUNT(*) AS employee_count,
        SUM(base_salary) AS total_base_salary,
        SUM(overtime_pay) AS total_overtime_pay,
        SUM(bonus) AS total_bonus,
        SUM(gross_pay) AS total_gross_pay,
        SUM(total_deduction) AS total_deduction,
        SUM(net_pay) AS total_net_pay
    FROM payroll_results
    GROUP BY dept_name
    ORDER BY total_net_pay DESC;
    
END //

DELIMITER ;
```

#### 📊 프로젝트 대시보드 시스템
```sql
DELIMITER //

-- 프로젝트 종합 대시보드 프로시저
CREATE PROCEDURE ProjectDashboard(
    IN start_date DATE,
    IN end_date DATE
)
BEGIN
    -- 1. 프로젝트 현황 요약
    SELECT 
        '프로젝트 현황' AS metric_category,
        status,
        COUNT(*) AS project_count,
        SUM(budget) AS total_budget,
        SUM(actual_cost) AS total_actual_cost,
        AVG(DATEDIFF(end_date, start_date)) AS avg_duration_days
    FROM projects
    WHERE start_date BETWEEN start_date AND end_date
    GROUP BY status
    
    UNION ALL
    
    -- 2. 부서별 프로젝트 참여도
    SELECT 
        '부서별 참여도' AS metric_category,
        d.dept_name AS status,
        COUNT(DISTINCT p.project_id) AS project_count,
        SUM(p.budget) AS total_budget,
        0 AS total_actual_cost,
        0 AS avg_duration_days
    FROM projects p
    INNER JOIN project_assignments pa ON p.project_id = pa.project_id
    INNER JOIN employees e ON pa.emp_id = e.emp_id
    INNER JOIN departments d ON e.dept_id = d.dept_id
    WHERE p.start_date BETWEEN start_date AND end_date
    GROUP BY d.dept_id, d.dept_name
    ORDER BY metric_category, total_budget DESC;
    
    -- 3. 수익성 분석
    WITH project_profitability AS (
        SELECT 
            p.project_name,
            p.budget,
            p.actual_cost,
            p.budget - p.actual_cost AS profit,
            ROUND((p.budget - p.actual_cost) / p.budget * 100, 2) AS profit_margin,
            CASE 
                WHEN p.actual_cost > p.budget * 1.1 THEN 'Over Budget'
                WHEN p.actual_cost > p.budget * 0.9 THEN 'On Budget'
                ELSE 'Under Budget'
            END AS budget_status
        FROM projects p
        WHERE p.status = '완료'
          AND p.start_date BETWEEN start_date AND end_date
    )
    SELECT 
        budget_status,
        COUNT(*) AS project_count,
        AVG(profit_margin) AS avg_profit_margin,
        SUM(profit) AS total_profit
    FROM project_profitability
    GROUP BY budget_status;
END //

DELIMITER ;

-- 대시보드 실행
CALL ProjectDashboard('2024-01-01', '2024-12-31');
```

### 4.3 보고서 자동화 시스템

#### 📈 경영진 보고서 생성
```sql
DELIMITER //

-- 월간 경영 보고서 생성 프로시저
CREATE PROCEDURE GenerateExecutiveReport(
    IN report_year INT,
    IN report_month INT
)
BEGIN
    DECLARE report_start_date DATE;
    DECLARE report_end_date DATE;
    
    SET report_start_date = STR_TO_DATE(CONCAT(report_year, '-', report_month, '-01'), '%Y-%m-%d');
    SET report_end_date = LAST_DAY(report_start_date);
    
    -- 보고서 헤더
    SELECT 
        CONCAT(report_year, '년 ', report_month, '월 경영 보고서') AS report_title,
        NOW() AS generated_at;
    
    -- 1. 인력 현황
    SELECT 
        '인력 현황' AS section,
        d.dept_name AS department,
        COUNT(e.emp_id) AS headcount,
        SUM(e.salary) AS total_salary_cost,
        AVG(e.salary) AS avg_salary,
        COUNT(CASE WHEN e.hire_date >= report_start_date THEN 1 END) AS new_hires,
        COUNT(CASE WHEN e.status = '퇴직' THEN 1 END) AS departures
    FROM departments d
    LEFT JOIN employees e ON d.dept_id = e.dept_id
    GROUP BY d.dept_id, d.dept_name
    ORDER BY total_salary_cost DESC;
    
    -- 2. 프로젝트 성과
    SELECT 
        '프로젝트 성과' AS section,
        p.status,
        COUNT(*) AS project_count,
        SUM(p.budget) AS total_budget,
        SUM(p.actual_cost) AS total_cost,
        SUM(p.budget - p.actual_cost) AS total_profit,
        ROUND(AVG((p.budget - p.actual_cost) / p.budget * 100), 2) AS avg_profit_margin
    FROM projects p
    WHERE p.start_date <= report_end_date
      AND (p.end_date >= report_start_date OR p.end_date IS NULL)
    GROUP BY p.status;
    
    -- 3. 재무 현황 (간단 버전)
    SELECT 
        '재무 현황' AS section,
        a.account_type,
        SUM(CASE WHEN td.debit_amount > 0 THEN td.debit_amount ELSE 0 END) AS total_debit,
        SUM(CASE WHEN td.credit_amount > 0 THEN td.credit_amount ELSE 0 END) AS total_credit,
        SUM(td.debit_amount - td.credit_amount) AS net_balance
    FROM accounts a
    LEFT JOIN transaction_details td ON a.account_id = td.account_id
    LEFT JOIN transactions t ON td.transaction_id = t.transaction_id
    WHERE t.transaction_date BETWEEN report_start_date AND report_end_date
    GROUP BY a.account_type;
    
    -- 4. 핵심 성과 지표 (KPI)
    SELECT 
        'KPI' AS section,
        'Employee Productivity' AS kpi_name,
        ROUND(
            (SELECT SUM(budget) FROM projects WHERE status = '완료' 
             AND end_date BETWEEN report_start_date AND report_end_date) /
            (SELECT COUNT(*) FROM employees WHERE status = '재직'), 0
        ) AS kpi_value,
        '원/인' AS unit;
        
END //

DELIMITER ;

-- 보고서 생성 실행
CALL GenerateExecutiveReport(2024, 5);
```

---

## 🔄 STEP 5: 백업과 복원 전략 (45분)

### 5.1 데이터베이스 백업 전략

#### 💾 자동화된 백업 시스템
```sql
-- 백업 로그 테이블
CREATE TABLE backup_log (
    backup_id INT PRIMARY KEY AUTO_INCREMENT,
    backup_type ENUM('FULL', 'INCREMENTAL', 'DIFFERENTIAL'),
    backup_file_path VARCHAR(500),
    backup_size_mb DECIMAL(10,2),
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    status ENUM('SUCCESS', 'FAILED', 'IN_PROGRESS'),
    error_message TEXT,
    created_by VARCHAR(50) DEFAULT USER()
);

-- 백업 실행 프로시저
DELIMITER //
CREATE PROCEDURE ExecuteBackup(
    IN backup_type_param VARCHAR(20),
    IN backup_path VARCHAR(500)
)
BEGIN
    DECLARE backup_start TIMESTAMP DEFAULT NOW();
    DECLARE backup_id INT;
    DECLARE backup_command TEXT;
    
    -- 백업 로그 시작 기록
    INSERT INTO backup_log (backup_type, backup_file_path, start_time, status)
    VALUES (backup_type_param, backup_path, backup_start, 'IN_PROGRESS');
    
    SET backup_id = LAST_INSERT_ID();
    
    -- 백업 명령어 생성 (실제 실행은 시스템 레벨에서)
    SET backup_command = CONCAT(
        'mysqldump -u root -p --routines --triggers --single-transaction ',
        DATABASE(), ' > ', backup_path
    );
    
    -- 백업 완료 기록 (시뮬레이션)
    UPDATE backup_log 
    SET end_time = NOW(), 
        status = 'SUCCESS',
        backup_size_mb = ROUND(RAND() * 1000 + 100, 2)  -- 시뮬레이션
    WHERE backup_log.backup_id = backup_id;
    
    -- 백업 명령어 출력
    SELECT backup_command AS 'Execute this command in terminal:';
    
END //
DELIMITER ;

-- 백업 실행
CALL ExecuteBackup('FULL', '/backup/daily_backup_2024_05_26.sql');

-- 백업 이력 조회
SELECT 
    backup_type,
    backup_file_path,
    backup_size_mb,
    TIMESTAMPDIFF(MINUTE, start_time, end_time) AS duration_minutes,
    status,
    start_time
FROM backup_log
ORDER BY start_time DESC;
```

### 5.2 재해 복구 계획

#### 🛡️ 비즈니스 연속성 계획
```sql
-- 중요 테이블 우선순위 정의
CREATE TABLE recovery_priorities (
    table_name VARCHAR(100) PRIMARY KEY,
    priority_level ENUM('CRITICAL', 'HIGH', 'MEDIUM', 'LOW'),
    recovery_time_objective_hours INT,  -- 복구 목표 시간
    backup_frequency_hours INT,         -- 백업 주기
    description TEXT
);

-- 복구 우선순위 데이터
INSERT INTO recovery_priorities VALUES
('companies', 'CRITICAL', 1, 6, '회사 기본 정보'),
('employees', 'CRITICAL', 1, 6, '직원 정보'),
('projects', 'HIGH', 4, 12, '프로젝트 정보'),
('transactions', 'HIGH', 4, 12, '재무 거래'),
('departments', 'CRITICAL', 1, 6, '조직 구조'),
('accounts', 'HIGH', 2, 8, '계정 정보'),
('salary_history', 'MEDIUM', 8, 24, '급여 이력'),
('project_assignments', 'MEDIUM', 8, 24, '프로젝트 배정'),
('backup_log', 'LOW', 24, 48, '백업 로그');

-- 복구 계획 조회
SELECT 
    priority_level,
    COUNT(*) AS table_count,
    MAX(recovery_time_objective_hours) AS max_rto_hours,
    MIN(backup_frequency_hours) AS min_backup_freq
FROM recovery_priorities
GROUP BY priority_level
ORDER BY FIELD(priority_level, 'CRITICAL', 'HIGH', 'MEDIUM', 'LOW');
```

---

## 🎯 STEP 6: 최종 성과 평가 (60분)

### 6.1 시스템 성능 벤치마크

#### 📊 종합 성능 테스트
```sql
-- 성능 테스트 결과 테이블
CREATE TABLE performance_benchmark (
    test_id INT PRIMARY KEY AUTO_INCREMENT,
    test_name VARCHAR(100),
    query_type VARCHAR(50),
    execution_time_ms DECIMAL(10,3),
    rows_examined INT,
    rows_returned INT,
    index_usage VARCHAR(200),
    optimization_notes TEXT,
    test_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 복잡한 분석 쿼리 성능 테스트
DELIMITER //
CREATE PROCEDURE BenchmarkComplexQueries()
BEGIN
    DECLARE start_time DECIMAL(15,6);
    DECLARE end_time DECIMAL(15,6);
    DECLARE execution_time DECIMAL(10,3);
    
    -- 1. 다중 JOIN 쿼리 테스트
    SET start_time = UNIX_TIMESTAMP(NOW(6));
    
    SELECT COUNT(*) FROM (
        SELECT 
            e.name,
            d.dept_name,
            p.project_name,
            SUM(pa.allocation_percent) as total_allocation
        FROM employees e
        INNER JOIN departments d ON e.dept_id = d.dept_id
        INNER JOIN project_assignments pa ON e.emp_id = pa.emp_id
        INNER JOIN projects p ON pa.project_id = p.project_id
        WHERE e.salary > 4000000
        GROUP BY e.emp_id, e.name, d.dept_name, p.project_name
        HAVING total_allocation > 50
    ) AS complex_query;
    
    SET end_time = UNIX_TIMESTAMP(NOW(6));
    SET execution_time = (end_time - start_time) * 1000;
    
    INSERT INTO performance_benchmark 
    (test_name, query_type, execution_time_ms, optimization_notes)
    VALUES ('Complex Multi-JOIN', 'ANALYTICAL', execution_time, 'Multi-table join with aggregation');
    
    -- 2. 서브쿼리 성능 테스트
    SET start_time = UNIX_TIMESTAMP(NOW(6));
    
    SELECT COUNT(*) FROM employees e
    WHERE e.salary > (
        SELECT AVG(salary) FROM employees 
        WHERE department = e.department
    ) AND EXISTS (
        SELECT 1 FROM project_assignments pa 
        WHERE pa.emp_id = e.emp_id
    );
    
    SET end_time = UNIX_TIMESTAMP(NOW(6));
    SET execution_time = (end_time - start_time) * 1000;
    
    INSERT INTO performance_benchmark 
    (test_name, query_type, execution_time_ms, optimization_notes)
    VALUES ('Correlated Subquery with EXISTS', 'SUBQUERY', execution_time, 'Correlated subquery performance');
    
    -- 3. 윈도우 함수 성능 테스트
    SET start_time = UNIX_TIMESTAMP(NOW(6));
    
    SELECT COUNT(*) FROM (
        SELECT 
            name,
            salary,
            RANK() OVER (PARTITION BY department ORDER BY salary DESC) as dept_rank,
            LAG(salary) OVER (PARTITION BY department ORDER BY hire_date) as prev_salary
        FROM employees
        WHERE salary IS NOT NULL
    ) ranked_employees;
    
    SET end_time = UNIX_TIMESTAMP(NOW(6));
    SET execution_time = (end_time - start_time) * 1000;
    
    INSERT INTO performance_benchmark 
    (test_name, query_type, execution_time_ms, optimization_notes)
    VALUES ('Window Functions', 'ANALYTICAL', execution_time, 'RANK and LAG window functions');
    
END //
DELIMITER ;

-- 벤치마크 실행
CALL BenchmarkComplexQueries();

-- 성능 결과 분석
SELECT 
    query_type,
    COUNT(*) as test_count,
    AVG(execution_time_ms) as avg_execution_time,
    MAX(execution_time_ms) as max_execution_time,
    MIN(execution_time_ms) as min_execution_time
FROM performance_benchmark
GROUP BY query_type
ORDER BY avg_execution_time DESC;
```

### 6.2 학습 성과 체크리스트

#### 📋 최종 역량 평가
```sql
-- 학습 성과 평가 테이블
CREATE TABLE learning_assessment (
    skill_category VARCHAR(50),
    skill_name VARCHAR(100),
    proficiency_level ENUM('초급', '중급', '고급', '전문가'),
    practical_examples TEXT,
    mastery_score INT CHECK (mastery_score BETWEEN 0 AND 100)
);

-- 학습 성과 데이터 입력
INSERT INTO learning_assessment VALUES
('기본 SQL', 'SELECT, INSERT, UPDATE, DELETE', '전문가', 'CRUD 연산 완벽 구사', 95),
('조인', 'INNER, LEFT, RIGHT, SELF JOIN', '전문가', '복잡한 다중 테이블 조인 구현', 90),
('서브쿼리', '상관 서브쿼리, EXISTS, CTE', '고급', '복잡한 비즈니스 로직 구현', 85),
('집계 함수', 'GROUP BY, HAVING, 윈도우 함수', '고급', '고급 분석 쿼리 작성', 85),
('성능 최적화', '인덱스, 실행 계획, 튜닝', '중급', '기본적인 성능 최적화', 75),
('함수/프로시저', '사용자 정의 함수, 저장 프로시저', '고급', '복잡한 비즈니스 로직 모듈화', 80),
('트랜잭션', 'ACID, 격리 수준, 동시성 제어', '중급', '안전한 트랜잭션 처리', 75),
('실무 응용', 'ERP 시스템, 보고서 자동화', '고급', '종합적인 시스템 구축', 85);

-- 최종 성과 리포트
SELECT 
    skill_category,
    COUNT(*) as skill_count,
    AVG(mastery_score) as avg_mastery_score,
    GROUP_CONCAT(
        CONCAT(skill_name, '(', proficiency_level, ')')
        ORDER BY mastery_score DESC
    ) as skills_summary
FROM learning_assessment
GROUP BY skill_category
ORDER BY avg_mastery_score DESC;

-- 전체 학습 성과 요약
SELECT 
    ROUND(AVG(mastery_score), 1) as overall_mastery_score,
    COUNT(CASE WHEN proficiency_level = '전문가' THEN 1 END) as expert_skills,
    COUNT(CASE WHEN proficiency_level = '고급' THEN 1 END) as advanced_skills,
    COUNT(CASE WHEN proficiency_level = '중급' THEN 1 END) as intermediate_skills,
    COUNT(*) as total_skills,
    CASE 
        WHEN AVG(mastery_score) >= 90 THEN 'SQL 전문가 수준'
        WHEN AVG(mastery_score) >= 80 THEN 'SQL 고급 개발자 수준'
        WHEN AVG(mastery_score) >= 70 THEN 'SQL 중급 개발자 수준'
        ELSE 'SQL 초급 개발자 수준'
    END as certification_level
FROM learning_assessment;
```

---

## 📚 Day 5 최종 정리

### ✅ 완료 체크리스트
- [ ] ACID 원칙 완전 이해 완료
- [ ] 트랜잭션 격리 수준 실습 완료
- [ ] 인덱스 최적화 전략 수립 완료
- [ ] 쿼리 성능 튜닝 기법 습득 완료
- [ ] 종합 ERP 시스템 구축 완료
- [ ] 백업/복원 전략 수립 완료
- [ ] 최종 성과 평가 완료

### 🎯 핵심 성취 사항

#### 트랜잭션 마스터
- ACID 원칙 완벽 이해
- 4가지 격리 수준 실습
- 교착상태 해결 방안 구현
- 안전한 금융 거래 시스템 구축

#### 성능 최적화 전문가
- 인덱스 설계 및 최적화
- 쿼리 실행 계획 분석
- 10가지 성능 튜닝 기법 습득
- 대용량 데이터 처리 최적화

#### 실무 프로젝트 완성
- 완전한 ERP 시스템 설계
- 급여 계산 자동화 시스템
- 프로젝트 관리 대시보드
- 경영진 보고서 자동화

### 💡 실무 적용 가이드

#### 즉시 적용 가능한 기술
1. **트랜잭션 설계**: 금융, 전자상거래 시스템
2. **성능 최적화**: 대용량 데이터 처리 시스템
3. **복합 쿼리**: 비즈니스 인텔리전스, 분석 시스템
4. **자동화 프로시저**: 정기 보고서, 배치 처리

#### 지속적 개발 영역
1. **NoSQL 연동**: MongoDB, Redis와의 통합
2. **클라우드 데이터베이스**: AWS RDS, Azure SQL
3. **빅데이터 처리**: Spark, Hadoop과의 연계
4. **실시간 분석**: 스트리밍 데이터 처리

### 🏆 인증 및 다음 단계

#### 획득 가능한 자격증
- **MySQL 8.0 Database Administrator**
- **Oracle Database SQL Certified Associate**
- **Microsoft Azure Database Administrator**
- **AWS Certified Database - Specialty**

#### 추천 학습 경로
1. **고급 데이터베이스 설계**: 정규화, 모델링
2. **데이터웨어하우스**: ETL, OLAP, 차원 모델링
3. **클라우드 데이터베이스**: 확장성, 가용성 설계
4. **데이터 엔지니어링**: 파이프라인, 실시간 처리

---

## 🎊 축하합니다!

**5일간의 SQL 마스터 과정을 완주하셨습니다!**

### 🏅 달성한 성과
- ✅ **300+ SQL 쿼리** 직접 작성 및 실행
- ✅ **완전한 ERP 시스템** 설계 및 구현
- ✅ **고급 최적화 기법** 습득
- ✅ **실무 즉시 적용 가능한 스킬** 확보

### 🚀 앞으로의 여정
이제 여러분은 **SQL 전문가**로서 다음과 같은 프로젝트를 자신 있게 수행할 수 있습니다:

1. **대규모 데이터베이스 설계** 📊
2. **복잡한 비즈니스 로직 구현** 💼
3. **성능 최적화 및 튜닝** ⚡
4. **자동화 시스템 구축** 🤖

### 💪 지속적인 성장을 위한 조언
- **실무 프로젝트에 적극 적용**하세요
- **새로운 기술 트렌드**를 지속적으로 학습하세요
- **커뮤니티 활동**을 통해 지식을 공유하세요
- **오픈소스 프로젝트**에 참여해보세요

**여러분의 SQL 여정은 이제 시작입니다! 계속해서 성장해나가시길 응원합니다!** 🎯✨ 