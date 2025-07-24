-- =====================================================
-- MySQL 6-8일차 통합 실습
-- 데이터베이스 설계, 고급 쿼리, 윈도우 함수 종합 학습
-- =====================================================

-- =====================================================
-- 1. 데이터베이스 및 사용자 설정
-- =====================================================

-- 프로젝트 전용 데이터베이스 생성
CREATE DATABASE project1; 

-- 전용 사용자 계정 생성 및 권한 부여
CREATE USER 'user03'@'localhost' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON project1.* TO 'user03'@'localhost';
FLUSH PRIVILEGES;

-- 프로젝트 데이터베이스 사용
USE project1;

-- =====================================================
-- 2. 테이블 생성 - 회원 관리 시스템
-- =====================================================

-- 회원 테이블 생성
-- MySQL에서 auto_increment 속성이 있는 필드는 반드시 primary key여야 함
CREATE TABLE tb_member(
    member_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(40) NOT NULL UNIQUE,
    password VARCHAR(300) NOT NULL,  -- MD5 암호화 알고리즘 사용 예정
    user_name VARCHAR(40) NOT NULL,
    email VARCHAR(40),
    phone VARCHAR(40),
    regdate DATETIME DEFAULT NOW()
); 

-- 성적 관리 테이블 생성
CREATE TABLE tb_score(
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    sname VARCHAR(20) NOT NULL,
    kor INT CHECK(kor >= 0 AND kor <= 100),
    eng INT CHECK(eng >= 0 AND eng <= 100),
    mat INT CHECK(mat >= 0 AND mat <= 100),
    regdate DATETIME DEFAULT NOW()
);

-- 테스트용 테이블들
CREATE TABLE test1( 
    id INT PRIMARY KEY,
    field VARCHAR(10) 
);

-- 기존 테이블 구조를 복사한 새 테이블 생성
CREATE TABLE test2 AS SELECT * FROM test1;

-- =====================================================
-- 3. 샘플 데이터 삽입
-- =====================================================

-- 회원 샘플 데이터
INSERT INTO tb_member(user_id, password, user_name, email, phone, regdate) 
VALUES('test1', '1234', '홍길동', 'hong@daum.net', '010-0000-0001', NOW());

INSERT INTO tb_member(user_id, password, user_name, email, phone, regdate) 
VALUES('test2', '5678', '김철수', 'kim@gmail.com', '010-1111-2222', NOW());

INSERT INTO tb_member(user_id, password, user_name, email, phone, regdate) 
VALUES('test3', '9999', '이영희', 'lee@naver.com', '010-3333-4444', NOW());

-- 성적 샘플 데이터
INSERT INTO tb_score(sname, kor, eng, mat, regdate) VALUES('김학생', 85, 90, 78, NOW());
INSERT INTO tb_score(sname, kor, eng, mat, regdate) VALUES('이학생', 92, 88, 94, NOW());
INSERT INTO tb_score(sname, kor, eng, mat, regdate) VALUES('박학생', 78, 82, 85, NOW());
INSERT INTO tb_score(sname, kor, eng, mat, regdate) VALUES('최학생', 65, 70, 68, NOW());
INSERT INTO tb_score(sname, kor, eng, mat, regdate) VALUES('정학생', 95, 96, 92, NOW());

-- =====================================================
-- 4. 기본 조회 및 검증 쿼리
-- =====================================================

-- 회원 정보 확인
SELECT * FROM tb_member;

-- 특정 사용자 존재 여부 확인
SELECT COUNT(*) AS cnt FROM tb_member WHERE user_id='test1';

-- 성적 정보 확인
SELECT * FROM tb_score;

-- 다음 ID 값 생성 (AUTO_INCREMENT 활용)
SELECT IFNULL(MAX(id), 0) + 1 AS next_id FROM test1;

-- =====================================================
-- 5. 고급 쿼리 - CASE문과 조건부 로직
-- =====================================================

-- CASE문을 활용한 성적 등급 분류
SELECT 
    id,
    sname,
    kor, eng, mat,
    (kor + eng + mat) AS total,
    ROUND((kor + eng + mat) / 3, 1) AS average,
    CASE 
        WHEN (kor + eng + mat) / 3 >= 90 THEN '수'
        WHEN (kor + eng + mat) / 3 >= 80 THEN '우' 
        WHEN (kor + eng + mat) / 3 >= 70 THEN '미'
        WHEN (kor + eng + mat) / 3 >= 60 THEN '양'
        ELSE '가' 
    END AS grade
