import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios';

function BoardList() {
    // 상태 변수들
    const [boardList, setBoardList] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);

    // API 기본 URL
    const API_BASE_URL = 'http://127.0.0.1:8000';

    // 게시판 목록 데이터 로드
    const loadBoardData = async () => {
        try {
            setIsLoading(true);
            setError(null);
            
            const response = await axios.get(`${API_BASE_URL}/board/list`);
            
            if (response.data && response.data.list) {
                setBoardList(response.data.list);
            } else {
                throw new Error('게시판 데이터를 가져올 수 없습니다.');
            }
        } catch (err) {
            console.error('게시판 목록 로드 오류:', err);
            setError(err.message || '데이터를 불러오는 중 오류가 발생했습니다.');
        } finally {
            setIsLoading(false);
        }
    };

    // 컴포넌트 마운트 시 데이터 로드
    useEffect(() => {
        loadBoardData();
    }, []);

    // 로딩 중 화면
    if (isLoading) {
        return (
            <div className="d-flex justify-content-center align-items-center" style={{ minHeight: '200px' }}>
                <div className="spinner-border" role="status">
                    <span className="visually-hidden">로딩 중...</span>
                </div>
                <span className="ms-2">데이터를 불러오는 중입니다...</span>
            </div>
        );
    }

    // 에러 발생 시 화면
    if (error) {
        return (
            <div className="alert alert-danger" role="alert">
                <h4 className="alert-heading">오류 발생</h4>
                <p>{error}</p>
                <button 
                    className="btn btn-outline-danger" 
                    onClick={loadBoardData}
                >
                    다시 시도
                </button>
            </div>
        );
    }

    return (
        <div className="container mt-4">
            <div className="d-flex justify-content-between align-items-center mb-3">
                <h2>게시판 목록</h2>
                <Link to="/board/write" className="btn btn-primary">
                    글쓰기
                </Link>
            </div>

            {boardList.length === 0 ? (
                <div className="text-center py-5">
                    <p className="text-muted">등록된 게시글이 없습니다.</p>
                </div>
            ) : (
                <div className="table-responsive">
                    <table className="table table-striped table-hover">
                        <thead className="table-dark">
                            <tr>
                                <th scope="col" style={{ width: '80px' }}>번호</th>
                                <th scope="col">제목</th>
                                <th scope="col" style={{ width: '150px' }}>작성자</th>
                                <th scope="col" style={{ width: '180px' }}>작성일</th>
                                <th scope="col" style={{ width: '100px' }}>조회수</th>
                            </tr>
                        </thead>
                        <tbody>
                            {boardList.map((item) => (
                                <tr key={item.id}>
                                    <td>{item.id}</td>
                                    <td>
                                        <Link 
                                            to={`/board/detail/${item.id}`} 
                                            className="text-decoration-none"
                                        >
                                            {item.title}
                                        </Link>
                                    </td>
                                    <td>{item.writer}</td>
                                    <td>{new Date(item.wdate).toLocaleDateString('ko-KR')}</td>
                                    <td>{item.hit}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            )}
        </div>
    );
}

export default BoardList;