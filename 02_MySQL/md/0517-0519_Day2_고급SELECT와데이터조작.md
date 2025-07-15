# 🔥 Day 2: 고급 SELECT문과 데이터 조작 마스터

##### 📅 학습 기간: 2025.05.17 ~ 2025.05.19 (3일)
##### 🎯 학습 목표: 복잡한 쿼리 작성 + 데이터 조작 + 제약조건 활용
##### 📝 Writer : Moon19ht

---

## 📋 Day 2 학습 체크리스트

- [x] 복잡한 WHERE 조건 10가지 이상 실습
- [x] 문자열 함수 5개 이상 활용
- [x] 날짜 함수 5개 이상 활용
- [x] UPDATE/DELETE 안전하게 수행
- [x] 제약조건 5가지 모두 적용
- [x] 서브쿼리 기본 패턴 3가지 실습
- [x] 실무 시나리오 3개 해결

---

## 🔍 STEP 1: 고급 WHERE 조건 완전 정복 (60분)

### 1.1 논리 연산자 활용

#### 🎯 AND, OR, NOT 조합
```sql
-- 복합 조건 1: 개발팀이면서 급여 400만원 이상
SELECT name, department, salary 
FROM employees 
WHERE department = '개발팀' AND salary >= 4000000;

-- 복합 조건 2: 개발팀 또는 디자인팀
SELECT name, department, salary 
FROM employees 
WHERE department = '개발팀' OR department = '디자인팀';

-- 복합 조건 3: 개발팀이 아닌 직원
SELECT name, department, salary 
FROM employees 
WHERE NOT department = '개발팀';

-- 복합 조건 4: (개발팀이면서 급여 500만원 이상) 또는 (마케팅팀이면서 급여 450만원 이상)
SELECT name, department, salary 
FROM employees 
WHERE (department = '개발팀' AND salary >= 5000000) 
   OR (department = '마케팅팀' AND salary >= 4500000);
```

### 1.2 범위 조건

#### 📊 BETWEEN, IN, NOT IN
```sql
-- 급여 범위 조건
SELECT name, salary 
FROM employees 
WHERE salary BETWEEN 4000000 AND 5500000;

-- 특정 부서들만 선택
SELECT name, department 
FROM employees 
WHERE department IN ('개발팀', '디자인팀', '마케팅팀');

-- 특정 부서 제외
SELECT name, department 
FROM employees 
WHERE department NOT IN ('인사팀', '영업팀');

-- 날짜 범위 조건
SELECT name, hire_date 
FROM employees 
WHERE hire_date BETWEEN '2024-01-01' AND '2024-02-28';
```

### 1.3 패턴 매칭 고급

#### 🔍 LIKE 연산자 완전 활용
```sql
-- 이름 패턴 검색
SELECT name, department 
FROM employees 
WHERE name LIKE '김%';          -- 김으로 시작

SELECT name, department 
FROM employees 
WHERE name LIKE '%수';          -- 수로 끝남

SELECT name, department 
FROM employees 
WHERE name LIKE '%철%';         -- 철이 포함

SELECT name, department 
FROM employees 
WHERE name LIKE '이__';         -- 이로 시작하는 3글자 이름

SELECT name, email 
FROM employees 
WHERE email LIKE '%@company.com';  -- 회사 도메인 이메일
```

### 1.4 NULL 처리

#### ⚠️ NULL 값 다루기
```sql
-- NULL 값 찾기
SELECT name, department 
FROM employees 
WHERE department IS NULL;

-- NULL이 아닌 값 찾기
SELECT name, department 
FROM employees 
WHERE department IS NOT NULL;

-- NULL 값을 다른 값으로 대체
SELECT name, IFNULL(department, '부서미정') AS department 
FROM employees;

-- COALESCE: 첫 번째 NULL이 아닌 값 반환
SELECT name, COALESCE(department, position, '정보없음') AS info 
FROM employees;
```

---

## 🔤 STEP 2: 문자열 함수 실무 활용 (45분)

### 2.1 기본 문자열 조작

