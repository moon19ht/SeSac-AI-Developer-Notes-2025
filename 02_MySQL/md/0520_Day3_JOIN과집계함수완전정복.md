# 🔗 Day 3: JOIN과 집계함수 완전 정복

##### 📅 학습 기간: 2025.05.20 (1일 집중)
##### 🎯 학습 목표: 모든 JOIN 유형 + 고급 집계 + 윈도우 함수 마스터
##### 📝 Writer : Moon19ht

---

## 📋 Day 3 학습 체크리스트

- [x] 5가지 JOIN 유형 모두 실습
- [x] 복잡한 다중 테이블 JOIN 구현
- [x] UNION과 UNION ALL 차이점 이해
- [x] GROUP BY + HAVING + ROLLUP 활용
- [x] 윈도우 함수 5개 이상 실습
- [x] 실무 복합 쿼리 10개 작성
- [x] 성능 최적화 JOIN 기법 적용

---

## 🏗️ STEP 1: JOIN 실습용 데이터 준비 (20분)

### 1.1 확장된 테이블 구조 생성

#### 👥 직원-부서-프로젝트 관계 설정
```sql
-- 기존 employees 테이블에 부서 ID 추가
ALTER TABLE employees ADD COLUMN dept_id INT;

-- 부서-직원 관계 설정을 위한 업데이트
UPDATE employees SET dept_id = 1 WHERE department = '개발팀';
UPDATE employees SET dept_id = 2 WHERE department = '마케팅팀';
UPDATE employees SET dept_id = 3 WHERE department = '디자인팀';
UPDATE employees SET dept_id = 4 WHERE department = '영업팀';
UPDATE employees SET dept_id = 5 WHERE department = '인사팀';

-- 외래키 제약조건 추가
ALTER TABLE employees 
ADD CONSTRAINT fk_emp_dept 
FOREIGN KEY (dept_id) REFERENCES departments(dept_id);
```

#### 📋 프로젝트-직원 매핑 테이블 생성
```sql
-- 프로젝트 참여자 테이블 (다대다 관계)
CREATE TABLE project_assignments (
    assignment_id INT PRIMARY KEY AUTO_INCREMENT,
    project_id INT NOT NULL,
    emp_id INT NOT NULL,
    role VARCHAR(50),
    start_date DATE,
    end_date DATE,
    allocation_percent DECIMAL(5,2) DEFAULT 100.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (project_id) REFERENCES projects(project_id),
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id),
    UNIQUE KEY unique_project_employee (project_id, emp_id)
);

-- 샘플 프로젝트 할당 데이터
INSERT INTO project_assignments (project_id, emp_id, role, start_date, end_date, allocation_percent)
VALUES 
    (1, 1, 'Project Lead', '2024-01-01', '2024-06-30', 80.00),
    (1, 3, 'Frontend Developer', '2024-01-15', '2024-06-30', 100.00),
    (2, 1, 'Technical Advisor', '2024-02-01', '2024-08-31', 30.00),
    (2, 3, 'UI/UX Designer', '2024-02-01', '2024-08-31', 60.00),
    (3, 2, 'Marketing Lead', '2024-03-01', '2024-05-31', 100.00),
    (4, 1, 'Technical Consultant', '2024-04-01', '2024-12-31', 20.00);
```

#### 💰 급여 이력 테이블 생성
```sql
-- 급여 변경 이력 테이블
CREATE TABLE salary_history (
    history_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_id INT NOT NULL,
    old_salary DECIMAL(10,2),
    new_salary DECIMAL(10,2),
    change_date DATE,
    change_reason VARCHAR(100),
    approved_by VARCHAR(50),
    
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
);

-- 급여 이력 샘플 데이터
INSERT INTO salary_history (emp_id, old_salary, new_salary, change_date, change_reason, approved_by)
VALUES 
    (1, 5000000, 5500000, '2024-01-15', '성과 평가 반영', '인사팀'),
    (1, 5500000, 5800000, '2024-03-01', '프로젝트 성과 보너스', '인사팀'),
    (2, 4500000, 4800000, '2024-02-01', '정기 인상', '인사팀'),
    (3, 3500000, 3800000, '2024-02-15', '신입 수습 완료', '인사팀'),
    (4, 4000000, 4200000, '2024-03-01', '정기 인상', '인사팀');
```

---

## 🔗 STEP 2: JOIN 완전 정복 (90분)

### 2.1 INNER JOIN - 교집합

#### 🎯 기본 INNER JOIN
```sql
-- 1. 직원과 부서 정보 조회
SELECT 
    e.name,
    e.salary,
    d.dept_name,
    d.location
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id;

-- 2. 직원, 부서, 현재 프로젝트 정보
SELECT 
    e.name AS employee_name,
    d.dept_name,
    p.project_name,
    pa.role,
    pa.allocation_percent
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id
INNER JOIN project_assignments pa ON e.emp_id = pa.emp_id
INNER JOIN projects p ON pa.project_id = p.project_id
WHERE pa.end_date >= CURDATE();  -- 진행 중인 프로젝트만
```

