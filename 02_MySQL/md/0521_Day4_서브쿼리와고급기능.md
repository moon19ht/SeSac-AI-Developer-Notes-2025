# 🧠 Day 4: 서브쿼리와 고급기능 마스터

##### 📅 학습 기간: 2025.05.21 (1일 집중)
##### 🎯 학습 목표: 서브쿼리 심화 + CASE문 + 저장 프로시저 + 고급 함수
##### 📝 Writer : Moon19ht

---

## 📋 Day 4 학습 체크리스트

- [x] 상관 서브쿼리 5가지 패턴 실습
- [x] CTE(Common Table Expression) 활용
- [x] 복잡한 CASE문 3가지 작성
- [x] 사용자 정의 함수 생성
- [x] 저장 프로시저 3개 작성
- [x] 트리거 기본 개념 이해
- [x] 조건부 로직 실무 시나리오 5개 해결

---

## 🎯 STEP 1: 서브쿼리 심화 완전 정복 (75분)

### 1.1 상관 서브쿼리 고급 패턴

#### 🔄 EXISTS와 NOT EXISTS 활용
```sql
-- 1. 프로젝트에 참여한 경험이 있는 직원
SELECT 
    e.name,
    e.department,
    e.salary,
    e.hire_date
FROM employees e
WHERE EXISTS (
    SELECT 1 
    FROM project_assignments pa 
    WHERE pa.emp_id = e.emp_id
);

-- 2. 프로젝트에 한 번도 참여하지 않은 직원
SELECT 
    e.name,
    e.department,
    e.salary,
    DATEDIFF(CURDATE(), e.hire_date) AS days_since_hire
FROM employees e
WHERE NOT EXISTS (
    SELECT 1 
    FROM project_assignments pa 
    WHERE pa.emp_id = e.emp_id
)
ORDER BY days_since_hire DESC;

-- 3. 최근 1년간 급여 인상이 없는 직원
SELECT 
    e.name,
    e.department,
    e.salary,
    COALESCE(
        (SELECT MAX(sh.change_date) 
         FROM salary_history sh 
         WHERE sh.emp_id = e.emp_id), 
        e.hire_date
    ) AS last_salary_change
FROM employees e
WHERE NOT EXISTS (
    SELECT 1 
    FROM salary_history sh 
    WHERE sh.emp_id = e.emp_id
      AND sh.change_date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
);
```

#### 📊 비교 분석용 상관 서브쿼리
```sql
-- 1. 부서 평균보다 급여가 높은 직원들
SELECT 
    e.name,
    e.department,
    e.salary,
    (SELECT AVG(e2.salary) 
     FROM employees e2 
     WHERE e2.department = e.department) AS dept_avg_salary,
    ROUND(e.salary / (SELECT AVG(e2.salary) 
                      FROM employees e2 
                      WHERE e2.department = e.department) * 100, 1) AS salary_vs_avg_percent
FROM employees e
WHERE e.salary > (
    SELECT AVG(e2.salary) 
    FROM employees e2 
    WHERE e2.department = e.department
);

-- 2. 각 부서에서 가장 오래 근무한 직원
SELECT 
    e.name,
    e.department,
    e.hire_date,
    DATEDIFF(CURDATE(), e.hire_date) AS days_worked
FROM employees e
WHERE e.hire_date = (
    SELECT MIN(e2.hire_date)
    FROM employees e2
    WHERE e2.department = e.department
      AND e2.hire_date IS NOT NULL
);

-- 3. 프로젝트별 최고 급여 직원
SELECT 
    p.project_name,
    e.name AS highest_paid_member,
    e.salary,
    pa.role,
    pa.allocation_percent
FROM projects p
INNER JOIN project_assignments pa ON p.project_id = pa.project_id
INNER JOIN employees e ON pa.emp_id = e.emp_id
WHERE e.salary = (
    SELECT MAX(e2.salary)
    FROM employees e2
    INNER JOIN project_assignments pa2 ON e2.emp_id = pa2.emp_id
    WHERE pa2.project_id = p.project_id
);
```

### 1.2 다중 레벨 서브쿼리

#### 🏗️ 중첩된 서브쿼리
```sql
-- 1. 가장 많은 프로젝트에 참여한 직원이 속한 부서의 모든 직원
SELECT 
    e.name,
    e.department,
    e.salary,
    (SELECT COUNT(*) 
     FROM project_assignments pa 
     WHERE pa.emp_id = e.emp_id) AS project_count
FROM employees e
WHERE e.department = (
    SELECT e2.department
    FROM employees e2
    WHERE e2.emp_id = (
        SELECT pa.emp_id
        FROM project_assignments pa
        GROUP BY pa.emp_id
        ORDER BY COUNT(*) DESC
        LIMIT 1
    )
);

-- 2. 평균 급여가 가장 높은 부서에서 급여가 가장 낮은 직원
SELECT 
    e.name,
    e.department,
    e.salary,
    (SELECT AVG(e3.salary) 
     FROM employees e3 
     WHERE e3.department = e.department) AS dept_avg
FROM employees e
WHERE e.department = (
    SELECT e2.department
    FROM employees e2
    WHERE e2.department IS NOT NULL
    GROUP BY e2.department
    ORDER BY AVG(e2.salary) DESC
    LIMIT 1
)
AND e.salary = (
    SELECT MIN(e4.salary)
    FROM employees e4
    WHERE e4.department = e.department
      AND e4.salary IS NOT NULL
);
```

### 1.3 CTE (Common Table Expression)

