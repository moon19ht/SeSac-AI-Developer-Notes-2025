import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios';

function ScoreWrite() {
    // 폼 데이터 상태 관리
    const [formData, setFormData] = useState({
        name: '',
        kor: 0,
        eng: 0,
        mat: 0
    });
    
    // 로딩 및 에러 상태 관리
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);
    
    const navigate = useNavigate();

    // API 기본 URL
    const API_BASE_URL = 'http://127.0.0.1:8000';

    // 입력 필드 변경 핸들러
    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setFormData(prev => ({
            ...prev,
            [name]: name === 'name' ? value : parseInt(value) || 0
        }));
    };

    // 폼 제출 핸들러
    const handleSubmit = async (e) => {
        e.preventDefault();
        
        // 입력 값 검증
        if (!formData.name.trim()) {
            setError('이름을 입력해주세요.');
            return;
        }

        if (formData.kor < 0 || formData.kor > 100 || 
            formData.eng < 0 || formData.eng > 100 || 
            formData.mat < 0 || formData.mat > 100) {
            setError('점수는 0~100 사이의 값을 입력해주세요.');
            return;
        }

        try {
            setIsLoading(true);
            setError(null);

            const response = await axios.post(`${API_BASE_URL}/score/score/insert`, formData);
            
            if (response.data && response.data.msg === "등록성공") {
                // 성공 시 목록 페이지로 이동
                navigate("/score/list");
            } else {
                throw new Error('성적 등록에 실패했습니다.');
            }
        } catch (err) {
            console.error('성적 등록 오류:', err);
            setError(err.response?.data?.msg || '성적 등록 중 오류가 발생했습니다.');
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="container mt-4">
            <div className="row justify-content-center">
                <div className="col-md-8">
                    <div className="d-flex justify-content-between align-items-center mb-4">
                        <h2>성적 등록</h2>
                        <Link to="/score/list" className="btn btn-secondary">
                            목록으로
                        </Link>
                    </div>

                    <div className="card">
                        <div className="card-header">
                            <h5 className="card-title mb-0">성적 정보 입력</h5>
                        </div>
                        <div className="card-body">
                            {error && (
                                <div className="alert alert-danger" role="alert">
                                    {error}
                                </div>
                            )}

                            <form onSubmit={handleSubmit}>
                                <div className="mb-3">
                                    <label htmlFor="name" className="form-label">이름</label>
                                    <input
                                        type="text"
                                        className="form-control"
                                        id="name"
                                        name="name"
                                        value={formData.name}
                                        onChange={handleInputChange}
                                        placeholder="학생 이름을 입력하세요"
                                        disabled={isLoading}
                                    />
                                </div>

                                <div className="mb-3">
                                    <label htmlFor="kor" className="form-label">국어</label>
                                    <input
                                        type="number"
                                        className="form-control"
                                        id="kor"
                                        name="kor"
                                        value={formData.kor}
                                        onChange={handleInputChange}
                                        min="0"
                                        max="100"
                                        placeholder="국어 점수를 입력하세요"
                                        disabled={isLoading}
                                    />
                                </div>

                                <div className="mb-3">
                                    <label htmlFor="eng" className="form-label">영어</label>
                                    <input
                                        type="number"
                                        className="form-control"
                                        id="eng"
                                        name="eng"
                                        value={formData.eng}
                                        onChange={handleInputChange}
                                        min="0"
                                        max="100"
                                        placeholder="영어 점수를 입력하세요"
                                        disabled={isLoading}
                                    />
                                </div>

                                <div className="mb-3">
                                    <label htmlFor="mat" className="form-label">수학</label>
                                    <input
                                        type="number"
                                        className="form-control"
                                        id="mat"
                                        name="mat"
                                        value={formData.mat}
                                        onChange={handleInputChange}
                                        min="0"
                                        max="100"
                                        placeholder="수학 점수를 입력하세요"
                                        disabled={isLoading}
                                    />
                                </div>

                                <div className="d-grid gap-2 d-md-flex justify-content-md-end">
                                    <Link 
                                        to="/score/list" 
                                        className="btn btn-outline-secondary me-md-2"
                                        disabled={isLoading}
                                    >
                                        취소
                                    </Link>
                                    <button 
                                        type="submit" 
                                        className="btn btn-primary"
                                        disabled={isLoading}
                                    >
                                        {isLoading ? (
                                            <>
                                                <span className="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>
                                                등록 중...
                                            </>
                                        ) : (
                                            '등록'
                                        )}
                                    </button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default ScoreWrite;