#### 🔍 조건부 INNER JOIN
```sql
-- 특정 조건을 만족하는 INNER JOIN
SELECT 
    e.name,
    e.salary,
    d.dept_name,
    d.budget
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id
WHERE e.salary > 4500000  -- 고급여 직원만
  AND d.budget > 25000000;  -- 예산이 큰 부서만
```

### 2.2 LEFT JOIN - 왼쪽 우선

#### 📊 모든 직원 정보 (부서 정보 포함)
```sql
-- 1. 부서가 없는 직원도 포함
SELECT 
    e.name,
    e.salary,
    COALESCE(d.dept_name, '부서미배정') AS department,
    COALESCE(d.location, '위치미정') AS location
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id;

-- 2. 모든 직원의 프로젝트 참여 현황
SELECT 
    e.name,
    e.department,
    COUNT(pa.project_id) AS project_count,
    GROUP_CONCAT(p.project_name) AS projects,
    SUM(pa.allocation_percent) AS total_allocation
FROM employees e
LEFT JOIN project_assignments pa ON e.emp_id = pa.emp_id
LEFT JOIN projects p ON pa.project_id = p.project_id
GROUP BY e.emp_id, e.name, e.department;
```

#### 🔍 LEFT JOIN으로 없는 데이터 찾기
```sql
-- 프로젝트에 참여하지 않은 직원 찾기
SELECT 
    e.name,
    e.department,
    e.salary
FROM employees e
LEFT JOIN project_assignments pa ON e.emp_id = pa.emp_id
WHERE pa.emp_id IS NULL;

-- 직원이 없는 부서 찾기
SELECT 
    d.dept_name,
    d.location,
    d.budget
FROM departments d
LEFT JOIN employees e ON d.dept_id = e.dept_id
WHERE e.emp_id IS NULL;
```

### 2.3 RIGHT JOIN - 오른쪽 우선

#### 📋 모든 부서의 직원 현황
```sql
-- 직원이 없는 부서도 포함하여 부서별 현황
SELECT 
    d.dept_name,
    d.location,
    COUNT(e.emp_id) AS employee_count,
    AVG(e.salary) AS avg_salary,
    MAX(e.salary) AS max_salary
FROM employees e
RIGHT JOIN departments d ON e.dept_id = d.dept_id
GROUP BY d.dept_id, d.dept_name, d.location;

-- 모든 프로젝트의 참여자 현황
SELECT 
    p.project_name,
    p.status,
    p.budget,
    COUNT(pa.emp_id) AS participant_count,
    GROUP_CONCAT(CONCAT(e.name, '(', pa.role, ')')) AS participants
FROM project_assignments pa
RIGHT JOIN projects p ON pa.project_id = p.project_id
LEFT JOIN employees e ON pa.emp_id = e.emp_id
GROUP BY p.project_id, p.project_name, p.status, p.budget;
```

### 2.4 FULL OUTER JOIN - MySQL 구현

#### 🔄 UNION으로 FULL OUTER JOIN 구현
```sql
-- 모든 직원과 모든 부서 정보 (매칭되지 않는 것도 포함)
SELECT 
    e.name AS employee_name,
    e.salary,
    d.dept_name,
    d.location
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id

UNION

SELECT 
    e.name AS employee_name,
    e.salary,
    d.dept_name,
    d.location
FROM employees e
RIGHT JOIN departments d ON e.dept_id = d.dept_id
WHERE e.emp_id IS NULL;
```

### 2.5 CROSS JOIN - 카테시안 곱

#### ⚠️ CROSS JOIN 활용 (주의해서 사용)
```sql
-- 모든 직원과 모든 프로젝트의 조합 (시뮬레이션 목적)
SELECT 
    e.name AS employee_name,
    e.department,
    p.project_name,
    p.budget,
    ROUND(p.budget / (SELECT COUNT(*) FROM employees), 0) AS estimated_share
FROM employees e
CROSS JOIN projects p
WHERE e.department IN ('개발팀', '디자인팀')  -- 관련 부서만
  AND p.status = 'Planning'  -- 계획 단계 프로젝트만
LIMIT 20;  -- 결과 제한
```

### 2.6 SELF JOIN - 자기 자신과 조인

#### 👥 조직도 구현
```sql
-- 먼저 관리자 정보를 employees 테이블에 추가
ALTER TABLE employees ADD COLUMN manager_id INT;

-- 샘플 관리자 관계 설정
UPDATE employees SET manager_id = NULL WHERE name = '김철수';  -- 팀장
UPDATE employees SET manager_id = 1 WHERE name IN ('박민수', '이영희');
UPDATE employees SET manager_id = 2 WHERE name = '최지은';

-- 직원과 그들의 관리자 정보 조회
SELECT 
    e.name AS employee_name,
    e.department AS employee_dept,
    e.salary AS employee_salary,
    m.name AS manager_name,
    m.department AS manager_dept
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.emp_id
ORDER BY m.name, e.name;

-- 각 관리자별 팀원 수와 평균 급여
SELECT 
    m.name AS manager_name,
    m.department,
    COUNT(e.emp_id) AS team_size,
    AVG(e.salary) AS avg_team_salary,
    MAX(e.salary) AS max_team_salary
FROM employees e
INNER JOIN employees m ON e.manager_id = m.emp_id
GROUP BY m.emp_id, m.name, m.department;
```