#### 🔗 WITH 절 활용
```sql
-- 1. 기본 CTE 사용
WITH department_stats AS (
    SELECT 
        department,
        COUNT(*) AS emp_count,
        AVG(salary) AS avg_salary,
        MAX(salary) AS max_salary,
        MIN(salary) AS min_salary
    FROM employees
    WHERE department IS NOT NULL
    GROUP BY department
),
salary_ranks AS (
    SELECT 
        name,
        department,
        salary,
        RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rank_in_dept
    FROM employees
    WHERE department IS NOT NULL
)
SELECT 
    ds.department,
    ds.emp_count,
    ds.avg_salary,
    sr.name AS top_earner,
    sr.salary AS top_salary,
    ROUND(sr.salary / ds.avg_salary * 100, 1) AS top_vs_avg_percent
FROM department_stats ds
INNER JOIN salary_ranks sr ON ds.department = sr.department
WHERE sr.rank_in_dept = 1
ORDER BY ds.avg_salary DESC;

-- 2. 재귀 CTE (조직도 구현)
WITH RECURSIVE org_hierarchy AS (
    -- 최상위 관리자 (manager_id가 NULL인 직원)
    SELECT 
        emp_id,
        name,
        department,
        manager_id,
        salary,
        1 AS level,
        CAST(name AS CHAR(1000)) AS hierarchy_path
    FROM employees
    WHERE manager_id IS NULL
    
    UNION ALL
    
    -- 하위 직원들
    SELECT 
        e.emp_id,
        e.name,
        e.department,
        e.manager_id,
        e.salary,
        oh.level + 1,
        CONCAT(oh.hierarchy_path, ' > ', e.name) AS hierarchy_path
    FROM employees e
    INNER JOIN org_hierarchy oh ON e.manager_id = oh.emp_id
    WHERE oh.level < 5  -- 무한 루프 방지
)
SELECT 
    CONCAT(REPEAT('  ', level - 1), name) AS org_chart,
    department,
    salary,
    level,
    hierarchy_path
FROM org_hierarchy
ORDER BY hierarchy_path;
```

---

## 🔀 STEP 2: CASE문 마스터 (60분)

### 2.1 단순 CASE vs 검색 CASE

#### 🎯 단순 CASE (값 비교)
```sql
-- 부서 코드를 부서명으로 변환
SELECT 
    name,
    department,
    salary,
    CASE department
        WHEN '개발팀' THEN 'Development'
        WHEN '마케팅팀' THEN 'Marketing'
        WHEN '디자인팀' THEN 'Design'
        WHEN '영업팀' THEN 'Sales'
        WHEN '인사팀' THEN 'HR'
        ELSE 'Other'
    END AS dept_english,
    -- 급여 통화 표시
    CASE 
        WHEN salary >= 10000000 THEN CONCAT(FORMAT(salary/10000, 0), '만원')
        WHEN salary >= 1000000 THEN CONCAT(FORMAT(salary/10000, 1), '만원')
        ELSE CONCAT(FORMAT(salary, 0), '원')
    END AS salary_display
FROM employees;
```

#### 🔍 검색 CASE (조건 비교)
```sql
-- 복합 등급 시스템
SELECT 
    name,
    department,
    salary,
    hire_date,
    DATEDIFF(CURDATE(), hire_date) / 365 AS years_of_service,
    -- 복합 등급 계산
    CASE 
        WHEN salary >= 6000000 AND DATEDIFF(CURDATE(), hire_date) >= 1095 THEN 'S급 (시니어)'
        WHEN salary >= 5000000 AND DATEDIFF(CURDATE(), hire_date) >= 730 THEN 'A급 (고급)'
        WHEN salary >= 4000000 AND DATEDIFF(CURDATE(), hire_date) >= 365 THEN 'B급 (중급)'
        WHEN salary >= 3000000 THEN 'C급 (초급)'
        ELSE 'D급 (수습)'
    END AS employee_grade,
    -- 승진 가능성
    CASE 
        WHEN salary >= 5000000 THEN '승진 대상'
        WHEN salary >= 4000000 AND DATEDIFF(CURDATE(), hire_date) >= 365 THEN '승진 검토'
        WHEN DATEDIFF(CURDATE(), hire_date) >= 180 THEN '평가 대기'
        ELSE '수습 중'
    END AS promotion_status
FROM employees
WHERE salary IS NOT NULL;
```

### 2.2 중첩 CASE와 복합 조건

#### 🏗️ 복잡한 비즈니스 로직 구현
```sql
-- 프로젝트 참여자 성과 평가 시스템
SELECT 
    e.name,
    e.department,
    p.project_name,
    pa.role,
    pa.allocation_percent,
    p.status AS project_status,
    DATEDIFF(CURDATE(), pa.start_date) AS days_on_project,
    -- 복합 성과 등급
    CASE 
        WHEN p.status = 'Completed' THEN
            CASE 
                WHEN pa.allocation_percent >= 80 AND pa.role LIKE '%Lead%' THEN 'A+ (프로젝트 리더 완료)'
                WHEN pa.allocation_percent >= 50 THEN 'A (핵심 기여자)'
                ELSE 'B+ (기여자)'
            END
        WHEN p.status = 'In Progress' THEN
            CASE 
                WHEN pa.allocation_percent >= 100 THEN 'B (과부하 주의)'
                WHEN pa.allocation_percent >= 70 THEN 'B+ (핵심 진행)'
                WHEN pa.allocation_percent >= 30 THEN 'C+ (부분 참여)'
                ELSE 'C (최소 참여)'
            END
        WHEN p.status = 'Planning' THEN 'D (계획 단계)'
        ELSE 'E (미분류)'
    END AS performance_grade,
    -- 보상 권고
    CASE 
        WHEN p.status = 'Completed' AND pa.allocation_percent >= 80 THEN
            ROUND(e.salary * 0.1, 0)  -- 10% 보너스
        WHEN p.status = 'Completed' AND pa.allocation_percent >= 50 THEN
            ROUND(e.salary * 0.05, 0)  -- 5% 보너스
        WHEN p.status = 'In Progress' AND pa.allocation_percent >= 100 THEN
            ROUND(e.salary * 0.02, 0)  -- 2% 과부하 수당
        ELSE 0
    END AS recommended_bonus
FROM employees e
INNER JOIN project_assignments pa ON e.emp_id = pa.emp_id
INNER JOIN projects p ON pa.project_id = p.project_id;
```

### 2.3 CASE문을 활용한 피벗 테이블