#### ✂️ 문자열 자르기와 조합
```sql
-- 문자열 길이 및 기본 조작
SELECT 
    name,
    LENGTH(name) AS name_length,           -- 문자열 길이
    CHAR_LENGTH(name) AS char_length,      -- 문자 개수 (한글 고려)
    UPPER(name) AS upper_name,             -- 대문자 변환
    LOWER(email) AS lower_email,           -- 소문자 변환
    SUBSTRING(name, 1, 1) AS first_char,   -- 첫 글자
    SUBSTRING(email, 1, LOCATE('@', email)-1) AS username  -- @ 앞의 사용자명
FROM employees;
```

#### 🔗 문자열 결합과 치환
```sql
-- 문자열 조합 및 포맷팅
SELECT 
    name,
    CONCAT(name, ' (', department, ')') AS name_with_dept,
    CONCAT(name, ' 님') AS greeting,
    REPLACE(email, '@company.com', '@newcompany.com') AS new_email,
    TRIM(CONCAT('  ', name, '  ')) AS trimmed_name
FROM employees;
```

### 2.2 실무 문자열 처리

#### 📞 전화번호 포맷팅 실습
```sql
-- 전화번호 테이블 추가 생성 (실습용)
CREATE TABLE employee_contacts (
    emp_id INT,
    phone VARCHAR(20),
    address VARCHAR(200)
);

-- 샘플 데이터 입력 (다양한 형태의 전화번호)
INSERT INTO employee_contacts VALUES
(1, '01012345678', '서울시 강남구'),
(2, '010-1234-5678', '서울시 홍대'),
(3, '010 1234 5678', '서울시 성수'),
(4, '02-123-4567', '서울시 명동'),
(5, '0212345678', '서울시 여의도');

-- 전화번호 표준화
SELECT 
    emp_id,
    phone,
    CASE 
        WHEN phone LIKE '010%' AND LENGTH(REPLACE(REPLACE(phone, '-', ''), ' ', '')) = 11 
        THEN CONCAT(
            SUBSTRING(REPLACE(REPLACE(phone, '-', ''), ' ', ''), 1, 3), '-',
            SUBSTRING(REPLACE(REPLACE(phone, '-', ''), ' ', ''), 4, 4), '-',
            SUBSTRING(REPLACE(REPLACE(phone, '-', ''), ' ', ''), 8, 4)
        )
        WHEN phone LIKE '02%'
        THEN CONCAT('02-', SUBSTRING(REPLACE(REPLACE(phone, '-', ''), ' ', ''), 3, 3), '-', SUBSTRING(REPLACE(REPLACE(phone, '-', ''), ' ', ''), 6))
        ELSE phone
    END AS formatted_phone
FROM employee_contacts;
```

---

## 📅 STEP 3: 날짜 함수 완전 정복 (45분)

### 3.1 현재 날짜/시간 함수

#### ⏰ 시간 정보 획득
```sql
-- 현재 시간 정보
SELECT 
    NOW() AS current_datetime,              -- 현재 날짜와 시간
    CURDATE() AS current_date,              -- 현재 날짜
    CURTIME() AS current_time,              -- 현재 시간
    UNIX_TIMESTAMP() AS unix_timestamp,     -- Unix 타임스탬프
    FROM_UNIXTIME(UNIX_TIMESTAMP()) AS from_unix;  -- Unix → 날짜 변환
```

### 3.2 날짜 추출 및 형식화

#### 📊 날짜 성분 추출
```sql
-- 입사일 분석
SELECT 
    name,
    hire_date,
    YEAR(hire_date) AS hire_year,           -- 입사 연도
    MONTH(hire_date) AS hire_month,         -- 입사 월
    DAY(hire_date) AS hire_day,             -- 입사 일
    DAYOFWEEK(hire_date) AS day_of_week,    -- 요일 (1=일요일)
    DAYNAME(hire_date) AS day_name,         -- 요일명
    MONTHNAME(hire_date) AS month_name,     -- 월명
    QUARTER(hire_date) AS quarter,          -- 분기
    WEEK(hire_date) AS week_number          -- 주차
FROM employees;
```

