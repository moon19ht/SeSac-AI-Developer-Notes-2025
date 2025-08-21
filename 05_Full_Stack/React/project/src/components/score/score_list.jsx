import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios';

function ScoreList() {
    const [scoreList, setScoreList] = useState([]);
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState(null);

    // API 기본 URL
    const API_BASE_URL = 'http://127.0.0.1:8000';

    // 성적 목록 조회 함수
    const loadScoreData = async () => {
        try {
            setIsLoading(true);
            setError(null);
            
            const response = await axios.get(`${API_BASE_URL}/score/scoreList`);
            setScoreList(response.data.scoreList || []);
        } catch (err) {
            console.error('성적 목록 조회 오류:', err);
            setError('성적 목록을 불러오는 중 오류가 발생했습니다.');
        } finally {
            setIsLoading(false);
        }
    };

    useEffect(() => {
        loadScoreData();
    }, []);

    // 로딩 컴포넌트
    const LoadingComponent = () => (
        <div className="d-flex justify-content-center align-items-center" style={{ minHeight: '200px' }}>
            <div className="spinner-border text-primary" role="status">
                <span className="visually-hidden">로딩 중...</span>
            </div>
        </div>
    );

    // 에러 컴포넌트
    const ErrorComponent = () => (
        <div className="alert alert-danger" role="alert">
            <h4 className="alert-heading">오류 발생!</h4>
            <p>{error}</p>
            <button 
                className="btn btn-outline-danger" 
                onClick={loadScoreData}
            >
                다시 시도
            </button>
        </div>
    );

    // 성적 테이블 컴포넌트
    const ScoreTable = () => (
        <div className="table-responsive">
            <table className="table table-striped table-hover">
                <thead className="table-dark">
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">이름</th>
                        <th scope="col">국어</th>
                        <th scope="col">영어</th>
                        <th scope="col">수학</th>
                        <th scope="col">총점</th>
                        <th scope="col">평균</th>
                    </tr>
                </thead>
                <tbody>
                    {scoreList.length > 0 ? (
                        scoreList.map((item, index) => (
                            <tr key={item.id || index}>
                                <th scope="row">{index + 1}</th>
                                <td>{item.name}</td>
                                <td>{item.kor}</td>
                                <td>{item.eng}</td>
                                <td>{item.mat}</td>
                                <td className="fw-bold">{item.total}</td>
                                <td className="fw-bold text-primary">{item.avg}</td>
                            </tr>
                        ))
                    ) : (
                        <tr>
                            <td colSpan="7" className="text-center text-muted">
                                등록된 성적이 없습니다.
                            </td>
                        </tr>
                    )}
                </tbody>
            </table>
        </div>
    );

    return (
        <div className="container mt-4">
            <div className="row justify-content-center">
                <div className="col-md-10">
                    <div className="d-flex justify-content-between align-items-center mb-4">
                        <h2>성적 관리</h2>
                        <Link 
                            to="/score/insert" 
                            className="btn btn-primary"
                        >
                            성적 등록
                        </Link>
                    </div>

                    <div className="card">
                        <div className="card-header">
                            <h5 className="card-title mb-0">성적 목록</h5>
                        </div>
                        <div className="card-body">
                            {isLoading ? (
                                <LoadingComponent />
                            ) : error ? (
                                <ErrorComponent />
                            ) : (
                                <ScoreTable />
                            )}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default ScoreList;