#### 📊 동적 피벗 구현
```sql
-- 부서별 월별 입사자 수 피벗 테이블
SELECT 
    department,
    SUM(CASE WHEN MONTH(hire_date) = 1 THEN 1 ELSE 0 END) AS Jan,
    SUM(CASE WHEN MONTH(hire_date) = 2 THEN 1 ELSE 0 END) AS Feb,
    SUM(CASE WHEN MONTH(hire_date) = 3 THEN 1 ELSE 0 END) AS Mar,
    SUM(CASE WHEN MONTH(hire_date) = 4 THEN 1 ELSE 0 END) AS Apr,
    SUM(CASE WHEN MONTH(hire_date) = 5 THEN 1 ELSE 0 END) AS May,
    SUM(CASE WHEN MONTH(hire_date) = 6 THEN 1 ELSE 0 END) AS Jun,
    SUM(CASE WHEN MONTH(hire_date) = 7 THEN 1 ELSE 0 END) AS Jul,
    SUM(CASE WHEN MONTH(hire_date) = 8 THEN 1 ELSE 0 END) AS Aug,
    SUM(CASE WHEN MONTH(hire_date) = 9 THEN 1 ELSE 0 END) AS Sep,
    SUM(CASE WHEN MONTH(hire_date) = 10 THEN 1 ELSE 0 END) AS Oct,
    SUM(CASE WHEN MONTH(hire_date) = 11 THEN 1 ELSE 0 END) AS Nov,
    SUM(CASE WHEN MONTH(hire_date) = 12 THEN 1 ELSE 0 END) AS Dec,
    COUNT(*) AS Total
FROM employees
WHERE hire_date IS NOT NULL AND department IS NOT NULL
GROUP BY department
ORDER BY Total DESC;

-- 급여 구간별 부서 분포
SELECT 
    CASE 
        WHEN salary < 3500000 THEN '3500만원 미만'
        WHEN salary < 4000000 THEN '3500-4000만원'
        WHEN salary < 4500000 THEN '4000-4500만원'
        WHEN salary < 5000000 THEN '4500-5000만원'
        WHEN salary < 5500000 THEN '5000-5500만원'
        ELSE '5500만원 이상'
    END AS salary_range,
    SUM(CASE WHEN department = '개발팀' THEN 1 ELSE 0 END) AS 개발팀,
    SUM(CASE WHEN department = '마케팅팀' THEN 1 ELSE 0 END) AS 마케팅팀,
    SUM(CASE WHEN department = '디자인팀' THEN 1 ELSE 0 END) AS 디자인팀,
    SUM(CASE WHEN department = '영업팀' THEN 1 ELSE 0 END) AS 영업팀,
    SUM(CASE WHEN department = '인사팀' THEN 1 ELSE 0 END) AS 인사팀,
    COUNT(*) AS Total
FROM employees
WHERE salary IS NOT NULL AND department IS NOT NULL
GROUP BY 
    CASE 
        WHEN salary < 3500000 THEN '3500만원 미만'
        WHEN salary < 4000000 THEN '3500-4000만원'
        WHEN salary < 4500000 THEN '4000-4500만원'
        WHEN salary < 5000000 THEN '4500-5000만원'
        WHEN salary < 5500000 THEN '5000-5500만원'
        ELSE '5500만원 이상'
    END
ORDER BY MIN(salary);
```

---

## 🔧 STEP 3: 사용자 정의 함수 (45분)

### 3.1 함수 생성 기초

#### 📝 간단한 함수 생성
```sql
-- 구분자 변경 (함수 생성 시 필요)
DELIMITER //

-- 1. 급여 등급 계산 함수
CREATE FUNCTION GetSalaryGrade(emp_salary DECIMAL(10,2))
RETURNS VARCHAR(10)
READS SQL DATA
DETERMINISTIC
BEGIN
    DECLARE grade VARCHAR(10);
    
    IF emp_salary >= 6000000 THEN
        SET grade = 'S급';
    ELSEIF emp_salary >= 5000000 THEN
        SET grade = 'A급';
    ELSEIF emp_salary >= 4000000 THEN
        SET grade = 'B급';
    ELSEIF emp_salary >= 3000000 THEN
        SET grade = 'C급';
    ELSE
        SET grade = 'D급';
    END IF;
    
    RETURN grade;
END //

-- 2. 근무 년수 계산 함수
CREATE FUNCTION GetYearsOfService(hire_date DATE)
RETURNS DECIMAL(4,2)
READS SQL DATA
DETERMINISTIC
BEGIN
    DECLARE years_worked DECIMAL(4,2);
    
    IF hire_date IS NULL THEN
        RETURN 0;
    END IF;
    
    SET years_worked = DATEDIFF(CURDATE(), hire_date) / 365.25;
    
    RETURN ROUND(years_worked, 2);
END //

-- 3. 한국어 숫자 포맷 함수
CREATE FUNCTION FormatKoreanNumber(amount DECIMAL(15,2))
RETURNS VARCHAR(50)
READS SQL DATA
DETERMINISTIC
BEGIN
    DECLARE formatted VARCHAR(50);
    
    IF amount >= 100000000 THEN
        SET formatted = CONCAT(FORMAT(amount/100000000, 1), '억원');
    ELSEIF amount >= 10000 THEN
        SET formatted = CONCAT(FORMAT(amount/10000, 0), '만원');
    ELSE
        SET formatted = CONCAT(FORMAT(amount, 0), '원');
    END IF;
    
    RETURN formatted;
END //

DELIMITER ;

-- 함수 사용 예시
SELECT 
    name,
    salary,
    GetSalaryGrade(salary) AS salary_grade,
    GetYearsOfService(hire_date) AS years_of_service,
    FormatKoreanNumber(salary) AS salary_formatted
FROM employees
WHERE salary IS NOT NULL;
```

### 3.2 복잡한 비즈니스 로직 함수