FROM tb_score
ORDER BY total DESC;

-- =====================================================
-- 6. UNION을 활용한 통계 리포트
-- =====================================================

-- 성적 등급별 통계 (전체 포함)
SELECT '전체' AS grade, COUNT(*) AS count
FROM tb_score 
UNION ALL 
SELECT grade, COUNT(*) AS count
FROM (
    SELECT id, 
        CASE  
            WHEN (kor + eng + mat) / 3 >= 90 THEN '수'
            WHEN (kor + eng + mat) / 3 >= 80 THEN '우' 
            WHEN (kor + eng + mat) / 3 >= 70 THEN '미'
            WHEN (kor + eng + mat) / 3 >= 60 THEN '양'
            ELSE '가' 
        END AS grade 
    FROM tb_score
) A
GROUP BY grade
ORDER BY FIELD(grade, '전체', '수', '우', '미', '양', '가');

-- =====================================================
-- 7. 뷰(View) 생성 및 활용
-- =====================================================

-- Sakila 데이터베이스 사용 (뷰 예제용)
USE sakila;

-- 고객 정보 뷰 생성 (MySQL 5 이상에서 지원)
CREATE OR REPLACE VIEW v_customer AS 
SELECT 
    CONCAT(a.last_name, " ", a.first_name) AS customer_name,
    postal_code, 
    district, 
    phone, 
    location, 
    address
FROM customer a 
JOIN address b ON a.address_id = b.address_id;

-- 뷰를 활용한 검색
SELECT * FROM v_customer
WHERE customer_name LIKE '%smith%';

-- 인덱스 정보 확인
SHOW INDEX FROM customer;

-- =====================================================
-- 8. 윈도우 함수 (Window Functions)
-- =====================================================

-- w3schools 데이터베이스 사용 (윈도우 함수 예제용)
USE w3schools; 

-- 기본 집계와 윈도우 함수 비교
SELECT SUM(quantity) AS total_quantity FROM orderdetails;

-- 그룹별 집계
SELECT orderid, SUM(quantity) AS order_total
FROM orderdetails
GROUP BY orderid
LIMIT 10;

-- 윈도우 함수로 전체 합계 표시
SELECT orderid, quantity, SUM(quantity) OVER() AS total_quantity
FROM orderdetails
LIMIT 10;

-- PARTITION BY를 활용한 그룹별 누적 합계
SELECT 
    productid, 
    orderid, 
    quantity,
    SUM(quantity) OVER(
        PARTITION BY orderid
        ORDER BY orderid
    ) AS running_total 
FROM orderdetails
LIMIT 20;

-- =====================================================
-- 9. 순위 함수 (Ranking Functions)
-- =====================================================

-- RANK vs DENSE_RANK 비교
SELECT 
    orderid, 
    quantity, 
    RANK() OVER(ORDER BY quantity DESC) AS rank_with_gaps,
    DENSE_RANK() OVER(ORDER BY quantity DESC) AS dense_rank_no_gaps
FROM orderdetails
ORDER BY quantity DESC
LIMIT 15;

-- NTILE을 활용한 균등 분할 (4그룹으로 분할)
SELECT 
    orderid, 
    quantity,
    NTILE(4) OVER(ORDER BY quantity DESC) AS quartile 
FROM orderdetails
ORDER BY quantity DESC
LIMIT 20;

-- =====================================================
-- 10. ROW_NUMBER를 활용한 페이징 처리
-- =====================================================

-- 게시판 페이징을 위한 행 번호 부여
-- AUTO_INCREMENT의 단점: 중간 삭제 시 번호 공백 발생
-- ROW_NUMBER로 연속된 번호 생성
SELECT 
    orderid, 
    quantity,
    ROW_NUMBER() OVER(ORDER BY orderid DESC) AS row_num 
FROM orderdetails
ORDER BY orderid DESC
LIMIT 10;

-- 페이징 처리 예제 (11번째부터 10개 조회)
SELECT 
    orderid, 
    quantity,
    ROW_NUMBER() OVER(ORDER BY orderid DESC) AS row_num 
