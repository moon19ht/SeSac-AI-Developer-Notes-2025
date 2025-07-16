# 데이터베이스 검색 및 최적화

데이터베이스의 검색 방법, 인덱스, 뷰, 제약조건, 윈도우 함수에 대한 학습 자료입니다.

---

## 목차

1. [데이터베이스 검색 방법](#1-데이터베이스-검색-방법)
2. [인덱스 (Index)](#2-인덱스-index)
3. [뷰 (View)](#3-뷰-view)
4. [제약조건 (Constraint)](#4-제약조건-constraint)
5. [윈도우 함수 (Window Function)](#5-윈도우-함수-window-function)

---

## 1. 데이터베이스 검색 방법

### 1.1 순차검색 (Sequential Search)

데이터베이스는 기본적으로 **순차검색**을 사용합니다.

```
순서: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10 → ... → 100만
```

**특징:**
- 처음부터 차례대로 읽어서 원하는 데이터가 나올 때까지 검색
- **시간 복잡도**: O(n) - 빅오 표기법
- 데이터가 n개 있을 때 운이 나쁘면 n번째에서 발견
- n이 커질수록 시간이 많이 걸림

**데이터베이스별 특징:**
- **Oracle**: 순차검색 + 병렬처리 (데이터를 읽는 프로세스가 여러 개 동시 동작)
- **MySQL**: 병렬처리 지원

---

### 1.2 색인순차검색 (Index Search)

인덱스를 활용한 검색 방법입니다.

**구조 예시:**
```
전체 데이터: 1~100만

색인표 구조:
AA (1~1000)
├── A: 1~100
├── B: 101~200  
└── C: 201~300
```

**특징:**
- 색인표를 먼저 찾고, 해당 색인표에서 데이터를 찾는 방식
- **시간 복잡도**: O(log N)
- 순차검색보다 훨씬 빠름

---

## 2. 인덱스 (Index)

### 2.1 자동 구성 인덱스

**Primary Key**
- Primary Key 필드는 **무조건 인덱스가 자동 생성**됨
- Primary Key를 이용한 검색을 많이 하기 때문

### 2.2 사용자 구성 인덱스

**인덱스 생성이 유용한 경우:**
- `WHERE` 조건절에서 자주 사용되는 필드
- `ORDER BY` 절에서 사용되는 필드  
- `JOIN` 절에서 사용되는 필드

### 2.3 인덱스 사용 시 주의사항

⚠️ **주의사항**
- 인덱스가 너무 많이 만들어지면 **시스템 성능이 떨어짐**
- 색인은 병렬처리가 안됨 (색인에서 먼저 찾고 → 원데이터에서 찾고 → 반복)

**인덱스가 불필요한 경우:**
```sql
-- 성별 같은 분포도가 높은 컬럼
WHERE gender = 'M'  -- 인덱스 만들 필요 없음
```

**인덱스 효과가 없는 경우:**
- 전체 데이터가 10,000건 이내 (Oracle은 100만건 이내는 그냥 둠)
- 데이터 분포도가 한쪽에 50% 넘어가는 값이 있을 경우
- **주소 검색** (서울시, 경기도로 검색) - 주로 2~3%의 값의 범위를 가질 때 효과적
- 인덱스를 잘못 만들면 옵티마이저(쿼리최적화)가 무시하고 지나감

---

## 3. 뷰 (View)

### 3.1 뷰란?

**정의**: 복잡한 데이터베이스 구조에서 여러 테이블을 조인해야 할 경우, 쿼리 자체를 저장해놓고 테이블처럼 사용할 수 있는 가상 테이블

**특징:**
- 주로 **조회용**으로 사용
- 뷰를 통해서 원본 테이블에 데이터를 업데이트할 수는 있지만 거의 사용하지 않음

### 3.2 뷰 생성 문법

```sql
-- 기본 문법
CREATE VIEW 뷰이름 AS 조회쿼리;

-- MySQL 5 이상에서 지원 (없으면 만들고, 있으면 수정)
CREATE OR REPLACE VIEW 뷰이름 AS 조회쿼리;
```

### 3.3 뷰 사용 예제

```sql
USE sakila;

-- 고객 정보 뷰 생성
CREATE OR REPLACE VIEW v_customer AS 
SELECT CONCAT(a.last_name, " ", a.first_name) AS customer_name,
       postal_code, 
       district, 
       phone, 
       location, 
       address
FROM customer a 
JOIN address b ON a.address_id = b.address_id;

-- 가상의 테이블처럼 사용
SELECT * FROM v_customer
WHERE customer_name LIKE '%smith%';
```

---

## 4. 제약조건 (Constraints)

### 4.1 Foreign Key (외래키)

**생성 조건:**
- Foreign Key를 만들려면 **참조되는 테이블의 필드가 Primary Key이거나 Unique 조건을 만족**해야 함

### 4.2 Unique Key

**특징:**
- **중복 불가**, **NULL 값 허용**
- **후보키**: Primary Key 가능성이 있는 필드
- 특정 필드가 Primary Key로 지정은 못하지만 중복되면 안 될 때 Unique 제약조건으로 대신 사용

```sql
-- Unique 제약조건 예시
ALTER TABLE 테이블명 ADD CONSTRAINT UK_컬럼명 UNIQUE (컬럼명);
```

---

## 5. 윈도우 함수 (Window Function)

### 5.1 윈도우 함수란?

**정의**: 분석용 함수로, 그룹 함수의 대체 함수

**장점:**
- 그룹 함수를 더 쉽게 사용 가능
- 속도가 빠름

### 5.2 문법

```sql
윈도우함수(컬럼) OVER (
    [PARTITION BY 컬럼]
    [ORDER BY 컬럼] 
    [ROWS BETWEEN ...]
)
```

### 5.3 주요 윈도우 함수

#### ROW_NUMBER()
- **중복 없이 순번을 부여**하는 함수

```sql
SELECT 
    empno,
    ename,
    sal,
    ROW_NUMBER() OVER (ORDER BY sal DESC) AS rank_num
FROM emp;
```

#### SUM() - 윈도우 함수 버전
- 그룹 함수인 `SUM()`과 윈도우 함수의 `SUM()`은 **OVER 절의 유무**로 구분

```sql
-- 일반 그룹 함수
SELECT SUM(sal) FROM emp;

-- 윈도우 함수 (누적 합계)
SELECT 
    empno,
    ename,
    sal,
    SUM(sal) OVER (ORDER BY empno ROWS UNBOUNDED PRECEDING) AS running_total
FROM emp;
```

### 5.4 윈도우 (Window) 개념

**ROWS BETWEEN**: 시작위치 AND 마지막위치를 지정하여 특정 범위의 데이터에 대해 함수를 적용

```sql
-- 현재 행과 이전 2행, 다음 2행 범위에서 평균 계산
SELECT 
    empno,
    sal,
    AVG(sal) OVER (
        ORDER BY empno 
        ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING
    ) AS moving_avg
FROM emp;
```

---

## 6. 성능 최적화 팁

### 6.1 인덱스 설계 원칙

1. **선택도가 높은 컬럼**에 인덱스 생성 (전체 데이터의 2-5% 수준)
2. **자주 사용되는 WHERE 조건**에 인덱스 생성
3. **조인 조건**에 사용되는 컬럼에 인덱스 생성
4. **과도한 인덱스**는 INSERT/UPDATE/DELETE 성능 저하

### 6.2 쿼리 최적화

1. **옵티마이저**가 올바른 실행계획을 선택하도록 적절한 인덱스 설계
2. **윈도우 함수** 활용으로 복잡한 그룹 연산 최적화
3. **뷰** 활용으로 복잡한 조인 쿼리 단순화

---

## 참고사항

- 이 문서는 MySQL과 Oracle 데이터베이스의 특성을 기반으로 작성되었습니다.
- 실제 운영환경에서는 데이터 크기와 사용 패턴에 따라 최적화 전략이 달라질 수 있습니다.
- 성능 튜닝 시에는 항상 실행계획(EXPLAIN)을 확인하여 최적화 효과를 검증해야 합니다. 