#### 🧮 종합 평가 함수
```sql
DELIMITER //

-- 직원 종합 점수 계산 함수
CREATE FUNCTION CalculateEmployeeScore(
    emp_id INT,
    current_salary DECIMAL(10,2),
    hire_date DATE,
    dept_name VARCHAR(50)
)
RETURNS INT
READS SQL DATA
DETERMINISTIC
BEGIN
    DECLARE total_score INT DEFAULT 0;
    DECLARE salary_score INT DEFAULT 0;
    DECLARE tenure_score INT DEFAULT 0;
    DECLARE project_score INT DEFAULT 0;
    DECLARE dept_avg_salary DECIMAL(10,2);
    DECLARE project_count INT;
    DECLARE years_worked DECIMAL(4,2);
    
    -- 근무 년수 계산
    SET years_worked = DATEDIFF(CURDATE(), hire_date) / 365.25;
    
    -- 부서 평균 급여 조회
    SELECT AVG(salary) INTO dept_avg_salary
    FROM employees 
    WHERE department = dept_name AND salary IS NOT NULL;
    
    -- 프로젝트 참여 수 조회
    SELECT COUNT(*) INTO project_count
    FROM project_assignments 
    WHERE project_assignments.emp_id = emp_id;
    
    -- 급여 점수 (40점 만점)
    IF current_salary >= dept_avg_salary * 1.3 THEN
        SET salary_score = 40;
    ELSEIF current_salary >= dept_avg_salary * 1.1 THEN
        SET salary_score = 30;
    ELSEIF current_salary >= dept_avg_salary * 0.9 THEN
        SET salary_score = 20;
    ELSE
        SET salary_score = 10;
    END IF;
    
    -- 근속 점수 (30점 만점)
    IF years_worked >= 5 THEN
        SET tenure_score = 30;
    ELSEIF years_worked >= 3 THEN
        SET tenure_score = 25;
    ELSEIF years_worked >= 1 THEN
        SET tenure_score = 15;
    ELSE
        SET tenure_score = 5;
    END IF;
    
    -- 프로젝트 참여 점수 (30점 만점)
    IF project_count >= 3 THEN
        SET project_score = 30;
    ELSEIF project_count >= 2 THEN
        SET project_score = 20;
    ELSEIF project_count >= 1 THEN
        SET project_score = 10;
    ELSE
        SET project_score = 0;
    END IF;
    
    SET total_score = salary_score + tenure_score + project_score;
    
    RETURN total_score;
END //

DELIMITER ;

-- 함수 활용 예시
SELECT 
    e.name,
    e.department,
    e.salary,
    GetYearsOfService(e.hire_date) AS years_worked,
    (SELECT COUNT(*) FROM project_assignments pa WHERE pa.emp_id = e.emp_id) AS project_count,
    CalculateEmployeeScore(e.emp_id, e.salary, e.hire_date, e.department) AS total_score,
    CASE 
        WHEN CalculateEmployeeScore(e.emp_id, e.salary, e.hire_date, e.department) >= 80 THEN 'S등급'
        WHEN CalculateEmployeeScore(e.emp_id, e.salary, e.hire_date, e.department) >= 60 THEN 'A등급'
        WHEN CalculateEmployeeScore(e.emp_id, e.salary, e.hire_date, e.department) >= 40 THEN 'B등급'
        ELSE 'C등급'
    END AS performance_grade
FROM employees e
WHERE e.salary IS NOT NULL
ORDER BY total_score DESC;
```

---

## 📦 STEP 4: 저장 프로시저 (75분)

### 4.1 기본 저장 프로시저

#### 🔧 매개변수가 있는 프로시저
```sql
DELIMITER //

-- 1. 부서별 급여 현황 조회 프로시저
CREATE PROCEDURE GetDepartmentSalaryReport(
    IN dept_name VARCHAR(50)
)
BEGIN
    SELECT 
        e.name,
        e.salary,
        e.hire_date,
        GetYearsOfService(e.hire_date) AS years_worked,
        RANK() OVER (ORDER BY e.salary DESC) AS salary_rank
    FROM employees e
    WHERE e.department = dept_name
      AND e.salary IS NOT NULL
    ORDER BY e.salary DESC;
    
    -- 부서 요약 정보도 함께 출력
    SELECT 
        COUNT(*) AS total_employees,
        AVG(salary) AS avg_salary,
        MAX(salary) AS max_salary,
        MIN(salary) AS min_salary,
        SUM(salary) AS total_salary_cost
    FROM employees
    WHERE department = dept_name
      AND salary IS NOT NULL;
END //

-- 2. 급여 인상 프로시저 (안전장치 포함)
CREATE PROCEDURE AdjustSalary(
    IN emp_id INT,
    IN increase_percent DECIMAL(5,2),
    IN reason VARCHAR(100),
    OUT result_message VARCHAR(200)
)
BEGIN
    DECLARE current_salary DECIMAL(10,2);
    DECLARE new_salary DECIMAL(10,2);
    DECLARE emp_name VARCHAR(50);
    DECLARE emp_dept VARCHAR(50);
    
    -- 예외 처리 선언
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
    BEGIN
        SET result_message = 'ERROR: 급여 조정 중 오류가 발생했습니다.';
        ROLLBACK;
    END;
    
    -- 트랜잭션 시작
    START TRANSACTION;
    
    -- 현재 급여 정보 조회
    SELECT name, department, salary 
    INTO emp_name, emp_dept, current_salary
    FROM employees 
    WHERE employees.emp_id = emp_id;
    
    -- 직원 존재 여부 확인
    IF current_salary IS NULL THEN
        SET result_message = 'ERROR: 해당 직원을 찾을 수 없습니다.';
        ROLLBACK;
    ELSE
        -- 인상률 검증 (최대 50% 까지만 허용)
        IF increase_percent > 50 OR increase_percent < -20 THEN
            SET result_message = 'ERROR: 인상률은 -20% ~ 50% 범위 내에서만 가능합니다.';
            ROLLBACK;
        ELSE
            -- 새로운 급여 계산
            SET new_salary = current_salary * (1 + increase_percent / 100);
            
            -- 급여 업데이트
            UPDATE employees 
            SET salary = new_salary, updated_at = NOW()
            WHERE employees.emp_id = emp_id;
            
            -- 급여 이력 기록
            INSERT INTO salary_history (emp_id, old_salary, new_salary, change_date, change_reason, approved_by)
            VALUES (emp_id, current_salary, new_salary, CURDATE(), reason, USER());
            
            -- 성공 메시지
            SET result_message = CONCAT(
                'SUCCESS: ', emp_name, '(', emp_dept, ')의 급여가 ',
                FormatKoreanNumber(current_salary), '에서 ',
                FormatKoreanNumber(new_salary), '로 조정되었습니다. (', increase_percent, '%)'
            );
            
            COMMIT;
        END IF;
    END IF;
END //

DELIMITER ;

-- 프로시저 사용 예시
CALL GetDepartmentSalaryReport('개발팀');

-- 급여 조정 예시
SET @result = '';
CALL AdjustSalary(1, 5.5, '2024년 성과 평가 반영', @result);
SELECT @result AS adjustment_result;
```

### 4.2 복잡한 비즈니스 로직 프로시저