FROM orderdetails
ORDER BY orderid DESC
LIMIT 11, 10;

-- =====================================================
-- 11. ROWS BETWEEN을 활용한 이동 평균
-- =====================================================

-- 윈도우 범위 지정 옵션들:
-- UNBOUNDED PRECEDING: 처음부터 
-- CURRENT ROW: 현재행 
-- N PRECEDING: 현재행에서 N행 이전 
-- N FOLLOWING: 현재행에서 N행 이후 
-- UNBOUNDED FOLLOWING: 맨 끝까지

-- 이동 합계 및 평균 계산
SELECT 
    orderid,
    quantity, 
    -- 이전 1행 + 현재행 + 다음 1행 합계
    SUM(quantity) OVER(
        ORDER BY orderid 
        ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
    ) AS moving_sum_3,
    -- 이전 1행 + 현재행 합계
    SUM(quantity) OVER(
        ORDER BY orderid 
        ROWS BETWEEN 1 PRECEDING AND CURRENT ROW
    ) AS cumulative_sum_2,
    -- 이동 평균 (3개 값)
    AVG(quantity) OVER(
        ORDER BY orderid 
        ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
    ) AS moving_avg_3
FROM orderdetails
ORDER BY orderid
LIMIT 20;

-- =====================================================
-- 12. 실무 활용 예제 - 성적 관리 시스템
-- =====================================================

-- project1 데이터베이스로 돌아가서 실무 예제
USE project1;

-- 성적 순위 및 통계 정보
SELECT 
    id,
    sname,
    kor, eng, mat,
    (kor + eng + mat) AS total,
    ROUND((kor + eng + mat) / 3, 1) AS average,
    RANK() OVER(ORDER BY (kor + eng + mat) DESC) AS total_rank,
    ROW_NUMBER() OVER(ORDER BY (kor + eng + mat) DESC) AS row_num,
    CASE 
        WHEN (kor + eng + mat) / 3 >= 90 THEN '수'
        WHEN (kor + eng + mat) / 3 >= 80 THEN '우' 
        WHEN (kor + eng + mat) / 3 >= 70 THEN '미'
        WHEN (kor + eng + mat) / 3 >= 60 THEN '양'
        ELSE '가' 
    END AS grade,
    -- 전체 학생 대비 백분율
    ROUND(
        PERCENT_RANK() OVER(ORDER BY (kor + eng + mat) DESC) * 100, 1
    ) AS percentile
FROM tb_score
ORDER BY total DESC;

-- 과목별 평균과 개인 성적 비교
SELECT 
    sname,
    kor,
    ROUND(AVG(kor) OVER(), 1) AS kor_avg,
    kor - ROUND(AVG(kor) OVER(), 1) AS kor_diff,
    eng,
    ROUND(AVG(eng) OVER(), 1) AS eng_avg,
    eng - ROUND(AVG(eng) OVER(), 1) AS eng_diff,
    mat,
    ROUND(AVG(mat) OVER(), 1) AS mat_avg,
    mat - ROUND(AVG(mat) OVER(), 1) AS mat_diff
FROM tb_score
ORDER BY sname;

-- =====================================================
-- 13. 데이터 정리 및 최종 검증
-- =====================================================

-- 생성된 테이블 목록 확인
SHOW TABLES;

-- 각 테이블별 데이터 개수 확인
SELECT 'tb_member' AS table_name, COUNT(*) AS record_count FROM tb_member
UNION ALL
SELECT 'tb_score' AS table_name, COUNT(*) AS record_count FROM tb_score
UNION ALL
SELECT 'test1' AS table_name, COUNT(*) AS record_count FROM test1
UNION ALL
SELECT 'test2' AS table_name, COUNT(*) AS record_count FROM test2;

-- =====================================================
-- 학습 완료! 
-- 
-- 이 스크립트를 통해 다음 내용을 학습했습니다:
-- 1. 데이터베이스 및 사용자 관리
-- 2. 테이블 설계 및 제약조건
-- 3. 고급 SQL 문법 (CASE, UNION)
-- 4. 뷰(View) 생성 및 활용
-- 5. 윈도우 함수 전반
-- 6. 순위 함수 및 페이징
-- 7. 이동 평균 및 누적 통계
-- 8. 실무 활용 예제
-- ===================================================== 