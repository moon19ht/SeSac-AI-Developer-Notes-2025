# 🧠 Deep Learning 완전 정복 가이드

##### 📝 Writer : Moon19ht

---

## 목차

1. [파이썬 기초 및 개발환경 설정](#1-파이썬-기초-및-개발환경-설정)
2. [웹 프로그래밍 기초](#2-웹-프로그래밍-기초)
3. [웹 크롤링](#3-웹-크롤링)
4. [통계학 기초](#4-통계학-기초)
5. [수학 라이브러리 활용](#5-수학-라이브러리-활용)
6. [이미지 처리](#6-이미지-처리)
7. [머신러닝 기초](#7-머신러닝-기초)
8. [딥러닝 핵심 개념](#8-딥러닝-핵심-개념)
9. [신경망 구조](#9-신경망-구조)
10. [CNN (합성곱 신경망)](#10-cnn-합성곱-신경망)
11. [RNN (순환 신경망)](#11-rnn-순환-신경망)
12. [고급 딥러닝 기법](#12-고급-딥러닝-기법)
13. [모델 평가 및 최적화](#13-모델-평가-및-최적화)
14. [실전 프로젝트](#14-실전-프로젝트)

---

## 1. 파이썬 기초 및 개발환경 설정

### 1.1 파이썬 소개

**파이썬(Python)**은 1991년 귀도 반 로썸(Guido van Rossum)이 발표한 인터프리터 언어입니다.

#### 파이썬의 특징
- **가독성**: 간결하고 읽기 쉬운 코드
- **들여쓰기**: 코드 블록을 들여쓰기로 구분
- **풍부한 라이브러리**: 다양한 분야의 라이브러리 제공
- **동적 타이핑**: 런타임에 타입 결정
- **무료**: 오픈소스 라이센스
- **접착성**: C언어와의 결합이 용이
- **크로스 플랫폼**: Windows, macOS, Linux 지원

#### 파이썬의 활용 분야
- 시스템 유틸리티 제작
- GUI 프로그래밍
- 웹 프로그래밍 (Django, Flask, FastAPI)
- 데이터 분석 및 시각화
- 머신러닝 및 딥러닝
- 크롤링 및 자동화
- IoT 및 임베디드 시스템
- 게임 개발
- 블록체인 개발

> **참고**: 파이썬은 학습하기 쉽고 강력한 기능을 제공하여 데이터 과학 분야에서 가장 인기 있는 언어입니다.

### 1.2 개발환경 설정

#### Anaconda 설치 및 설정
1. [Anaconda 공식 사이트](https://www.anaconda.com/download)에서 운영체제에 맞는 버전 다운로드
2. 설치 시 "Add Anaconda to PATH" 옵션 체크 (권장)
3. 설치 완료 후 Anaconda Prompt 또는 터미널 실행

#### 가상환경 생성 및 관리
```bash
# 가상환경 생성 (Python 3.9 권장)
conda create --name deeplearning python=3.9

# 가상환경 활성화
conda activate deeplearning

# 가상환경 비활성화
conda deactivate

# 가상환경 목록 확인
conda env list

# 가상환경 삭제
conda remove --name deeplearning --all
```

#### 필수 라이브러리 설치
```bash
# 기본 데이터 과학 라이브러리
conda install numpy pandas matplotlib seaborn scikit-learn

# 딥러닝 프레임워크
pip install tensorflow
pip install torch torchvision torchaudio

# 추가 유용한 라이브러리
pip install jupyter jupyterlab
pip install opencv-python
pip install pillow
pip install requests beautifulsoup4
pip install plotly
pip install streamlit
```

#### GPU 지원 설정 (선택사항)
```bash
# NVIDIA GPU 드라이버 확인
nvidia-smi

# CUDA 버전 확인
nvcc --version

# PyTorch GPU 버전 설치 (CUDA 11.8 기준)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# TensorFlow GPU 버전 (TensorFlow 2.10+ 자동 GPU 지원)
pip install tensorflow[and-cuda]
```

#### 설치 확인
```python
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import torch

print(f"Python 버전: {sys.version}")
print(f"NumPy 버전: {np.__version__}")
print(f"Pandas 버전: {pd.__version__}")
print(f"TensorFlow 버전: {tf.__version__}")
print(f"PyTorch 버전: {torch.__version__}")

# GPU 사용 가능 여부 확인
print(f"TensorFlow GPU 사용 가능: {tf.config.list_physical_devices('GPU')}")
print(f"PyTorch GPU 사용 가능: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"GPU 장치명: {torch.cuda.get_device_name(0)}")
```

### 1.3 개발 도구 설정

#### Visual Studio Code 설정
1. **Python 확장팩 설치**
   - Python (Microsoft)
   - Pylance
   - Python Docstring Generator
   - autoDocstring

2. **작업 환경 설정**
   ```json
   // settings.json
   {
       "python.defaultInterpreterPath": "~/anaconda3/envs/deeplearning/bin/python",
       "python.linting.enabled": true,
       "python.linting.pylintEnabled": true,
       "python.formatting.provider": "black",
       "python.terminal.activateEnvironment": true
   }
   ```

3. **유용한 단축키**
   - `Ctrl + Shift + P`: 명령 팔레트
   - `Ctrl + /`: 주석 토글
   - `Shift + Alt + F`: 코드 포맷팅
   - `F5`: 디버깅 시작

#### Jupyter Notebook/Lab 설정
```bash
# Jupyter 확장 설치
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user

# JupyterLab 확장
pip install jupyterlab-git
pip install jupyterlab-lsp
pip install python-lsp-server[all]

# Jupyter 시작
jupyter notebook  # 기본 노트북
jupyter lab      # JupyterLab (권장)
```

**주요 단축키**:
- `Shift + Enter`: 셀 실행 후 다음 셀로 이동
- `Ctrl + Enter`: 셀 실행
- `Alt + Enter`: 셀 실행 후 새 셀 추가
- `A`: 위에 새 셀 추가
- `B`: 아래에 새 셀 추가
- `DD`: 셀 삭제
- `M`: 마크다운 셀로 변경
- `Y`: 코드 셀로 변경

#### 프로젝트 구조 설정
```
deeplearning_project/
├── data/
│   ├── raw/           # 원본 데이터
│   ├── processed/     # 전처리된 데이터
│   └── external/      # 외부 데이터
├── notebooks/         # Jupyter 노트북
├── src/              # 소스 코드
│   ├── data/         # 데이터 처리
│   ├── features/     # 특성 엔지니어링
│   ├── models/       # 모델 정의
│   └── visualization/ # 시각화
├── models/           # 저장된 모델
├── reports/          # 보고서
├── requirements.txt  # 의존성 목록
└── README.md        # 프로젝트 설명
```

---

## 2. 웹 프로그래밍 기초

### 2.1 Flask 기초

Flask는 Python으로 만들어진 마이크로 웹 프레임워크로, 간단하고 유연한 웹 애플리케이션 개발에 적합합니다.

#### 설치 및 기본 사용법
```bash
pip install flask flask-cors flask-restful
```

```python
# app.py
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # CORS 설정으로 브라우저에서 접근 가능

@app.route("/")
def home():
    return jsonify({
        "message": "딥러닝 API 서버에 오신 것을 환영합니다!",
        "status": "success"
    })

@app.route("/health")
def health_check():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
```

#### 라우팅과 HTTP 메서드
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# GET 요청
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({"users": ["Alice", "Bob", "Charlie"]})

# POST 요청
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "이름이 필요합니다"}), 400
    
    return jsonify({
        "message": f"사용자 {data['name']}가 생성되었습니다",
        "user": data
    }), 201

# 경로 매개변수
@app.route('/users/<int:user_id>')
def get_user(user_id):
    return jsonify({"user_id": user_id, "name": f"User{user_id}"})

# 쿼리 매개변수
@app.route('/search')
def search():
    query = request.args.get('q', '')
    limit = request.args.get('limit', 10, type=int)
    
    return jsonify({
        "query": query,
        "limit": limit,
        "results": []
    })
```

> **참고**: `debug=True` 옵션을 사용하면 코드 변경 시 자동으로 서버가 재시작되어 개발이 편리합니다.

### 2.2 RESTful API 설계

```python
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import uuid
from datetime import datetime

app = Flask(__name__)
api = Api(app)

# 메모리 저장소 (실제로는 데이터베이스 사용)
models = {}

class ModelResource(Resource):
    def get(self, model_id=None):
        if model_id:
            if model_id in models:
                return models[model_id]
            return {"error": "모델을 찾을 수 없습니다"}, 404
        return {"models": list(models.values())}
    
    def post(self):
        data = request.get_json()
        
        # 입력 검증
        required_fields = ['name', 'type', 'accuracy']
        for field in required_fields:
            if field not in data:
                return {"error": f"{field}는 필수 항목입니다"}, 400
        
        # 모델 생성
        model_id = str(uuid.uuid4())
        model = {
            "id": model_id,
            "name": data['name'],
            "type": data['type'],
            "accuracy": data['accuracy'],
            "created_at": datetime.now().isoformat(),
            "status": "active"
        }
        
        models[model_id] = model
        return model, 201
    
    def put(self, model_id):
        if model_id not in models:
            return {"error": "모델을 찾을 수 없습니다"}, 404
        
        data = request.get_json()
        models[model_id].update(data)
        models[model_id]["updated_at"] = datetime.now().isoformat()
        
        return models[model_id]
    
    def delete(self, model_id):
        if model_id not in models:
            return {"error": "모델을 찾을 수 없습니다"}, 404
        
        del models[model_id]
        return {"message": "모델이 삭제되었습니다"}

# 라우트 등록
api.add_resource(ModelResource, '/api/models', '/api/models/<string:model_id>')

if __name__ == '__main__':
    app.run(debug=True)
```

---

## 3. 웹 크롤링

### 3.1 크롤링 기초 개념

웹 크롤링은 웹상의 데이터를 자동으로 수집하는 기술로, 머신러닝 프로젝트에서 데이터 수집에 널리 사용됩니다.

#### 크롤링 vs 스크래핑
- **크롤링**: 웹사이트를 체계적으로 탐색하여 링크를 따라가며 데이터 수집
- **스크래핑**: 특정 웹페이지에서 원하는 데이터만 추출

#### 법적/윤리적 고려사항
- robots.txt 파일 확인 및 준수
- 웹사이트 이용약관 검토
- 적절한 요청 간격 유지 (서버 부하 방지)
- 저작권 및 개인정보 보호 준수

#### 필요한 라이브러리 설치
```bash
pip install requests beautifulsoup4 selenium lxml
pip install pandas numpy matplotlib
```

### 3.2 Requests와 BeautifulSoup

#### 기본 HTTP 요청
```python
import requests
from bs4 import BeautifulSoup
import time
import random

def make_request(url, headers=None, timeout=10):
    """안전한 HTTP 요청 함수"""
    default_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    if headers:
        default_headers.update(headers)
    
    try:
        response = requests.get(url, headers=default_headers, timeout=timeout)
        response.raise_for_status()  # HTTP 오류 발생 시 예외 발생
        return response
    except requests.RequestException as e:
        print(f"요청 실패: {e}")
        return None

# 사용 예제
url = 'https://httpbin.org/html'
response = make_request(url)

if response:
    print(f"상태 코드: {response.status_code}")
    print(f"응답 헤더: {response.headers}")
    print(f"콘텐츠 타입: {response.headers.get('content-type')}")
```

#### BeautifulSoup을 이용한 HTML 파싱
```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_quotes():
    """명언 사이트에서 데이터 수집 예제"""
    base_url = "http://quotes.toscrape.com"
    quotes_data = []
    page = 1
    
    while True:
        url = f"{base_url}/page/{page}/"
        response = make_request(url)
        
        if not response:
            break
            
        soup = BeautifulSoup(response.content, 'html.parser')
        quotes = soup.find_all('div', class_='quote')
        
        if not quotes:  # 더 이상 명언이 없으면 종료
            break
        
        for quote in quotes:
            text = quote.find('span', class_='text').get_text()
            author = quote.find('small', class_='author').get_text()
            tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
            
            quotes_data.append({
                'text': text,
                'author': author,
                'tags': ', '.join(tags)
            })
        
        print(f"페이지 {page} 완료: {len(quotes)}개 명언 수집")
        page += 1
        
        # 서버 부하 방지를 위한 지연
        time.sleep(random.uniform(1, 3))
    
    return pd.DataFrame(quotes_data)

# 데이터 수집 및 저장
quotes_df = scrape_quotes()
print(f"총 {len(quotes_df)}개의 명언을 수집했습니다.")
quotes_df.to_csv('quotes.csv', index=False, encoding='utf-8')
```

> **참고**: 웹 크롤링 시 robots.txt를 확인하고 서버에 과도한 부하를 주지 않도록 적절한 지연 시간을 두세요.

### 3.3 Selenium을 이용한 동적 웹페이지 크롤링

JavaScript가 많이 사용된 동적 웹페이지나 사용자 상호작용이 필요한 경우 Selenium을 사용합니다.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def setup_driver(headless=True):
    """Chrome 드라이버 설정"""
    chrome_options = Options()
    
    if headless:
        chrome_options.add_argument("--headless")  # 브라우저 창 숨김
    
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    
    # User-Agent 설정
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
    
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def scrape_dynamic_content():
    """동적 콘텐츠 크롤링 예제"""
    driver = setup_driver(headless=False)
    
    try:
        # 페이지 로드
        driver.get("https://example.com")
        
        # 특정 요소가 로드될 때까지 대기
        wait = WebDriverWait(driver, 10)
        element = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "content"))
        )
        
        # 요소 찾기 (다양한 방법)
        title = driver.find_element(By.TAG_NAME, "h1").text
        links = driver.find_elements(By.TAG_NAME, "a")
        
        # 스크롤 (무한 스크롤 페이지의 경우)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        
        # 클릭 이벤트
        button = driver.find_element(By.ID, "load-more")
        if button.is_enabled():
            button.click()
            time.sleep(2)
        
        # 폼 입력
        search_box = driver.find_element(By.NAME, "search")
        search_box.send_keys("딥러닝")
        search_box.submit()
        
        # 결과 대기
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "results")))
        
        return {"title": title, "links": [link.get_attribute("href") for link in links]}
        
    except Exception as e:
        print(f"크롤링 중 오류 발생: {e}")
        return None
        
    finally:
        driver.quit()

# 사용 예제
result = scrape_dynamic_content()
if result:
    print(f"제목: {result['title']}")
    print(f"링크 수: {len(result['links'])}")
``` 

---

## 4. 통계학 기초

### 4.1 통계학의 필요성

데이터 분석과 머신러닝에서 통계학은 필수적인 기초 지식입니다. 데이터의 특성을 이해하고, 모델의 성능을 평가하며, 결과를 해석하는 데 통계학적 지식이 필요합니다.

#### 통계학의 분류
- **기술통계학(Descriptive Statistics)**: 데이터의 정리, 요약, 시각화
- **추론통계학(Inferential Statistics)**: 표본을 통한 모집단의 특성 추정

#### 모집단과 표본
- **모집단(Population)**: 연구 대상이 되는 전체 집단
- **표본(Sample)**: 모집단에서 선택된 일부 개체들
- **모수(Parameter)**: 모집단의 특성값 (μ, σ 등)
- **통계량(Statistic)**: 표본의 특성값 (x̄, s 등)

### 4.2 대표값과 산포도

#### 중심경향성 측도
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# 샘플 데이터 생성
np.random.seed(42)
data = np.random.normal(100, 15, 1000)  # 평균 100, 표준편차 15
data_with_outliers = np.append(data, [150, 160, 170])  # 이상치 추가

def calculate_central_tendency(data):
    """중심경향성 측도 계산"""
    return {
        '산술평균': np.mean(data),
        '중위값': np.median(data),
        '최빈값': stats.mode(data, keepdims=True)[0][0],
        '기하평균': stats.gmean(data[data > 0]),  # 양수만
        '조화평균': stats.hmean(data[data > 0])   # 양수만
    }

# 정상 데이터와 이상치 포함 데이터 비교
normal_stats = calculate_central_tendency(data)
outlier_stats = calculate_central_tendency(data_with_outliers)

print("정상 데이터:")
for key, value in normal_stats.items():
    print(f"  {key}: {value:.2f}")

print("\n이상치 포함 데이터:")
for key, value in outlier_stats.items():
    print(f"  {key}: {value:.2f}")
```

#### 산포도 측도
```python
def calculate_dispersion(data):
    """산포도 측도 계산"""
    return {
        '범위': np.max(data) - np.min(data),
        '분산': np.var(data, ddof=1),  # 표본분산
        '표준편차': np.std(data, ddof=1),  # 표본표준편차
        '변동계수': np.std(data, ddof=1) / np.mean(data) * 100,
        '사분위범위': np.percentile(data, 75) - np.percentile(data, 25),
        '평균절대편차': np.mean(np.abs(data - np.mean(data)))
    }

dispersion_stats = calculate_dispersion(data)
print("산포도 측도:")
for key, value in dispersion_stats.items():
    print(f"  {key}: {value:.2f}")
```

#### 분포의 형태
```python
def analyze_distribution_shape(data):
    """분포의 형태 분석"""
    return {
        '왜도(Skewness)': stats.skew(data),      # 비대칭성
        '첨도(Kurtosis)': stats.kurtosis(data),  # 뾰족함
        '정규성 검정(p-value)': stats.normaltest(data)[1]
    }

shape_stats = analyze_distribution_shape(data)
print("분포의 형태:")
for key, value in shape_stats.items():
    print(f"  {key}: {value:.4f}")

# 정규성 해석
if shape_stats['정규성 검정(p-value)'] > 0.05:
    print("  -> 정규분포를 따른다고 볼 수 있습니다 (α=0.05)")
else:
    print("  -> 정규분포를 따르지 않습니다 (α=0.05)")
```

### 4.3 확률분포

#### 주요 확률분포
```python
import matplotlib.pyplot as plt
from scipy.stats import norm, binom, poisson, uniform

# 한글 폰트 설정 (크로스 플랫폼 대응)
try:
    # Windows
    plt.rcParams['font.family'] = 'Malgun Gothic'
except:
    try:
        # macOS
        plt.rcParams['font.family'] = 'AppleGothic'
    except:
        # Linux 또는 기타
        plt.rcParams['font.family'] = 'DejaVu Sans'

plt.rcParams['axes.unicode_minus'] = False

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 정규분포
x = np.linspace(-4, 4, 1000)
axes[0, 0].plot(x, norm.pdf(x, 0, 1), 'b-', label='N(0,1)')
axes[0, 0].plot(x, norm.pdf(x, 0, 2), 'r-', label='N(0,2)')
axes[0, 0].set_title('정규분포')
axes[0, 0].legend()
axes[0, 0].grid(True)

# 이항분포
n, p = 20, 0.3
x_binom = np.arange(0, n+1)
axes[0, 1].bar(x_binom, binom.pmf(x_binom, n, p), alpha=0.7)
axes[0, 1].set_title(f'이항분포 B({n}, {p})')
axes[0, 1].grid(True)

# 포아송분포
lam = 3
x_poisson = np.arange(0, 15)
axes[1, 0].bar(x_poisson, poisson.pmf(x_poisson, lam), alpha=0.7, color='green')
axes[1, 0].set_title(f'포아송분포 Po({lam})')
axes[1, 0].grid(True)

# 균등분포
a, b = 0, 5
x_uniform = np.linspace(a-1, b+1, 1000)
axes[1, 1].plot(x_uniform, uniform.pdf(x_uniform, a, b-a), 'purple', linewidth=2)
axes[1, 1].set_title(f'균등분포 U({a}, {b})')
axes[1, 1].grid(True)

plt.tight_layout()
plt.show()
```

### 4.4 가설검정

```python
from scipy.stats import ttest_1samp, ttest_ind, chi2_contingency

def perform_hypothesis_tests():
    """다양한 가설검정 예제"""
    
    # 1. 일표본 t-검정
    sample = np.random.normal(100, 15, 50)
    t_stat, p_value = ttest_1samp(sample, 95)
    
    print("1. 일표본 t-검정 (H0: μ = 95)")
    print(f"   t-통계량: {t_stat:.4f}")
    print(f"   p-값: {p_value:.4f}")
    print(f"   결론: {'H0 기각' if p_value < 0.05 else 'H0 채택'} (α=0.05)")
    
    # 2. 이표본 t-검정
    group1 = np.random.normal(100, 15, 50)
    group2 = np.random.normal(105, 15, 50)
    t_stat, p_value = ttest_ind(group1, group2)
    
    print("\n2. 이표본 t-검정 (H0: μ1 = μ2)")
    print(f"   t-통계량: {t_stat:.4f}")
    print(f"   p-값: {p_value:.4f}")
    print(f"   결론: {'두 그룹 평균에 차이 있음' if p_value < 0.05 else '두 그룹 평균에 차이 없음'} (α=0.05)")
    
    # 3. 카이제곱 독립성 검정
    observed = np.array([[10, 10, 20], [20, 20, 40]])
    chi2_stat, p_value, dof, expected = chi2_contingency(observed)
    
    print("\n3. 카이제곱 독립성 검정")
    print(f"   카이제곱 통계량: {chi2_stat:.4f}")
    print(f"   p-값: {p_value:.4f}")
    print(f"   자유도: {dof}")
    print(f"   결론: {'변수들이 독립적이지 않음' if p_value < 0.05 else '변수들이 독립적임'} (α=0.05)")

perform_hypothesis_tests()
```

> **참고**: 가설검정에서 p-값은 귀무가설이 참일 때 관찰된 결과 또는 더 극단적인 결과가 나올 확률입니다.

---

## 5. 수학 라이브러리 활용

### 5.1 NumPy 심화

NumPy는 다차원 배열과 수학 연산을 효율적으로 처리하는 라이브러리로, 딥러닝의 기초가 됩니다.

#### 배열 생성과 조작
```python
import numpy as np

# 다양한 배열 생성 방법
def create_arrays():
    """다양한 NumPy 배열 생성 예제"""
    
    # 기본 배열
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([[1, 2], [3, 4], [5, 6]])
    
    # 특수 배열
    zeros = np.zeros((3, 4), dtype=np.float32)
    ones = np.ones((2, 3), dtype=np.int32)
    identity = np.eye(4)  # 단위행렬
    diagonal = np.diag([1, 2, 3, 4])  # 대각행렬
    
    # 범위 배열
    arange = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
    linspace = np.linspace(0, 1, 11)  # 0부터 1까지 11개 균등분할
    logspace = np.logspace(0, 2, 5)  # 10^0부터 10^2까지 5개 로그스케일
    
    # 랜덤 배열
    np.random.seed(42)  # 재현 가능한 결과
    random_uniform = np.random.uniform(0, 1, (3, 3))
    random_normal = np.random.normal(0, 1, (3, 3))
    random_int = np.random.randint(0, 10, (3, 3))
    
    return {
        'basic': (arr1, arr2),
        'special': (zeros, ones, identity, diagonal),
        'range': (arange, linspace, logspace),
        'random': (random_uniform, random_normal, random_int)
    }

arrays = create_arrays()
print("배열 생성 완료")
```

#### 배열 연산과 브로드캐스팅
```python
def array_operations():
    """배열 연산 예제"""
    
    # 기본 연산
    a = np.array([1, 2, 3, 4])
    b = np.array([5, 6, 7, 8])
    
    print("기본 연산:")
    print(f"덧셈: {a + b}")
    print(f"뺄셈: {a - b}")
    print(f"곱셈: {a * b}")  # 요소별 곱셈
    print(f"나눗셈: {a / b}")
    print(f"거듭제곱: {a ** 2}")
    
    # 행렬 연산
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    
    print("\n행렬 연산:")
    print(f"행렬 곱셈:\n{np.dot(A, B)}")
    print(f"또는:\n{A @ B}")
    print(f"전치행렬:\n{A.T}")
    print(f"역행렬:\n{np.linalg.inv(A)}")
    print(f"행렬식: {np.linalg.det(A)}")
    
    # 브로드캐스팅
    print("\n브로드캐스팅:")
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    vector = np.array([1, 0, 1])
    
    print(f"원본 행렬:\n{matrix}")
    print(f"벡터: {vector}")
    print(f"브로드캐스팅 결과:\n{matrix + vector}")

array_operations()
```

#### 고급 인덱싱과 슬라이싱
```python
def advanced_indexing():
    """고급 인덱싱 예제"""
    
    # 2D 배열 생성
    arr = np.arange(24).reshape(4, 6)
    print(f"원본 배열:\n{arr}")
    
    # 기본 슬라이싱
    print(f"\n첫 두 행: \n{arr[:2]}")
    print(f"마지막 두 열: \n{arr[:, -2:]}")
    print(f"2행 3열부터 4행 5열까지: \n{arr[1:3, 2:5]}")
    
    # 불린 인덱싱
    mask = arr > 10
    print(f"\n10보다 큰 요소들: {arr[mask]}")
    
    # 팬시 인덱싱
    indices = [0, 2, 3]
    print(f"0, 2, 3번 행: \n{arr[indices]}")
    
    # 조건부 선택
    even_elements = arr[arr % 2 == 0]
    print(f"짝수 요소들: {even_elements}")

advanced_indexing()
```

### 5.2 Pandas 심화

Pandas는 구조화된 데이터 분석을 위한 고수준 라이브러리입니다.

#### DataFrame 고급 조작
```python
import pandas as pd
import numpy as np

def create_sample_dataframe():
    """샘플 데이터프레임 생성"""
    np.random.seed(42)
    
    data = {
        'name': ['김철수', '이영희', '박민수', '최지영', '정호준'] * 20,
        'age': np.random.randint(20, 60, 100),
        'city': np.random.choice(['서울', '부산', '대구', '인천', '광주'], 100),
        'salary': np.random.normal(50000, 15000, 100),
        'department': np.random.choice(['IT', '마케팅', '영업', '인사'], 100),
        'experience': np.random.randint(0, 20, 100),
        'performance': np.random.uniform(0.5, 1.0, 100)
    }
    
    df = pd.DataFrame(data)
    df['salary'] = df['salary'].round(0).astype(int)
    df['performance'] = df['performance'].round(3)
    
    return df

def dataframe_operations():
    """DataFrame 고급 조작 예제"""
    df = create_sample_dataframe()
    
    print("데이터프레임 기본 정보:")
    print(df.info())
    print(f"\n기술통계:\n{df.describe()}")
    
    # 그룹화와 집계
    print("\n부서별 평균 연봉:")
    dept_salary = df.groupby('department')['salary'].agg(['mean', 'std', 'count'])
    print(dept_salary)
    
    # 다중 그룹화
    print("\n부서별, 도시별 평균 성과:")
    multi_group = df.groupby(['department', 'city'])['performance'].mean().unstack()
    print(multi_group)
    
    # 피벗 테이블
    print("\n피벗 테이블 (부서 x 도시별 평균 연봉):")
    pivot = pd.pivot_table(df, values='salary', index='department', 
                          columns='city', aggfunc='mean', fill_value=0)
    print(pivot)
    
    # 조건부 필터링
    high_performers = df[(df['performance'] > 0.8) & (df['experience'] > 5)]
    print(f"\n고성과자 (성과 > 0.8, 경력 > 5년): {len(high_performers)}명")
    
    return df

df = dataframe_operations()
```

#### 데이터 전처리
```python
def data_preprocessing(df):
    """데이터 전처리 예제"""
    
    # 결측값 처리
    df_copy = df.copy()
    
    # 인위적으로 결측값 생성
    np.random.seed(42)
    missing_indices = np.random.choice(df_copy.index, size=10, replace=False)
    df_copy.loc[missing_indices, 'salary'] = np.nan
    
    print("결측값 확인:")
    print(df_copy.isnull().sum())
    
    # 결측값 처리 방법들
    df_copy['salary_filled_mean'] = df_copy['salary'].fillna(df_copy['salary'].mean())
    df_copy['salary_filled_median'] = df_copy['salary'].fillna(df_copy['salary'].median())
    df_copy['salary_filled_forward'] = df_copy['salary'].fillna(method='ffill')
    
    # 이상치 탐지 (IQR 방법)
    Q1 = df_copy['salary'].quantile(0.25)
    Q3 = df_copy['salary'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = df_copy[(df_copy['salary'] < lower_bound) | (df_copy['salary'] > upper_bound)]
    print(f"\n이상치 개수: {len(outliers)}")
    
    # 범주형 변수 인코딩
    df_encoded = pd.get_dummies(df_copy, columns=['city', 'department'], prefix=['city', 'dept'])
    
    print(f"\n원본 컬럼 수: {len(df_copy.columns)}")
    print(f"인코딩 후 컬럼 수: {len(df_encoded.columns)}")
    
    return df_encoded

df_processed = data_preprocessing(df)
```

### 5.3 Matplotlib과 Seaborn 시각화

#### 고급 시각화 기법
```python
import matplotlib.pyplot as plt
import seaborn as sns

def advanced_visualization(df):
    """고급 시각화 예제"""
    
    # 스타일 설정
    plt.style.use('seaborn-v0_8')
    sns.set_palette("husl")
    
    # 서브플롯 생성
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    fig.suptitle('직원 데이터 분석 대시보드', fontsize=16, fontweight='bold')
    
    # 1. 연봉 분포 히스토그램
    axes[0, 0].hist(df['salary'], bins=30, alpha=0.7, color='skyblue', edgecolor='black')
    axes[0, 0].axvline(df['salary'].mean(), color='red', linestyle='--', 
                      label=f'평균: {df["salary"].mean():.0f}')
    axes[0, 0].set_title('연봉 분포')
    axes[0, 0].set_xlabel('연봉')
    axes[0, 0].set_ylabel('빈도')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)
    
    # 2. 부서별 연봉 박스플롯
    sns.boxplot(data=df, x='department', y='salary', ax=axes[0, 1])
    axes[0, 1].set_title('부서별 연봉 분포')
    axes[0, 1].tick_params(axis='x', rotation=45)
    
    # 3. 경력과 연봉의 산점도
    scatter = axes[0, 2].scatter(df['experience'], df['salary'], 
                                c=df['performance'], cmap='viridis', alpha=0.6)
    axes[0, 2].set_title('경력 vs 연봉 (성과별 색상)')
    axes[0, 2].set_xlabel('경력 (년)')
    axes[0, 2].set_ylabel('연봉')
    plt.colorbar(scatter, ax=axes[0, 2], label='성과')
    
    # 4. 도시별 직원 수
    city_counts = df['city'].value_counts()
    axes[1, 0].pie(city_counts.values, labels=city_counts.index, autopct='%1.1f%%')
    axes[1, 0].set_title('도시별 직원 분포')
    
    # 5. 상관관계 히트맵
    numeric_cols = ['age', 'salary', 'experience', 'performance']
    corr_matrix = df[numeric_cols].corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, 
                ax=axes[1, 1], square=True)
    axes[1, 1].set_title('변수 간 상관관계')
    
    # 6. 나이대별 성과 분포
    df['age_group'] = pd.cut(df['age'], bins=[20, 30, 40, 50, 60], 
                            labels=['20대', '30대', '40대', '50대'])
    sns.violinplot(data=df, x='age_group', y='performance', ax=axes[1, 2])
    axes[1, 2].set_title('나이대별 성과 분포')
    
    plt.tight_layout()
    plt.show()
    
    # 추가: 인터랙티브 플롯 (plotly 사용)
    try:
        import plotly.express as px
        import plotly.graph_objects as go
        from plotly.subplots import make_subplots
        
        # 3D 산점도
        fig_3d = px.scatter_3d(df, x='age', y='experience', z='salary',
                              color='department', size='performance',
                              title='3D 산점도: 나이, 경력, 연봉')
        fig_3d.show()
        
    except ImportError:
        print("Plotly가 설치되지 않았습니다. pip install plotly로 설치하세요.")

advanced_visualization(df)
```

> **참고**: 시각화는 데이터의 패턴을 발견하고 인사이트를 얻는 중요한 도구입니다. 목적에 맞는 적절한 차트 유형을 선택하세요. 

---

## 6. 이미지 처리

### 6.1 이미지 기초 개념

#### 디지털 이미지의 구조
- **픽셀(Pixel)**: 이미지의 최소 단위, Picture Element의 줄임말
- **해상도**: 이미지의 크기 (가로픽셀 × 세로픽셀)
- **비트 깊이**: 픽셀당 저장되는 비트 수 (8bit = 256 색상)
- **채널**: 색상 정보를 나타내는 차원 수

#### 주요 색공간
1. **그레이스케일**: 0(검정)~255(흰색)의 명도값 하나
2. **RGB**: Red, Green, Blue 각각 0~255 (3채널)
3. **HSV**: Hue(색상), Saturation(채도), Value(명도)
4. **CMYK**: Cyan, Magenta, Yellow, Black (인쇄용)

### 6.2 이미지 처리 라이브러리

#### OpenCV 기초
```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

def image_processing_basics():
    """OpenCV 기본 이미지 처리"""
    
    # 이미지 생성 (예제용)
    # 실제로는 cv2.imread('image_path.jpg')로 이미지 로드
    height, width = 300, 400
    
    # 그라디언트 이미지 생성
    img = np.zeros((height, width, 3), dtype=np.uint8)
    for i in range(height):
        img[i, :, 0] = int(255 * i / height)  # Red 채널
        img[i, :, 1] = int(255 * (1 - i / height))  # Green 채널
        img[i, :, 2] = 128  # Blue 채널 고정
    
    # 기본 정보 출력
    print(f"이미지 크기: {img.shape}")
    print(f"데이터 타입: {img.dtype}")
    print(f"최솟값: {img.min()}, 최댓값: {img.max()}")
    
    # 색공간 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # 시각화
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # 원본 이미지 (BGR -> RGB 변환)
    axes[0, 0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    axes[0, 0].set_title('원본 이미지')
    axes[0, 0].axis('off')
    
    # 그레이스케일
    axes[0, 1].imshow(gray, cmap='gray')
    axes[0, 1].set_title('그레이스케일')
    axes[0, 1].axis('off')
    
    # HSV 색공간
    axes[1, 0].imshow(cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB))
    axes[1, 0].set_title('HSV 색공간')
    axes[1, 0].axis('off')
    
    # 히스토그램
    axes[1, 1].hist(gray.flatten(), bins=50, alpha=0.7)
    axes[1, 1].set_title('그레이스케일 히스토그램')
    axes[1, 1].set_xlabel('픽셀 값')
    axes[1, 1].set_ylabel('빈도')
    
    plt.tight_layout()
    plt.show()
    
    return img, gray

# 이미지 처리 기본 함수 실행
original_img, gray_img = image_processing_basics()
```

#### Pillow (PIL) 사용법
```python
from PIL import Image, ImageFilter, ImageEnhance
import numpy as np

def pillow_image_processing():
    """Pillow를 이용한 이미지 처리"""
    
    # 샘플 이미지 생성 (실제로는 Image.open('path')로 로드)
    # 그라디언트 이미지 생성
    width, height = 400, 300
    img_array = np.zeros((height, width, 3), dtype=np.uint8)
    
    for i in range(height):
        for j in range(width):
            img_array[i, j] = [
                int(255 * j / width),      # Red
                int(255 * i / height),     # Green
                int(255 * (i + j) / (height + width))  # Blue
            ]
    
    img = Image.fromarray(img_array)
    
    # 이미지 정보
    print(f"이미지 크기: {img.size}")
    print(f"이미지 모드: {img.mode}")
    
    # 기본 변환
    resized = img.resize((200, 150))
    rotated = img.rotate(45, expand=True)
    cropped = img.crop((50, 50, 250, 200))
    
    # 필터 적용
    blurred = img.filter(ImageFilter.BLUR)
    sharpened = img.filter(ImageFilter.SHARPEN)
    edge_enhanced = img.filter(ImageFilter.EDGE_ENHANCE)
    
    # 색상 조정
    enhancer = ImageEnhance.Brightness(img)
    brighter = enhancer.enhance(1.5)  # 1.5배 밝게
    
    enhancer = ImageEnhance.Contrast(img)
    high_contrast = enhancer.enhance(2.0)  # 2배 대비
    
    # 시각화
    fig, axes = plt.subplots(3, 3, figsize=(15, 12))
    
    images = [
        (img, '원본'),
        (resized, '크기 변경'),
        (rotated, '회전'),
        (cropped, '자르기'),
        (blurred, '블러'),
        (sharpened, '샤프닝'),
        (edge_enhanced, '엣지 강화'),
        (brighter, '밝기 증가'),
        (high_contrast, '대비 증가')
    ]
    
    for i, (image, title) in enumerate(images):
        row, col = i // 3, i % 3
        axes[row, col].imshow(image)
        axes[row, col].set_title(title)
        axes[row, col].axis('off')
    
    plt.tight_layout()
    plt.show()
    
    return img

processed_img = pillow_image_processing()
```

### 6.3 이미지 전처리 기법

```python
def advanced_image_preprocessing():
    """고급 이미지 전처리 기법"""
    
    # 샘플 이미지 생성 (노이즈가 포함된 이미지)
    np.random.seed(42)
    clean_img = np.zeros((200, 200), dtype=np.float32)
    
    # 기하학적 패턴 생성
    center_x, center_y = 100, 100
    for i in range(200):
        for j in range(200):
            distance = np.sqrt((i - center_x)**2 + (j - center_y)**2)
            clean_img[i, j] = 255 * np.exp(-distance / 50)
    
    # 노이즈 추가
    noise = np.random.normal(0, 20, clean_img.shape)
    noisy_img = np.clip(clean_img + noise, 0, 255).astype(np.uint8)
    
    # 1. 노이즈 제거 필터
    # 가우시안 필터
    gaussian_filtered = cv2.GaussianBlur(noisy_img, (5, 5), 0)
    
    # 미디안 필터 (점 노이즈 제거에 효과적)
    median_filtered = cv2.medianBlur(noisy_img, 5)
    
    # 양방향 필터 (엣지 보존하면서 노이즈 제거)
    bilateral_filtered = cv2.bilateralFilter(noisy_img, 9, 75, 75)
    
    # 2. 엣지 검출
    # Canny 엣지 검출
    edges_canny = cv2.Canny(noisy_img, 50, 150)
    
    # Sobel 엣지 검출
    sobel_x = cv2.Sobel(noisy_img, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(noisy_img, cv2.CV_64F, 0, 1, ksize=3)
    sobel_combined = np.sqrt(sobel_x**2 + sobel_y**2)
    
    # 3. 모폴로지 연산
    kernel = np.ones((3, 3), np.uint8)
    
    # 침식과 팽창
    erosion = cv2.erode(noisy_img, kernel, iterations=1)
    dilation = cv2.dilate(noisy_img, kernel, iterations=1)
    
    # 열림과 닫힘
    opening = cv2.morphologyEx(noisy_img, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(noisy_img, cv2.MORPH_CLOSE, kernel)
    
    # 시각화
    fig, axes = plt.subplots(3, 4, figsize=(16, 12))
    
    images = [
        (clean_img.astype(np.uint8), '원본 (깨끗한 이미지)'),
        (noisy_img, '노이즈 추가'),
        (gaussian_filtered, '가우시안 필터'),
        (median_filtered, '미디안 필터'),
        (bilateral_filtered, '양방향 필터'),
        (edges_canny, 'Canny 엣지'),
        (sobel_combined.astype(np.uint8), 'Sobel 엣지'),
        (erosion, '침식'),
        (dilation, '팽창'),
        (opening, '열림'),
        (closing, '닫힘'),
        (np.zeros_like(noisy_img), '여유 공간')
    ]
    
    for i, (image, title) in enumerate(images):
        row, col = i // 4, i % 4
        if i < 11:  # 마지막 여유 공간 제외
            axes[row, col].imshow(image, cmap='gray')
        axes[row, col].set_title(title)
        axes[row, col].axis('off')
    
    plt.tight_layout()
    plt.show()

advanced_image_preprocessing()
```

> **참고**: 이미지 전처리는 딥러닝 모델의 성능에 큰 영향을 미칩니다. 데이터의 특성에 맞는 적절한 전처리 기법을 선택하세요.

---

## 7. 머신러닝 기초

### 7.1 머신러닝 개념과 분류

**머신러닝**은 명시적인 프로그래밍 없이 컴퓨터가 데이터로부터 패턴을 학습하여 예측이나 결정을 내리는 기술입니다.

#### AI, ML, DL의 관계
```
인공지능 (Artificial Intelligence)
├── 머신러닝 (Machine Learning)
│   ├── 딥러닝 (Deep Learning)
│   │   ├── CNN (Convolutional Neural Networks)
│   │   ├── RNN (Recurrent Neural Networks)
│   │   ├── Transformer
│   │   └── GAN (Generative Adversarial Networks)
│   ├── 의사결정트리 (Decision Tree)
│   ├── 서포트 벡터 머신 (SVM)
│   ├── 랜덤 포레스트 (Random Forest)
│   └── k-최근접 이웃 (k-NN)
├── 전문가 시스템 (Expert Systems)
└── 규칙 기반 시스템 (Rule-based Systems)
```

### 7.2 머신러닝 유형

#### 지도학습 (Supervised Learning)
입력(X)과 정답(y)이 모두 주어진 데이터로 학습하는 방법

**분류 (Classification)**
```python
from sklearn.datasets import make_classification, load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns

def classification_example():
    """분류 문제 예제"""
    
    # 데이터 로드
    iris = load_iris()
    X, y = iris.data, iris.target
    
    # 훈련/테스트 분할
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )
    
    # 여러 분류 모델 비교
    models = {
        'Logistic Regression': LogisticRegression(random_state=42),
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
        'SVM': SVC(kernel='rbf', random_state=42)
    }
    
    results = {}
    
    for name, model in models.items():
        # 모델 훈련
        model.fit(X_train, y_train)
        
        # 예측
        y_pred = model.predict(X_test)
        
        # 성능 평가
        from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
        
        results[name] = {
            'accuracy': accuracy_score(y_test, y_pred),
            'precision': precision_score(y_test, y_pred, average='weighted'),
            'recall': recall_score(y_test, y_pred, average='weighted'),
            'f1': f1_score(y_test, y_pred, average='weighted')
        }
        
        print(f"\n{name} 성능:")
        print(classification_report(y_test, y_pred, target_names=iris.target_names))
    
    # 결과 비교
    import pandas as pd
    results_df = pd.DataFrame(results).T
    print("\n모델 성능 비교:")
    print(results_df.round(4))
    
    # 혼동 행렬 시각화
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    
    for i, (name, model) in enumerate(models.items()):
        y_pred = model.predict(X_test)
        cm = confusion_matrix(y_test, y_pred)
        
        sns.heatmap(cm, annot=True, fmt='d', ax=axes[i], 
                   xticklabels=iris.target_names, 
                   yticklabels=iris.target_names)
        axes[i].set_title(f'{name} 혼동행렬')
        axes[i].set_xlabel('예측값')
        axes[i].set_ylabel('실제값')
    
    plt.tight_layout()
    plt.show()
    
    return models, results_df

models, performance = classification_example()
```

**회귀 (Regression)**
```python
from sklearn.datasets import make_regression, load_boston
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

def regression_example():
    """회귀 문제 예제"""
    
    # 합성 데이터 생성
    X, y = make_regression(n_samples=1000, n_features=10, noise=0.1, random_state=42)
    
    # 훈련/테스트 분할
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )
    
    # 여러 회귀 모델 비교
    models = {
        'Linear Regression': LinearRegression(),
        'Ridge Regression': Ridge(alpha=1.0),
        'Lasso Regression': Lasso(alpha=1.0),
        'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42)
    }
    
    results = {}
    predictions = {}
    
    for name, model in models.items():
        # 모델 훈련
        model.fit(X_train, y_train)
        
        # 예측
        y_pred = model.predict(X_test)
        predictions[name] = y_pred
        
        # 성능 평가
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        results[name] = {
            'MSE': mse,
            'RMSE': rmse,
            'MAE': mae,
            'R²': r2
        }
        
        print(f"\n{name} 성능:")
        print(f"  MSE: {mse:.4f}")
        print(f"  RMSE: {rmse:.4f}")
        print(f"  MAE: {mae:.4f}")
        print(f"  R²: {r2:.4f}")
    
    # 결과 비교
    results_df = pd.DataFrame(results).T
    print("\n모델 성능 비교:")
    print(results_df.round(4))
    
    # 예측 vs 실제값 시각화
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.ravel()
    
    for i, (name, y_pred) in enumerate(predictions.items()):
        axes[i].scatter(y_test, y_pred, alpha=0.6)
        axes[i].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
        axes[i].set_xlabel('실제값')
        axes[i].set_ylabel('예측값')
        axes[i].set_title(f'{name}\nR² = {results[name]["R²"]:.4f}')
        axes[i].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    return models, results_df

regression_models, regression_performance = regression_example()
```

#### 비지도학습 (Unsupervised Learning)
```python
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler

def unsupervised_learning_example():
    """비지도학습 예제"""
    
    # 클러스터링용 데이터 생성
    from sklearn.datasets import make_blobs
    X_cluster, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, 
                             random_state=42, n_features=2)
    
    # 1. 클러스터링
    clustering_models = {
        'K-Means': KMeans(n_clusters=4, random_state=42),
        'DBSCAN': DBSCAN(eps=0.5, min_samples=5),
        'Agglomerative': AgglomerativeClustering(n_clusters=4)
    }
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.ravel()
    
    # 원본 데이터
    axes[0].scatter(X_cluster[:, 0], X_cluster[:, 1], alpha=0.7)
    axes[0].set_title('원본 데이터')
    axes[0].grid(True, alpha=0.3)
    
    # 클러스터링 결과
    for i, (name, model) in enumerate(clustering_models.items()):
        labels = model.fit_predict(X_cluster)
        
        scatter = axes[i+1].scatter(X_cluster[:, 0], X_cluster[:, 1], 
                                   c=labels, cmap='viridis', alpha=0.7)
        axes[i+1].set_title(f'{name} 클러스터링')
        axes[i+1].grid(True, alpha=0.3)
        
        # 클러스터 중심점 표시 (K-Means의 경우)
        if hasattr(model, 'cluster_centers_'):
            centers = model.cluster_centers_
            axes[i+1].scatter(centers[:, 0], centers[:, 1], 
                            c='red', marker='x', s=200, linewidths=3)
    
    plt.tight_layout()
    plt.show()
    
    # 2. 차원 축소
    # 고차원 데이터 생성
    X_high_dim, y_high_dim = make_classification(n_samples=1000, n_features=20, 
                                                n_informative=10, n_redundant=10, 
                                                n_clusters_per_class=1, random_state=42)
    
    # 데이터 정규화
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_high_dim)
    
    # PCA
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    
    # t-SNE
    tsne = TSNE(n_components=2, random_state=42, perplexity=30)
    X_tsne = tsne.fit_transform(X_scaled)
    
    # 차원 축소 결과 시각화
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # PCA 결과
    scatter1 = axes[0].scatter(X_pca[:, 0], X_pca[:, 1], c=y_high_dim, cmap='viridis', alpha=0.7)
    axes[0].set_title(f'PCA 차원축소\n설명된 분산: {pca.explained_variance_ratio_.sum():.3f}')
    axes[0].set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.3f})')
    axes[0].set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.3f})')
    axes[0].grid(True, alpha=0.3)
    
    # t-SNE 결과
    scatter2 = axes[1].scatter(X_tsne[:, 0], X_tsne[:, 1], c=y_high_dim, cmap='viridis', alpha=0.7)
    axes[1].set_title('t-SNE 차원축소')
    axes[1].set_xlabel('t-SNE 1')
    axes[1].set_ylabel('t-SNE 2')
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    print(f"원본 데이터 차원: {X_high_dim.shape}")
    print(f"PCA 후 차원: {X_pca.shape}")
    print(f"주성분별 설명된 분산 비율: {pca.explained_variance_ratio_}")
    print(f"총 설명된 분산: {pca.explained_variance_ratio_.sum():.4f}")

unsupervised_learning_example()
```

### 7.3 모델 평가와 검증

```python
from sklearn.model_selection import cross_val_score, GridSearchCV, learning_curve
from sklearn.metrics import roc_curve, auc, precision_recall_curve

def model_evaluation_techniques():
    """모델 평가 기법들"""
    
    # 데이터 준비
    iris = load_iris()
    X, y = iris.data, iris.target
    
    # 이진 분류를 위해 클래스 2개만 사용
    binary_mask = y != 2
    X_binary = X[binary_mask]
    y_binary = y[binary_mask]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X_binary, y_binary, test_size=0.3, random_state=42, stratify=y_binary
    )
    
    # 1. 교차 검증
    model = RandomForestClassifier(random_state=42)
    cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
    
    print("교차 검증 결과:")
    print(f"  평균 정확도: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")
    print(f"  각 폴드 점수: {cv_scores}")
    
    # 2. 하이퍼파라미터 튜닝
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [3, 5, 7, None],
        'min_samples_split': [2, 5, 10]
    }
    
    grid_search = GridSearchCV(
        RandomForestClassifier(random_state=42),
        param_grid,
        cv=5,
        scoring='accuracy',
        n_jobs=-1
    )
    
    grid_search.fit(X_train, y_train)
    
    print(f"\n최적 하이퍼파라미터: {grid_search.best_params_}")
    print(f"최적 교차 검증 점수: {grid_search.best_score_:.4f}")
    
    # 3. 학습 곡선
    train_sizes, train_scores, val_scores = learning_curve(
        grid_search.best_estimator_, X_train, y_train,
        train_sizes=np.linspace(0.1, 1.0, 10),
        cv=5, scoring='accuracy'
    )
    
    # 학습 곡선 시각화
    plt.figure(figsize=(12, 8))
    
    plt.subplot(2, 2, 1)
    plt.plot(train_sizes, train_scores.mean(axis=1), 'o-', label='훈련 점수')
    plt.plot(train_sizes, val_scores.mean(axis=1), 'o-', label='검증 점수')
    plt.xlabel('훈련 데이터 크기')
    plt.ylabel('정확도')
    plt.title('학습 곡선')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # 4. ROC 곡선
    best_model = grid_search.best_estimator_
    y_prob = best_model.predict_proba(X_test)[:, 1]
    
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)
    
    plt.subplot(2, 2, 2)
    plt.plot(fpr, tpr, color='darkorange', lw=2, 
             label=f'ROC 곡선 (AUC = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('거짓 양성 비율')
    plt.ylabel('참 양성 비율')
    plt.title('ROC 곡선')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # 5. Precision-Recall 곡선
    precision, recall, _ = precision_recall_curve(y_test, y_prob)
    
    plt.subplot(2, 2, 3)
    plt.plot(recall, precision, color='blue', lw=2)
    plt.xlabel('재현율 (Recall)')
    plt.ylabel('정밀도 (Precision)')
    plt.title('Precision-Recall 곡선')
    plt.grid(True, alpha=0.3)
    
    # 6. 특성 중요도
    feature_importance = best_model.feature_importances_
    feature_names = iris.feature_names
    
    plt.subplot(2, 2, 4)
    indices = np.argsort(feature_importance)[::-1]
    plt.bar(range(len(feature_importance)), feature_importance[indices])
    plt.xticks(range(len(feature_importance)), 
               [feature_names[i] for i in indices], rotation=45)
    plt.title('특성 중요도')
    plt.ylabel('중요도')
    
    plt.tight_layout()
    plt.show()
    
    return grid_search.best_estimator_

best_model = model_evaluation_techniques()
```

> **참고**: 모델 평가는 단순히 정확도만으로 판단하지 말고, 문제의 특성에 맞는 다양한 지표를 종합적으로 고려해야 합니다.

---

## 8. 딥러닝 핵심 개념

### 8.1 딥러닝 소개

**딥러닝**은 인간의 뇌 구조를 모방한 인공신경망을 여러 층으로 깊게 쌓아 복잡한 패턴을 학습하는 머신러닝의 한 분야입니다.

#### 딥러닝의 특징
- **자동 특성 추출**: 수동으로 특성을 설계할 필요 없음
- **계층적 학습**: 저수준에서 고수준 특성까지 단계적 학습
- **대용량 데이터**: 많은 데이터에서 더 좋은 성능 발휘
- **GPU 활용**: 병렬 처리로 빠른 학습 가능
- **표현 학습**: 데이터의 내재된 구조를 자동으로 발견

#### 딥러닝 vs 전통적 머신러닝
```python
import matplotlib.pyplot as plt
import numpy as np

def compare_ml_vs_dl():
    """머신러닝 vs 딥러닝 비교 시각화"""
    
    # 데이터 양에 따른 성능 비교 (가상의 데이터)
    data_sizes = np.logspace(2, 6, 50)  # 100 ~ 1,000,000
    
    # 전통적 머신러닝 성능 (포화 곡선)
    ml_performance = 85 * (1 - np.exp(-data_sizes / 50000))
    
    # 딥러닝 성능 (지속적 증가)
    dl_performance = 95 * (1 - np.exp(-data_sizes / 200000)) + np.log(data_sizes) * 2
    dl_performance = np.clip(dl_performance, 0, 95)
    
    plt.figure(figsize=(12, 8))
    
    plt.subplot(2, 2, 1)
    plt.semilogx(data_sizes, ml_performance, 'b-', linewidth=2, label='전통적 머신러닝')
    plt.semilogx(data_sizes, dl_performance, 'r-', linewidth=2, label='딥러닝')
    plt.xlabel('데이터 크기')
    plt.ylabel('성능 (%)')
    plt.title('데이터 크기에 따른 성능 비교')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # 특성 추출 과정 비교
    plt.subplot(2, 2, 2)
    
    # 전통적 ML 파이프라인
    stages_ml = ['원시 데이터', '특성 추출\n(수동)', '머신러닝\n알고리즘', '결과']
    y_ml = [0.7, 0.7, 0.7, 0.7]
    
    # 딥러닝 파이프라인
    stages_dl = ['원시 데이터', '특성 추출\n(자동)', '딥러닝\n모델', '결과']
    y_dl = [0.3, 0.3, 0.3, 0.3]
    
    for i in range(len(stages_ml)-1):
        plt.arrow(i, y_ml[i], 0.8, 0, head_width=0.05, head_length=0.1, fc='blue', ec='blue')
        plt.arrow(i, y_dl[i], 0.8, 0, head_width=0.05, head_length=0.1, fc='red', ec='red')
    
    for i, stage in enumerate(stages_ml):
        plt.text(i, y_ml[i]+0.1, stage, ha='center', va='bottom', fontsize=9, color='blue')
        plt.text(i, y_dl[i]-0.1, stages_dl[i], ha='center', va='top', fontsize=9, color='red')
    
    plt.xlim(-0.5, 3.5)
    plt.ylim(0, 1)
    plt.title('처리 파이프라인 비교')
    plt.axis('off')
    
    # 복잡도와 성능
    plt.subplot(2, 2, 3)
    complexity = np.linspace(1, 10, 100)
    ml_complexity = 70 + 10 * np.log(complexity) - 0.5 * complexity
    dl_complexity = 50 + 8 * complexity - 0.3 * complexity**2
    
    plt.plot(complexity, ml_complexity, 'b-', linewidth=2, label='전통적 머신러닝')
    plt.plot(complexity, dl_complexity, 'r-', linewidth=2, label='딥러닝')
    plt.xlabel('문제 복잡도')
    plt.ylabel('성능')
    plt.title('문제 복잡도에 따른 성능')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # 학습 시간 비교
    plt.subplot(2, 2, 4)
    model_sizes = ['작은 모델', '중간 모델', '큰 모델', '매우 큰 모델']
    ml_time = [1, 5, 20, 50]
    dl_time = [10, 100, 1000, 10000]
    
    x = np.arange(len(model_sizes))
    width = 0.35
    
    plt.bar(x - width/2, ml_time, width, label='전통적 머신러닝', alpha=0.8)
    plt.bar(x + width/2, dl_time, width, label='딥러닝', alpha=0.8)
    
    plt.xlabel('모델 크기')
    plt.ylabel('학습 시간 (상대적)')
    plt.title('모델 크기별 학습 시간')
    plt.yscale('log')
    plt.xticks(x, model_sizes, rotation=45)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

compare_ml_vs_dl()
```

### 8.2 신경망의 기본 구조

#### 퍼셉트론 (Perceptron)
```python
import numpy as np
import matplotlib.pyplot as plt

class Perceptron:
    """단순 퍼셉트론 구현"""
    
    def __init__(self, learning_rate=0.1, n_iterations=100):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None
        self.errors = []
    
    def fit(self, X, y):
        """퍼셉트론 학습"""
        # 가중치 초기화
        n_features = X.shape[1]
        self.weights = np.random.normal(0, 0.1, n_features)
        self.bias = 0
        
        # 학습 과정
        for i in range(self.n_iterations):
            errors = 0
            for xi, yi in zip(X, y):
                # 예측
                prediction = self.predict_single(xi)
                
                # 가중치 업데이트
                if prediction != yi:
                    self.weights += self.learning_rate * yi * xi
                    self.bias += self.learning_rate * yi
                    errors += 1
            
            self.errors.append(errors)
            
            # 수렴 확인
            if errors == 0:
                print(f"수렴 완료: {i+1}번째 반복")
                break
    
    def predict_single(self, x):
        """단일 샘플 예측"""
        return 1 if np.dot(x, self.weights) + self.bias > 0 else 0
    
    def predict(self, X):
        """다중 샘플 예측"""
        return np.array([self.predict_single(x) for x in X])

def perceptron_example():
    """퍼셉트론 예제"""
    
    # AND 게이트 데이터
    X_and = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y_and = np.array([0, 0, 0, 1])
    
    # OR 게이트 데이터
    X_or = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y_or = np.array([0, 1, 1, 1])
    
    # XOR 게이트 데이터 (선형 분리 불가능)
    X_xor = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y_xor = np.array([0, 1, 1, 0])
    
    datasets = [
        (X_and, y_and, 'AND 게이트'),
        (X_or, y_or, 'OR 게이트'),
        (X_xor, y_xor, 'XOR 게이트')
    ]
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    
    for i, (X, y, title) in enumerate(datasets):
        # 퍼셉트론 학습
        perceptron = Perceptron(learning_rate=0.1, n_iterations=100)
        perceptron.fit(X, y)
        
        # 결과 시각화
        ax1 = axes[0, i]
        ax2 = axes[1, i]
        
        # 데이터 포인트 시각화
        colors = ['red' if label == 0 else 'blue' for label in y]
        ax1.scatter(X[:, 0], X[:, 1], c=colors, s=100, alpha=0.8)
        
        # 결정 경계 그리기 (XOR은 선형 분리 불가능)
        if title != 'XOR 게이트':
            if perceptron.weights[1] != 0:
                x_line = np.linspace(-0.5, 1.5, 100)
                y_line = -(perceptron.weights[0] * x_line + perceptron.bias) / perceptron.weights[1]
                ax1.plot(x_line, y_line, 'g--', linewidth=2, label='결정 경계')
        
        ax1.set_xlim(-0.5, 1.5)
        ax1.set_ylim(-0.5, 1.5)
        ax1.set_xlabel('입력 1')
        ax1.set_ylabel('입력 2')
        ax1.set_title(f'{title} - 결정 경계')
        ax1.grid(True, alpha=0.3)
        ax1.legend()
        
        # 학습 곡선
        ax2.plot(range(1, len(perceptron.errors) + 1), perceptron.errors, 'b-o')
        ax2.set_xlabel('반복 횟수')
        ax2.set_ylabel('오류 개수')
        ax2.set_title(f'{title} - 학습 곡선')
        ax2.grid(True, alpha=0.3)
        
        # 예측 결과 출력
        predictions = perceptron.predict(X)
        accuracy = np.mean(predictions == y)
        print(f"\n{title} 결과:")
        print(f"  정확도: {accuracy:.2f}")
        print(f"  예측값: {predictions}")
        print(f"  실제값: {y}")
    
    plt.tight_layout()
    plt.show()

perceptron_example()
```

#### 다층 퍼셉트론 (Multi-Layer Perceptron)
```python
class MLPFromScratch:
    """다층 퍼셉트론 직접 구현"""
    
    def __init__(self, layers, learning_rate=0.01, epochs=1000):
        self.layers = layers  # [입력층, 은닉층1, 은닉층2, ..., 출력층]
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = []
        self.biases = []
        self.losses = []
        
        # 가중치와 편향 초기화
        for i in range(len(layers) - 1):
            w = np.random.randn(layers[i], layers[i+1]) * 0.1
            b = np.zeros((1, layers[i+1]))
            self.weights.append(w)
            self.biases.append(b)
    
    def sigmoid(self, x):
        """시그모이드 활성화 함수"""
        return 1 / (1 + np.exp(-np.clip(x, -250, 250)))
    
    def sigmoid_derivative(self, x):
        """시그모이드 도함수"""
        return x * (1 - x)
    
    def forward(self, X):
        """순전파"""
        self.activations = [X]
        
        for i in range(len(self.weights)):
            z = np.dot(self.activations[-1], self.weights[i]) + self.biases[i]
            a = self.sigmoid(z)
            self.activations.append(a)
        
        return self.activations[-1]
    
    def backward(self, X, y, output):
        """역전파"""
        m = X.shape[0]
        
        # 출력층 오차
        dA = output - y
        
        # 역전파 수행
        for i in reversed(range(len(self.weights))):
            dZ = dA * self.sigmoid_derivative(self.activations[i+1])
            dW = np.dot(self.activations[i].T, dZ) / m
            db = np.sum(dZ, axis=0, keepdims=True) / m
            
            if i > 0:
                dA = np.dot(dZ, self.weights[i].T)
            
            # 가중치 업데이트
            self.weights[i] -= self.learning_rate * dW
            self.biases[i] -= self.learning_rate * db
    
    def fit(self, X, y):
        """모델 학습"""
        for epoch in range(self.epochs):
            # 순전파
            output = self.forward(X)
            
            # 손실 계산
            loss = np.mean((output - y) ** 2)
            self.losses.append(loss)
            
            # 역전파
            self.backward(X, y, output)
            
            if epoch % 100 == 0:
                print(f"Epoch {epoch}, Loss: {loss:.6f}")
    
    def predict(self, X):
        """예측"""
        return self.forward(X)

def mlp_xor_example():
    """MLP로 XOR 문제 해결"""
    
    # XOR 데이터
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])
    
    # MLP 모델 생성 (2-4-1 구조)
    mlp = MLPFromScratch([2, 4, 1], learning_rate=1.0, epochs=1000)
    
    print("XOR 문제를 MLP로 해결:")
    mlp.fit(X, y)
    
    # 예측
    predictions = mlp.predict(X)
    
    print("\n결과:")
    for i in range(len(X)):
        print(f"입력: {X[i]}, 예측: {predictions[i][0]:.4f}, 실제: {y[i][0]}")
    
    # 결과 시각화
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # 학습 곡선
    axes[0].plot(mlp.losses)
    axes[0].set_xlabel('Epoch')
    axes[0].set_ylabel('Loss')
    axes[0].set_title('학습 곡선')
    axes[0].grid(True, alpha=0.3)
    
    # 결정 경계 시각화
    h = 0.01
    x_min, x_max = -0.5, 1.5
    y_min, y_max = -0.5, 1.5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    
    grid_points = np.c_[xx.ravel(), yy.ravel()]
    Z = mlp.predict(grid_points)
    Z = Z.reshape(xx.shape)
    
    axes[1].contourf(xx, yy, Z, levels=50, alpha=0.8, cmap='RdYlBu')
    colors = ['red' if label[0] == 0 else 'blue' for label in y]
    axes[1].scatter(X[:, 0], X[:, 1], c=colors, s=100, edgecolors='black')
    axes[1].set_xlabel('입력 1')
    axes[1].set_ylabel('입력 2')
    axes[1].set_title('MLP 결정 경계 (XOR)')
    
    plt.tight_layout()
    plt.show()

mlp_xor_example()
```

### 8.3 활성화 함수

```python
def activation_functions_comparison():
    """다양한 활성화 함수 비교"""
    
    x = np.linspace(-5, 5, 1000)
    
    # 활성화 함수들 정의
    def sigmoid(x):
        return 1 / (1 + np.exp(-np.clip(x, -250, 250)))
    
    def tanh(x):
        return np.tanh(x)
    
    def relu(x):
        return np.maximum(0, x)
    
    def leaky_relu(x, alpha=0.01):
        return np.where(x > 0, x, alpha * x)
    
    def elu(x, alpha=1.0):
        return np.where(x > 0, x, alpha * (np.exp(x) - 1))
    
    def swish(x):
        return x * sigmoid(x)
    
    # 도함수들
    def sigmoid_derivative(x):
        s = sigmoid(x)
        return s * (1 - s)
    
    def tanh_derivative(x):
        return 1 - np.tanh(x)**2
    
    def relu_derivative(x):
        return np.where(x > 0, 1, 0)
    
    def leaky_relu_derivative(x, alpha=0.01):
        return np.where(x > 0, 1, alpha)
    
    # 시각화
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    
    functions = [
        (sigmoid, sigmoid_derivative, 'Sigmoid'),
        (tanh, tanh_derivative, 'Tanh'),
        (relu, relu_derivative, 'ReLU'),
        (leaky_relu, leaky_relu_derivative, 'Leaky ReLU'),
        (elu, lambda x: np.where(x > 0, 1, elu(x) + 1), 'ELU'),
        (swish, lambda x: sigmoid(x) + x * sigmoid_derivative(x), 'Swish')
    ]
    
    for i, (func, derivative, name) in enumerate(functions):
        row, col = i // 3, i % 3
        
        # 함수 그래프
        y = func(x)
        axes[row, col].plot(x, y, 'b-', linewidth=2, label=f'{name}')
        
        # 도함수 그래프
        dy = derivative(x)
        axes[row, col].plot(x, dy, 'r--', linewidth=2, label=f"{name} 도함수")
        
        axes[row, col].set_xlabel('x')
        axes[row, col].set_ylabel('f(x)')
        axes[row, col].set_title(f'{name} 활성화 함수')
        axes[row, col].grid(True, alpha=0.3)
        axes[row, col].legend()
        axes[row, col].axhline(y=0, color='k', linewidth=0.5)
        axes[row, col].axvline(x=0, color='k', linewidth=0.5)
    
    plt.tight_layout()
    plt.show()
    
    # 활성화 함수 특성 비교표
    print("활성화 함수 특성 비교:")
    print("=" * 80)
    print(f"{'함수':<12} {'범위':<15} {'미분가능':<8} {'기울기소실':<10} {'특징'}")
    print("-" * 80)
    print(f"{'Sigmoid':<12} {'(0, 1)':<15} {'Yes':<8} {'High':<10} {'확률 출력, 이진분류'}")
    print(f"{'Tanh':<12} {'(-1, 1)':<15} {'Yes':<8} {'High':<10} {'0 중심, 은닉층'}")
    print(f"{'ReLU':<12} {'[0, ∞)':<15} {'No':<8} {'Low':<10} {'빠른계산, 죽은뉴런'}")
    print(f"{'Leaky ReLU':<12} {'(-∞, ∞)':<15} {'No':<8} {'Low':<10} {'죽은뉴런 해결'}")
    print(f"{'ELU':<12} {'(-α, ∞)':<15} {'No':<8} {'Low':<10} {'부드러운 음수'}")
    print(f"{'Swish':<12} {'(-∞, ∞)':<15} {'Yes':<8} {'Low':<10} {'자기조정, 최신'}")

activation_functions_comparison()
```

> **참고**: 활성화 함수 선택은 모델 성능에 큰 영향을 미칩니다. 일반적으로 은닉층에는 ReLU, 출력층에는 문제 유형에 맞는 함수를 사용합니다. 

---

## 9. 신경망 구조

### 9.1 TensorFlow/Keras 기초

#### 모델 생성 방법

**Sequential 모델**:
```python
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Sequential 모델 (순차적 층 쌓기)
def create_sequential_model():
    """Sequential 모델 생성 예제"""
    
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(128, activation='relu', input_shape=(784,)),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    
    return model

# Functional API 모델
def create_functional_model():
    """Functional API 모델 생성 예제"""
    
    inputs = tf.keras.Input(shape=(784,))
    x = tf.keras.layers.Dense(128, activation='relu')(inputs)
    x = tf.keras.layers.Dropout(0.2)(x)
    x = tf.keras.layers.Dense(64, activation='relu')(x)
    x = tf.keras.layers.Dropout(0.2)(x)
    outputs = tf.keras.layers.Dense(10, activation='softmax')(x)
    
    model = tf.keras.Model(inputs=inputs, outputs=outputs)
    return model

# 모델 비교
sequential_model = create_sequential_model()
functional_model = create_functional_model()

print("Sequential 모델 구조:")
sequential_model.summary()

print("\nFunctional API 모델 구조:")
functional_model.summary()
```

#### 모델 컴파일과 훈련
```python
def compile_and_train_model():
    """모델 컴파일 및 훈련 예제"""
    
    # MNIST 데이터 로드
    (X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()
    
    # 데이터 전처리
    X_train = X_train.astype('float32') / 255.0
    X_test = X_test.astype('float32') / 255.0
    X_train = X_train.reshape(-1, 784)
    X_test = X_test.reshape(-1, 784)
    
    # 모델 생성
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(128, activation='relu', input_shape=(784,)),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    
    # 모델 컴파일
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    # 콜백 설정
    callbacks = [
        tf.keras.callbacks.EarlyStopping(
            monitor='val_loss',
            patience=5,
            restore_best_weights=True
        ),
        tf.keras.callbacks.ReduceLROnPlateau(
            monitor='val_loss',
            factor=0.2,
            patience=3,
            min_lr=1e-7
        )
    ]
    
    # 모델 훈련
    history = model.fit(
        X_train, y_train,
        batch_size=128,
        epochs=20,
        validation_split=0.1,
        callbacks=callbacks,
        verbose=1
    )
    
    # 모델 평가
    test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
    print(f"\n테스트 정확도: {test_acc:.4f}")
    
    # 학습 곡선 시각화
    plt.figure(figsize=(12, 4))
    
    plt.subplot(1, 2, 1)
    plt.plot(history.history['loss'], label='훈련 손실')
    plt.plot(history.history['val_loss'], label='검증 손실')
    plt.title('모델 손실')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.subplot(1, 2, 2)
    plt.plot(history.history['accuracy'], label='훈련 정확도')
    plt.plot(history.history['val_accuracy'], label='검증 정확도')
    plt.title('모델 정확도')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    return model, history

trained_model, training_history = compile_and_train_model()
```

---

## 10. CNN (합성곱 신경망)

### 10.1 CNN 개념과 구조

**CNN(Convolutional Neural Network)**은 이미지 처리에 특화된 신경망으로, 이미지의 공간적 정보를 유지하면서 특징을 추출합니다.

#### CNN의 핵심 구성요소

```python
def demonstrate_cnn_operations():
    """CNN 연산 시연"""
    
    # 샘플 이미지 생성
    image = np.random.rand(1, 28, 28, 1)  # 배치크기, 높이, 너비, 채널
    
    # 1. 합성곱 층
    conv_layer = tf.keras.layers.Conv2D(
        filters=32,
        kernel_size=(3, 3),
        activation='relu',
        padding='same'
    )
    
    conv_output = conv_layer(image)
    print(f"합성곱 결과 크기: {conv_output.shape}")
    
    # 2. 풀링 층
    pool_layer = tf.keras.layers.MaxPooling2D(pool_size=(2, 2))
    pool_output = pool_layer(conv_output)
    print(f"풀링 결과 크기: {pool_output.shape}")
    
    # 3. 배치 정규화
    bn_layer = tf.keras.layers.BatchNormalization()
    bn_output = bn_layer(pool_output)
    print(f"배치 정규화 결과 크기: {bn_output.shape}")
    
    # CNN 모델 전체 구조
    model = tf.keras.Sequential([
        # 첫 번째 합성곱 블록
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Dropout(0.25),
        
        # 두 번째 합성곱 블록
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Dropout(0.25),
        
        # 세 번째 합성곱 블록
        tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dropout(0.25),
        
        # 완전연결층
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    
    model.summary()
    return model

cnn_model = demonstrate_cnn_operations()
```

### 10.2 CIFAR-10 이미지 분류 프로젝트

```python
def cifar10_classification():
    """CIFAR-10 이미지 분류 프로젝트"""
    
    # 데이터 로드
    (X_train, y_train), (X_test, y_test) = tf.keras.datasets.cifar10.load_data()
    
    # 클래스 이름
    class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
                   'dog', 'frog', 'horse', 'ship', 'truck']
    
    # 데이터 전처리
    X_train = X_train.astype('float32') / 255.0
    X_test = X_test.astype('float32') / 255.0
    
    # 일부 이미지 시각화
    plt.figure(figsize=(12, 8))
    for i in range(20):
        plt.subplot(4, 5, i + 1)
        plt.imshow(X_train[i])
        plt.title(f'{class_names[y_train[i][0]]}')
        plt.axis('off')
    plt.suptitle('CIFAR-10 샘플 이미지')
    plt.tight_layout()
    plt.show()
    
    # 데이터 증강
    datagen = tf.keras.preprocessing.image.ImageDataGenerator(
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        horizontal_flip=True,
        zoom_range=0.2,
        shear_range=0.2,
        fill_mode='nearest'
    )
    
    # CNN 모델 생성
    model = tf.keras.Sequential([
        # 첫 번째 블록
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Dropout(0.25),
        
        # 두 번째 블록
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Dropout(0.25),
        
        # 세 번째 블록
        tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
        tf.keras.layers.Dropout(0.25),
        
        # 완전연결층
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    
    # 모델 컴파일
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    # 콜백 설정
    callbacks = [
        tf.keras.callbacks.EarlyStopping(patience=10, restore_best_weights=True),
        tf.keras.callbacks.ReduceLROnPlateau(factor=0.2, patience=5)
    ]
    
    # 모델 훈련
    history = model.fit(
        datagen.flow(X_train, y_train, batch_size=32),
        epochs=50,
        validation_data=(X_test, y_test),
        callbacks=callbacks,
        verbose=1
    )
    
    # 성능 평가
    test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
    print(f"테스트 정확도: {test_acc:.4f}")
    
    # 예측 결과 시각화
    predictions = model.predict(X_test[:20])
    predicted_classes = np.argmax(predictions, axis=1)
    
    plt.figure(figsize=(15, 8))
    for i in range(20):
        plt.subplot(4, 5, i + 1)
        plt.imshow(X_test[i])
        actual = class_names[y_test[i][0]]
        predicted = class_names[predicted_classes[i]]
        confidence = predictions[i][predicted_classes[i]]
        
        color = 'green' if actual == predicted else 'red'
        plt.title(f'실제: {actual}\n예측: {predicted}\n({confidence:.2f})', 
                 color=color, fontsize=8)
        plt.axis('off')
    
    plt.suptitle('CIFAR-10 예측 결과')
    plt.tight_layout()
    plt.show()
    
    return model, history

cifar_model, cifar_history = cifar10_classification()
```

---

## 11. RNN (순환 신경망)

### 11.1 RNN 기본 개념

**RNN(Recurrent Neural Network)**은 시퀀스 데이터를 처리하기 위한 신경망으로, 시간적 의존성을 모델링할 수 있습니다.

```python
def demonstrate_rnn_concepts():
    """RNN 개념 시연"""
    
    # 시계열 데이터 생성
    def create_time_series_data(n_samples=1000, seq_length=50):
        """사인파 기반 시계열 데이터 생성"""
        time = np.linspace(0, 100, n_samples + seq_length)
        data = np.sin(time) + 0.5 * np.sin(3 * time) + 0.1 * np.random.randn(len(time))
        
        X, y = [], []
        for i in range(n_samples):
            X.append(data[i:i + seq_length])
            y.append(data[i + seq_length])
        
        return np.array(X), np.array(y)
    
    X, y = create_time_series_data()
    X = X.reshape(X.shape[0], X.shape[1], 1)  # (samples, timesteps, features)
    
    # 데이터 분할
    train_size = int(0.8 * len(X))
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]
    
    print(f"훈련 데이터 크기: {X_train.shape}")
    print(f"테스트 데이터 크기: {X_test.shape}")
    
    # 다양한 RNN 모델 비교
    models = {}
    
    # 1. 단순 RNN
    models['Simple RNN'] = tf.keras.Sequential([
        tf.keras.layers.SimpleRNN(50, activation='tanh', input_shape=(50, 1)),
        tf.keras.layers.Dense(25),
        tf.keras.layers.Dense(1)
    ])
    
    # 2. LSTM
    models['LSTM'] = tf.keras.Sequential([
        tf.keras.layers.LSTM(50, input_shape=(50, 1)),
        tf.keras.layers.Dense(25),
        tf.keras.layers.Dense(1)
    ])
    
    # 3. GRU
    models['GRU'] = tf.keras.Sequential([
        tf.keras.layers.GRU(50, input_shape=(50, 1)),
        tf.keras.layers.Dense(25),
        tf.keras.layers.Dense(1)
    ])
    
    # 4. 양방향 LSTM
    models['Bidirectional LSTM'] = tf.keras.Sequential([
        tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(25), input_shape=(50, 1)),
        tf.keras.layers.Dense(25),
        tf.keras.layers.Dense(1)
    ])
    
    # 모델 훈련 및 평가
    results = {}
    
    plt.figure(figsize=(16, 12))
    
    for i, (name, model) in enumerate(models.items()):
        print(f"\n{name} 훈련 중...")
        
        model.compile(optimizer='adam', loss='mse', metrics=['mae'])
        history = model.fit(X_train, y_train, epochs=50, batch_size=32, 
                          validation_data=(X_test, y_test), verbose=0)
        
        # 예측
        y_pred = model.predict(X_test)
        mse = np.mean((y_test - y_pred.flatten())**2)
        results[name] = mse
        
        # 시각화
        plt.subplot(2, 2, i + 1)
        plt.plot(y_test[:100], label='실제값', alpha=0.7)
        plt.plot(y_pred[:100], label='예측값', alpha=0.7)
        plt.title(f'{name}\nMSE: {mse:.6f}')
        plt.legend()
        plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    # 결과 비교
    print("\n모델 성능 비교 (MSE):")
    for name, mse in sorted(results.items(), key=lambda x: x[1]):
        print(f"{name}: {mse:.6f}")
    
    return models, results

rnn_models, rnn_results = demonstrate_rnn_concepts()
```

### 11.2 자연어 처리 예제

```python
def sentiment_analysis_example():
    """감정 분석 예제"""
    
    # IMDB 영화 리뷰 데이터
    max_features = 10000
    maxlen = 200
    
    (X_train, y_train), (X_test, y_test) = tf.keras.datasets.imdb.load_data(
        num_words=max_features
    )
    
    print(f"훈련 샘플 수: {len(X_train)}")
    print(f"테스트 샘플 수: {len(X_test)}")
    
    # 시퀀스 패딩
    X_train = tf.keras.preprocessing.sequence.pad_sequences(X_train, maxlen=maxlen)
    X_test = tf.keras.preprocessing.sequence.pad_sequences(X_test, maxlen=maxlen)
    
    # 모델 생성
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(max_features, 128, input_length=maxlen),
        tf.keras.layers.LSTM(64, dropout=0.5, recurrent_dropout=0.5),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    
    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    
    print("모델 구조:")
    model.summary()
    
    # 훈련
    history = model.fit(
        X_train, y_train,
        batch_size=32,
        epochs=10,
        validation_data=(X_test, y_test),
        verbose=1
    )
    
    # 평가
    test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
    print(f"\n테스트 정확도: {test_acc:.4f}")
    
    # 학습 곡선 시각화
    plt.figure(figsize=(12, 4))
    
    plt.subplot(1, 2, 1)
    plt.plot(history.history['loss'], label='훈련 손실')
    plt.plot(history.history['val_loss'], label='검증 손실')
    plt.title('모델 손실')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.subplot(1, 2, 2)
    plt.plot(history.history['accuracy'], label='훈련 정확도')
    plt.plot(history.history['val_accuracy'], label='검증 정확도')
    plt.title('모델 정확도')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    return model, history

sentiment_model, sentiment_history = sentiment_analysis_example()
```

---

## 12. 고급 딥러닝 기법

### 12.1 전이학습 (Transfer Learning)

```python
def transfer_learning_example():
    """전이학습 예제"""
    
    # 사전 훈련된 모델 로드
    base_model = tf.keras.applications.VGG16(
        weights='imagenet',
        include_top=False,
        input_shape=(224, 224, 3)
    )
    
    # 기본 모델 동결
    base_model.trainable = False
    
    # 새로운 분류기 추가
    model = tf.keras.Sequential([
        base_model,
        tf.keras.layers.GlobalAveragePooling2D(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(10, activation='softmax')  # CIFAR-10용
    ])
    
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    print("전이학습 모델 구조:")
    model.summary()
    
    return model

transfer_model = transfer_learning_example()
```

### 12.2 정규화 기법

```python
def regularization_techniques():
    """정규화 기법들"""
    
    # 샘플 데이터 생성
    (X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()
    X_train = X_train.astype('float32') / 255.0
    X_test = X_test.astype('float32') / 255.0
    X_train = X_train.reshape(-1, 784)
    X_test = X_test.reshape(-1, 784)
    
    # 다양한 정규화 기법을 적용한 모델들
    models = {}
    
    # 1. 기본 모델 (정규화 없음)
    models['기본 모델'] = tf.keras.Sequential([
        tf.keras.layers.Dense(512, activation='relu', input_shape=(784,)),
        tf.keras.layers.Dense(256, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    
    # 2. 드롭아웃
    models['드롭아웃'] = tf.keras.Sequential([
        tf.keras.layers.Dense(512, activation='relu', input_shape=(784,)),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(256, activation='relu'),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    
    # 3. 배치 정규화
    models['배치 정규화'] = tf.keras.Sequential([
        tf.keras.layers.Dense(512, activation='relu', input_shape=(784,)),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dense(256, activation='relu'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    
    # 4. L2 정규화
    models['L2 정규화'] = tf.keras.Sequential([
        tf.keras.layers.Dense(512, activation='relu', input_shape=(784,),
                            kernel_regularizer=tf.keras.regularizers.l2(0.001)),
        tf.keras.layers.Dense(256, activation='relu',
                            kernel_regularizer=tf.keras.regularizers.l2(0.001)),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    
    # 5. 모든 기법 결합
    models['모든 기법'] = tf.keras.Sequential([
        tf.keras.layers.Dense(512, activation='relu', input_shape=(784,),
                            kernel_regularizer=tf.keras.regularizers.l2(0.001)),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(256, activation='relu',
                            kernel_regularizer=tf.keras.regularizers.l2(0.001)),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    
    # 모델 훈련 및 비교
    results = {}
    histories = {}
    
    for name, model in models.items():
        print(f"\n{name} 훈련 중...")
        
        model.compile(
            optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy']
        )
        
        history = model.fit(
            X_train, y_train,
            batch_size=128,
            epochs=20,
            validation_data=(X_test, y_test),
            verbose=0
        )
        
        test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
        results[name] = test_acc
        histories[name] = history
        
        print(f"{name} 테스트 정확도: {test_acc:.4f}")
    
    # 결과 시각화
    plt.figure(figsize=(15, 10))
    
    # 정확도 비교
    plt.subplot(2, 3, 1)
    names = list(results.keys())
    accuracies = list(results.values())
    bars = plt.bar(names, accuracies)
    plt.title('모델별 테스트 정확도')
    plt.ylabel('정확도')
    plt.xticks(rotation=45)
    
    # 각 막대에 값 표시
    for bar, acc in zip(bars, accuracies):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
                f'{acc:.3f}', ha='center', va='bottom')
    
    # 학습 곡선들
    colors = ['blue', 'red', 'green', 'orange', 'purple']
    for i, (name, history) in enumerate(histories.items()):
        plt.subplot(2, 3, i + 2)
        plt.plot(history.history['accuracy'], label='훈련', color=colors[i % len(colors)])
        plt.plot(history.history['val_accuracy'], label='검증', 
                color=colors[i % len(colors)], linestyle='--')
        plt.title(f'{name} 학습 곡선')
        plt.xlabel('Epoch')
        plt.ylabel('정확도')
        plt.legend()
        plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    return models, results

reg_models, reg_results = regularization_techniques()
```

---

## 13. 모델 평가 및 최적화

### 13.1 성능 지표

```python
def comprehensive_model_evaluation():
    """종합적인 모델 평가"""
    
    from sklearn.metrics import classification_report, confusion_matrix
    from sklearn.metrics import precision_recall_fscore_support, roc_auc_score
    
    # CIFAR-10 데이터로 모델 평가
    (X_train, y_train), (X_test, y_test) = tf.keras.datasets.cifar10.load_data()
    X_test = X_test.astype('float32') / 255.0
    
    # 간단한 CNN 모델 생성 및 훈련 (예시)
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    
    # 빠른 훈련을 위해 적은 에포크 사용
    model.fit(X_train[:5000], y_train[:5000], epochs=5, verbose=0)
    
    # 예측
    y_pred_proba = model.predict(X_test[:1000])
    y_pred = np.argmax(y_pred_proba, axis=1)
    y_true = y_test[:1000].flatten()
    
    # 1. 기본 지표들
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
    
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average='weighted')
    recall = recall_score(y_true, y_pred, average='weighted')
    f1 = f1_score(y_true, y_pred, average='weighted')
    
    print("기본 성능 지표:")
    print(f"정확도 (Accuracy): {accuracy:.4f}")
    print(f"정밀도 (Precision): {precision:.4f}")
    print(f"재현율 (Recall): {recall:.4f}")
    print(f"F1 점수: {f1:.4f}")
    
    # 2. 클래스별 상세 리포트
    class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
                   'dog', 'frog', 'horse', 'ship', 'truck']
    
    print("\n클래스별 성능:")
    print(classification_report(y_true, y_pred, target_names=class_names))
    
    # 3. 혼동 행렬 시각화
    cm = confusion_matrix(y_true, y_pred)
    
    plt.figure(figsize=(12, 10))
    
    plt.subplot(2, 2, 1)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=class_names, yticklabels=class_names)
    plt.title('혼동 행렬')
    plt.xlabel('예측 클래스')
    plt.ylabel('실제 클래스')
    
    # 4. 클래스별 정확도
    class_accuracy = cm.diagonal() / cm.sum(axis=1)
    
    plt.subplot(2, 2, 2)
    bars = plt.bar(class_names, class_accuracy)
    plt.title('클래스별 정확도')
    plt.ylabel('정확도')
    plt.xticks(rotation=45)
    
    for bar, acc in zip(bars, class_accuracy):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
                f'{acc:.2f}', ha='center', va='bottom')
    
    # 5. 예측 확신도 분포
    max_probs = np.max(y_pred_proba, axis=1)
    
    plt.subplot(2, 2, 3)
    plt.hist(max_probs, bins=30, alpha=0.7, edgecolor='black')
    plt.title('예측 확신도 분포')
    plt.xlabel('최대 확률')
    plt.ylabel('빈도')
    plt.grid(True, alpha=0.3)
    
    # 6. 틀린 예측 분석
    wrong_predictions = y_true != y_pred
    wrong_confidences = max_probs[wrong_predictions]
    correct_confidences = max_probs[~wrong_predictions]
    
    plt.subplot(2, 2, 4)
    plt.hist(correct_confidences, bins=20, alpha=0.7, label='정확한 예측', color='green')
    plt.hist(wrong_confidences, bins=20, alpha=0.7, label='틀린 예측', color='red')
    plt.title('정확/틀린 예측의 확신도 비교')
    plt.xlabel('확신도')
    plt.ylabel('빈도')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    # 7. 성능 요약
    print(f"\n성능 요약:")
    print(f"전체 정확도: {accuracy:.4f}")
    print(f"평균 클래스 정확도: {np.mean(class_accuracy):.4f}")
    print(f"최고 클래스 정확도: {np.max(class_accuracy):.4f} ({class_names[np.argmax(class_accuracy)]})")
    print(f"최저 클래스 정확도: {np.min(class_accuracy):.4f} ({class_names[np.argmin(class_accuracy)]})")
    print(f"평균 예측 확신도: {np.mean(max_probs):.4f}")
    
    return model, {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1': f1,
        'class_accuracy': class_accuracy,
        'confusion_matrix': cm
    }

eval_model, eval_metrics = comprehensive_model_evaluation()
```

### 13.2 하이퍼파라미터 튜닝

```python
def hyperparameter_tuning_example():
    """하이퍼파라미터 튜닝 예제"""
    
    # Keras Tuner 사용 (설치 필요: pip install keras-tuner)
    try:
        import keras_tuner as kt
        
        def build_model(hp):
            """하이퍼파라미터를 받아 모델을 생성하는 함수"""
            model = tf.keras.Sequential()
            
            # 첫 번째 층
            model.add(tf.keras.layers.Dense(
                units=hp.Int('units_1', min_value=32, max_value=512, step=32),
                activation=hp.Choice('activation_1', ['relu', 'tanh']),
                input_shape=(784,)
            ))
            
            # 드롭아웃
            model.add(tf.keras.layers.Dropout(
                rate=hp.Float('dropout_1', min_value=0.0, max_value=0.5, step=0.1)
            ))
            
            # 두 번째 층 (선택적)
            if hp.Boolean('use_second_layer'):
                model.add(tf.keras.layers.Dense(
                    units=hp.Int('units_2', min_value=32, max_value=256, step=32),
                    activation=hp.Choice('activation_2', ['relu', 'tanh'])
                ))
                model.add(tf.keras.layers.Dropout(
                    rate=hp.Float('dropout_2', min_value=0.0, max_value=0.5, step=0.1)
                ))
            
            # 출력층
            model.add(tf.keras.layers.Dense(10, activation='softmax'))
            
            # 컴파일
            model.compile(
                optimizer=tf.keras.optimizers.Adam(
                    learning_rate=hp.Float('learning_rate', min_value=1e-4, max_value=1e-2, sampling='LOG')
                ),
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy']
            )
            
            return model
        
        # 데이터 준비
        (X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()
        X_train = X_train.astype('float32') / 255.0
        X_test = X_test.astype('float32') / 255.0
        X_train = X_train.reshape(-1, 784)
        X_test = X_test.reshape(-1, 784)
        
        # 작은 데이터셋으로 빠른 튜닝
        X_train_small = X_train[:5000]
        y_train_small = y_train[:5000]
        
        # 튜너 설정
        tuner = kt.RandomSearch(
            build_model,
            objective='val_accuracy',
            max_trials=10,  # 실제로는 더 많이 설정
            directory='hyperparameter_tuning',
            project_name='mnist_tuning'
        )
        
        print("하이퍼파라미터 튜닝 시작...")
        tuner.search(X_train_small, y_train_small,
                    epochs=5,
                    validation_split=0.2,
                    verbose=0)
        
        # 최적 하이퍼파라미터
        best_hps = tuner.get_best_hyperparameters(num_trials=1)[0]
        
        print("최적 하이퍼파라미터:")
        print(f"첫 번째 층 유닛 수: {best_hps.get('units_1')}")
        print(f"첫 번째 층 활성화 함수: {best_hps.get('activation_1')}")
        print(f"첫 번째 드롭아웃 비율: {best_hps.get('dropout_1')}")
        print(f"두 번째 층 사용: {best_hps.get('use_second_layer')}")
        if best_hps.get('use_second_layer'):
            print(f"두 번째 층 유닛 수: {best_hps.get('units_2')}")
            print(f"두 번째 층 활성화 함수: {best_hps.get('activation_2')}")
            print(f"두 번째 드롭아웃 비율: {best_hps.get('dropout_2')}")
        print(f"학습률: {best_hps.get('learning_rate')}")
        
        # 최적 모델로 재훈련
        best_model = tuner.hypermodel.build(best_hps)
        history = best_model.fit(X_train, y_train, epochs=10, 
                                validation_data=(X_test, y_test), verbose=0)
        
        test_loss, test_acc = best_model.evaluate(X_test, y_test, verbose=0)
        print(f"\n최적 모델 테스트 정확도: {test_acc:.4f}")
        
        return best_model, best_hps
        
    except ImportError:
        print("Keras Tuner가 설치되지 않았습니다.")
        print("설치하려면: pip install keras-tuner")
        
        # 수동 그리드 서치 예제
        print("\n수동 하이퍼파라미터 튜닝 예제:")
        
        # 간단한 그리드 서치
        param_grid = {
            'units': [64, 128, 256],
            'dropout': [0.2, 0.3, 0.5],
            'learning_rate': [0.001, 0.01]
        }
        
        best_score = 0
        best_params = {}
        
        for units in param_grid['units']:
            for dropout in param_grid['dropout']:
                for lr in param_grid['learning_rate']:
                    print(f"테스트 중: units={units}, dropout={dropout}, lr={lr}")
                    
                    model = tf.keras.Sequential([
                        tf.keras.layers.Dense(units, activation='relu', input_shape=(784,)),
                        tf.keras.layers.Dropout(dropout),
                        tf.keras.layers.Dense(10, activation='softmax')
                    ])
                    
                    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=lr),
                                loss='sparse_categorical_crossentropy',
                                metrics=['accuracy'])
                    
                    # 빠른 평가를 위해 적은 데이터와 에포크 사용
                    history = model.fit(X_train[:1000], y_train[:1000], 
                                      epochs=3, validation_split=0.2, verbose=0)
                    
                    val_acc = max(history.history['val_accuracy'])
                    
                    if val_acc > best_score:
                        best_score = val_acc
                        best_params = {'units': units, 'dropout': dropout, 'learning_rate': lr}
        
        print(f"\n최적 파라미터: {best_params}")
        print(f"최고 검증 정확도: {best_score:.4f}")
        
        return None, best_params

tuning_result = hyperparameter_tuning_example()
```

---

## 14. 실전 프로젝트

### 14.1 이미지 분류 프로젝트

```python
def complete_image_classification_project():
    """완전한 이미지 분류 프로젝트"""
    
    print("=== 개/고양이 이미지 분류 프로젝트 ===")
    
    # 1. 데이터 준비 (실제로는 외부 데이터 사용)
    # 여기서는 CIFAR-10에서 고양이(3)와 개(5)만 사용
    (X_train, y_train), (X_test, y_test) = tf.keras.datasets.cifar10.load_data()
    
    # 고양이(3)와 개(5)만 필터링
    cat_dog_filter_train = (y_train == 3) | (y_train == 5)
    cat_dog_filter_test = (y_test == 3) | (y_test == 5)
    
    X_train = X_train[cat_dog_filter_train.flatten()]
    y_train = y_train[cat_dog_filter_train.flatten()]
    X_test = X_test[cat_dog_filter_test.flatten()]
    y_test = y_test[cat_dog_filter_test.flatten()]
    
    # 라벨 재조정 (3->0: 고양이, 5->1: 개)
    y_train = (y_train == 5).astype(int)
    y_test = (y_test == 5).astype(int)
    
    # 데이터 정규화
    X_train = X_train.astype('float32') / 255.0
    X_test = X_test.astype('float32') / 255.0
    
    print(f"훈련 데이터: {X_train.shape}, 라벨: {y_train.shape}")
    print(f"테스트 데이터: {X_test.shape}, 라벨: {y_test.shape}")
    
    # 2. 데이터 증강
    datagen = tf.keras.preprocessing.image.ImageDataGenerator(
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        horizontal_flip=True,
        zoom_range=0.2,
        shear_range=0.2,
        fill_mode='nearest'
    )
    
    # 3. 모델 설계
    def create_cnn_model():
        model = tf.keras.Sequential([
            # 첫 번째 블록
            tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
            tf.keras.layers.BatchNormalization(),
            tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Dropout(0.25),
            
            # 두 번째 블록
            tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
            tf.keras.layers.BatchNormalization(),
            tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Dropout(0.25),
            
            # 세 번째 블록
            tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
            tf.keras.layers.BatchNormalization(),
            tf.keras.layers.Dropout(0.25),
            
            # 분류기
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(512, activation='relu'),
            tf.keras.layers.BatchNormalization(),
            tf.keras.layers.Dropout(0.5),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])
        
        return model
    
    model = create_cnn_model()
    
    # 4. 모델 컴파일
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    
    print("\n모델 구조:")
    model.summary()
    
    # 5. 콜백 설정
    callbacks = [
        tf.keras.callbacks.EarlyStopping(
            monitor='val_loss',
            patience=10,
            restore_best_weights=True
        ),
        tf.keras.callbacks.ReduceLROnPlateau(
            monitor='val_loss',
            factor=0.2,
            patience=5,
            min_lr=1e-7
        ),
        tf.keras.callbacks.ModelCheckpoint(
            'best_model.h5',
            monitor='val_accuracy',
            save_best_only=True,
            mode='max'
        )
    ]
    
    # 6. 모델 훈련
    print("\n모델 훈련 시작...")
    history = model.fit(
        datagen.flow(X_train, y_train, batch_size=32),
        epochs=30,
        validation_data=(X_test, y_test),
        callbacks=callbacks,
        verbose=1
    )
    
    # 7. 결과 평가
    test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
    print(f"\n최종 테스트 정확도: {test_acc:.4f}")
    
    # 8. 예측 및 시각화
    predictions = model.predict(X_test)
    predicted_classes = (predictions > 0.5).astype(int).flatten()
    
    # 혼동 행렬
    cm = confusion_matrix(y_test, predicted_classes)
    
    plt.figure(figsize=(15, 12))
    
    # 학습 곡선
    plt.subplot(2, 3, 1)
    plt.plot(history.history['loss'], label='훈련 손실')
    plt.plot(history.history['val_loss'], label='검증 손실')
    plt.title('모델 손실')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.subplot(2, 3, 2)
    plt.plot(history.history['accuracy'], label='훈련 정확도')
    plt.plot(history.history['val_accuracy'], label='검증 정확도')
    plt.title('모델 정확도')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # 혼동 행렬
    plt.subplot(2, 3, 3)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=['고양이', '개'], yticklabels=['고양이', '개'])
    plt.title('혼동 행렬')
    plt.xlabel('예측')
    plt.ylabel('실제')
    
    # 예측 예시
    sample_indices = np.random.choice(len(X_test), 9, replace=False)
    
    for i, idx in enumerate(sample_indices):
        plt.subplot(2, 3, 4 + (i % 6))
        if i >= 6:
            break
            
        plt.imshow(X_test[idx])
        actual = '개' if y_test[idx] == 1 else '고양이'
        predicted = '개' if predicted_classes[idx] == 1 else '고양이'
        confidence = predictions[idx][0] if predicted_classes[idx] == 1 else 1 - predictions[idx][0]
        
        color = 'green' if actual == predicted else 'red'
        plt.title(f'실제: {actual}\n예측: {predicted}\n확신도: {confidence:.2f}', 
                 color=color, fontsize=8)
        plt.axis('off')
    
    plt.tight_layout()
    plt.show()
    
    # 9. 성능 분석
    from sklearn.metrics import classification_report
    print("\n상세 성능 리포트:")
    print(classification_report(y_test, predicted_classes, target_names=['고양이', '개']))
    
    return model, history

# 프로젝트 실행
final_model, final_history = complete_image_classification_project()
```

### 14.2 모델 배포

```python
def model_deployment_example():
    """모델 배포 예제"""
    
    # Flask API 서버 코드 생성
    flask_code = '''
from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import base64

app = Flask(__name__)

# 모델 로드
model = tf.keras.models.load_model('best_model.h5')

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 이미지 데이터 받기
        data = request.get_json()
        
        if 'image' not in data:
            return jsonify({"error": "이미지가 필요합니다"}), 400
        
        # Base64 디코딩
        image_data = base64.b64decode(data['image'])
        image = Image.open(io.BytesIO(image_data))
        
        # 이미지 전처리
        image = image.resize((32, 32))
        image_array = np.array(image) / 255.0
        image_array = np.expand_dims(image_array, axis=0)
        
        # 예측
        prediction = model.predict(image_array)
        probability = float(prediction[0][0])
        
        # 결과 반환
        result = {
            "prediction": "개" if probability > 0.5 else "고양이",
            "probability": probability,
            "confidence": max(probability, 1 - probability)
        }
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
'''
    
    # 파일로 저장
    with open('flask_api.py', 'w', encoding='utf-8') as f:
        f.write(flask_code)
    
    print("Flask API 서버 코드가 'flask_api.py'로 저장되었습니다.")
    
    # Docker 설정 파일
    dockerfile_content = '''
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "flask_api.py"]
'''
    
    requirements_content = '''
flask==2.3.3
tensorflow==2.13.0
pillow==10.0.0
numpy==1.24.3
'''
    
    with open('Dockerfile', 'w') as f:
        f.write(dockerfile_content)
    
    with open('requirements.txt', 'w') as f:
        f.write(requirements_content)
    
    print("Docker 설정 파일들이 생성되었습니다.")
    
    # 클라이언트 테스트 코드
    client_code = '''
import requests
import base64
import json

def test_api():
    # API 엔드포인트
    url = "http://localhost:5000/predict"
    
    # 테스트 이미지 (실제로는 파일에서 로드)
    # with open('test_image.jpg', 'rb') as f:
    #     image_data = f.read()
    
    # 임시로 더미 데이터 사용
    image_data = b"dummy_image_data"
    
    # Base64 인코딩
    encoded_image = base64.b64encode(image_data).decode('utf-8')
    
    # 요청 데이터
    data = {
        "image": encoded_image
    }
    
    try:
        # API 호출
        response = requests.post(url, json=data)
        
        if response.status_code == 200:
            result = response.json()
            print(f"예측 결과: {result['prediction']}")
            print(f"확신도: {result['confidence']:.2f}")
        else:
            print(f"오류: {response.json()}")
            
    except requests.exceptions.ConnectionError:
        print("API 서버에 연결할 수 없습니다.")

if __name__ == "__main__":
    test_api()
'''
    
    with open('test_client.py', 'w', encoding='utf-8') as f:
        f.write(client_code)
    
    print("클라이언트 테스트 코드가 'test_client.py'로 저장되었습니다.")
    
    print("\n배포 가이드:")
    print("1. 모델 저장: model.save('best_model.h5')")
    print("2. Flask 서버 실행: python flask_api.py")
    print("3. Docker 빌드: docker build -t ml-api .")
    print("4. Docker 실행: docker run -p 5000:5000 ml-api")
    print("5. 테스트: python test_client.py")

model_deployment_example()
```

---

## 추가 학습 자료

### 권장 도서
- **"밑바닥부터 시작하는 딥러닝"** - 사이토 고키
- **"핸즈온 머신러닝"** - 오렐리앙 제롱
- **"파이썬 머신러닝 완벽 가이드"** - 권철민
- **"Deep Learning"** - Ian Goodfellow, Yoshua Bengio, Aaron Courville
- **"Pattern Recognition and Machine Learning"** - Christopher Bishop

### 온라인 강의
- **Coursera**: Deep Learning Specialization (Andrew Ng)
- **edX**: MIT Introduction to Machine Learning
- **Udacity**: Deep Learning Nanodegree
- **Fast.ai**: Practical Deep Learning for Coders
- **Stanford CS231n**: Convolutional Neural Networks for Visual Recognition

### 실습 플랫폼
- **Kaggle**: 데이터 과학 경진대회 플랫폼
- **Google Colab**: 무료 GPU 제공 Jupyter 환경
- **Papers with Code**: 최신 논문과 코드
- **Towards Data Science**: 머신러닝 블로그 플랫폼
- **GitHub**: 오픈소스 프로젝트

### 유용한 라이브러리
- **딥러닝 프레임워크**: TensorFlow, PyTorch, Keras
- **전통적 머신러닝**: Scikit-learn, XGBoost, LightGBM
- **컴퓨터 비전**: OpenCV, PIL/Pillow, Albumentations
- **자연어 처리**: NLTK, spaCy, Transformers (Hugging Face)
- **데이터 처리**: Pandas, NumPy, Dask
- **시각화**: Matplotlib, Seaborn, Plotly, Bokeh

### 최신 동향
- **Transformer 아키텍처**: BERT, GPT, T5
- **컴퓨터 비전**: Vision Transformer, EfficientNet
- **생성 모델**: GAN, VAE, Diffusion Models
- **강화학습**: Deep Q-Learning, Policy Gradient
- **메타학습**: Few-shot Learning, MAML
- **설명 가능한 AI**: LIME, SHAP, GradCAM

---

## 학습 로드맵

### 초급 (1-2개월)
1. **Python 기초 문법 숙달**
   - 변수, 함수, 클래스, 모듈
   - 리스트, 딕셔너리, 튜플 활용
   - 파일 입출력, 예외 처리

2. **수학 및 통계 기초**
   - 선형대수: 벡터, 행렬 연산
   - 확률과 통계: 분포, 가설검정
   - 미적분: 편미분, 연쇄법칙

3. **라이브러리 활용**
   - NumPy: 배열 연산
   - Pandas: 데이터 조작
   - Matplotlib: 시각화

4. **간단한 프로젝트**
   - 데이터 탐색 및 시각화
   - 기본적인 분류/회귀 문제

### 중급 (3-4개월)
1. **머신러닝 기초**
   - 지도/비지도/강화학습 개념
   - 주요 알고리즘 이해
   - 모델 평가 및 검증

2. **딥러닝 입문**
   - 신경망 기초 이론
   - TensorFlow/Keras 활용
   - 손실함수, 최적화 알고리즘

3. **실전 프로젝트**
   - MNIST 손글씨 분류
   - 이미지 분류 (CIFAR-10)
   - 간단한 자연어 처리

4. **모델 개선**
   - 하이퍼파라미터 튜닝
   - 정규화 기법
   - 데이터 증강

### 고급 (5-6개월)
1. **고급 아키텍처**
   - CNN 심화 (ResNet, DenseNet)
   - RNN 심화 (LSTM, GRU, Attention)
   - Transformer 이해

2. **전문 분야**
   - 컴퓨터 비전: 객체 검출, 세그멘테이션
   - 자연어 처리: 언어 모델, 기계 번역
   - 생성 모델: GAN, VAE

3. **실무 기술**
   - 모델 배포 (Flask, FastAPI)
   - 클라우드 서비스 (AWS, GCP, Azure)
   - MLOps: 모델 관리, 모니터링

4. **연구 및 개발**
   - 최신 논문 읽기
   - 오픈소스 기여
   - 개인 프로젝트 포트폴리오

### 전문가 (6개월 이상)
1. **특화 분야 심화**
   - 선택한 분야의 최신 기술
   - 산업별 응용 사례
   - 연구 동향 파악

2. **리더십 및 협업**
   - 팀 프로젝트 리딩
   - 기술 멘토링
   - 컨퍼런스 발표

3. **지속적 학습**
   - 새로운 프레임워크 학습
   - 다른 분야와의 융합
   - 창의적 문제 해결

> **참고**: 꾸준한 실습과 프로젝트 경험이 가장 중요합니다. 이론과 실습의 균형을 맞춰 학습하고, 실제 문제를 해결하는 경험을 쌓으세요!