#### 📊 성과 평가 및 보상 프로시저
```sql
DELIMITER //

-- 연간 성과 평가 및 보상 계산 프로시저
CREATE PROCEDURE ProcessAnnualPerformanceReview(
    IN review_year INT,
    IN budget_limit DECIMAL(15,2)
)
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE emp_id INT;
    DECLARE emp_name VARCHAR(50);
    DECLARE current_salary DECIMAL(10,2);
    DECLARE performance_score INT;
    DECLARE recommended_increase DECIMAL(5,2);
    DECLARE bonus_amount DECIMAL(10,2);
    DECLARE total_cost DECIMAL(15,2) DEFAULT 0;
    
    -- 커서 선언
    DECLARE emp_cursor CURSOR FOR
        SELECT e.emp_id, e.name, e.salary,
               CalculateEmployeeScore(e.emp_id, e.salary, e.hire_date, e.department) AS score
        FROM employees e
        WHERE e.salary IS NOT NULL
        ORDER BY CalculateEmployeeScore(e.emp_id, e.salary, e.hire_date, e.department) DESC;
    
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    
    -- 결과 테이블 임시 생성
    DROP TEMPORARY TABLE IF EXISTS performance_review_results;
    CREATE TEMPORARY TABLE performance_review_results (
        emp_id INT,
        emp_name VARCHAR(50),
        current_salary DECIMAL(10,2),
        performance_score INT,
        performance_grade VARCHAR(10),
        salary_increase_percent DECIMAL(5,2),
        new_salary DECIMAL(10,2),
        bonus_amount DECIMAL(10,2),
        total_compensation_increase DECIMAL(10,2)
    );
    
    -- 커서 오픈
    OPEN emp_cursor;
    
    read_loop: LOOP
        FETCH emp_cursor INTO emp_id, emp_name, current_salary, performance_score;
        
        IF done THEN
            LEAVE read_loop;
        END IF;
        
        -- 성과 점수에 따른 인상률 및 보너스 계산
        CASE 
            WHEN performance_score >= 80 THEN
                SET recommended_increase = 8.0;
                SET bonus_amount = current_salary * 0.15;
            WHEN performance_score >= 60 THEN
                SET recommended_increase = 5.0;
                SET bonus_amount = current_salary * 0.10;
            WHEN performance_score >= 40 THEN
                SET recommended_increase = 3.0;
                SET bonus_amount = current_salary * 0.05;
            ELSE
                SET recommended_increase = 0.0;
                SET bonus_amount = 0;
        END CASE;
        
        -- 예산 한도 확인
        IF total_cost + (current_salary * recommended_increase / 100) + bonus_amount <= budget_limit THEN
            SET total_cost = total_cost + (current_salary * recommended_increase / 100) + bonus_amount;
        ELSE
            -- 예산 초과 시 조정
            SET recommended_increase = recommended_increase * 0.5;
            SET bonus_amount = bonus_amount * 0.5;
        END IF;
        
        -- 결과 삽입
        INSERT INTO performance_review_results VALUES (
            emp_id,
            emp_name,
            current_salary,
            performance_score,
            CASE 
                WHEN performance_score >= 80 THEN 'S등급'
                WHEN performance_score >= 60 THEN 'A등급'
                WHEN performance_score >= 40 THEN 'B등급'
                ELSE 'C등급'
            END,
            recommended_increase,
            current_salary * (1 + recommended_increase / 100),
            bonus_amount,
            (current_salary * recommended_increase / 100) + bonus_amount
        );
        
    END LOOP;
    
    CLOSE emp_cursor;
    
    -- 결과 출력
    SELECT * FROM performance_review_results
    ORDER BY performance_score DESC;
    
    -- 요약 정보
    SELECT 
        COUNT(*) AS total_employees_reviewed,
        SUM(total_compensation_increase) AS total_budget_used,
        budget_limit - SUM(total_compensation_increase) AS remaining_budget,
        AVG(salary_increase_percent) AS avg_increase_percent
    FROM performance_review_results;
    
END //

DELIMITER ;

-- 프로시저 실행
CALL ProcessAnnualPerformanceReview(2024, 50000000);
```

### 4.3 프로젝트 관리 프로시저

#### 📋 프로젝트 배정 자동화
```sql
DELIMITER //

-- 프로젝트 팀 구성 최적화 프로시저
CREATE PROCEDURE OptimizeProjectTeam(
    IN project_id INT,
    IN required_roles JSON,
    OUT team_composition TEXT
)
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE role_name VARCHAR(50);
    DECLARE role_count INT;
    DECLARE selected_employees TEXT DEFAULT '';
    
    -- JSON 파싱을 위한 변수
    DECLARE role_index INT DEFAULT 0;
    DECLARE total_roles INT;
    
    -- 임시 결과 테이블
    DROP TEMPORARY TABLE IF EXISTS optimal_team;
    CREATE TEMPORARY TABLE optimal_team (
        emp_id INT,
        emp_name VARCHAR(50),
        department VARCHAR(50),
        role VARCHAR(50),
        salary DECIMAL(10,2),
        availability_score DECIMAL(5,2)
    );
    
    -- JSON에서 역할별 필요 인원 수 추출
    SET total_roles = JSON_LENGTH(required_roles);
    
    WHILE role_index < total_roles DO
        SET role_name = JSON_UNQUOTE(JSON_EXTRACT(required_roles, CONCAT('$[', role_index, '].role')));
        SET role_count = JSON_EXTRACT(required_roles, CONCAT('$[', role_index, '].count'));
        
        -- 각 역할에 적합한 직원 선발
        INSERT INTO optimal_team
        SELECT 
            e.emp_id,
            e.name,
            e.department,
            role_name,
            e.salary,
            -- 가용성 점수 계산 (현재 프로젝트 부하 고려)
            100 - COALESCE(
                (SELECT SUM(pa.allocation_percent) 
                 FROM project_assignments pa 
                 WHERE pa.emp_id = e.emp_id 
                   AND pa.end_date >= CURDATE()), 0
            ) AS availability_score
        FROM employees e
        WHERE e.department = CASE 
                WHEN role_name LIKE '%Developer%' THEN '개발팀'
                WHEN role_name LIKE '%Designer%' THEN '디자인팀'
                WHEN role_name LIKE '%Marketing%' THEN '마케팅팀'
                ELSE e.department
            END
            AND NOT EXISTS (
                SELECT 1 FROM project_assignments pa2
                WHERE pa2.emp_id = e.emp_id 
                  AND pa2.project_id = project_id
            )
        ORDER BY availability_score DESC, e.salary ASC
        LIMIT role_count;
        
        SET role_index = role_index + 1;
    END WHILE;
    
    -- 팀 구성 결과 생성
    SELECT GROUP_CONCAT(
        CONCAT(emp_name, '(', role, '-', department, ')')
        ORDER BY role, emp_name
        SEPARATOR ', '
    ) INTO team_composition
    FROM optimal_team;
    
    -- 상세 결과 출력
    SELECT 
        role,
        COUNT(*) AS assigned_count,
        GROUP_CONCAT(emp_name ORDER BY availability_score DESC) AS team_members,
        AVG(salary) AS avg_role_salary,
        AVG(availability_score) AS avg_availability
    FROM optimal_team
    GROUP BY role;
    
    -- 전체 팀 비용 계산
    SELECT 
        COUNT(*) AS total_team_size,
        SUM(salary) AS total_monthly_cost,
        AVG(availability_score) AS avg_team_availability
    FROM optimal_team;
    
END //

DELIMITER ;

-- 프로시저 사용 예시
SET @team_result = '';
SET @required_roles = '[
    {"role": "Lead Developer", "count": 1},
    {"role": "Frontend Developer", "count": 2},
    {"role": "UI Designer", "count": 1},
    {"role": "Marketing Specialist", "count": 1}
]';

CALL OptimizeProjectTeam(1, @required_roles, @team_result);
SELECT @team_result AS recommended_team;
```