#### 🎨 날짜 형식화
```sql
-- 다양한 날짜 형식
SELECT 
    name,
    hire_date,
    DATE_FORMAT(hire_date, '%Y년 %m월 %d일') AS korean_format,
    DATE_FORMAT(hire_date, '%Y-%m-%d (%a)') AS date_with_day,
    DATE_FORMAT(hire_date, '%c/%e/%Y') AS us_format,
    DATE_FORMAT(hire_date, '%Y년 %c월 %e일 %W') AS full_korean
FROM employees;
```

### 3.3 날짜 계산

#### ➕ 날짜 연산
```sql
-- 날짜 계산 및 분석
SELECT 
    name,
    hire_date,
    DATEDIFF(NOW(), hire_date) AS days_worked,              -- 근무 일수
    DATEDIFF(NOW(), hire_date) / 365 AS years_worked,       -- 근무 년수
    DATE_ADD(hire_date, INTERVAL 1 YEAR) AS first_anniversary,    -- 1주년
    DATE_ADD(hire_date, INTERVAL 6 MONTH) AS probation_end,       -- 수습 종료일
    DATE_SUB(NOW(), INTERVAL 1 YEAR) AS one_year_ago,             -- 1년 전
    LAST_DAY(hire_date) AS month_end,                             -- 입사월 마지막 날
    -- 근무 기간 카테고리
    CASE 
        WHEN DATEDIFF(NOW(), hire_date) < 365 THEN '신입'
        WHEN DATEDIFF(NOW(), hire_date) < 1095 THEN '주니어'
        ELSE '시니어'
    END AS experience_level
FROM employees;
```

---

## 🔄 STEP 4: UPDATE와 DELETE 안전 활용 (45분)

### 4.1 안전한 UPDATE

#### ⚠️ UPDATE 실습 (반드시 WHERE 조건 포함)
```sql
-- 1. 단일 컬럼 업데이트
UPDATE employees 
SET salary = 5800000 
WHERE name = '김철수';

-- 2. 여러 컬럼 동시 업데이트
UPDATE employees 
SET salary = salary * 1.1, 
    updated_at = NOW() 
WHERE department = '개발팀';

-- 3. 조건부 업데이트 (CASE 사용)
UPDATE employees 
SET salary = CASE 
    WHEN department = '개발팀' THEN salary * 1.15
    WHEN department = '디자인팀' THEN salary * 1.10
    WHEN department = '마케팅팀' THEN salary * 1.08
    ELSE salary * 1.05
END
WHERE salary IS NOT NULL;

-- 4. 부분 문자열 업데이트
UPDATE employees 
SET email = REPLACE(email, '@company.com', '@newcompany.co.kr')
WHERE email LIKE '%@company.com';
```

#### 🛡️ 안전한 UPDATE 절차
```sql
-- 1단계: 업데이트할 데이터 먼저 확인
SELECT emp_id, name, salary, department 
FROM employees 
WHERE department = '개발팀';

-- 2단계: 실제 업데이트 실행
UPDATE employees 
SET salary = salary * 1.1 
WHERE department = '개발팀';

-- 3단계: 결과 확인
SELECT emp_id, name, salary, department 
FROM employees 
WHERE department = '개발팀';
```

### 4.2 안전한 DELETE

#### 🗑️ DELETE 실습
```sql
-- 실습용 임시 데이터 생성
INSERT INTO employees (name, email, department, position, salary, hire_date)
VALUES 
    ('임시직원1', 'temp1@company.com', '임시팀', 'Temp', 3000000, '2024-05-01'),
    ('임시직원2', 'temp2@company.com', '임시팀', 'Temp', 3000000, '2024-05-01');

-- 1. 조건부 삭제
DELETE FROM employees 
WHERE department = '임시팀';

-- 2. 복합 조건 삭제
DELETE FROM employees 
WHERE salary < 3500000 AND hire_date < '2024-01-01';

-- 3. 서브쿼리를 이용한 삭제 (위험할 수 있으므로 주의)
-- DELETE FROM employees 
-- WHERE emp_id IN (
--     SELECT emp_id FROM (
--         SELECT emp_id FROM employees WHERE salary < 3000000
--     ) AS temp
-- );
```

