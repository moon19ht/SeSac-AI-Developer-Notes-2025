-- ============================================================================
-- MySQL 1-5일차 통합 실습
-- ============================================================================
-- 1. 샘플 데이터베이스 구축 (orders 시스템)
-- 2. 기본 조인과 서브쿼리 실습 (w3schools)
-- 3. 고급 SQL 기능 실습 (스포츠 데이터베이스)
-- 4. 실무 활용 예제
-- ============================================================================

-- ============================================================================
-- 섹션 1: 주문 관리 시스템 (Sample Orders Database)
-- ============================================================================

-- 데이터베이스 생성 및 선택
DROP DATABASE IF EXISTS sample_orders;
CREATE DATABASE sample_orders CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE sample_orders;

-- 1.1 customers 테이블 생성 및 데이터 삽입
DROP TABLE IF EXISTS customers;
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE
);

INSERT INTO customers (name, email) VALUES
('Alice', 'alice@example.com'),
('Bob', 'bob@example.com'),
('Charlie', 'charlie@example.com'),
('Diana', 'diana@example.com'),
('Eve', 'eve@example.com');

-- 1.2 orders 테이블 생성 및 데이터 삽입
DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    status VARCHAR(20),
    total_amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO orders (customer_id, order_date, status, total_amount) VALUES
(1, '2024-05-01', 'Pending', 120.50),
(2, '2024-05-03', 'Completed', 300.00),
(3, '2024-05-05', 'Shipped', 89.99),
(1, '2024-05-10', 'Cancelled', 49.00),
(4, '2024-05-12', 'Completed', 199.90),
(2, '2024-05-15', 'Pending', 150.75),
(5, '2024-05-17', 'Shipped', 80.00);

-- 1.3 order_items 테이블 생성 및 데이터 삽입
DROP TABLE IF EXISTS order_items;
CREATE TABLE order_items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    product_name VARCHAR(100),
    quantity INT,
    price DECIMAL(10,2),
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

INSERT INTO order_items (order_id, product_name, quantity, price) VALUES
(1, 'USB Cable', 2, 15.00),
(1, 'Mouse', 1, 25.50),
(2, 'Keyboard', 1, 100.00),
(2, 'Monitor', 2, 100.00),
(3, 'Headphones', 1, 89.99),
(4, 'Phone Case', 1, 49.00),
(5, 'Webcam', 1, 99.95),
(5, 'Tripod', 1, 99.95),
(6, 'Charger', 3, 50.25),
(7, 'Laptop Stand', 1, 80.00);

-- 1.4 기본 조회 예제
-- 고객별 주문 현황
SELECT c.name, c.email, o.order_id, o.order_date, o.status, o.total_amount
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
ORDER BY c.name, o.order_date;

-- 주문 상세 내역
SELECT c.name, o.order_id, oi.product_name, oi.quantity, oi.price, 
       (oi.quantity * oi.price) AS item_total
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
ORDER BY c.name, o.order_id;

-- ============================================================================
-- 섹션 2: w3schools 데이터베이스 고급 실습
-- ============================================================================

-- w3schools 데이터베이스 사용 (사전에 설치되어 있어야 함)
USE w3schools;

-- 2.1 조인(JOIN) 실습
-- ============================================================================

-- 2.1.1 INNER JOIN - 교집합
-- 고객 이름이 'Handel'인 사람의 주문 내용 확인
SELECT o.OrderID, c.CustomerID, c.CustomerName 
FROM customers c
INNER JOIN orders o ON c.CustomerID = o.CustomerID
WHERE c.CustomerName LIKE '%Handel%';

-- 2.1.2 고객 'Handel'이 주문한 상품명 확인 (다중 조인)
SELECT od.ProductID, od.Quantity, p.ProductName, od.OrderID 
FROM orderdetails od 
INNER JOIN products p ON od.ProductID = p.ProductID
WHERE od.OrderID IN (
    SELECT o.OrderID
    FROM customers c
    INNER JOIN orders o ON c.CustomerID = o.CustomerID
    WHERE c.CustomerName LIKE '%Handel%'
); 