---

## 🔔 STEP 5: 트리거 기초 (45분)

### 5.1 기본 트리거 생성

#### ⚡ 자동 로깅 트리거
```sql
-- 급여 변경 로그 테이블 생성
CREATE TABLE salary_change_log (
    log_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_id INT,
    old_salary DECIMAL(10,2),
    new_salary DECIMAL(10,2),
    change_amount DECIMAL(10,2),
    change_percent DECIMAL(5,2),
    changed_by VARCHAR(50),
    change_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DELIMITER //

-- 급여 변경 자동 로그 트리거
CREATE TRIGGER salary_change_audit
    AFTER UPDATE ON employees
    FOR EACH ROW
BEGIN
    IF OLD.salary != NEW.salary THEN
        INSERT INTO salary_change_log (
            emp_id, 
            old_salary, 
            new_salary, 
            change_amount,
            change_percent,
            changed_by
        ) VALUES (
            NEW.emp_id,
            OLD.salary,
            NEW.salary,
            NEW.salary - OLD.salary,
            ROUND((NEW.salary - OLD.salary) / OLD.salary * 100, 2),
            USER()
        );
    END IF;
END //

-- 직원 삭제 방지 트리거 (프로젝트 진행 중인 경우)
CREATE TRIGGER prevent_employee_deletion
    BEFORE DELETE ON employees
    FOR EACH ROW
BEGIN
    DECLARE project_count INT;
    
    SELECT COUNT(*) INTO project_count
    FROM project_assignments pa
    INNER JOIN projects p ON pa.project_id = p.project_id
    WHERE pa.emp_id = OLD.emp_id
      AND p.status = 'In Progress'
      AND pa.end_date >= CURDATE();
    
    IF project_count > 0 THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = '진행 중인 프로젝트가 있는 직원은 삭제할 수 없습니다.';
    END IF;
END //

DELIMITER ;

-- 트리거 테스트
UPDATE employees SET salary = salary * 1.1 WHERE emp_id = 1;
SELECT * FROM salary_change_log;
```

### 5.2 비즈니스 규칙 트리거

#### 🛡️ 데이터 무결성 보장 트리거
```sql
DELIMITER //

-- 프로젝트 할당 검증 트리거
CREATE TRIGGER validate_project_assignment
    BEFORE INSERT ON project_assignments
    FOR EACH ROW
BEGIN
    DECLARE emp_dept VARCHAR(50);
    DECLARE current_allocation DECIMAL(5,2);
    DECLARE project_status VARCHAR(20);
    
    -- 직원 부서 확인
    SELECT department INTO emp_dept
    FROM employees
    WHERE emp_id = NEW.emp_id;
    
    -- 현재 할당률 확인
    SELECT COALESCE(SUM(allocation_percent), 0) INTO current_allocation
    FROM project_assignments
    WHERE emp_id = NEW.emp_id
      AND end_date >= CURDATE();
    
    -- 프로젝트 상태 확인
    SELECT status INTO project_status
    FROM projects
    WHERE project_id = NEW.project_id;
    
    -- 검증 규칙들
    IF NEW.allocation_percent <= 0 OR NEW.allocation_percent > 100 THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = '할당률은 1-100% 범위 내에서 설정해야 합니다.';
    END IF;
    
    IF current_allocation + NEW.allocation_percent > 150 THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = '총 할당률이 150%를 초과할 수 없습니다.';
    END IF;
    
    IF project_status = 'Completed' THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = '완료된 프로젝트에는 새로운 인원을 할당할 수 없습니다.';
    END IF;
    
    -- 시작일이 종료일보다 늦으면 안됨
    IF NEW.start_date > NEW.end_date THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = '시작일이 종료일보다 늦을 수 없습니다.';
    END IF;
END //

-- 부서 예산 초과 방지 트리거
CREATE TRIGGER check_department_budget
    BEFORE UPDATE ON employees
    FOR EACH ROW
BEGIN
    DECLARE dept_budget DECIMAL(15,2);
    DECLARE current_total_salary DECIMAL(15,2);
    DECLARE salary_increase DECIMAL(10,2);
    
    IF OLD.salary != NEW.salary THEN
        -- 부서 예산 조회
        SELECT budget INTO dept_budget
        FROM departments d
        WHERE d.dept_name = NEW.department;
        
        -- 현재 부서 총 급여 (연봉 기준)
        SELECT SUM(salary * 12) INTO current_total_salary
        FROM employees
        WHERE department = NEW.department
          AND emp_id != NEW.emp_id;
        
        SET salary_increase = (NEW.salary - OLD.salary) * 12;
        
        -- 예산 초과 확인
        IF current_total_salary + (NEW.salary * 12) > dept_budget THEN
            SIGNAL SQLSTATE '45000' 
            SET MESSAGE_TEXT = CONCAT(
                '부서 예산을 초과합니다. 현재 사용: ',
                FORMAT(current_total_salary + (NEW.salary * 12), 0),
                ', 예산: ',
                FORMAT(dept_budget, 0)
            );
        END IF;
    END IF;
END //

DELIMITER ;
```