#### 🛡️ 안전한 DELETE 절차
```sql
-- 1단계: 삭제할 데이터 먼저 확인
SELECT emp_id, name, department 
FROM employees 
WHERE department = '임시팀';

-- 2단계: 백업 테이블 생성 (선택사항)
CREATE TABLE employees_backup AS 
SELECT * FROM employees WHERE department = '임시팀';

-- 3단계: 실제 삭제 실행
DELETE FROM employees 
WHERE department = '임시팀';

-- 4단계: 결과 확인
SELECT COUNT(*) FROM employees WHERE department = '임시팀';
```

---

## 🔐 STEP 5: 제약조건 완전 활용 (45분)

### 5.1 기본 제약조건 실습

#### 🔑 제약조건이 포함된 테이블 생성
```sql
-- 고객 테이블 생성 (모든 제약조건 포함)
CREATE TABLE customers (
    -- 기본키 (PRIMARY KEY)
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    
    -- 필수 입력 (NOT NULL)
    customer_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,  -- 유일값 (UNIQUE)
    
    -- 선택 입력
    phone VARCHAR(20),
    age TINYINT CHECK (age >= 18 AND age <= 100),  -- 체크 제약 (CHECK)
    gender CHAR(1) DEFAULT 'M' CHECK (gender IN ('M', 'F')),  -- 기본값 (DEFAULT)
    
    -- 날짜 관련
    birth_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 주문 테이블 생성 (외래키 포함)
CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    order_date DATE DEFAULT CURDATE(),
    total_amount DECIMAL(10,2) CHECK (total_amount >= 0),
    status VARCHAR(20) DEFAULT 'pending' CHECK (status IN ('pending', 'confirmed', 'shipped', 'delivered', 'cancelled')),
    
    -- 외래키 제약조건 (FOREIGN KEY)
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        ON DELETE CASCADE  -- 고객 삭제 시 주문도 삭제
        ON UPDATE CASCADE  -- 고객 ID 변경 시 주문도 함께 변경
);
```

### 5.2 제약조건 테스트

#### ✅ 성공 케이스
```sql
-- 정상 데이터 입력
INSERT INTO customers (customer_name, email, phone, age, gender, birth_date)
VALUES 
    ('김고객', 'kim.customer@email.com', '010-1111-2222', 25, 'M', '1999-01-15'),
    ('이고객', 'lee.customer@email.com', '010-3333-4444', 30, 'F', '1994-05-20');

-- 주문 데이터 입력
INSERT INTO orders (customer_id, total_amount, status)
VALUES 
    (1, 50000, 'confirmed'),
    (2, 75000, 'pending');
```

#### ❌ 실패 케이스 (제약조건 위반)
```sql
-- 1. NOT NULL 위반
-- INSERT INTO customers (email, phone) VALUES ('test@email.com', '010-0000-0000');

-- 2. UNIQUE 위반 (동일한 이메일)
-- INSERT INTO customers (customer_name, email) VALUES ('중복고객', 'kim.customer@email.com');

-- 3. CHECK 제약조건 위반 (나이)
-- INSERT INTO customers (customer_name, email, age) VALUES ('어린고객', 'young@email.com', 15);

-- 4. CHECK 제약조건 위반 (성별)
-- INSERT INTO customers (customer_name, email, gender) VALUES ('성별오류', 'gender@email.com', 'X');

-- 5. 외래키 위반 (존재하지 않는 고객)
-- INSERT INTO orders (customer_id, total_amount) VALUES (999, 10000);
```

### 5.3 제약조건 관리