-- 2.1.3 3개 테이블 조인
SELECT o.OrderID, c.CustomerName, s.ShipperName
FROM Orders o
INNER JOIN Customers c ON o.CustomerID = c.CustomerID
INNER JOIN Shippers s ON o.ShipperID = s.ShipperID;

-- 2.1.4 5개 테이블 복합 조인 - 직원 'King'이 판매한 내역
SELECT o.OrderID, c.CustomerName, s.ShipperName, p.ProductName
FROM orders o 
INNER JOIN employees e ON o.EmployeeID = e.EmployeeID
INNER JOIN customers c ON o.CustomerID = c.CustomerID
INNER JOIN orderdetails od ON o.OrderID = od.OrderID
INNER JOIN products p ON od.ProductID = p.ProductID
INNER JOIN shippers s ON o.ShipperID = s.ShipperID
WHERE e.LastName LIKE 'King%'; 

-- 2.2 UNION과 UNION ALL
-- ============================================================================

-- 독일에 있는 고객과 공급자 도시 목록
SELECT City, Country, 'Customer' AS Type FROM Customers
WHERE Country='Germany'
UNION ALL
SELECT City, Country, 'Supplier' AS Type FROM Suppliers
WHERE Country='Germany'
ORDER BY City;

-- 2.3 집계 함수와 GROUP BY
-- ============================================================================

-- 나라별 고객 수
SELECT country, COUNT(*) AS customer_count
FROM customers 
GROUP BY country
ORDER BY customer_count DESC;

-- 배달업체별 주문 개수
SELECT s.ShipperName, COUNT(*) AS order_count
FROM orders o 
INNER JOIN shippers s ON o.ShipperID = s.ShipperID
GROUP BY s.ShipperName
ORDER BY order_count DESC; 

-- 2.4 서브쿼리 활용
-- ============================================================================

-- 스칼라 서브쿼리 - 각 주문에 배송업체별 총 주문 수 포함
SELECT o.OrderID, o.ShipperID,
    (SELECT COUNT(*) FROM orders o2 WHERE o2.ShipperID = o.ShipperID) AS shipper_total_orders
FROM orders o;

-- EXISTS 서브쿼리 - 가격이 20달러 미만인 제품을 공급하는 공급자
SELECT s.SupplierName
FROM Suppliers s
WHERE EXISTS (
    SELECT 1 FROM Products p
    WHERE p.SupplierID = s.SupplierID AND p.Price < 20
);

-- 2.5 내장 함수 활용
-- ============================================================================

-- 문자열 함수
SELECT CONCAT("Tom ", "is", " a student") AS sentence;
SELECT CONCAT(Address, " ", PostalCode, " ", City) AS full_address
FROM customers
LIMIT 5;

-- 날짜 함수
SELECT NOW() AS current_datetime;
SELECT ADDDATE("2025-01-01", INTERVAL 10 DAY) AS future_date;
SELECT DATEDIFF("2025-12-31", "2025-01-01") AS days_in_year;

-- 문자열 처리
SELECT 
    SUBSTR("2025-05-20", 1, 4) AS year,
    SUBSTR("2025-05-20", 6, 2) AS month,
    SUBSTR("2025-05-20", 9, 2) AS day;

-- ============================================================================
-- 섹션 3: 스포츠 데이터베이스 고급 실습 (mydb2)
-- ============================================================================

USE mydb2;

-- 3.1 기본 조회와 정렬
-- ============================================================================

-- K01 팀 선수들의 명단 (입단연도, 이름 순 정렬)
SELECT player_name, join_yyyy, posit 
FROM player 
WHERE team_id = 'K01'
ORDER BY join_yyyy IS NULL, join_yyyy, player_name;

-- 3.2 다중 테이블 조인
-- ============================================================================

-- 울산 지역 팀과 선수 정보
SELECT t.team_name, p.player_name, t.region_name, 
       CONCAT(t.zip_code1, "-", t.zip_code2) AS zipcode,
       t.address
FROM player p 
INNER JOIN team t ON p.team_id = t.team_id
WHERE t.region_name = '울산';