---

## 🔄 STEP 3: UNION 마스터 (45분)

### 3.1 UNION vs UNION ALL

#### 🎯 기본 UNION (중복 제거)
```sql
-- 현재 직원과 이전 직원 정보 합치기 (예시를 위한 이전 직원 테이블 생성)
CREATE TABLE former_employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(30),
    last_salary DECIMAL(10,2),
    termination_date DATE,
    reason VARCHAR(100)
);

-- 샘플 이전 직원 데이터
INSERT INTO former_employees VALUES
(100, '김퇴사', '개발팀', 5200000, '2023-12-31', '이직'),
(101, '이전직', '마케팅팀', 4300000, '2024-01-15', '개인사정'),
(102, '박과거', '디자인팀', 3900000, '2024-02-28', '이직');

-- 현재 + 이전 직원 통합 명단 (UNION - 중복 제거)
SELECT name, department, salary AS current_salary, 'Current' AS status
FROM employees
WHERE department IS NOT NULL

UNION

SELECT name, department, last_salary AS current_salary, 'Former' AS status
FROM former_employees;
```

#### 🔄 UNION ALL (중복 포함)
```sql
-- 모든 급여 변동 이력 조회 (현재 + 과거)
SELECT 
    e.name,
    e.salary AS amount,
    '현재급여' AS salary_type,
    CURDATE() AS reference_date
FROM employees e
WHERE e.salary IS NOT NULL

UNION ALL

SELECT 
    e.name,
    sh.new_salary AS amount,
    CONCAT('변경급여_', sh.change_date) AS salary_type,
    sh.change_date AS reference_date
FROM salary_history sh
INNER JOIN employees e ON sh.emp_id = e.emp_id

ORDER BY name, reference_date;
```

### 3.2 복잡한 UNION 활용

#### 📊 종합 리포트 생성
```sql
-- 부서별 다양한 통계를 하나의 결과로 합치기
SELECT 
    dept_name AS category,
    'Active Employees' AS metric,
    COUNT(*) AS value,
    'count' AS unit
FROM departments d
INNER JOIN employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_id, d.dept_name

UNION ALL

SELECT 
    dept_name AS category,
    'Average Salary' AS metric,
    AVG(e.salary) AS value,
    'KRW' AS unit
FROM departments d
INNER JOIN employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_id, d.dept_name

UNION ALL

SELECT 
    dept_name AS category,
    'Budget Utilization' AS metric,
    (SUM(e.salary * 12) / d.budget * 100) AS value,
    'percent' AS unit
FROM departments d
INNER JOIN employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_id, d.dept_name, d.budget

ORDER BY category, metric;
```

---

## 📊 STEP 4: GROUP BY 심화 (60분)

### 4.1 다차원 그룹핑

#### 🎯 복합 GROUP BY
```sql
-- 부서별, 연도별 입사자 통계
SELECT 
    department,
    YEAR(hire_date) AS hire_year,
    COUNT(*) AS new_hires,
    AVG(salary) AS avg_starting_salary,
    MIN(hire_date) AS first_hire,
    MAX(hire_date) AS last_hire
FROM employees
WHERE hire_date IS NOT NULL
GROUP BY department, YEAR(hire_date)
ORDER BY department, hire_year;

-- 프로젝트별, 역할별 참여자 분석
SELECT 
    p.project_name,
    pa.role,
    COUNT(*) AS role_count,
    AVG(e.salary) AS avg_salary,
    AVG(pa.allocation_percent) AS avg_allocation,
    GROUP_CONCAT(e.name) AS team_members
FROM project_assignments pa
INNER JOIN projects p ON pa.project_id = p.project_id
INNER JOIN employees e ON pa.emp_id = e.emp_id
GROUP BY p.project_id, p.project_name, pa.role
ORDER BY p.project_name, pa.role;
```

### 4.2 HAVING으로 그룹 필터링

#### 🔍 조건부 그룹 분석
```sql
-- 평균 급여가 높은 부서만 (450만원 이상)
SELECT 
    department,
    COUNT(*) AS employee_count,
    AVG(salary) AS avg_salary,
    MAX(salary) AS max_salary,
    MIN(salary) AS min_salary,
    STDDEV(salary) AS salary_stddev
FROM employees
WHERE department IS NOT NULL
GROUP BY department
HAVING AVG(salary) >= 4500000
   AND COUNT(*) >= 2  -- 2명 이상인 부서만
ORDER BY avg_salary DESC;

-- 복수 프로젝트에 참여하는 직원 분석
SELECT 
    e.name,
    e.department,
    COUNT(pa.project_id) AS project_count,
    SUM(pa.allocation_percent) AS total_allocation,
    AVG(pa.allocation_percent) AS avg_allocation,
    GROUP_CONCAT(p.project_name) AS projects
FROM employees e
INNER JOIN project_assignments pa ON e.emp_id = pa.emp_id
INNER JOIN projects p ON pa.project_id = p.project_id
GROUP BY e.emp_id, e.name, e.department
HAVING COUNT(pa.project_id) > 1  -- 2개 이상 프로젝트 참여
   AND SUM(pa.allocation_percent) > 100  -- 과부하 상태
ORDER BY total_allocation DESC;
```