#### 🔧 제약조건 확인 및 수정
```sql
-- 테이블 제약조건 확인
SHOW CREATE TABLE customers;
SHOW CREATE TABLE orders;

-- 제약조건 정보 조회
SELECT 
    CONSTRAINT_NAME,
    CONSTRAINT_TYPE,
    TABLE_NAME,
    COLUMN_NAME
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE 
WHERE TABLE_SCHEMA = 'my_first_db';

-- 제약조건 추가 (기존 테이블에)
ALTER TABLE customers 
ADD CONSTRAINT chk_phone 
CHECK (phone REGEXP '^010-[0-9]{4}-[0-9]{4}$');

-- 제약조건 삭제
ALTER TABLE customers 
DROP CONSTRAINT chk_phone;
```

---

## 🎯 STEP 6: 서브쿼리 기초 (45분)

### 6.1 단일 값 서브쿼리

#### 📊 기본 서브쿼리
```sql
-- 평균 급여보다 높은 급여를 받는 직원
SELECT name, salary, department
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- 가장 높은 급여를 받는 직원
SELECT name, salary, department
FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);

-- 특정 부서의 직원들
SELECT name, salary
FROM employees
WHERE department = (SELECT dept_name FROM departments WHERE dept_id = 1);
```

### 6.2 다중 값 서브쿼리

#### 📋 IN, ANY, ALL 활용
```sql
-- IN: 여러 부서 중 하나
SELECT name, department, salary
FROM employees
WHERE department IN (
    SELECT dept_name 
    FROM departments 
    WHERE budget > 30000000
);

-- ANY: 어떤 관리자보다 급여가 높은 직원
SELECT name, salary
FROM employees
WHERE salary > ANY (
    SELECT salary 
    FROM employees 
    WHERE position LIKE '%Manager%'
);

-- ALL: 모든 디자이너보다 급여가 높은 직원
SELECT name, salary, department
FROM employees
WHERE salary > ALL (
    SELECT salary 
    FROM employees 
    WHERE department = '디자인팀'
);
```

### 6.3 상관 서브쿼리

#### 🔄 외부 쿼리와 연관된 서브쿼리
```sql
-- 각 부서에서 평균 급여보다 높은 급여를 받는 직원
SELECT name, department, salary
FROM employees e1
WHERE salary > (
    SELECT AVG(salary)
    FROM employees e2
    WHERE e2.department = e1.department
);

-- 각 부서에서 가장 높은 급여를 받는 직원
SELECT name, department, salary
FROM employees e1
WHERE salary = (
    SELECT MAX(salary)
    FROM employees e2
    WHERE e2.department = e1.department
);
```

---

## 💼 STEP 7: 실무 시나리오 해결 (60분)

### 시나리오 1: 인사 평가 시스템

#### 📊 문제: 각 부서별 성과 분석
```sql
-- 부서별 직원 현황 및 급여 통계
SELECT 
    department,
    COUNT(*) AS total_employees,
    AVG(salary) AS avg_salary,
    MAX(salary) AS max_salary,
    MIN(salary) AS min_salary,
    STDDEV(salary) AS salary_stddev,
    -- 급여 등급별 분포
    SUM(CASE WHEN salary >= 5000000 THEN 1 ELSE 0 END) AS high_salary_count,
    SUM(CASE WHEN salary BETWEEN 4000000 AND 4999999 THEN 1 ELSE 0 END) AS mid_salary_count,
    SUM(CASE WHEN salary < 4000000 THEN 1 ELSE 0 END) AS low_salary_count
FROM employees
WHERE department IS NOT NULL
GROUP BY department
ORDER BY avg_salary DESC;
```

#### 🎯 해결: 승진 대상자 선정
```sql
-- 승진 대상자 선정 기준
-- 1. 근무 기간 6개월 이상
-- 2. 해당 부서 평균 급여보다 높은 성과
-- 3. 현재 급여가 상위 30% 이내
SELECT 
    e.name,
    e.department,
    e.salary,
    e.hire_date,
    DATEDIFF(NOW(), e.hire_date) AS days_worked,
    -- 부서 내 급여 순위
    RANK() OVER (PARTITION BY e.department ORDER BY e.salary DESC) AS dept_salary_rank,
    -- 전체 급여 순위
    RANK() OVER (ORDER BY e.salary DESC) AS overall_salary_rank
FROM employees e
WHERE e.department IS NOT NULL
  AND DATEDIFF(NOW(), e.hire_date) >= 180  -- 6개월 이상
  AND e.salary > (
      SELECT AVG(salary) 
      FROM employees e2 
      WHERE e2.department = e.department
  )
ORDER BY e.department, e.salary DESC;
```