-- 선수, 팀, 경기장 정보 (K05, K07, K12 구단)
SELECT p.player_name, t.team_name, s.stadium_name 
FROM player p 
LEFT OUTER JOIN team t ON p.team_id = t.team_id 
LEFT OUTER JOIN stadium s ON t.stadium_id = s.stadium_id
WHERE p.team_id IN ('K05', 'K07', 'K12')
ORDER BY t.team_name, p.back_no;

-- 3.3 CASE 문 활용
-- ============================================================================

-- 포지션별 한글 표기
SELECT player_name, 
       CASE posit 
           WHEN 'GK' THEN '골키퍼' 
           WHEN 'DF' THEN '수비수'
           WHEN 'FW' THEN '공격수'
           WHEN 'MF' THEN '미드필더'
           ELSE '없음'
       END AS position_kr 
FROM player 
WHERE team_id = 'K01';

-- 키 기준 등급 분류
SELECT player_name, height, 
       CASE 
           WHEN height > 190 THEN 'A등급'
           WHEN height > 180 THEN 'B등급' 
           ELSE 'C등급'
       END AS height_grade 
FROM player 
WHERE team_id = 'K03' AND height IS NOT NULL;

-- 3.4 집계 함수와 GROUP BY
-- ============================================================================

-- 팀별 키 180cm 이상 선수 수
SELECT t.team_name, COUNT(*) AS tall_players_count
FROM player p
INNER JOIN team t ON p.team_id = t.team_id
WHERE p.height >= 180
GROUP BY t.team_name
ORDER BY tall_players_count DESC;

-- 3.5 복잡한 조인과 UNION
-- ============================================================================

-- FC서울의 전체 일정 (홈/어웨이 포함)
SELECT s.sche_date, t.team_name, 'Home' AS game_type 
FROM schedule s
INNER JOIN team t ON s.hometeam_id = t.team_id
WHERE t.team_name = 'FC서울' 
UNION ALL 
SELECT s.sche_date, t.team_name, 'Away' AS game_type 
FROM schedule s
INNER JOIN team t ON s.awayteam_id = t.team_id
WHERE t.team_name = 'FC서울'
ORDER BY sche_date;

-- 2012년 10월 19일 C06, C05 스타디움 경기 선수들
SELECT p.player_name, t.team_name, s.stadium_id, s.sche_date
FROM player p
INNER JOIN team t ON p.team_id = t.team_id
INNER JOIN schedule s ON (s.hometeam_id = t.team_id OR s.awayteam_id = t.team_id)
WHERE s.stadium_id IN ('C05', 'C06') 
  AND s.sche_date = '20121019'
ORDER BY t.team_id;

-- 3.6 경기 결과 분석
-- ============================================================================

-- 경기 결과별 승부 분석
SELECT stadium_id, sche_date, 
       CASE 
           WHEN home_score > away_score THEN '홈팀 승리'
           WHEN home_score < away_score THEN '어웨이팀 승리'
           ELSE '무승부'
       END AS match_result,
       CASE 
           WHEN home_score > away_score THEN hometeam_id
           WHEN home_score < away_score THEN awayteam_id
           ELSE 'Draw'
       END AS winner_team_id,
       CONCAT(home_score, ' : ', away_score) AS score
FROM schedule
WHERE home_score IS NOT NULL AND away_score IS NOT NULL
ORDER BY sche_date DESC
LIMIT 10;

-- ============================================================================
-- 섹션 4: 테이블 생성과 데이터 조작 (DDL/DML)
-- ============================================================================

USE mydb;

-- 4.1 테이블 생성과 데이터 삽입
-- ============================================================================

-- 부서 테이블에 데이터 추가
INSERT INTO dept VALUES(50, '개발1부', '서울');
INSERT INTO dept(deptno, dname) VALUES(60, '개발2부');

-- 직원 테이블에 데이터 추가 (단일/다중)
INSERT INTO emp(empno, ename, sal) VALUES(8000, '홍길동', 3300);