### 4.3 WITH ROLLUP - 소계와 총계

#### 📈 계층적 집계
```sql
-- 부서별, 전체 급여 통계 (소계 포함)
SELECT 
    COALESCE(department, '전체') AS department,
    COUNT(*) AS employee_count,
    SUM(salary) AS total_salary,
    AVG(salary) AS avg_salary,
    MAX(salary) AS max_salary
FROM employees
WHERE department IS NOT NULL AND salary IS NOT NULL
GROUP BY department WITH ROLLUP;

-- 연도별, 부서별 입사자 통계 (다단계 소계)
SELECT 
    COALESCE(YEAR(hire_date), '전체연도') AS hire_year,
    COALESCE(department, '전체부서') AS department,
    COUNT(*) AS hire_count,
    AVG(salary) AS avg_starting_salary
FROM employees
WHERE hire_date IS NOT NULL AND department IS NOT NULL
GROUP BY YEAR(hire_date), department WITH ROLLUP
ORDER BY hire_year, department;
```

---

## 📊 STEP 5: 윈도우 함수 마스터 (75분)

### 5.1 순위 함수

#### 🏆 ROW_NUMBER, RANK, DENSE_RANK
```sql
-- 부서별 급여 순위 (3가지 방식 비교)
SELECT 
    name,
    department,
    salary,
    -- 연속된 순위 (동점자도 다른 번호)
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS row_num,
    -- 일반적인 순위 (동점자는 같은 순위, 다음 순위는 건너뜀)
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rank_num,
    -- 조밀한 순위 (동점자는 같은 순위, 다음 순위는 연속)
    DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dense_rank_num,
    -- 전체 급여 순위
    RANK() OVER (ORDER BY salary DESC) AS overall_rank
FROM employees
WHERE department IS NOT NULL AND salary IS NOT NULL
ORDER BY department, salary DESC;
```

#### 🎯 상위 N개 추출
```sql
-- 각 부서별 상위 2명
SELECT *
FROM (
    SELECT 
        name,
        department,
        salary,
        hire_date,
        ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank
    FROM employees
    WHERE department IS NOT NULL
) ranked
WHERE dept_rank <= 2
ORDER BY department, dept_rank;
```

### 5.2 집계 윈도우 함수

#### 📊 누적합과 이동평균
```sql
-- 입사일 순서대로 누적 급여 합계
SELECT 
    name,
    department,
    hire_date,
    salary,
    -- 누적 합계
    SUM(salary) OVER (ORDER BY hire_date) AS cumulative_salary,
    -- 누적 평균
    AVG(salary) OVER (ORDER BY hire_date) AS cumulative_avg,
    -- 부서별 누적 합계
    SUM(salary) OVER (PARTITION BY department ORDER BY hire_date) AS dept_cumulative,
    -- 전체 대비 비율
    ROUND(salary / SUM(salary) OVER () * 100, 2) AS salary_percentage
FROM employees
WHERE hire_date IS NOT NULL AND salary IS NOT NULL
ORDER BY hire_date;
```

#### 🔄 이동 윈도우
```sql
-- 3명씩 이동평균 (급여 기준 정렬)
SELECT 
    name,
    department,
    salary,
    -- 현재 행 포함 앞뒤 1개씩 (총 3개) 평균
    AVG(salary) OVER (
        ORDER BY salary 
        ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
    ) AS moving_avg_3,
    -- 현재 행 포함 이전 2개 (총 3개) 평균
    AVG(salary) OVER (
        ORDER BY salary 
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS trailing_avg_3,
    -- 부서별 이동평균
    AVG(salary) OVER (
        PARTITION BY department 
        ORDER BY salary 
        ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
    ) AS dept_moving_avg
FROM employees
WHERE salary IS NOT NULL
ORDER BY salary;
```

### 5.3 LAG와 LEAD

#### ⏮️ 이전/다음 값 참조
```sql
-- 급여 변동 분석
SELECT 
    sh.emp_id,
    e.name,
    sh.change_date,
    sh.old_salary,
    sh.new_salary,
    (sh.new_salary - sh.old_salary) AS salary_increase,
    -- 이전 급여 변동일
    LAG(sh.change_date) OVER (PARTITION BY sh.emp_id ORDER BY sh.change_date) AS prev_change_date,
    -- 다음 급여 변동일
    LEAD(sh.change_date) OVER (PARTITION BY sh.emp_id ORDER BY sh.change_date) AS next_change_date,
    -- 이전 급여와 비교
    LAG(sh.new_salary) OVER (PARTITION BY sh.emp_id ORDER BY sh.change_date) AS prev_salary,
    -- 연속 인상 여부
    CASE 
        WHEN sh.new_salary > LAG(sh.new_salary) OVER (PARTITION BY sh.emp_id ORDER BY sh.change_date)
        THEN '인상'
        ELSE '동결/삭감'
    END AS change_type
FROM salary_history sh
INNER JOIN employees e ON sh.emp_id = e.emp_id
ORDER BY e.name, sh.change_date;
```