---

## 💼 STEP 6: 실무 시나리오 통합 (90분)

### 시나리오 1: 인사 관리 시스템 완성

#### 🏢 종합 인사 관리 쿼리
```sql
-- 인사 관리 대시보드 통합 뷰
WITH employee_analytics AS (
    SELECT 
        e.emp_id,
        e.name,
        e.department,
        e.salary,
        e.hire_date,
        GetYearsOfService(e.hire_date) AS years_worked,
        CalculateEmployeeScore(e.emp_id, e.salary, e.hire_date, e.department) AS performance_score,
        -- 현재 프로젝트 참여 현황
        (SELECT COUNT(*) FROM project_assignments pa WHERE pa.emp_id = e.emp_id) AS total_projects,
        (SELECT COUNT(*) FROM project_assignments pa 
         INNER JOIN projects p ON pa.project_id = p.project_id
         WHERE pa.emp_id = e.emp_id AND p.status = 'In Progress') AS active_projects,
        (SELECT COALESCE(SUM(pa.allocation_percent), 0) FROM project_assignments pa 
         INNER JOIN projects p ON pa.project_id = p.project_id
         WHERE pa.emp_id = e.emp_id AND pa.end_date >= CURDATE()) AS current_allocation,
        -- 급여 변동 이력
        (SELECT COUNT(*) FROM salary_history sh WHERE sh.emp_id = e.emp_id) AS salary_changes,
        (SELECT MAX(sh.change_date) FROM salary_history sh WHERE sh.emp_id = e.emp_id) AS last_salary_change
    FROM employees e
    WHERE e.salary IS NOT NULL
),
department_benchmarks AS (
    SELECT 
        department,
        AVG(salary) AS dept_avg_salary,
        AVG(performance_score) AS dept_avg_score,
        COUNT(*) AS dept_size
    FROM employee_analytics
    GROUP BY department
)
SELECT 
    ea.name,
    ea.department,
    ea.salary,
    FormatKoreanNumber(ea.salary) AS salary_formatted,
    ea.years_worked,
    ea.performance_score,
    GetSalaryGrade(ea.salary) AS salary_grade,
    -- 부서 내 상대적 위치
    RANK() OVER (PARTITION BY ea.department ORDER BY ea.salary DESC) AS dept_salary_rank,
    RANK() OVER (PARTITION BY ea.department ORDER BY ea.performance_score DESC) AS dept_score_rank,
    -- 성과 대비 급여 적정성
    CASE 
        WHEN ea.salary > db.dept_avg_salary * 1.2 AND ea.performance_score < db.dept_avg_score * 0.8 THEN '과다지급'
        WHEN ea.salary < db.dept_avg_salary * 0.8 AND ea.performance_score > db.dept_avg_score * 1.2 THEN '저평가'
        WHEN ea.salary >= db.dept_avg_salary * 1.1 AND ea.performance_score >= db.dept_avg_score * 1.1 THEN '우수보상'
        ELSE '적정'
    END AS compensation_assessment,
    -- 업무 부하 상태
    CASE 
        WHEN ea.current_allocation > 120 THEN '과부하'
        WHEN ea.current_allocation > 80 THEN '적정'
        WHEN ea.current_allocation > 0 THEN '여유'
        ELSE '미배정'
    END AS workload_status,
    -- 승진/조치 권고
    CASE 
        WHEN ea.performance_score >= 80 AND ea.years_worked >= 2 THEN '승진 검토'
        WHEN ea.performance_score < 40 AND ea.years_worked >= 1 THEN '개선 필요'
        WHEN ea.current_allocation = 0 AND ea.years_worked >= 0.5 THEN '프로젝트 배정 필요'
        WHEN ea.salary < db.dept_avg_salary * 0.9 AND ea.performance_score >= db.dept_avg_score THEN '급여 조정 검토'
        ELSE '현상 유지'
    END AS hr_recommendation
FROM employee_analytics ea
INNER JOIN department_benchmarks db ON ea.department = db.department
ORDER BY ea.department, ea.performance_score DESC;
```

### 시나리오 2: 프로젝트 포트폴리오 최적화