INSERT INTO emp(empno, ename, sal) VALUES
(8001, '둘리', 3200),
(8002, '도우너', 3200),
(8003, '또치', 3200),
(8004, 'Tom''s', 3200),
(8005, '''jane''', 3200);

-- 4.2 CASE문을 활용한 부서명 변환
-- ============================================================================

SELECT ename, 
       CASE deptno 
           WHEN 10 THEN '총무부'
           WHEN 20 THEN '홍보부' 
           WHEN 30 THEN '개발1부'
           WHEN 40 THEN '개발2부'
           WHEN 50 THEN '개발1부'
           WHEN 60 THEN '개발2부'
           ELSE '미지정'
       END AS department_name 
FROM emp;

-- 4.3 테이블 복사와 구조 생성
-- ============================================================================

-- 전체 테이블 복사 (데이터 포함)
CREATE TABLE emp2 AS SELECT * FROM emp; 

-- 구조만 복사 (데이터 제외)
CREATE TABLE emp3 AS SELECT * FROM emp WHERE 1=0; 

-- 특정 조건의 데이터만 복사
CREATE TABLE emp4 AS 
SELECT empno, ename, sal 
FROM emp 
WHERE deptno IN (10, 20); 

-- 다른 테이블에서 데이터 삽입
INSERT INTO emp3 (empno, ename, sal) 
SELECT empno, ename, sal 
FROM emp;

-- ============================================================================
-- 섹션 5: 실무 활용 종합 예제
-- ============================================================================

-- 5.1 w3schools 데이터베이스 종합 문제
-- ============================================================================

USE w3schools;

-- 문제1: customers 테이블 구조 복사 및 특정 고객 데이터 복사
CREATE TABLE customers2 AS SELECT * FROM customers WHERE 1=0;

INSERT INTO customers2 
SELECT * FROM customers 
WHERE CustomerID IN (3, 23, 21, 45, 67, 89, 54);

-- 문제2: 제품가격이 100달러를 넘는 제품을 구매한 고객 리스트
SELECT DISTINCT c.CustomerName, c.ContactName, c.Country
FROM customers c
INNER JOIN orders o ON c.CustomerID = o.CustomerID
INNER JOIN orderdetails od ON o.OrderID = od.OrderID
INNER JOIN products p ON od.ProductID = p.ProductID
WHERE p.Price > 100
ORDER BY c.CustomerName;

-- 문제3: 고객별 총 구매 금액 (quantity × price)
SELECT c.CustomerName, p.ProductName, 
       od.Quantity, p.Price,
       (od.Quantity * p.Price) AS total_amount
FROM customers c
INNER JOIN orders o ON c.CustomerID = o.CustomerID
INNER JOIN orderdetails od ON o.OrderID = od.OrderID
INNER JOIN products p ON od.ProductID = p.ProductID
ORDER BY c.CustomerName, total_amount DESC;

-- 문제4: 핀란드 공급자 리스트
SELECT SupplierName, ContactName, City, Country
FROM suppliers
WHERE Country = 'Finland';

-- 문제5: Seafood 카테고리 제품 구매자 리스트
SELECT DISTINCT c.CustomerName, c.ContactName, c.Country
FROM customers c
INNER JOIN orders o ON c.CustomerID = o.CustomerID
INNER JOIN orderdetails od ON o.OrderID = od.OrderID
INNER JOIN products p ON od.ProductID = p.ProductID
INNER JOIN categories cat ON p.CategoryID = cat.CategoryID
WHERE cat.CategoryName = 'Seafood'
ORDER BY c.CustomerName;

-- 5.2 성능 최적화 예제
-- ============================================================================

-- 인덱스 활용 예제 (실제 운영에서는 신중하게 결정)
-- CREATE INDEX idx_customer_name ON customers(CustomerName);
-- CREATE INDEX idx_product_price ON products(Price);

-- 효율적인 쿼리 작성 예제
SELECT o.OrderID, c.CustomerName, 
       COUNT(od.ProductID) AS item_count,
       SUM(od.Quantity * p.Price) AS total_amount