### 5.4 분할 함수 (NTILE)

#### 📊 데이터 분할
```sql
-- 급여 기준 4분위 분석
SELECT 
    name,
    department,
    salary,
    -- 전체 직원을 급여 기준 4그룹으로 분할
    NTILE(4) OVER (ORDER BY salary) AS salary_quartile,
    -- 부서 내에서 급여 기준 3그룹으로 분할
    NTILE(3) OVER (PARTITION BY department ORDER BY salary) AS dept_tercile,
    -- 분위수별 라벨
    CASE NTILE(4) OVER (ORDER BY salary)
        WHEN 1 THEN '하위 25%'
        WHEN 2 THEN '하위 50%'
        WHEN 3 THEN '상위 50%'
        WHEN 4 THEN '상위 25%'
    END AS quartile_label
FROM employees
WHERE salary IS NOT NULL
ORDER BY salary DESC;
```

---

## 💼 STEP 6: 실무 복합 쿼리 (90분)

### 시나리오 1: 인사 대시보드

#### 📊 종합 인사 현황 분석
```sql
-- 부서별 종합 현황 (인원, 급여, 프로젝트 참여 등)
SELECT 
    d.dept_name,
    d.location,
    d.budget,
    -- 인원 현황
    COUNT(DISTINCT e.emp_id) AS total_employees,
    COUNT(DISTINCT CASE WHEN e.hire_date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR) THEN e.emp_id END) AS new_hires_last_year,
    -- 급여 현황
    AVG(e.salary) AS avg_salary,
    MAX(e.salary) AS max_salary,
    MIN(e.salary) AS min_salary,
    -- 프로젝트 참여 현황
    COUNT(DISTINCT pa.project_id) AS active_projects,
    AVG(pa.allocation_percent) AS avg_allocation,
    -- 예산 대비 급여 비율
    ROUND(SUM(e.salary * 12) / d.budget * 100, 2) AS salary_budget_ratio,
    -- 부서 성과 지표
    CASE 
        WHEN AVG(e.salary) >= 5000000 THEN 'A등급'
        WHEN AVG(e.salary) >= 4000000 THEN 'B등급'
        ELSE 'C등급'
    END AS dept_grade
FROM departments d
LEFT JOIN employees e ON d.dept_id = e.dept_id
LEFT JOIN project_assignments pa ON e.emp_id = pa.emp_id 
    AND pa.end_date >= CURDATE()
GROUP BY d.dept_id, d.dept_name, d.location, d.budget
ORDER BY avg_salary DESC;
```

### 시나리오 2: 프로젝트 포트폴리오 분석

#### 📋 프로젝트별 리소스 분석
```sql
-- 프로젝트별 상세 현황 및 리소스 분석
WITH project_stats AS (
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
        GROUP_CONCAT(
            CONCAT(e.name, '(', pa.role, '-', pa.allocation_percent, '%)')
            ORDER BY pa.allocation_percent DESC
        ) AS team_composition
    FROM projects p
    LEFT JOIN project_assignments pa ON p.project_id = pa.project_id
    LEFT JOIN employees e ON pa.emp_id = e.emp_id
    GROUP BY p.project_id, p.project_name, p.status, p.budget, p.start_date, p.end_date
)
SELECT 
    ps.*,
    -- 프로젝트 기간 계산
    DATEDIFF(ps.end_date, ps.start_date) AS duration_days,
    -- 진행률 계산
    CASE 
        WHEN CURDATE() < ps.start_date THEN 0
        WHEN CURDATE() > ps.end_date THEN 100
        ELSE ROUND(DATEDIFF(CURDATE(), ps.start_date) / DATEDIFF(ps.end_date, ps.start_date) * 100, 1)
    END AS progress_percent,
    -- 예상 인건비
    ROUND(ps.avg_team_salary * ps.team_size * DATEDIFF(ps.end_date, ps.start_date) / 365, 0) AS estimated_labor_cost,
    -- 예산 대비 인건비 비율
    ROUND(ps.avg_team_salary * ps.team_size * DATEDIFF(ps.end_date, ps.start_date) / 365 / ps.budget * 100, 2) AS labor_budget_ratio,
    -- 리소스 효율성 등급
    CASE 
        WHEN ps.total_allocation <= 100 THEN '적정'
        WHEN ps.total_allocation <= 150 THEN '보통'
        ELSE '과부하'
    END AS resource_efficiency
FROM project_stats ps
ORDER BY ps.budget DESC, ps.start_date;
```