#### 📊 프로젝트 리소스 분석 및 재배치
```sql
-- 프로젝트 리소스 최적화 분석
WITH project_resource_summary AS (
    SELECT 
        p.project_id,
        p.project_name,
        p.status,
        p.budget,
        p.start_date,
        p.end_date,
        COUNT(pa.emp_id) AS team_size,
        SUM(pa.allocation_percent) AS total_allocation,
        AVG(e.salary) AS avg_team_salary,
        SUM(e.salary * pa.allocation_percent / 100) AS monthly_cost,
        -- 예상 총 비용
        SUM(e.salary * pa.allocation_percent / 100) * 
        GREATEST(1, DATEDIFF(GREATEST(p.end_date, CURDATE()), LEAST(p.start_date, CURDATE())) / 30) AS estimated_total_cost,
        -- 팀 구성 다양성
        COUNT(DISTINCT e.department) AS dept_diversity,
        GROUP_CONCAT(DISTINCT pa.role) AS roles_covered
    FROM projects p
    LEFT JOIN project_assignments pa ON p.project_id = pa.project_id
    LEFT JOIN employees e ON pa.emp_id = e.emp_id
    GROUP BY p.project_id, p.project_name, p.status, p.budget, p.start_date, p.end_date
),
employee_utilization AS (
    SELECT 
        e.emp_id,
        e.name,
        e.department,
        e.salary,
        COALESCE(SUM(pa.allocation_percent), 0) AS total_allocation,
        COUNT(pa.project_id) AS active_projects,
        GROUP_CONCAT(p.project_name) AS assigned_projects,
        -- 가용 역량
        100 - COALESCE(SUM(pa.allocation_percent), 0) AS available_capacity
    FROM employees e
    LEFT JOIN project_assignments pa ON e.emp_id = pa.emp_id 
        AND pa.end_date >= CURDATE()
    LEFT JOIN projects p ON pa.project_id = p.project_id 
        AND p.status IN ('Planning', 'In Progress')
    GROUP BY e.emp_id, e.name, e.department, e.salary
)
-- 프로젝트별 리소스 효율성 분석
SELECT 
    prs.project_name,
    prs.status,
    prs.team_size,
    prs.total_allocation,
    ROUND(prs.avg_team_salary, 0) AS avg_team_salary,
    ROUND(prs.monthly_cost, 0) AS monthly_cost,
    ROUND(prs.estimated_total_cost, 0) AS estimated_total_cost,
    ROUND(prs.estimated_total_cost / prs.budget * 100, 2) AS cost_budget_ratio,
    prs.dept_diversity,
    -- 리소스 효율성 지표
    ROUND(prs.budget / prs.team_size / DATEDIFF(prs.end_date, prs.start_date), 0) AS daily_budget_per_person,
    -- 권고사항
    CASE 
        WHEN prs.total_allocation > 200 THEN 'CRITICAL: 리소스 과부하 - 즉시 인력 충원 필요'
        WHEN prs.total_allocation < 100 AND prs.team_size > 1 THEN 'WARNING: 리소스 부족 - 추가 배정 검토'
        WHEN prs.estimated_total_cost > prs.budget * 1.3 THEN 'ALERT: 예산 초과 위험 - 비용 절감 방안 필요'
        WHEN prs.dept_diversity < 2 AND prs.team_size > 3 THEN 'NOTICE: 팀 다양성 부족 - 타 부서 인력 고려'
        ELSE 'OK: 적정 수준'
    END AS optimization_recommendation,
    -- 개선 가능 점수 (낮을수록 개선 필요)
    CASE 
        WHEN prs.total_allocation BETWEEN 80 AND 120 THEN 30
        WHEN prs.total_allocation BETWEEN 60 AND 140 THEN 20
        ELSE 10
    END +
    CASE 
        WHEN prs.estimated_total_cost <= prs.budget THEN 30
        WHEN prs.estimated_total_cost <= prs.budget * 1.1 THEN 20
        ELSE 10
    END +
    CASE 
        WHEN prs.dept_diversity >= 3 THEN 20
        WHEN prs.dept_diversity >= 2 THEN 15
        ELSE 10
    END AS efficiency_score
FROM project_resource_summary prs
WHERE prs.status IN ('Planning', 'In Progress')
ORDER BY efficiency_score ASC, cost_budget_ratio DESC;

-- 가용 인력 현황
SELECT 
    eu.department,
    COUNT(*) AS total_employees,
    COUNT(CASE WHEN eu.available_capacity > 50 THEN 1 END) AS highly_available,
    COUNT(CASE WHEN eu.available_capacity BETWEEN 20 AND 50 THEN 1 END) AS moderately_available,
    COUNT(CASE WHEN eu.available_capacity < 20 THEN 1 END) AS low_availability,
    ROUND(AVG(eu.available_capacity), 1) AS avg_available_capacity,
    GROUP_CONCAT(
        CASE WHEN eu.available_capacity > 50 
        THEN CONCAT(eu.name, '(', eu.available_capacity, '%)')
        END
    ) AS high_availability_members
FROM employee_utilization eu
GROUP BY eu.department
ORDER BY avg_available_capacity DESC;
```

---

## 📚 오늘의 핵심 정리

### ✅ 완료 체크리스트
- [ ] 상관 서브쿼리 5가지 패턴 실습 완료
- [ ] CTE 활용 완료
- [ ] 복잡한 CASE문 작성 완료
- [ ] 사용자 정의 함수 생성 완료
- [ ] 저장 프로시저 3개 작성 완료
- [ ] 트리거 기본 개념 이해 완료
- [ ] 실무 시나리오 해결 완료

### 🎯 핵심 문법 정리

#### 서브쿼리 패턴
```sql
-- 상관 서브쿼리
WHERE column > (SELECT AVG(column) FROM table WHERE condition = outer.condition)

-- EXISTS 패턴
WHERE EXISTS (SELECT 1 FROM table WHERE condition)

-- CTE 패턴
WITH cte_name AS (SELECT ...) SELECT ... FROM cte_name
```

#### CASE문 패턴
```sql
-- 단순 CASE
CASE column WHEN value1 THEN result1 WHEN value2 THEN result2 ELSE default END

-- 검색 CASE
CASE WHEN condition1 THEN result1 WHEN condition2 THEN result2 ELSE default END
```

#### 함수/프로시저 기본 구조
```sql
-- 함수
CREATE FUNCTION function_name(param TYPE) RETURNS TYPE
BEGIN
    DECLARE variable TYPE;
    -- 로직
    RETURN value;
END

-- 프로시저
CREATE PROCEDURE procedure_name(IN param TYPE, OUT result TYPE)
BEGIN
    -- 로직
END
```

### 💡 실무 팁

1. **서브쿼리 최적화**: EXISTS가 IN보다 대용량 데이터에서 더 효율적
2. **CTE 활용**: 복잡한 쿼리를 단계별로 분해하여 가독성 향상
3. **CASE문**: 피벗 테이블 생성이나 복잡한 분류 로직에 활용
4. **함수**: 자주 사용되는 계산 로직을 재사용 가능하게 모듈화
5. **프로시저**: 복잡한 비즈니스 로직을 데이터베이스 레벨에서 처리
6. **트리거**: 데이터 무결성 보장과 자동 로깅에 활용

### 🚨 주의사항
- 트리거는 성능에 영향을 줄 수 있으므로 신중하게 사용
- 복잡한 프로시저는 디버깅이 어려우므로 단위별로 테스트
- CTE는 MySQL 8.0 이상에서만 지원

---

## 🚀 내일 학습 예고: Day 5

### 📅 Day 5 학습 내용 (0522-0526)
- **트랜잭션과 동시성 제어**: ACID 원칙, 격리 수준
- **인덱스 최적화**: 복합 인덱스, 실행 계획 분석
- **성능 튜닝**: 쿼리 최적화, 파티셔닝
- **실무 프로젝트**: 종합 데이터베이스 시스템 구축

### 🎯 준비사항
- [ ] 오늘 만든 함수와 프로시저 복습
- [ ] 서브쿼리 vs JOIN 성능 차이 이해
- [ ] 복잡한 CASE문 1개 직접 작성

---

💪 **Day 4 고생하셨습니다! 고급 SQL 기능을 마스터하셨네요!** 🚀 