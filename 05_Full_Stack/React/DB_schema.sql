-- ===============================================
-- 게시판 데이터베이스 스키마 및 초기 데이터 설정
-- ===============================================

-- 데이터베이스 연결
-- mysql -u root -p 
-- Enter your password : 1234
USE mydb;

-- 게시판 테이블 생성
CREATE TABLE IF NOT EXISTS tb_board (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(300) NOT NULL,
    contents LONGTEXT,
    filename VARCHAR(300),
    image_url VARCHAR(300),
    writer VARCHAR(100) NOT NULL,
    wdate DATETIME DEFAULT CURRENT_TIMESTAMP,
    hit INT DEFAULT 0,
    
    -- 인덱스 추가 (성능 최적화)
    INDEX idx_writer (writer),
    INDEX idx_wdate (wdate),
    INDEX idx_title (title)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 기존 데이터 삭제 (테스트용)
-- DELETE FROM tb_board WHERE writer = 'test1';

-- 초기 테스트 데이터 삽입
INSERT INTO tb_board (title, contents, writer, wdate, hit) VALUES
('제목1', '내용1', 'test1', NOW(), 0),
('제목2', '내용2', 'test1', NOW(), 0),
('제목3', '내용3', 'test1', NOW(), 0),
('제목4', '내용4', 'test1', NOW(), 0),
('제목5', '내용5', 'test1', NOW(), 0);

-- ===============================================
-- 백엔드 환경 설정 명령어
-- ===============================================
-- cmd - 관리자권한으로 실행
-- conda activate backend 
-- conda install pymysql sqlalchemy