### 시나리오 3: 급여 밴드 분석

#### 💰 급여 구조 및 형평성 분석
```sql
-- 직급별, 부서별 급여 형평성 분석
WITH salary_analysis AS (
    SELECT 
        e.name,
        e.department,
        e.position,
        e.salary,
        e.hire_date,
        DATEDIFF(CURDATE(), e.hire_date) / 365 AS years_of_service,
        -- 부서 내 급여 순위
        RANK() OVER (PARTITION BY e.department ORDER BY e.salary DESC) AS dept_salary_rank,
        -- 직급별 급여 순위
        RANK() OVER (PARTITION BY e.position ORDER BY e.salary DESC) AS position_salary_rank,
        -- 급여 분위수
        NTILE(4) OVER (ORDER BY e.salary) AS salary_quartile,
        -- 부서 평균 대비 비율
        ROUND(e.salary / AVG(e.salary) OVER (PARTITION BY e.department) * 100, 1) AS dept_avg_ratio,
        -- 전체 평균 대비 비율
        ROUND(e.salary / AVG(e.salary) OVER () * 100, 1) AS overall_avg_ratio
    FROM employees e
    WHERE e.salary IS NOT NULL
),
quartile_ranges AS (
    SELECT 
        salary_quartile,
        MIN(salary) AS min_salary,
        MAX(salary) AS max_salary,
        AVG(salary) AS avg_salary,
        COUNT(*) AS employee_count
    FROM salary_analysis
    GROUP BY salary_quartile
)
SELECT 
    sa.name,
    sa.department,
    sa.position,
    sa.salary,
    sa.years_of_service,
    sa.salary_quartile,
    qr.min_salary AS quartile_min,
    qr.max_salary AS quartile_max,
    sa.dept_avg_ratio,
    sa.overall_avg_ratio,
    -- 급여 적정성 평가
    CASE 
        WHEN sa.years_of_service >= 3 AND sa.salary_quartile <= 2 THEN '재검토 필요'
        WHEN sa.years_of_service < 1 AND sa.salary_quartile >= 3 THEN '높음'
        ELSE '적정'
    END AS salary_assessment,
    -- 조정 권고사항
    CASE 
        WHEN sa.dept_avg_ratio < 80 AND sa.years_of_service >= 2 THEN '인상 검토'
        WHEN sa.dept_avg_ratio > 130 AND sa.years_of_service < 1 THEN '수준 검토'
        ELSE '유지'
    END AS adjustment_recommendation
FROM salary_analysis sa
INNER JOIN quartile_ranges qr ON sa.salary_quartile = qr.salary_quartile
ORDER BY sa.department, sa.salary DESC;
```

---

## 🚀 STEP 7: 성능 최적화 JOIN (45분)

### 7.1 인덱스 활용

#### 📈 JOIN 성능 최적화를 위한 인덱스
```sql
-- JOIN에 최적화된 인덱스 생성
CREATE INDEX idx_emp_dept_id ON employees(dept_id);
CREATE INDEX idx_emp_manager_id ON employees(manager_id);
CREATE INDEX idx_project_assignments_emp_id ON project_assignments(emp_id);
CREATE INDEX idx_project_assignments_project_id ON project_assignments(project_id);
CREATE INDEX idx_salary_history_emp_id ON salary_history(emp_id);

-- 복합 인덱스 (자주 함께 사용되는 컬럼들)
CREATE INDEX idx_emp_dept_salary ON employees(dept_id, salary);
CREATE INDEX idx_project_emp_dates ON project_assignments(emp_id, start_date, end_date);

-- 인덱스 사용 현황 확인
EXPLAIN SELECT 
    e.name, d.dept_name, p.project_name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id
INNER JOIN project_assignments pa ON e.emp_id = pa.emp_id
INNER JOIN projects p ON pa.project_id = p.project_id;
```

### 7.2 효율적인 JOIN 순서

#### 🎯 JOIN 순서 최적화
```sql
-- 비효율적인 JOIN (큰 테이블부터)
-- EXPLAIN SELECT ...
-- FROM large_table lt
-- INNER JOIN small_table st ON ...

-- 효율적인 JOIN (작은 테이블, 선택적 조건부터)
EXPLAIN SELECT 
    e.name,
    d.dept_name,
    p.project_name,
    pa.role
FROM departments d                -- 1. 가장 작은 테이블
INNER JOIN employees e ON d.dept_id = e.dept_id
    AND e.salary > 5000000        -- 2. 선택적 조건 추가
INNER JOIN project_assignments pa ON e.emp_id = pa.emp_id
    AND pa.end_date >= CURDATE()  -- 3. 또 다른 선택적 조건
INNER JOIN projects p ON pa.project_id = p.project_id
    AND p.status = 'In Progress'; -- 4. 최종 필터링
```

### 7.3 서브쿼리 vs JOIN 성능 비교

