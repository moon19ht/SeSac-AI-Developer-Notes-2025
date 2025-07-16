# 📊 Machine Learning 이론

##### 🗓️ 2025.07.07
##### 📝 Writer : Moon19ht

---

## 📚 목차

1. [머신러닝 모델링 워크플로우](#1-머신러닝-모델링-워크플로우)
2. [분류 알고리즘](#2-분류-알고리즘)
3. [다중 레이블 분류](#3-다중-레이블-분류)
4. [회귀 분석](#4-회귀-분석)
5. [규제 기법](#5-규제-기법)
6. [실습 데이터셋](#6-실습-데이터셋)
7. [성능 비교 결과](#7-성능-비교-결과)
8. [핵심 포인트](#8-핵심-포인트)
9. [다음 학습 과제](#9-다음-학습-과제)

---

## 1. 머신러닝 모델링 워크플로우
### 1. 데이터 준비 (80%의 시간을 투자해야 하는 핵심 단계)

#### 목표: 모델이 학습할 수 있는 **정제된 특징(feature) 공간**을 구성

실제 성능은 이 단계에서 거의 결정된다.

##### 데이터 수집

* API, 웹 크롤링, DB, CSV, 센서 등 다양한 방식으로 수집
* 실무에서는 정형/비정형 데이터 혼합도 많음

##### 전처리

* **결측치 처리**: 제거(dropna), 평균/중앙값/모드 대체, KNN/모델 기반 대체
* **이상치 처리**: IQR, Z-score, 시각화(boxplot) 기반 제거 또는 수정
* **중복 제거**: `.drop_duplicates()`
* **데이터 타입 변환**: 날짜형, 범주형 처리

##### 정규화 / 표준화

* 정규화 (MinMaxScaler): \[0, 1] 스케일
* 표준화 (StandardScaler): 평균 0, 분산 1
* 트리 기반 모델은 필요 없음, 선형 모델/딥러닝 계열은 중요

##### 차원 축소 / 특성 선택

* PCA, t-SNE, UMAP (비지도 차원 축소)
* SelectKBest, Recursive Feature Elimination (지도 특성 선택)
* 중요 변수 추출: Random Forest feature importance, SHAP, LIME

##### 범주형 처리

* One-Hot Encoding (pandas `get_dummies()`, `OneHotEncoder`)
* Label Encoding (순서 있는 경우에만), Ordinal Encoding

---

### 2. 데이터셋 분할 (Train/Test Split)

#### 목표: 모델이 훈련 데이터에 과적합되지 않고 **미래를 일반화(generalization)** 할 수 있게 한다.

* 일반 비율: `train:test = 7:3`, `8:2` 추천
* `train_test_split()` 함수 사용
  예:

  ```python
  from sklearn.model_selection import train_test_split
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
  ```
* **교차검증(K-Fold Cross Validation)** 도 도입 가능 (특히 데이터가 적을 때)

---

### 3. 알고리즘 선택 및 학습 (모델 훈련)

#### 목표: 문제 유형(분류/회귀/클러스터링 등)에 적합한 알고리즘을 선택하고 하이퍼파라미터 튜닝으로 최적화한다.

##### 분류(Classification) 문제일 경우 주요 알고리즘

| 알고리즘                                       | 설명               | 특징                |
| ------------------------------------------ | ---------------- | ----------------- |
| **KNN**                                    | 가장 가까운 k개의 이웃 기준 | 단순, 느림, 정규화 필요    |
| **로지스틱 회귀**                                | 확률 기반 이진 분류      | 선형, 해석 쉬움         |
| **의사결정트리**                                 | 규칙 기반 분기         | 시각화 용이, 과적합 주의    |
| **랜덤포레스트**                                 | 여러 트리의 앙상블       | 강력함, 변수 중요도 파악 가능 |
| **Gradient Boosting / XGBoost / LightGBM** | 부스팅 기반 강력 모델     | Kaggle 우승자 즐겨씀    |
| **SVM**                                    | 마진 최대화 초평면       | 고차원, 느림, 정규화 필수   |

##### 하이퍼파라미터 튜닝

* `GridSearchCV`, `RandomizedSearchCV`, `Optuna` 등 활용
* 하이퍼파라미터 예:

  * KNN: `n_neighbors`
  * RandomForest: `n_estimators`, `max_depth`
  * XGBoost: `learning_rate`, `max_depth`, `n_estimators`

---

### 4. 예측 (Prediction)

#### 목표: 학습된 모델로 **새로운 데이터의 정답을 추정**

```python
y_pred = model.predict(X_test)
```

* 확률 기반 예측이 필요한 경우: `model.predict_proba()`

---

### 5. 성능 평가 (Evaluation)

#### 목표: 모델의 **정확도, 일반화 능력, 오류 원인** 등을 정량적으로 평가

##### 기본 평가지표 (분류)

| 지표                   | 의미                         |
| -------------------- | -------------------------- |
| Accuracy             | 전체 정확도                     |
| Precision            | 양성으로 예측한 것 중 실제 양성 비율      |
| Recall (Sensitivity) | 실제 양성 중 예측에 성공한 비율         |
| F1-Score             | 정밀도와 재현율의 조화 평균            |
| ROC-AUC              | 분류 경계 민감도, 좋은 모델일수록 1에 가까움 |

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
```

##### 상세 분석

* Confusion Matrix (`sklearn.metrics.confusion_matrix`)
* Classification Report (`classification_report`)
* ROC Curve, PR Curve 시각화

---

## 2. 분류 알고리즘

### 1. KNN (K-Nearest Neighbors)

#### 핵심 개념
* **"내 이웃이 누구인가?"**
* 새로운 데이터가 주어졌을 때, **가장 가까운 K개의 이웃의 레이블을 기반으로 예측**
* 거리 기반 알고리즘 → 유클리드 거리 기본 사용

#### 작동 방식
1. 테스트 데이터와 훈련 데이터 간 거리를 계산
2. 가장 가까운 `K개` 이웃 선택
3. 분류일 경우: 다수결 투표로 클래스 결정
4. 회귀일 경우: 이웃의 값의 평균으로 예측값 계산

#### 주요 하이퍼파라미터

| 파라미터          | 설명                                          |
| ------------- | ------------------------------------------- |
| `n_neighbors` | 이웃의 수 (일반적으로 홀수 사용)                         |
| `weights`     | 'uniform' (동일 가중치), 'distance' (가까울수록 영향 ↑) |
| `metric`      | 거리 측정 방식 (기본: 'minkowski' → p=2는 유클리드)      |

```python
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=5, weights='uniform', metric='euclidean')
```

#### 특징 요약

| 항목    | 내용                                    |
| ----- | ------------------------------------- |
| 학습 방식 | 저장 기반 (모델이 별도 학습 없이 저장된 데이터 활용)       |
| 분류/회귀 | 모두 가능                                 |
| 장점    | 이해 쉬움, 파라미터 적음                        |
| 단점    | 느린 예측 속도, 차원의 저주 영향                   |

---

### 2. 로지스틱 회귀 (Logistic Regression)

#### 특징
* 확률 기반 분류 알고리즘
* 선형 모델이지만 시그모이드 함수로 확률값 출력
* 해석이 쉬움 (계수와 절편)

```python
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=1000)
```

---

### 3. 의사결정트리 (Decision Tree)

#### 특징
* 규칙 기반 분기로 예측
* **필연적으로 과대적합** 발생
* **특성의 중요도 파악용**으로 주로 사용
* 시각화가 용이

```python
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(random_state=1)
```

#### 특성 중요도 시각화
```python
def treeChart(model, feature_name):
    n_features = len(model.feature_importances_)
    plt.figure(figsize=(10, 6))
    plt.barh(np.arange(n_features), model.feature_importances_, align="center")
    plt.yticks(np.arange(n_features), feature_name)
    plt.xlabel('특성 중요도')
    plt.title('의사결정트리 특성 중요도')
    plt.show()
```

---

### 4. 랜덤포레스트 (Random Forest)

#### 특징
* 의사결정트리를 랜덤하게 많이 만들어서 평균값으로 예측하는 **앙상블**
* 과대적합 위험을 줄임

#### 주요 하이퍼파라미터
* `random_state`: 재현성을 위해 꼭 지정
* `max_depth`: 트리의 깊이 제한
* `n_estimators`: 결정트리 개수 (너무 크면 시간 소요, 너무 작으면 과대적합)

```python
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(
    random_state=0, 
    max_depth=3, 
    n_estimators=1000
)
```

---

## 3. 다중 레이블 분류 (Multi-Label Classification)

### 개념
하나의 샘플이 **여러 개의 클래스(레이블)에 동시에 속할 수 있는** 분류 문제

### 예시
* **이메일 분류**: 하나의 이메일이 "업무", "중요", "개인" 등 여러 카테고리에 동시 속함
* **영화 장르 분류**: 하나의 영화가 "액션", "코미디", "로맨스" 등 여러 장르에 속함
* **의료 진단**: 환자가 여러 질병을 동시에 가질 수 있음

### MultiOutputClassifier

```python
from sklearn.svm import SVC
from sklearn.multioutput import MultiOutputClassifier

base_svm = SVC(kernel='linear', probability=True, random_state=42)
multi_label_svm = MultiOutputClassifier(base_svm, n_jobs=-1)
```

#### 특징
* 각 출력(레이블)에 대해 독립적인 분류기를 훈련
* One-vs-Rest 전략과 유사하게 작동
* 병렬 처리 가능 (`n_jobs=-1`)

### 다중 레이블 평가 지표

| 지표                          | 설명                                |
| --------------------------- | --------------------------------- |
| **Hamming Loss**            | 잘못 예측된 레이블의 비율 (0에 가까울수록 좋음)      |
| **Jaccard Similarity**      | 모든 레이블을 정확히 예측한 샘플의 비율 (엄격한 지표)  |
| **Micro F1**                | 전체 TP, FP, FN을 합산하여 계산           |
| **Macro F1**                | 각 레이블에 대한 F1-score를 계산한 후 평균     |

```python
from sklearn.metrics import hamming_loss, jaccard_score, f1_score

# 햄밍 손실
h_loss = hamming_loss(y_test, y_pred)

# Jaccard 유사도
jaccard_similarity = jaccard_score(y_test, y_pred, average='samples')

# F1-스코어
f1_micro = f1_score(y_test, y_pred, average='micro')
f1_macro = f1_score(y_test, y_pred, average='macro')
```

---

## 4. 회귀 분석

### 개념
연속적인 수치 값을 예측하는 머신러닝 기법

### 1. 단순 선형 회귀

#### 특징
* **특성이 딱 하나**인 단순한 회귀 분석
* 수식: `y = ax + b` (a: 기울기, b: 절편)

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

print("기울기:", model.coef_)
print("절편:", model.intercept_)
```

---

### 2. 다중 선형 회귀

#### 특징
* 여러 특성을 사용한 회귀
* 수식: `y = w1*x1 + w2*x2 + ... + wn*xn + b`
* **다중공선성 문제** 발생 가능

#### 문제점
* **공분산**: 특성간 서로 영향을 주고받음
* **처리 능력 저하**: 특성의 개수가 많을 경우
* **해결책**: 규제(Regularization) 기법 적용

---

### 3. KNN 회귀

```python
from sklearn.neighbors import KNeighborsRegressor

model = KNeighborsRegressor(n_neighbors=3)
model.fit(X_train, y_train)
```

#### 특징
* 이웃의 값의 평균으로 예측
* 분류와 동일한 원리

---

## 5. 규제 기법 (Regularization)

### 목적
* **과대적합 방지**
* 가중치를 규제하여 **일반화 성능 향상**

### 1. Ridge 회귀 (L2 정규화)

#### 특징
* 계수를 완전히 0으로 만들지는 못함
* 계수의 제곱합에 페널티 부여

```python
from sklearn.linear_model import Ridge

model = Ridge(alpha=10)
model.fit(X_train, y_train)
```

---

### 2. Lasso 회귀 (L1 정규화)

#### 특징
* **불필요한 특성의 계수를 0으로 만듦**
* **특성 선택 효과** 있음
* 모델을 심플하게 만듦

```python
from sklearn.linear_model import Lasso

model = Lasso(alpha=10)
model.fit(X_train, y_train)

# 0이 된 계수들 확인
zero_coef_count = sum(coef == 0 for coef in model.coef_)
print(f"0이 된 계수의 개수: {zero_coef_count}/{len(model.coef_)}")
```

---

### 3. 하이퍼파라미터 alpha

| alpha 값 | 효과                        |
| ------- | ------------------------- |
| **0**   | 규제 없음 (LinearRegression과 동일) |
| **작은 값** | 약한 규제                     |
| **큰 값**  | 강한 규제                     |

#### 적절한 alpha 찾기

```python
alpha_values = [0.1, 1, 10, 100]

for alpha in alpha_values:
    model_ridge = Ridge(alpha=alpha)
    model_ridge.fit(X_train, y_train)
    print(f"Alpha {alpha}: Train {model_ridge.score(X_train, y_train):.4f}, Test {model_ridge.score(X_test, y_test):.4f}")
```

---

## 6. 실습 데이터셋

### 1. Breast Cancer Wisconsin
* **목적**: 유방암 진단 (악성/양성)
* **샘플 수**: 569개
* **특성 수**: 30개
* **특징**: 결측치 없음, 균형잡힌 데이터

### 2. Iris Plants
* **목적**: 붓꽃 종류 분류 (3개 클래스)
* **샘플 수**: 150개 (각 클래스당 50개)
* **특성 수**: 4개
* **특징**: 가장 유명한 분류 데이터셋

### 3. Boston Housing
* **목적**: 주택 가격 예측 (회귀)
* **샘플 수**: 506개
* **특성 수**: 13개
* **특징**: 다중 회귀 분석에 적합

---

## 7. 성능 비교 결과

### Iris 데이터셋 알고리즘 비교

| 알고리즘      | 테스트셋 정확도 |
| --------- | -------- |
| KNN       | 0.9778   |
| 로지스틱 회귀   | 0.9778   |
| 의사결정트리    | 0.9778   |
| 랜덤포레스트    | 0.9778   |

### 보스톤 주택가격 회귀 모델 비교

| 모델              | Alpha | 훈련셋 점수 | 테스트셋 점수 |
| --------------- | ----- | ------ | ------- |
| LinearRegression | None  | 0.7481 | 0.6844  |
| Ridge           | 0.1   | 0.7480 | 0.6838  |
| Ridge           | 10    | 0.7398 | 0.6724  |
| Lasso           | 0.1   | 0.7369 | 0.6660  |
| Lasso           | 10    | 0.5374 | 0.4946  |

---

## 8. 핵심 포인트

### 알고리즘 선택 기준
1. **데이터 크기**: 작으면 KNN, 크면 선형 모델
2. **해석 필요성**: 필요하면 로지스틱 회귀/의사결정트리
3. **성능 우선**: 랜덤포레스트/부스팅 계열
4. **특성 선택**: Lasso 회귀

### 과적합 방지 전략
1. **교차 검증** 사용
2. **규제 기법** 적용 (Ridge/Lasso)
3. **하이퍼파라미터 튜닝**
4. **충분한 데이터** 확보

### 모델 평가 주의사항
* 훈련셋과 테스트셋 점수 **차이** 확인
* **일반화 성능**이 더 중요
* **도메인 지식** 활용한 특성 엔지니어링

---

## 9. 다음 학습 과제

1. **교차 검증**을 통한 더 정확한 모델 평가
2. **앙상블 기법** 심화 학습
3. **특성 엔지니어링** 기법 적용
4. **하이퍼파라미터 자동 튜닝** (Optuna, GridSearchCV)
5. **다른 평가 지표** 활용 (ROC-AUC, PR-AUC)