### 시나리오 2: 프로젝트 관리 시스템

#### 📋 문제: 프로젝트 진행 현황 분석
```sql
-- 프로젝트 현황 대시보드
SELECT 
    project_name,
    status,
    start_date,
    end_date,
    budget,
    DATEDIFF(end_date, start_date) AS total_duration,
    DATEDIFF(NOW(), start_date) AS elapsed_days,
    DATEDIFF(end_date, NOW()) AS remaining_days,
    -- 진행률 계산
    CASE 
        WHEN NOW() < start_date THEN 0
        WHEN NOW() > end_date THEN 100
        ELSE ROUND((DATEDIFF(NOW(), start_date) / DATEDIFF(end_date, start_date)) * 100, 1)
    END AS progress_percentage,
    -- 상태별 색상 코딩
    CASE 
        WHEN status = 'Planning' THEN '🔵 계획'
        WHEN status = 'In Progress' THEN '🟡 진행중'
        WHEN status = 'Completed' THEN '🟢 완료'
        ELSE '🔴 기타'
    END AS status_display
FROM projects
ORDER BY start_date;
```

### 시나리오 3: 고객 관리 시스템

#### 👥 문제: 고객 세분화 및 분석
```sql
-- 고객 등급 분류 및 주문 패턴 분석
SELECT 
    c.customer_name,
    c.age,
    c.gender,
    COUNT(o.order_id) AS total_orders,
    COALESCE(SUM(o.total_amount), 0) AS total_spent,
    COALESCE(AVG(o.total_amount), 0) AS avg_order_amount,
    MAX(o.order_date) AS last_order_date,
    DATEDIFF(NOW(), MAX(o.order_date)) AS days_since_last_order,
    -- 고객 등급 분류
    CASE 
        WHEN COUNT(o.order_id) = 0 THEN '비활성'
        WHEN COUNT(o.order_id) >= 5 AND SUM(o.total_amount) >= 200000 THEN 'VIP'
        WHEN COUNT(o.order_id) >= 3 OR SUM(o.total_amount) >= 100000 THEN '우수'
        ELSE '일반'
    END AS customer_grade
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name, c.age, c.gender
ORDER BY total_spent DESC;
```

---

## 📊 STEP 8: 성능 최적화 기초 (30분)

### 8.1 쿼리 실행 계획 확인

#### 🔍 EXPLAIN 사용법
```sql
-- 실행 계획 확인
EXPLAIN SELECT * FROM employees WHERE department = '개발팀';

-- 상세 실행 계획
EXPLAIN FORMAT=JSON SELECT * FROM employees WHERE salary > 5000000;

-- 실제 실행 통계
EXPLAIN ANALYZE SELECT e.name, d.dept_name 
FROM employees e 
JOIN departments d ON e.department = d.dept_name;
```

### 8.2 인덱스 기초

#### 📈 인덱스 생성 및 활용
```sql
-- 자주 검색되는 컬럼에 인덱스 생성
CREATE INDEX idx_employees_department ON employees(department);
CREATE INDEX idx_employees_salary ON employees(salary);
CREATE INDEX idx_employees_hire_date ON employees(hire_date);

-- 복합 인덱스
CREATE INDEX idx_employees_dept_salary ON employees(department, salary);

-- 인덱스 확인
SHOW INDEX FROM employees;

-- 인덱스 사용 전후 성능 비교
EXPLAIN SELECT * FROM employees WHERE department = '개발팀';
```

---

## 🎯 STEP 9: 오늘의 종합 실습 (45분)