#### ⚡ 성능 비교 실습
```sql
-- 서브쿼리 방식 (일반적으로 느림)
EXPLAIN SELECT e.name, e.salary
FROM employees e
WHERE e.dept_id IN (
    SELECT d.dept_id 
    FROM departments d 
    WHERE d.budget > 30000000
);

-- JOIN 방식 (일반적으로 빠름)
EXPLAIN SELECT DISTINCT e.name, e.salary
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id
WHERE d.budget > 30000000;

-- EXISTS 방식 (중복 제거 불필요시 가장 효율적)
EXPLAIN SELECT e.name, e.salary
FROM employees e
WHERE EXISTS (
    SELECT 1 
    FROM departments d 
    WHERE d.dept_id = e.dept_id 
      AND d.budget > 30000000
);
```

---

## 🎯 STEP 8: 종합 실습 문제 (60분)

### 💪 고급 문제 1: 종합 성과 대시보드
```sql
-- 문제: 다음 정보를 포함한 종합 대시보드 쿼리 작성
-- 1. 부서별 인원, 평균급여, 프로젝트 수
-- 2. 각 부서의 급여 상위자와 하위자
-- 3. 프로젝트 참여율과 업무 과부하 현황
-- 4. 부서별 성과 등급 (A/B/C)

WITH dept_summary AS (
    SELECT 
        d.dept_name,
        COUNT(DISTINCT e.emp_id) AS employee_count,
        AVG(e.salary) AS avg_salary,
        COUNT(DISTINCT pa.project_id) AS project_count,
        AVG(pa.allocation_percent) AS avg_allocation
    FROM departments d
    LEFT JOIN employees e ON d.dept_id = e.dept_id
    LEFT JOIN project_assignments pa ON e.emp_id = pa.emp_id
    GROUP BY d.dept_id, d.dept_name
),
dept_salary_ranks AS (
    SELECT 
        e.department,
        MAX(CASE WHEN rn = 1 THEN e.name END) AS highest_paid,
        MAX(CASE WHEN rn = 1 THEN e.salary END) AS highest_salary,
        MAX(CASE WHEN rn_desc = 1 THEN e.name END) AS lowest_paid,
        MAX(CASE WHEN rn_desc = 1 THEN e.salary END) AS lowest_salary
    FROM (
        SELECT 
            e.*,
            ROW_NUMBER() OVER (PARTITION BY e.department ORDER BY e.salary DESC) AS rn,
            ROW_NUMBER() OVER (PARTITION BY e.department ORDER BY e.salary ASC) AS rn_desc
        FROM employees e
        WHERE e.salary IS NOT NULL
    ) e
    WHERE rn = 1 OR rn_desc = 1
    GROUP BY e.department
)
SELECT 
    ds.dept_name,
    ds.employee_count,
    ROUND(ds.avg_salary, 0) AS avg_salary,
    ds.project_count,
    ROUND(ds.avg_allocation, 1) AS avg_allocation,
    dsr.highest_paid,
    dsr.highest_salary,
    dsr.lowest_paid,
    dsr.lowest_salary,
    -- 업무 과부하 현황
    CASE 
        WHEN ds.avg_allocation > 100 THEN '과부하'
        WHEN ds.avg_allocation > 80 THEN '적정'
        ELSE '여유'
    END AS workload_status,
    -- 부서 성과 등급
    CASE 
        WHEN ds.avg_salary >= 5000000 AND ds.project_count >= 2 THEN 'A등급'
        WHEN ds.avg_salary >= 4000000 AND ds.project_count >= 1 THEN 'B등급'
        ELSE 'C등급'
    END AS performance_grade
FROM dept_summary ds
LEFT JOIN dept_salary_ranks dsr ON ds.dept_name = dsr.department
ORDER BY ds.avg_salary DESC;
```

