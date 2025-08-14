import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios';

function BoardWrite() {
    // 폼 데이터 상태 관리
    const [formData, setFormData] = useState({
        title: '',
        writer: '',
        contents: ''
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
            [name]: value
        }));
    };

    // 폼 제출 핸들러
    const handleSubmit = async (e) => {
        e.preventDefault();
        
        // 입력 값 검증
        if (!formData.title.trim() || !formData.writer.trim() || !formData.contents.trim()) {
            setError('모든 필드를 입력해주세요.');
            return;
        }

        try {
            setIsLoading(true);
            setError(null);

            const response = await axios.post(`${API_BASE_URL}/board/insert`, formData);
            
            if (response.data && response.data.msg === "등록성공") {
                // 성공 시 목록 페이지로 이동
                navigate("/board/list");
            } else {
                throw new Error('게시글 등록에 실패했습니다.');
            }
        } catch (err) {
            console.error('게시글 등록 오류:', err);
            setError(err.response?.data?.msg || '게시글 등록 중 오류가 발생했습니다.');
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="container mt-4">
            <div className="row justify-content-center">
                <div className="col-md-8">
                    <div className="d-flex justify-content-between align-items-center mb-4">
                        <h2>게시글 작성</h2>
                        <Link to="/board/list" className="btn btn-secondary">
                            목록으로
                        </Link>
                    </div>

                    {error && (
                        <div className="alert alert-danger" role="alert">
                            {error}
                        </div>
                    )}

                    <div className="card">
                        <div className="card-body">
                            <form onSubmit={handleSubmit}>
                                <div className="mb-3">
                                    <label htmlFor="title" className="form-label">제목 *</label>
                                    <input 
                                        type="text" 
                                        id="title"
                                        name="title" 
                                        className="form-control"
                                        value={formData.title}
                                        onChange={handleInputChange}
                                        placeholder="제목을 입력하세요"
                                        disabled={isLoading}
                                        required
                                    />
                                </div>

                                <div className="mb-3">
                                    <label htmlFor="writer" className="form-label">작성자 *</label>
                                    <input 
                                        type="text" 
                                        id="writer"
                                        name="writer" 
                                        className="form-control"
                                        value={formData.writer}
                                        onChange={handleInputChange}
                                        placeholder="작성자를 입력하세요"
                                        disabled={isLoading}
                                        required
                                    />
                                </div>

                                <div className="mb-4">
                                    <label htmlFor="contents" className="form-label">내용 *</label>
                                    <textarea 
                                        id="contents"
                                        name="contents" 
                                        className="form-control"
                                        rows="8"
                                        value={formData.contents}
                                        onChange={handleInputChange}
                                        placeholder="내용을 입력하세요"
                                        disabled={isLoading}
                                        required
                                    />
                                </div>

                                <div className="d-flex justify-content-end gap-2">
                                    <Link 
                                        to="/board/list" 
                                        className="btn btn-outline-secondary"
                                        style={{ display: isLoading ? 'none' : 'inline-block' }}
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

export default BoardWrite;