### 💪 종합 문제 1: 직원 성과 분석
```sql
-- 문제: 다음 조건을 만족하는 쿼리를 작성하세요
-- 1. 각 부서별로 직원 수, 평균 급여, 최고 급여를 구하기
-- 2. 평균 급여가 450만원 이상인 부서만 표시
-- 3. 평균 급여 높은 순으로 정렬

SELECT 
    department,
    COUNT(*) AS employee_count,
    ROUND(AVG(salary), 0) AS avg_salary,
    MAX(salary) AS max_salary,
    MIN(salary) AS min_salary
FROM employees
WHERE department IS NOT NULL
GROUP BY department
HAVING AVG(salary) >= 4500000
ORDER BY avg_salary DESC;
```

### 💪 종합 문제 2: 고객 주문 패턴 분석
```sql
-- 문제: 다음 정보를 포함한 고객 주문 리포트 작성
-- 1. 고객명, 총 주문 수, 총 주문 금액
-- 2. 첫 주문일과 마지막 주문일
-- 3. 평균 주문 간격 (일)
-- 4. 고객 등급 (VIP/일반) 분류

SELECT 
    c.customer_name,
    COUNT(o.order_id) AS total_orders,
    COALESCE(SUM(o.total_amount), 0) AS total_amount,
    MIN(o.order_date) AS first_order_date,
    MAX(o.order_date) AS last_order_date,
    CASE 
        WHEN COUNT(o.order_id) > 1 
        THEN ROUND(DATEDIFF(MAX(o.order_date), MIN(o.order_date)) / (COUNT(o.order_id) - 1), 1)
        ELSE NULL 
    END AS avg_days_between_orders,
    CASE 
        WHEN COUNT(o.order_id) >= 3 AND SUM(o.total_amount) >= 150000 THEN 'VIP'
        ELSE '일반'
    END AS customer_grade
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
ORDER BY total_amount DESC;
```

---

## 📚 오늘의 핵심 정리

### ✅ 완료 체크리스트
- [ ] 복잡한 WHERE 조건 10가지 실습 완료
- [ ] 문자열 함수 활용 완료
- [ ] 날짜 함수 활용 완료
- [ ] 안전한 UPDATE/DELETE 실습 완료
- [ ] 모든 제약조건 적용 완료
- [ ] 서브쿼리 기본 패턴 실습 완료
- [ ] 실무 시나리오 3개 해결 완료

### 🎯 핵심 문법 정리

#### 필수 암기 함수
```sql
-- 문자열 함수
LENGTH(), SUBSTRING(), CONCAT(), REPLACE(), TRIM(), UPPER(), LOWER()

-- 날짜 함수
NOW(), CURDATE(), DATE_ADD(), DATE_SUB(), DATEDIFF(), DATE_FORMAT()

-- 조건 함수
CASE WHEN, IF(), IFNULL(), COALESCE()

-- 집계 함수
COUNT(), SUM(), AVG(), MAX(), MIN(), GROUP_CONCAT()
```

### 💡 실무 팁
1. **WHERE 절 없는 UPDATE/DELETE 절대 금지**
2. **복잡한 쿼리는 단계별로 작성 후 조합**
3. **제약조건으로 데이터 품질 보장**
4. **인덱스로 성능 향상**
5. **EXPLAIN으로 실행 계획 확인 습관화**

---

## 🚀 내일 학습 예고: Day 3

### 📅 Day 3 학습 내용 (0520)
- **JOIN 마스터**: INNER, LEFT, RIGHT, FULL OUTER JOIN
- **UNION 활용**: 집합 연산
- **GROUP BY 심화**: HAVING, ROLLUP
- **윈도우 함수**: RANK, ROW_NUMBER, LEAD, LAG

### 🎯 준비사항
- [ ] 오늘 학습한 내용 복습
- [ ] 서브쿼리 패턴 3가지 암기
- [ ] 제약조건 있는 테이블 유지

---

💪 **Day 2 완주하셨습니다! 내일은 본격적인 JOIN의 세계로 떠나요!** 🚀 