### 💪 고급 문제 2: 프로젝트 리소스 최적화
```sql
-- 문제: 프로젝트별 리소스 배치 최적화 분석
-- 1. 각 프로젝트의 현재 팀 구성과 역할별 비중
-- 2. 프로젝트 기간 대비 리소스 투입량
-- 3. 유사한 프로젝트와의 비교 분석
-- 4. 리소스 재배치 권고사항

WITH project_resource_analysis AS (
    SELECT 
        p.project_name,
        p.status,
        p.budget,
        DATEDIFF(p.end_date, p.start_date) AS duration_days,
        COUNT(pa.emp_id) AS team_size,
        SUM(pa.allocation_percent) AS total_allocation,
        AVG(e.salary) AS avg_team_cost,
        -- 역할별 분포
        SUM(CASE WHEN pa.role LIKE '%Lead%' OR pa.role LIKE '%Manager%' THEN 1 ELSE 0 END) AS leadership_count,
        SUM(CASE WHEN pa.role LIKE '%Developer%' THEN 1 ELSE 0 END) AS developer_count,
        SUM(CASE WHEN pa.role LIKE '%Designer%' THEN 1 ELSE 0 END) AS designer_count,
        -- 예상 총 비용
        SUM(e.salary * pa.allocation_percent / 100 * DATEDIFF(p.end_date, p.start_date) / 365) AS estimated_cost
    FROM projects p
    LEFT JOIN project_assignments pa ON p.project_id = pa.project_id
    LEFT JOIN employees e ON pa.emp_id = e.emp_id
    GROUP BY p.project_id, p.project_name, p.status, p.budget, p.start_date, p.end_date
)
SELECT 
    pra.project_name,
    pra.status,
    pra.budget,
    pra.duration_days,
    pra.team_size,
    pra.total_allocation,
    ROUND(pra.avg_team_cost, 0) AS avg_team_cost,
    ROUND(pra.estimated_cost, 0) AS estimated_cost,
    ROUND(pra.estimated_cost / pra.budget * 100, 2) AS cost_budget_ratio,
    -- 팀 구성 분석
    CONCAT(
        'Lead:', pra.leadership_count, ' ',
        'Dev:', pra.developer_count, ' ',
        'Design:', pra.designer_count
    ) AS team_composition,
    -- 리소스 효율성
    ROUND(pra.budget / pra.duration_days / pra.team_size, 0) AS daily_budget_per_person,
    -- 비교 분석 (같은 상태의 다른 프로젝트 평균과 비교)
    ROUND(pra.total_allocation / AVG(pra.total_allocation) OVER (PARTITION BY pra.status) * 100, 1) AS allocation_vs_similar,
    -- 권고사항
    CASE 
        WHEN pra.total_allocation > 150 THEN '리소스 과부하 - 인원 추가 필요'
        WHEN pra.total_allocation < 50 THEN '리소스 부족 - 투입 확대 필요'
        WHEN pra.estimated_cost > pra.budget * 1.2 THEN '예산 초과 위험 - 비용 절감 필요'
        WHEN pra.leadership_count = 0 AND pra.team_size > 3 THEN '리더십 부재 - 책임자 배정 필요'
        ELSE '적정 수준'
    END AS recommendation
FROM project_resource_analysis pra
ORDER BY pra.cost_budget_ratio DESC;
```

---

## 📚 오늘의 핵심 정리

### ✅ 완료 체크리스트
- [ ] 5가지 JOIN 유형 실습 완료
- [ ] 복잡한 다중 테이블 JOIN 구현 완료
- [ ] UNION과 UNION ALL 활용 완료
- [ ] GROUP BY + HAVING + ROLLUP 마스터
- [ ] 윈도우 함수 5개 이상 실습 완료
- [ ] 실무 복합 쿼리 작성 완료
- [ ] 성능 최적화 JOIN 기법 적용 완료

### 🎯 핵심 문법 정리

#### JOIN 유형별 사용법
```sql
-- INNER JOIN: 양쪽 모두 있는 데이터만
INNER JOIN table2 ON table1.key = table2.key

-- LEFT JOIN: 왼쪽 테이블 모든 데이터 + 매칭되는 오른쪽 데이터
LEFT JOIN table2 ON table1.key = table2.key

-- RIGHT JOIN: 오른쪽 테이블 모든 데이터 + 매칭되는 왼쪽 데이터
RIGHT JOIN table2 ON table1.key = table2.key

-- SELF JOIN: 같은 테이블끼리 조인
FROM table1 t1 JOIN table1 t2 ON t1.manager_id = t2.emp_id
```

#### 윈도우 함수 패턴
```sql
-- 순위 함수
ROW_NUMBER() OVER (PARTITION BY column ORDER BY column)
RANK() OVER (PARTITION BY column ORDER BY column)
DENSE_RANK() OVER (PARTITION BY column ORDER BY column)

-- 집계 윈도우 함수
SUM(column) OVER (PARTITION BY column ORDER BY column)
AVG(column) OVER (ROWS BETWEEN n PRECEDING AND CURRENT ROW)

-- LAG/LEAD
LAG(column, 1) OVER (PARTITION BY column ORDER BY column)
LEAD(column, 1) OVER (PARTITION BY column ORDER BY column)
```

### 💡 실무 팁
1. **JOIN 순서**: 작은 테이블부터, 선택적 조건 먼저
2. **인덱스**: JOIN 컬럼에 반드시 인덱스 생성
3. **윈도우 함수**: 복잡한 분석 쿼리에 활용
4. **EXISTS vs IN**: 대량 데이터에서는 EXISTS가 더 효율적
5. **EXPLAIN**: 복잡한 JOIN은 반드시 실행계획 확인

---

## 🚀 내일 학습 예고: Day 4

### 📅 Day 4 학습 내용 (0521)
- **서브쿼리 심화**: 상관 서브쿼리, CTE(Common Table Expression)
- **CASE 문 활용**: 복잡한 조건 로직
- **저장 프로시저**: 재사용 가능한 SQL 코드
- **트리거**: 자동 실행 SQL

### 🎯 준비사항
- [ ] 오늘 학습한 JOIN 패턴 5개 복습
- [ ] 윈도우 함수 3개 암기
- [ ] 복합 쿼리 1개 직접 작성

---

💪 **Day 3 고생하셨습니다! JOIN과 윈도우 함수를 마스터하셨어요!** 🚀 