FROM orders o
INNER JOIN customers c ON o.CustomerID = c.CustomerID
INNER JOIN orderdetails od ON o.OrderID = od.OrderID
INNER JOIN products p ON od.ProductID = p.ProductID
GROUP BY o.OrderID, c.CustomerName
HAVING total_amount > 1000
ORDER BY total_amount DESC
LIMIT 10;

-- ============================================================================
-- 섹션 6: 고급 SQL 패턴과 실무 팁
-- ============================================================================

-- 6.1 윈도우 함수 활용 (MySQL 8.0+)
-- ============================================================================

USE w3schools;

-- 고객별 주문 순위
SELECT c.CustomerName, o.OrderID, o.OrderDate,
       ROW_NUMBER() OVER (PARTITION BY c.CustomerID ORDER BY o.OrderDate) AS order_sequence,
       RANK() OVER (ORDER BY COUNT(od.ProductID) DESC) AS customer_rank
FROM customers c
INNER JOIN orders o ON c.CustomerID = o.CustomerID
INNER JOIN orderdetails od ON o.OrderID = od.OrderID
GROUP BY c.CustomerName, o.OrderID, o.OrderDate;

-- 6.2 재귀 CTE (Common Table Expression) 예제
-- ============================================================================

-- 계층형 데이터 처리 (직원-상사 관계)
USE mydb;

WITH RECURSIVE emp_hierarchy AS (
    -- 최상위 직원 (MGR이 NULL인 직원)
    SELECT empno, ename, mgr, 1 AS level, ename AS path
    FROM emp 
    WHERE mgr IS NULL
    
    UNION ALL
    
    -- 하위 직원들
    SELECT e.empno, e.ename, e.mgr, eh.level + 1, 
           CONCAT(eh.path, ' -> ', e.ename) AS path
    FROM emp e
    INNER JOIN emp_hierarchy eh ON e.mgr = eh.empno
    WHERE eh.level < 5  -- 무한 루프 방지
)
SELECT empno, ename, mgr, level, path
FROM emp_hierarchy
ORDER BY level, ename;

-- ============================================================================
-- 부록: 유용한 MySQL 관리 쿼리
-- ============================================================================

-- 데이터베이스 및 테이블 정보 조회
SHOW DATABASES;
SHOW TABLES;
SHOW CREATE TABLE customers;

-- 테이블 상태 및 용량 확인
SELECT 
    table_name,
    table_rows,
    ROUND((data_length + index_length) / 1024 / 1024, 2) AS table_size_mb
FROM information_schema.tables 
WHERE table_schema = DATABASE()
ORDER BY table_size_mb DESC;

-- 외래키 제약조건 확인
SELECT 
    constraint_name,
    table_name,
    column_name,
    referenced_table_name,
    referenced_column_name
FROM information_schema.key_column_usage 
WHERE table_schema = DATABASE() 
  AND referenced_table_name IS NOT NULL;

-- ============================================================================
-- 마무리: 학습 정리 및 다음 단계 가이드
-- ============================================================================

/*
축하합니다! MySQL 종합 실습을 완료하셨습니다.

학습한 주요 내용:
1. 테이블 생성과 데이터 관리 (DDL/DML)
2. 다양한 조인 방법 (INNER, LEFT, RIGHT, SELF JOIN)
3. 서브쿼리와 집계 함수 활용
4. CASE문을 통한 조건부 로직
5. UNION을 통한 데이터 결합
6. 윈도우 함수와 CTE 활용
7. 성능 최적화 기초

다음 단계 학습 제안:
- 저장 프로시저와 함수 작성
- 트리거와 이벤트 스케줄러
- 트랜잭션과 락 관리
- 인덱스 최적화와 성능 튜닝
- NoSQL과의 연동 (JSON 데이터 타입)
- 파티셔닝과 샤딩
- 백업과 복구 전략

실무 활용 팁:
- 항상 WHERE 절에 인덱스를 활용하세요
- 대용량 데이터 처리 시 LIMIT와 페이징을 활용하세요
- 복잡한 쿼리는 단계별로 나누어 테스트하세요
- 정기적인 EXPLAIN을 통해 쿼리 성능을 확인하세요
*/

-- END OF FILE
-- ============================================================================ 