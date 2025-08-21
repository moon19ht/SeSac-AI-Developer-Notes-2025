import { useState, useCallback } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

function Counter() {
  const [count, setCount] = useState(0);

  // 카운터 증가 함수 - useCallback으로 최적화
  const handleIncrement = useCallback(() => {
    setCount(prevCount => prevCount + 1);
  }, []);

  // 카운터 감소 함수 - useCallback으로 최적화
  const handleDecrement = useCallback(() => {
    setCount(prevCount => prevCount - 1);
  }, []);

  // 카운터 초기화 함수
  const handleReset = useCallback(() => {
    setCount(0);
  }, []);

  return (
    <div className="container mt-4">
      <div className="row justify-content-center">
        <div className="col-md-6">
          <div className="card">
            <div className="card-header text-center">
              <h1 className="mb-0">카운터</h1>
            </div>
            <div className="card-body text-center">
              <h2 className="display-4 mb-4 text-primary">{count}</h2>
              <div className="d-grid gap-2 d-md-flex justify-content-md-center">
                <button 
                  type="button" 
                  className="btn btn-success me-md-2"
                  onClick={handleIncrement}
                  aria-label="카운터 증가"
                >
                  증가 (+1)
                </button>
                <button 
                  type="button" 
                  className="btn btn-danger me-md-2"
                  onClick={handleDecrement}
                  aria-label="카운터 감소"
                >
                  감소 (-1)
                </button>
                <button 
                  type="button" 
                  className="btn btn-secondary"
                  onClick={handleReset}
                  aria-label="카운터 초기화"
                >
                  초기화
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Counter;