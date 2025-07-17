# 📊 Machine Learning 이론

##### 🗓️ 2025.07.16
##### 📝 Writer : Moon19ht

---

## 📚 목차

1. [머신러닝 모델 평가 종합 실습](#1-머신러닝-모델-평가-종합-실습)
2. [Matplotlib & Seaborn 데이터 시각화 완전 정복](#2-matplotlib--seaborn-데이터-시각화-완전-정복)
3. [자연어 처리 및 텍스트 분석 종합 실습](#3-자연어-처리-및-텍스트-분석-종합-실습)

---

## 1. 머신러닝 모델 평가 종합 실습

### 1.1 목표 및 개요
- **이진분류 모델 평가지표** 이해 및 실습
- **회귀 모델 평가지표** 이해 및 실습
- **혼동행렬, ROC 곡선, 회귀 평가지표** 시각화

### 1.2 사용 데이터셋
- **유방암 데이터셋**: 이진분류 평가 실습
- **캘리포니아 주택가격 데이터셋**: 회귀 평가 실습
- **아이리스 데이터셋**: 데이터 시각화 예시

### 1.3 이진분류 모델 평가 (유방암 데이터셋)

#### 1.3.1 데이터 준비 및 전처리
```python
# 유방암 데이터셋 로드
cancer = load_breast_cancer()
X = pd.DataFrame(cancer.data, columns=cancer.feature_names)
y = cancer.target

# 타겟 변수 변환 (0: 악성(malignant) -> 1, 1: 양성(benign) -> 0)
y_changed = np.where(y == 0, 1, 0)
```

#### 1.3.2 혼동행렬 (Confusion Matrix)
- **TN (True Negative)**: 양성을 양성으로 예측
- **FP (False Positive)**: 양성을 악성으로 예측
- **FN (False Negative)**: 악성을 양성으로 예측
- **TP (True Positive)**: 악성을 악성으로 예측

#### 1.3.3 분류 평가지표
- **정확도 (Accuracy)**: 전체 예측 중 올바른 예측의 비율
- **정밀도 (Precision)**: 예측한 양성 중 실제 양성의 비율
- **재현율 (Recall)**: 실제 양성 중 예측한 양성의 비율
- **F1-score**: 정밀도와 재현율의 조화평균

#### 1.3.4 ROC 곡선 및 AUC
- **ROC 곡선**: 다양한 임계값에서의 TPR vs FPR
- **AUC (Area Under Curve)**: ROC 곡선 아래 면적
- **AUC 해석**: 1에 가까울수록 좋은 모델

### 1.4 회귀 모델 평가 (캘리포니아 주택가격)

#### 1.4.1 회귀 평가지표
- **MAE (Mean Absolute Error)**: 평균 절대 오차
- **MSE (Mean Squared Error)**: 평균 제곱 오차
- **RMSE (Root Mean Squared Error)**: 평균 제곱근 오차
- **R² (R-squared)**: 결정계수

#### 1.4.2 시각화 기법
- **실제값 vs 예측값 산점도**
- **잔차 분석 (Residual Plot)**
- **예측값 분포 히스토그램**

---

## 2. Matplotlib & Seaborn 데이터 시각화 완전 정복

### 2.1 환경 설정 및 기초

#### 2.1.1 라이브러리 Import 및 한글 폰트 설정
```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import font_manager, rc
import seaborn as sns

# 한글 폰트 설정
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/H2GTRM.TTF").get_name()
plt.rcParams['font.family'] = font_name
plt.rcParams['axes.unicode_minus'] = False
```

#### 2.1.2 matplotlib 기본 구조
- **Figure**: 전체 차트 영역
- **Axes**: 실제 그래프가 그려지는 영역
- **Axis**: x축, y축
- **Artist**: 차트의 모든 요소 (선, 점, 텍스트 등)

### 2.2 기본 차트 생성

#### 2.2.1 라인 차트 (Line Chart)
```python
plt.figure(figsize=(12, 8))
plt.plot(x, y, label='데이터', marker='o', linewidth=2, markersize=8)
plt.title('제목', fontsize=16, fontweight='bold')
plt.xlabel('X축', fontsize=12)
plt.ylabel('Y축', fontsize=12)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
```

#### 2.2.2 데이터 타입별 처리
- **List vs NumPy 벡터 연산**의 차이점
- **List comprehension**을 활용한 데이터 변환
- **NumPy array**의 벡터화 연산

### 2.3 고급 시각화 기법

#### 2.3.1 Seaborn 스타일 적용
- **darkgrid**: 어두운 배경 + 격자
- **whitegrid**: 밝은 배경 + 격자
- **dark**: 어두운 배경 (격자 없음)
- **white**: 밝은 배경 (격자 없음)
- **ticks**: 최소한의 스타일

#### 2.3.2 다중 함수 비교 차트
```python
plt.subplot(2, 1, 1)  # 서브플롯 생성
plt.plot(x, x, label='선형 함수 (y = x)', color='#2E8B57', linewidth=3)
plt.plot(x, x**2, label='2차 함수 (y = x²)', color='#4169E1', linewidth=3)
plt.plot(x, x**3, label='3차 함수 (y = x³)', color='#DC143C', linewidth=3)
```

### 2.4 통계적 시각화

#### 2.4.1 히스토그램 (Histogram)
- **데이터 분포** 시각화
- **bin 개수** 조정을 통한 해상도 조절
- **밀도 히스토그램** vs **빈도 히스토그램**

#### 2.4.2 확률분포 시각화
- **정규분포** 시각화
- **커널 밀도 추정 (KDE)**
- **다양한 분포 비교 분석**

### 2.5 실무 응용
- **서브플롯**을 활용한 종합 분석
- **함수별 변화율(기울기)** 비교
- **고급 색상 팔레트** 활용

---

## 3. 자연어 처리 및 텍스트 분석 종합 실습

### 3.1 목표 및 개요
- **텍스트 전처리 및 벡터화** 기법 이해
- **한글과 영어 텍스트 분석** 비교
- **감정 분석 모델** 구축 및 평가
- **인터랙티브 시각화**를 통한 결과 표현

### 3.2 텍스트 분석 기초 이론

#### 3.2.1 텍스트 분석의 핵심 개념
텍스트 분석은 비정형 텍스트 데이터를 머신러닝이 처리할 수 있는 수치형 데이터로 변환하는 과정입니다.

#### 3.2.2 주요 단계
1. **토큰화(Tokenization)**: 텍스트를 단어 단위로 분리
2. **어휘사전 구축**: 단어에 고유 번호 할당
3. **벡터화**: 텍스트를 수치 벡터로 변환
4. **모델 학습**: 머신러닝 알고리즘 적용

### 3.3 벡터화 방법

#### 3.3.1 Count Vectorizer
```python
from sklearn.feature_extraction.text import CountVectorizer

vect = CountVectorizer()
vect.fit(sample_texts)
bag_of_words = vect.transform(sample_texts)
```

**특징**:
- 단어 빈도수 기반
- 불용어 제거 가능
- N-gram 적용 가능

#### 3.3.2 TF-IDF (Term Frequency-Inverse Document Frequency)
```python
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer()
tfidf.fit(sample_texts)
tfidf_matrix = tfidf.transform(sample_texts)
```

**특징**:
- **TF (Term Frequency)**: 단어 빈도수가 높을수록 중요
- **IDF (Inverse Document Frequency)**: 문서 빈도수가 낮을수록 중요
- 자주 등장하지만 여러 문서에 공통으로 나타나는 단어는 가중치가 낮아짐

### 3.4 한글 텍스트 분석

#### 3.4.1 KoNLPy를 이용한 형태소 분석
```python
from konlpy.tag import Okt

okt = Okt()
sample_korean = "안녕하세요 만나서 반갑습니다."

# 형태소 분리
morphs = okt.morphs(sample_korean)
# 명사 추출
nouns = okt.nouns(sample_korean)
# 구문 추출
phrases = okt.phrases(sample_korean)
```

#### 3.4.2 한글 토크나이저 함수
```python
def korean_tokenizer(text):
    """한글 텍스트를 형태소 단위로 토큰화"""
    return okt.morphs(text)

def korean_tokenizer_with_stopwords(text):
    """불용어 제거가 포함된 한글 토크나이저"""
    words = okt.morphs(text)
    return [word for word in words if word not in stop_words_korean]
```

### 3.5 감정 분석 모델 구축

#### 3.5.1 데이터셋
- **네이버 영화 리뷰**: 한글 감정 분석 (긍정/부정)
- **IMDB 영화 리뷰**: 영어 감정 분석 (긍정/부정)

#### 3.5.2 모델 학습 과정
1. **텍스트 전처리**: 정규화, 토큰화, 불용어 제거
2. **벡터화**: CountVectorizer 또는 TF-IDF 적용
3. **모델 학습**: 로지스틱 회귀 등 분류 알고리즘 적용
4. **모델 평가**: 정확도, 분류 리포트, 혼동행렬

### 3.6 인터랙티브 시각화

#### 3.6.1 Plotly 활용
```python
import plotly.graph_objects as go
import plotly.express as px

# 인터랙티브 산점도
fig = px.scatter(df, x='x', y='y', color='category', 
                 title='인터랙티브 산점도')
fig.show()
```

#### 3.6.2 시각화 종류
- **워드 클라우드**: 단어 빈도 시각화
- **감정 분포 차트**: 긍정/부정 비율
- **모델 성능 비교**: 다양한 벡터화 방법 비교

---

## 📋 핵심 요약

### 머신러닝 모델 평가
- **이진분류**: 혼동행렬, 정밀도, 재현율, F1-score, ROC-AUC
- **회귀**: MAE, MSE, RMSE, R²
- **시각화**: 혼동행렬 히트맵, ROC 곡선, 잔차 분석

### 데이터 시각화
- **Matplotlib**: 기본 차트 생성, 서브플롯 활용
- **Seaborn**: 통계적 시각화, 고급 스타일링
- **한글 폰트 설정**: 시스템 폰트 활용

### 자연어 처리
- **텍스트 벡터화**: CountVectorizer, TF-IDF
- **한글 처리**: KoNLPy, 형태소 분석
- **감정 분석**: 로지스틱 회귀, 분류 평가
