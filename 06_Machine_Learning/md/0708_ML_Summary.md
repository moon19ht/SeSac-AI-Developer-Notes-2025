# 📊 Machine Learning 이론

##### 🗓️ 2025.07.08
##### 📝 Writer : Moon19ht

---

## 📚 목차

1. [회귀 분석 모델 비교](#1-회귀-분석-모델-비교)
2. [이미지 분류 모델 비교](#2-이미지-분류-모델-비교)
3. [이미지 처리 및 데이터 변환](#3-이미지-처리-및-데이터-변환)
4. [실제 프로젝트: 꽃 분류 시스템](#4-실제-프로젝트-꽃-분류-시스템)
5. [성능 비교 및 분석](#5-성능-비교-및-분석)
6. [핵심 포인트](#6-핵심-포인트)
7. [다음 학습 과제](#7-다음-학습-과제)

---

## 1. 회귀 분석 모델 비교

### 데이터셋: 당뇨병 예측

#### 데이터 특성
- **샘플 수**: 442개
- **특성 수**: 10개 (나이, 성별, BMI, 혈압, 혈청 수치 등)
- **목표**: 1년 후 당뇨병 진행도 예측
- **특징**: 모든 특성이 정규화되어 제공됨

#### 특성 설명
- **age**: 나이
- **sex**: 성별
- **bmi**: 체질량 지수
- **bp**: 평균 혈압
- **s1**: tc, 총 혈청 콜레스테롤
- **s2**: ldl, 저밀도 지단백질
- **s3**: hdl, 고밀도 지단백질
- **s4**: tch, 총 콜레스테롤 / HDL 비율
- **s5**: ltg, 혈청 중성지방 로그 값
- **s6**: glu, 혈당 수치

### 회귀 모델 성능 비교

#### 1. Linear Regression (선형 회귀)
```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
```
- **특징**: 가장 기본적인 회귀 모델
- **성능**: 훈련셋 R² = 0.5304, 테스트셋 R² = 0.4694
- **장점**: 해석이 쉽고 빠름
- **단점**: 복잡한 관계 포착 한계

#### 2. Ridge Regression (L2 정규화)
```python
from sklearn.linear_model import Ridge
model = Ridge(alpha=0.1)
```
- **특징**: L2 정규화로 과적합 방지
- **성능**: 훈련셋 R² = 0.5225, 테스트셋 R² = 0.4723
- **장점**: 계수 크기 제한으로 안정성 향상
- **하이퍼파라미터**: alpha (정규화 강도)

#### 3. Lasso Regression (L1 정규화)
```python
from sklearn.linear_model import Lasso
model = Lasso(alpha=0.1)
```
- **특징**: L1 정규화로 특성 선택 효과
- **성능**: 훈련셋 R² = 0.5202, 테스트셋 R² = 0.4752
- **장점**: 불필요한 특성의 계수를 0으로 만듦
- **특징**: 자동 특성 선택 기능

#### 4. Decision Tree Regressor (의사결정트리 회귀)
```python
from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor()
```
- **특징**: 비선형 관계 포착 가능
- **성능**: 훈련셋 R² = 1.0000, 테스트셋 R² = -0.0732
- **문제점**: 심각한 과적합 발생
- **주의**: 테스트셋 성능이 음수 (매우 위험)

#### 5. Random Forest Regressor (랜덤포레스트 회귀)
```python
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(random_state=0, n_estimators=300, max_depth=3)
```
- **특징**: 의사결정트리의 앙상블
- **성능**: 훈련셋 R² = 0.5810, 테스트셋 R² = 0.4800
- **장점**: 과적합 위험 감소, 특성 중요도 제공
- **하이퍼파라미터**: n_estimators, max_depth

#### 6. Gradient Boosting Regressor (그라디언트 부스팅)
```python
from sklearn.ensemble import GradientBoostingRegressor
model = GradientBoostingRegressor(random_state=0, n_estimators=10, max_depth=3, learning_rate=0.1)
```
- **특징**: 순차적 학습으로 오류 보정
- **성능**: 훈련셋 R² = 0.5086, 테스트셋 R² = 0.4397
- **하이퍼파라미터**: learning_rate (학습 속도 조절)

#### 7. XGBoost Regressor
```python
from xgboost import XGBRegressor
model = XGBRegressor(random_state=0, n_estimators=10, max_depth=3, learning_rate=0.1)
```
- **특징**: 고성능 그라디언트 부스팅 구현
- **성능**: 훈련셋 R² = 0.4964, 테스트셋 R² = 0.4179
- **장점**: Kaggle 대회에서 자주 우승하는 알고리즘

---

## 2. 이미지 분류 모델 비교

### 데이터셋: 손글씨 숫자 분류

#### 데이터 특성
- **샘플 수**: 1,797개 (숫자 0-9)
- **이미지 크기**: 8×8 픽셀 (64개 특성)
- **색상**: 흑백 (grayscale)
- **목표**: 0-9 숫자 분류 (10개 클래스)

#### 데이터 전처리
```python
# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1, test_size=0.3)
# 훈련 데이터: (1257, 64), 테스트 데이터: (540, 64)
```

### 분류 모델 성능 비교

#### 1. Logistic Regression (로지스틱 회귀)
```python
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(solver='lbfgs', max_iter=5000, random_state=0)
```
- **성능**: 훈련셋 = 1.0000, 테스트셋 = 0.9685
- **특징**: 확률 기반 선형 분류
- **장점**: 빠르고 해석 가능
- **다중 분류**: One-vs-Rest 방식 사용

#### 2. K-Nearest Neighbors (KNN)
```python
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=3)
```
- **성능**: 훈련셋 = 0.9889, 테스트셋 = 0.9889
- **특징**: 거리 기반 분류
- **장점**: 단순하고 직관적
- **단점**: 계산 비용이 높음

#### 3. Decision Tree (의사결정트리)
```python
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(max_depth=5)
```
- **성능**: 훈련셋 = 0.6866, 테스트셋 = 0.6796
- **특징**: 규칙 기반 분류
- **문제점**: 성능이 상대적으로 낮음
- **개선**: max_depth로 과적합 방지

#### 4. Random Forest (랜덤포레스트)
```python
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(max_depth=4, n_estimators=100, random_state=0)
```
- **성능**: 훈련셋 = 0.9387, 테스트셋 = 0.9370
- **특징**: 의사결정트리의 앙상블
- **장점**: 과적합 방지, 안정적 성능

#### 5. Gradient Boosting (그라디언트 부스팅)
```python
from sklearn.ensemble import GradientBoostingClassifier
model = GradientBoostingClassifier(max_depth=4, n_estimators=100, random_state=0, learning_rate=0.1)
```
- **성능**: 훈련셋 = 1.0000, 테스트셋 = 0.9574
- **특징**: 순차적 학습으로 성능 향상
- **주의**: 과적합 경향 (훈련셋 100% 정확도)

---

## 3. 이미지 처리 및 데이터 변환

### 기본 이미지 처리

#### PIL을 이용한 이미지 읽기
```python
import PIL.Image as pilimg
import numpy as np

# 이미지 읽기 및 변환
img = pilimg.open("./img/1.jpg")
pix = np.array(img)  # numpy 배열로 변환
print(f"이미지 형태: {pix.shape}")  # (높이, 너비, 채널)
```

#### 이미지 형태 이해
- **컬러 이미지**: (높이, 너비, 3) - RGB 3채널
- **흑백 이미지**: (높이, 너비) - 단일 채널
- **픽셀 값 범위**: 0-255 (8bit)

### 다중 이미지 처리

#### 폴더별 배치 처리
```python
import os

path = "./img/animal"
filenameList = os.listdir(path)
imageList = []

for filename in filenameList:
    img = pilimg.open(path + "/" + filename)
    img = img.resize((80, 80))  # 크기 통일
    img = np.array(img)
    imageList.append(img)

# NPZ 파일로 저장
np.savez("./data/data_animal.npz", data=imageList)
```

### 머신러닝을 위한 데이터 변환

#### 차원 변환
```python
# 4차원 → 2차원 변환 (머신러닝용)
# 원본: (이미지개수, 높이, 너비, 채널)
# 변환: (이미지개수, 높이×너비×채널)
X_reshaped = np.array(imageList).reshape(len(imageList), -1)
```

#### 정규화
```python
# 픽셀 값을 0-1 범위로 정규화
X_normalized = X_reshaped / 255.0
```

#### 라벨링
```python
# 폴더명 기반 자동 라벨링
# daisy=0, dandelion=1, rose=2, sunflower=3, tulip=4
```

---

## 4. 실제 프로젝트: 꽃 분류 시스템

### 프로젝트 개요
- **목표**: 5가지 꽃 종류 자동 분류
- **데이터**: 총 4,317개 이미지
- **꽃 종류**: daisy(764개), dandelion(1052개), sunflower(733개), rose(784개), tulip(984개)

### 데이터 처리 파이프라인

#### 1. 이미지 전처리 함수
```python
def makeData(folder, label):
    data = []
    labels = []
    path = "./img/flowers" + "/" + folder
    
    for filename in os.listdir(path):
        kind = imghdr.what(path + "/" + filename)
        if kind in ["gif", "png", "jpg", "jpeg"]:
            img = pilimg.open(path + "/" + filename)
            resize_img = img.resize((80, 80))
            pixel = np.array(resize_img)
            
            if pixel.shape == (80, 80, 3):
                data.append(pixel)
                labels.append(label)
    
    np.savez(f"./data/{folder}.npz", data=data, targets=labels)
```

#### 2. 데이터 통합
```python
def loadData():
    # 각 꽃 종류별 NPZ 파일 로드
    daisy = np.load("./data/daisy.npz")
    dandelion = np.load("./data/dandelion.npz")
    # ... 다른 꽃들도 로드
    
    # 모든 데이터 통합
    data = np.concatenate((daisy["data"], dandelion["data"], ...))
    target = np.concatenate((daisy["targets"], dandelion["targets"], ...))
    
    return data, target
```

#### 3. 전처리 및 모델 학습
```python
# 차원 축소 및 정규화
data = data.reshape(data.shape[0], 80*80*3)  # (4317, 19200)
data = data / 255.0  # 정규화

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.5)

# KNN 모델 학습
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)
```

### 모델 성능 결과

#### 기본 성능
- **훈련셋 정확도**: 45.32%
- **테스트셋 정확도**: 32.93%
- **문제점**: 과적합 발생 (성능 차이가 큼)

#### K값 최적화 결과
| K값 | 테스트셋 정확도 |
|-----|----------------|
| 3   | 32.10%         |
| 5   | 32.93%         |
| 7   | **34.09%**     |
| 9   | 34.04%         |
| 11  | 33.67%         |

- **최적 K값**: 7 (정확도 34.09%)

#### 상세 분류 성능
| 꽃 종류     | Precision | Recall | F1-Score |
|-------------|-----------|---------|----------|
| daisy       | 0.18      | 0.07    | 0.10     |
| dandelion   | 0.30      | 0.86    | 0.44     |
| sunflower   | 0.54      | 0.34    | 0.42     |
| rose        | 0.45      | 0.14    | 0.22     |
| tulip       | 0.47      | 0.09    | 0.15     |

---

## 5. 성능 비교 및 분석

### 회귀 모델 성능 순위

| 순위 | 모델명               | 테스트셋 R² | 특징                    |
|------|---------------------|-------------|-------------------------|
| 1    | Random Forest       | 0.4800      | 앙상블, 과적합 방지      |
| 2    | Lasso              | 0.4752      | L1 정규화, 특성 선택     |
| 3    | Ridge              | 0.4723      | L2 정규화, 안정성       |
| 4    | Linear Regression  | 0.4694      | 기본 모델               |
| 5    | Gradient Boosting  | 0.4397      | 순차적 학습             |
| 6    | XGBoost            | 0.4179      | 고성능 부스팅           |
| 7    | Decision Tree      | -0.0732     | 심각한 과적합           |

### 분류 모델 성능 순위

| 순위 | 모델명               | 테스트셋 정확도 | 특징                    |
|------|---------------------|----------------|-------------------------|
| 1    | KNN                | 98.89%         | 거리 기반, 안정적        |
| 2    | Logistic Regression| 96.85%         | 확률 기반, 빠름         |
| 3    | Gradient Boosting  | 95.74%         | 순차적 학습             |
| 4    | Random Forest      | 93.70%         | 앙상블 방법             |
| 5    | Decision Tree      | 67.96%         | 단순 규칙 기반          |

### 주요 관찰 사항

#### 회귀 분석
- **Random Forest**가 가장 좋은 성능
- **Decision Tree**는 과적합으로 실패
- **정규화 기법**(Ridge, Lasso)이 안정적
- **앙상블 방법**이 전반적으로 우수

#### 이미지 분류
- **KNN**이 최고 성능 (단순하지만 효과적)
- **손글씨 숫자**는 상대적으로 쉬운 문제
- **꽃 분류**는 훨씬 어려운 문제 (34% vs 99%)

---

## 6. 핵심 포인트

### 회귀 vs 분류

#### 회귀 분석 특징
- **목표**: 연속적인 수치 예측
- **평가 지표**: R², MSE, MAE
- **해석**: 결정계수 (1에 가까울수록 좋음)
- **주의**: 음수 R²는 매우 위험한 신호

#### 분류 분석 특징
- **목표**: 카테고리 예측
- **평가 지표**: 정확도, Precision, Recall, F1-Score
- **다중 분류**: 여러 클래스 동시 처리
- **불균형**: 클래스별 데이터 개수 차이 주의

### 이미지 데이터 처리

#### 전처리 중요성
1. **크기 통일**: 모든 이미지를 동일한 크기로 조정
2. **정규화**: 픽셀 값을 0-1 범위로 변환
3. **차원 변환**: 4차원 → 2차원 (머신러닝용)
4. **데이터 형식**: NPZ 파일로 효율적 저장

#### 성능 향상 방법
- **해상도 증가**: 80×80 → 더 높은 해상도
- **데이터 증강**: 회전, 뒤집기, 밝기 조정
- **딥러닝 활용**: CNN 모델 사용
- **전이 학습**: 사전 훈련된 모델 활용

### 과적합 탐지 및 방지

#### 과적합 신호
- 훈련셋과 테스트셋 성능 차이가 큼
- 훈련셋 성능이 비현실적으로 높음 (100%)
- 테스트셋 성능이 급격히 낮음

#### 방지 방법
1. **정규화**: Ridge (L2), Lasso (L1)
2. **앙상블**: Random Forest, Gradient Boosting
3. **하이퍼파라미터 제한**: max_depth, min_samples_leaf
4. **교차 검증**: K-Fold Cross Validation
5. **더 많은 데이터**: 데이터 수집 또는 증강

---

## 7. 다음 학습 과제

### 단기 과제 (1-2주)
1. **더 많은 알고리즘 시도**
   - SVM (Support Vector Machine)
   - Naive Bayes
   - Neural Networks

2. **하이퍼파라미터 최적화**
   - GridSearchCV 활용
   - RandomizedSearchCV 사용
   - Optuna를 이용한 베이지안 최적화

3. **특성 엔지니어링**
   - PCA를 이용한 차원 축소
   - LDA를 이용한 특성 선택
   - 이미지 특성 추출 (HOG, SIFT)

### 중기 과제 (1개월)
1. **딥러닝 도입**
   - CNN (Convolutional Neural Network) 학습
   - TensorFlow/PyTorch 사용법
   - 전이 학습 (Transfer Learning)

2. **실제 프로젝트 확장**
   - 웹 애플리케이션 개발 (Flask/Django)
   - 모바일 앱 연동
   - 실시간 이미지 분류

3. **성능 개선**
   - 데이터 증강 기법 적용
   - 앙상블 방법 심화
   - 모델 파이프라인 최적화

### 장기 과제 (3개월)
1. **전문 분야 특화**
   - 의료 이미지 분석
   - 자율주행 객체 인식
   - 자연어 처리와 결합

2. **MLOps 구축**
   - 모델 배포 자동화
   - 모니터링 시스템 구축
   - A/B 테스트 설계

3. **연구 및 논문**
   - 새로운 알고리즘 개발
   - 성능 벤치마크 비교
   - 학회 발표 준비
