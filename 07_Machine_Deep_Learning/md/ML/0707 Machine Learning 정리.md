# 📊 Machine Learning 이론

##### 🗓️ 2025.07.07
##### 📝 Writer : Moon19ht

---

## 📚 목차

---

## ✅ 머신러닝 모델링 워크플로우
### 1. 데이터 준비 (80%의 시간을 투자해야 하는 핵심 단계)

#### 📌 목표: 모델이 학습할 수 있는 **정제된 특징(feature) 공간**을 구성

실제 성능은 이 단계에서 거의 결정된다.

##### 🔹 데이터 수집

* API, 웹 크롤링, DB, CSV, 센서 등 다양한 방식으로 수집
* 실무에서는 정형/비정형 데이터 혼합도 많음

##### 🔹 전처리

* **결측치 처리**: 제거(dropna), 평균/중앙값/모드 대체, KNN/모델 기반 대체
* **이상치 처리**: IQR, Z-score, 시각화(boxplot) 기반 제거 또는 수정
* **중복 제거**: `.drop_duplicates()`
* **데이터 타입 변환**: 날짜형, 범주형 처리

##### 🔹 정규화 / 표준화

* 정규화 (MinMaxScaler): \[0, 1] 스케일
* 표준화 (StandardScaler): 평균 0, 분산 1
* 트리 기반 모델은 필요 없음, 선형 모델/딥러닝 계열은 중요

##### 🔹 차원 축소 / 특성 선택

* PCA, t-SNE, UMAP (비지도 차원 축소)
* SelectKBest, Recursive Feature Elimination (지도 특성 선택)
* 중요 변수 추출: Random Forest feature importance, SHAP, LIME

##### 🔹 범주형 처리

* One-Hot Encoding (pandas `get_dummies()`, `OneHotEncoder`)
* Label Encoding (순서 있는 경우에만), Ordinal Encoding

---

### 2. 데이터셋 분할 (Train/Test Split)

#### 📌 목표: 모델이 훈련 데이터에 과적합되지 않고 **미래를 일반화(generalization)** 할 수 있게 한다.

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

#### 📌 목표: 문제 유형(분류/회귀/클러스터링 등)에 적합한 알고리즘을 선택하고 하이퍼파라미터 튜닝으로 최적화한다.

##### 🔹 분류(Classification) 문제일 경우 주요 알고리즘

| 알고리즘                                       | 설명               | 특징                |
| ------------------------------------------ | ---------------- | ----------------- |
| **KNN**                                    | 가장 가까운 k개의 이웃 기준 | 단순, 느림, 정규화 필요    |
| **로지스틱 회귀**                                | 확률 기반 이진 분류      | 선형, 해석 쉬움         |
| **의사결정트리**                                 | 규칙 기반 분기         | 시각화 용이, 과적합 주의    |
| **랜덤포레스트**                                 | 여러 트리의 앙상블       | 강력함, 변수 중요도 파악 가능 |
| **Gradient Boosting / XGBoost / LightGBM** | 부스팅 기반 강력 모델     | Kaggle 우승자 즐겨씀    |
| **SVM**                                    | 마진 최대화 초평면       | 고차원, 느림, 정규화 필수   |

##### 🔹 하이퍼파라미터 튜닝

* `GridSearchCV`, `RandomizedSearchCV`, `Optuna` 등 활용
* 하이퍼파라미터 예:

  * KNN: `n_neighbors`
  * RandomForest: `n_estimators`, `max_depth`
  * XGBoost: `learning_rate`, `max_depth`, `n_estimators`

---

### 4. 예측 (Prediction)

#### 📌 목표: 학습된 모델로 **새로운 데이터의 정답을 추정**

```python
y_pred = model.predict(X_test)
```

* 확률 기반 예측이 필요한 경우: `model.predict_proba()`

---

### 5. 성능 평가 (Evaluation)

#### 📌 목표: 모델의 **정확도, 일반화 능력, 오류 원인** 등을 정량적으로 평가

##### 🔹 기본 평가지표 (분류)

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

##### 🔹 기본 평가지표 (분류)
#### 🔹 상세 분석

* Confusion Matrix (`sklearn.metrics.confusion_matrix`)
* Classification Report (`classification_report`)
* ROC Curve, PR Curve 시각화

