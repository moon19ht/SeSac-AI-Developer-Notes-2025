# 📊 Machine Learning 이론

##### 🗓️ 2025.07.14
##### 📝 Writer : Moon19ht

---

## 📚 목차

1. [데이터 특성 처리 (범주형 데이터)](#1-데이터-특성-처리-범주형-데이터)
2. [하이퍼파라미터 튜닝](#2-하이퍼파라미터-튜닝)
3. [모델 평가 및 비교](#3-모델-평가-및-비교)
4. [고급 최적화 전략](#4-고급-최적화-전략)
5. [고급 기법 및 다음 단계](#5-고급-기법-및-다음-단계)
6. [체크리스트 및 베스트 프랙티스](#6-체크리스트-및-베스트-프랙티스)
7. [학습 정리 및 다음 단계](#7-학습-정리-및-다음-단계)

---

## 1. 데이터 특성 처리 (범주형 데이터)

### 1.1 범주형 데이터 처리의 필요성

#### 문제점
- 머신러닝 알고리즘은 대부분 숫자형 데이터만 처리 가능
- 문자열 형태의 범주형 데이터는 직접 사용 불가
- 숫자 형태의 범주형 데이터도 잘못 해석될 위험

#### 예시
```python
# 직업분류가 1~16의 숫자로 코딩된 경우
# 1보다 16이 더 큰 값으로 인식되어 모델이 잘못된 중요도를 학습
```

### 1.2 방법 1: `pd.get_dummies()`

#### 특징
- **장점**: 간단하고 직관적, pandas와 잘 통합됨
- **단점**: 숫자형 범주 데이터 인식 못함, 컬럼별 다른 처리 어려움

#### 사용법
```python
# 기본 사용법
data_encoded = pd.get_dummies(data)

# 타겟 변수와 특성 변수 분리
income_columns = [col for col in data_encoded.columns if col.startswith('income_')]
feature_columns = [col for col in data_encoded.columns if not col.startswith('income_')]

X = data_encoded[feature_columns]
y = data_encoded['income_ >50K']  # 타겟 변수
```

#### 적용 예시
```python
# Adult 데이터셋 적용 결과
원본 데이터 컬럼 수: 7
인코딩 후 컬럼 수: 46
```

### 1.3 방법 2: `OneHotEncoder`

#### 특징
- **장점**: 숫자형 범주 데이터 처리 가능, scikit-learn 파이프라인과 호환
- **단점**: 별도 클래스 사용 필요, pandas DataFrame과 분리됨

#### 사용법
```python
from sklearn.preprocessing import OneHotEncoder

# OneHotEncoder 생성
ohe = OneHotEncoder(sparse_output=False)

# 변환 수행
encoded_array = ohe.fit_transform(demo_df)

# 특성명 확인
feature_names = ohe.get_feature_names_out()
```

#### 숫자형 범주 데이터 처리
```python
# 문제: get_dummies는 숫자형 범주를 일반 숫자로 처리
demo_df = pd.DataFrame({
    '숫자특성': [0, 1, 2, 1],  # 범주형이지만 숫자로 표현
    '범주형특성': ['양말', '여우', '양말', '상자']    
})

# 해결방법 1: 문자열 변환 후 get_dummies
demo_df['숫자특성'] = demo_df['숫자특성'].astype(str)

# 해결방법 2: OneHotEncoder 사용 (자동으로 범주로 인식)
```

### 1.4 방법 3: `ColumnTransformer`

#### 특징
- **장점**: 컬럼별 다른 전처리 가능, 복잡한 전처리 파이프라인 구축, 재사용성 높음
- **단점**: 설정이 복잡, 초보자에게 어려움

#### 사용법
```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# 컬럼 구분
numeric_columns = ['age', 'hours-per-week']
categorical_columns = ['workclass', 'education', 'gender', 'occupation']

# ColumnTransformer 생성
ct = ColumnTransformer([
    ("scaling", StandardScaler(), numeric_columns),
    ("onehot", OneHotEncoder(sparse_output=False), categorical_columns)
])

# 변환 수행
transformed_data = ct.fit_transform(ct_data)
```

#### 장점
```python
# 한 번에 여러 전처리 작업 수행
원본 데이터 형태: (32561, 6)
변환된 데이터 형태: (32561, 44)

# 숫자형: StandardScaler 적용
# 범주형: OneHotEncoder 적용
```

### 1.5 방법별 비교 및 권장사항

| 방법 | 장점 | 단점 | 사용 시점 |
|------|------|------| --------|
| **pd.get_dummies()** | 간단하고 직관적<br>pandas와 잘 통합됨 | 숫자형 범주 데이터 인식 못함<br>컬럼별 다른 처리 어려움 | 모든 컬럼이 문자열 범주형<br>간단한 전처리 |
| **OneHotEncoder** | 숫자형 범주 데이터 처리 가능<br>scikit-learn 파이프라인과 호환 | 별도 클래스 사용 필요<br>pandas DataFrame과 분리됨 | 숫자형 범주 데이터 포함<br>ML 파이프라인 구축 |
| **ColumnTransformer** | 컬럼별 다른 전처리 가능<br>복잡한 전처리 파이프라인 구축<br>재사용성 높음 | 설정이 복잡<br>초보자에게 어려움 | 혼합된 데이터 타입<br>복잡한 전처리 필요 |

#### 권장 사용법
1. **간단한 범주형 데이터**: `pd.get_dummies()`
2. **숫자형 범주 데이터**: `OneHotEncoder`
3. **복잡한 혼합 데이터**: `ColumnTransformer`

---

## 2. 하이퍼파라미터 튜닝

### 2.1 하이퍼파라미터 개념

#### 정의
- **하이퍼파라미터**: 모델 학습 전에 미리 설정해야 하는 파라미터
- **특징**: 데이터로부터 학습되지 않고 사용자가 직접 설정
- **중요성**: 모델의 성능과 과적합/과소적합에 직접적 영향

#### 주요 하이퍼파라미터 예시
```python
# SVM
C = [0.1, 1, 10, 100]          # 규제 파라미터
gamma = [1, 0.1, 0.01, 0.001]  # 커널 파라미터  
kernel = ['rbf', 'linear']      # 커널 함수

# RandomForest
n_estimators = [50, 100, 200]     # 트리 개수
max_depth = [None, 3, 10, 20]     # 최대 깊이
min_samples_split = [2, 5, 10]    # 분할을 위한 최소 샘플 수

# GradientBoosting
n_estimators = [50, 100, 200]     # 부스팅 스테이지 수
max_depth = [3, 5, 10]            # 최대 깊이
learning_rate = [0.01, 0.1, 0.2]  # 학습률
```

### 2.2 GridSearchCV 활용

#### 기본 개념
```python
from sklearn.model_selection import GridSearchCV

# 파라미터 그리드 설정
param_grid = {
    'C': [0.1, 1, 10, 100],
    'gamma': [1, 0.1, 0.01, 0.001],
    'kernel': ['rbf', 'linear']
}

# GridSearchCV 설정
grid_search = GridSearchCV(
    estimator=SVC(random_state=42), 
    param_grid=param_grid, 
    cv=5,                    # 5-fold 교차검증
    scoring='accuracy',      # 평가 지표
    n_jobs=-1,              # 모든 CPU 코어 사용
    verbose=1               # 진행상황 출력
)

# 학습 실행
grid_search.fit(X_train, y_train)
```

#### 결과 분석
```python
# 최적 결과 확인
print(f"최적의 파라미터: {grid_search.best_params_}")
print(f"최고 교차검증 점수: {grid_search.best_score_:.4f}")
print(f"최적 모델: {grid_search.best_estimator_}")
```

### 2.3 단일 모델 튜닝 (SVM 예시)

#### SVM 주요 하이퍼파라미터

##### 1. C (규제 파라미터)
- **역할**: 오차 허용 범위 조절
- **높은 값**: 과대적합 위험 증가, 훈련 데이터에 더 정확
- **낮은 값**: 과소적합 위험 증가, 일반화 성능 향상

##### 2. gamma (커널 파라미터)
- **역할**: RBF 커널의 영향 범위 조절
- **높은 값**: 과대적합 위험, 결정 경계가 복잡
- **낮은 값**: 과소적합 위험, 결정 경계가 단순

##### 3. kernel (커널 함수)
- **linear**: 선형 데이터에 적합
- **rbf**: 비선형 데이터에 적합 (가장 일반적)
- **poly**: 다항식 커널
- **sigmoid**: 시그모이드 커널

#### 수렴 문제 해결
```python
# 데이터 스케일링으로 수렴 문제 해결
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 모델 파라미터 조정
model = LogisticRegression(
    max_iter=5000,        # 반복 횟수 증가
    solver='liblinear',   # 이진 분류에 효과적인 솔버
    C=1.0,               # 정규화 강도
    random_state=42      # 재현성을 위한 시드
)
```

### 2.4 다중 모델 비교

#### 실습 결과 예시
```python
# 유방암 데이터셋 결과 (정확도 기준)
교차검증 성능 순위:
1. RANDOM_FOREST: 0.9554 (95.54%)
2. SVM: 0.9530 (95.30%)  
3. GRADIENT_BOOSTING: 0.9530 (95.30%)

테스트 데이터 성능:
- SVM: 0.9441 (94.41%)
- RANDOM_FOREST: 0.9720 (97.20%)  
- GRADIENT_BOOSTING: 0.9720 (97.20%)
```

#### 각 모델의 특징

##### SVM (Support Vector Machine)
- **장점**: 고차원 데이터에 효과적, 커널 트릭으로 비선형 분류 가능
- **단점**: 대용량 데이터에 느림, 하이퍼파라미터에 민감
- **적용**: 텍스트 분류, 이미지 분류

##### RandomForest
- **장점**: 과적합 방지 효과, 특성 중요도 제공, 안정적
- **단점**: 해석이 어려움, 메모리 사용량 많음
- **적용**: 일반적인 분류/회귀 문제

##### GradientBoosting
- **장점**: 높은 예측 성능, 순차적 학습으로 오류 개선
- **단점**: 하이퍼파라미터에 민감, 과적합 위험
- **적용**: 경진대회, 고성능이 필요한 문제

### 2.5 과적합 감지 및 방지

#### 과적합 감지 방법
```python
# 훈련 vs 테스트 정확도 비교
train_accuracy = best_model.score(X_train, y_train)
test_accuracy = best_model.score(X_test, y_test)

overfitting_gap = train_accuracy - test_accuracy

if overfitting_gap > 0.05:
    print("과적합 의심 (훈련-테스트 정확도 차이 > 5%)")
elif overfitting_gap < -0.02:
    print("과소적합 의심")
else:
    print("적절한 모델")
```

#### 과적합 방지 방법
1. **교차검증 사용**: 5-fold, 10-fold CV
2. **정규화 적용**: L1, L2 정규화
3. **조기 종료**: Early Stopping
4. **데이터 증강**: Data Augmentation
5. **앙상블 기법**: Voting, Bagging

---

## 📊 3. 모델 평가 및 비교

### 3.1 평가 지표

#### 분류 문제 주요 지표
```python
from sklearn.metrics import classification_report, confusion_matrix

# 상세 분류 보고서
print(classification_report(y_test, y_pred, target_names=['악성', '양성']))

# 혼동 행렬
cm = confusion_matrix(y_test, y_pred)
```

#### 주요 지표 설명
- **정확도 (Accuracy)**: 전체 예측 중 맞춘 비율
- **정밀도 (Precision)**: 양성 예측 중 실제 양성 비율
- **재현율 (Recall)**: 실제 양성 중 양성으로 예측한 비율  
- **F1-Score**: 정밀도와 재현율의 조화평균
- **특이도 (Specificity)**: 실제 음성 중 음성으로 예측한 비율

### 3.2 교차검증 전략

#### K-Fold 교차검증
```python
from sklearn.model_selection import cross_val_score

# 5-fold 교차검증
cv_scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
print(f"교차검증 평균 점수: {cv_scores.mean():.4f} (±{cv_scores.std():.4f})")
```

#### Stratified K-Fold
```python
from sklearn.model_selection import StratifiedKFold

# 불균형 데이터에 적합
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(model, X, y, cv=skf, scoring='accuracy')
```

### 3.3 성능 비교 시각화

#### 막대 그래프 비교
```python
import matplotlib.pyplot as plt
import seaborn as sns

# 모델별 성능 비교
models = ['SVM', 'RandomForest', 'GradientBoosting']
cv_scores = [0.9530, 0.9554, 0.9530]
test_scores = [0.9441, 0.9720, 0.9720]

x_pos = np.arange(len(models))
width = 0.35

plt.figure(figsize=(10, 6))
plt.bar(x_pos - width/2, cv_scores, width, label='교차검증', alpha=0.8)
plt.bar(x_pos + width/2, test_scores, width, label='테스트', alpha=0.8)

plt.xlabel('모델')
plt.ylabel('정확도')
plt.title('교차검증 vs 테스트 성능')
plt.xticks(x_pos, models)
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

#### 혼동 행렬 히트맵
```python
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['악성', '양성'],
            yticklabels=['악성', '양성'])
plt.title('혼동 행렬')
plt.ylabel('실제')
plt.xlabel('예측')
plt.show()
```

---

## 🎯 4. 실무 적용 가이드

### 4.1 효율적인 하이퍼파라미터 탐색 전략

#### 1단계: 넓은 범위 탐색
```python
# 대략적인 범위에서 시작
param_grid_coarse = {
    'C': [0.001, 0.1, 1, 10, 100],
    'gamma': [0.001, 0.01, 0.1, 1, 10]
}
```

#### 2단계: 세밀한 탐색
```python
# 유망한 영역에서 세밀하게
param_grid_fine = {
    'C': [0.5, 1, 2, 5],
    'gamma': [0.01, 0.05, 0.1, 0.2]
}
```

#### 3단계: RandomizedSearchCV 활용
```python
from sklearn.model_selection import RandomizedSearchCV

# 더 넓은 탐색 공간을 효율적으로
random_search = RandomizedSearchCV(
    estimator=model,
    param_distributions=param_dist,
    n_iter=100,  # 시도 횟수
    cv=5,
    random_state=42,
    n_jobs=-1
)
```

### 4.2 모델 선택 기준

#### 고려사항
1. **예측 성능**: 정확도, F1-score 등
2. **해석 가능성**: 특성 중요도, 결정 경계
3. **계산 효율성**: 학습 시간, 예측 시간
4. **일반화 능력**: 과적합 위험도
5. **데이터 특성**: 크기, 차원, 노이즈 수준

#### 의사결정 매트릭스
| 모델 | 성능 | 해석성 | 속도 | 일반화 | 종합 점수 |
|------|------|--------|------|--------|----------|
| SVM | 높음 | 낮음 | 보통 | 높음 | 5/4 |
| RandomForest | 높음 | 보통 | 빠름 | 높음 | 5/5 |
| GradientBoosting | 매우높음 | 낮음 | 느림 | 보통 | 5/4 |

### 4.3 파이프라인 구축

#### 전처리 + 모델 통합
```python
from sklearn.pipeline import Pipeline

# 완전한 파이프라인 구축
pipeline = Pipeline([
    ('preprocessor', ColumnTransformer([
        ('scaler', StandardScaler(), numeric_features),
        ('encoder', OneHotEncoder(), categorical_features)
    ])),
    ('classifier', RandomForestClassifier(random_state=42))
])

# 파이프라인에 GridSearch 적용
param_grid = {
    'classifier__n_estimators': [50, 100, 200],
    'classifier__max_depth': [None, 10, 20],
    'preprocessor__scaler__with_mean': [True, False]
}

grid_search = GridSearchCV(pipeline, param_grid, cv=5)
grid_search.fit(X_train, y_train)
```

### 4.4 성능 모니터링

#### 지속적인 모델 평가
```python
# 성능 추적 함수
def evaluate_model(model, X_test, y_test):
    """모델 성능을 종합적으로 평가"""
    y_pred = model.predict(X_test)
    
    metrics = {
        'accuracy': accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred, average='weighted'),
        'recall': recall_score(y_test, y_pred, average='weighted'),
        'f1': f1_score(y_test, y_pred, average='weighted')
    }
    
    return metrics

# 여러 모델 비교
results = {}
for name, model in models.items():
    results[name] = evaluate_model(model, X_test, y_test)
    
# 결과 DataFrame으로 정리
import pandas as pd
results_df = pd.DataFrame(results).T
print(results_df.round(4))
```

---

## 5. 고급 기법 및 다음 단계

### 5.1 고급 최적화 기법

#### Bayesian Optimization
```python
# Optuna 사용 예시
import optuna

def objective(trial):
    C = trial.suggest_float('C', 0.01, 100, log=True)
    gamma = trial.suggest_float('gamma', 0.001, 1, log=True)
    
    model = SVC(C=C, gamma=gamma, random_state=42)
    score = cross_val_score(model, X_train, y_train, cv=5).mean()
    return score

study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=100)
```

#### AutoML 도구
- **Auto-sklearn**: 자동 모델 선택 및 튜닝
- **TPOT**: 유전자 알고리즘 기반 파이프라인 최적화
- **H2O AutoML**: 엔터프라이즈급 AutoML

### 5.2 앙상블 기법

#### Voting Classifier
```python
from sklearn.ensemble import VotingClassifier

# 여러 모델 조합
voting_clf = VotingClassifier(
    estimators=[
        ('svm', best_svm),
        ('rf', best_rf), 
        ('gb', best_gb)
    ],
    voting='soft'  # 확률 평균
)

voting_clf.fit(X_train, y_train)
```

#### Stacking
```python
from sklearn.ensemble import StackingClassifier

# 메타 학습기 사용
stacking_clf = StackingClassifier(
    estimators=[
        ('svm', best_svm),
        ('rf', best_rf)
    ],
    final_estimator=LogisticRegression(),
    cv=5
)
```

### 5.3 모델 해석

#### 특성 중요도 분석
```python
# RandomForest 특성 중요도
feature_importance = best_rf.feature_importances_
feature_names = X.columns

# 시각화
plt.figure(figsize=(10, 8))
indices = np.argsort(feature_importance)[::-1][:10]
plt.barh(range(10), feature_importance[indices])
plt.yticks(range(10), [feature_names[i] for i in indices])
plt.title('특성 중요도 (상위 10개)')
plt.show()
```

#### SHAP 값 활용
```python
import shap

# SHAP 설명자 생성
explainer = shap.TreeExplainer(best_rf)
shap_values = explainer.shap_values(X_test[:100])

# 요약 플롯
shap.summary_plot(shap_values[1], X_test[:100])
```

---

## 6. 체크리스트 및 베스트 프랙티스

### 6.1 데이터 전처리 체크리스트

- [ ] **결측값 처리**: 적절한 대치 방법 선택
- [ ] **이상값 탐지**: IQR, Z-score 등 활용
- [ ] **범주형 인코딩**: 상황에 맞는 방법 선택
- [ ] **수치형 스케일링**: StandardScaler, MinMaxScaler 등
- [ ] **특성 선택**: 상관관계, 중요도 기반 선택
- [ ] **데이터 분할**: train/validation/test 적절한 비율

### 6.2 모델링 체크리스트

- [ ] **기준 모델**: 단순한 모델로 기준 설정
- [ ] **교차검증**: 적절한 CV 전략 선택
- [ ] **하이퍼파라미터**: 체계적인 탐색 전략
- [ ] **과적합 확인**: 훈련/검증 성능 차이 모니터링
- [ ] **다중 모델**: 여러 알고리즘 비교
- [ ] **앙상블**: 성능 향상을 위한 모델 조합

### 6.3 평가 및 검증 체크리스트

- [ ] **적절한 지표**: 비즈니스 목표에 맞는 지표 선택
- [ ] **통계적 유의성**: 성능 차이의 신뢰성 검증
- [ ] **실제 데이터**: 최신 데이터로 성능 재검증
- [ ] **에러 분석**: 오분류 사례 분석
- [ ] **해석 가능성**: 모델 결정 과정 이해
- [ ] **배포 준비**: 실제 환경 고려사항 점검

---

## 🎓 7. 학습 정리 및 다음 단계

### 7.1 핵심 학습 내용

#### 데이터 전처리
- 범주형 데이터 처리 3가지 방법 (`get_dummies`, `OneHotEncoder`, `ColumnTransformer`)
- 각 방법의 장단점 및 적용 시나리오
- 숫자형 범주 데이터의 올바른 처리법

#### 하이퍼파라미터 튜닝
- GridSearchCV를 통한 체계적 최적화
- 교차검증과 과적합 감지
- 다중 모델 비교 및 성능 평가
- SVM, RandomForest, GradientBoosting 특성 이해

#### 모델 평가
- 다양한 평가 지표 활용
- 혼동 행렬 및 분류 보고서 해석
- 시각화를 통한 성능 비교

### 7.2 실무 적용 포인트

1. **단계적 접근**: 간단한 모델 → 복잡한 모델
2. **체계적 튜닝**: 넓은 탐색 → 세밀한 조정  
3. **종합적 평가**: 성능 + 해석성 + 효율성
4. **지속적 모니터링**: 모델 성능 추적 및 업데이트

### 7.3 다음 학습 권장사항

#### 단기 목표 (1-2주)
- [ ] **RandomizedSearchCV** 및 **Bayesian Optimization** 학습
- [ ] **앙상블 기법** (Voting, Bagging, Stacking) 실습
- [ ] **특성 선택** 및 **차원 축소** 기법 학습

#### 중기 목표 (1-2개월)  
- [ ] **AutoML 도구** (Auto-sklearn, TPOT) 활용
- [ ] **모델 해석** 기법 (SHAP, LIME) 학습
- [ ] **실제 프로젝트** 데이터로 end-to-end 파이프라인 구축

#### 장기 목표 (3-6개월)
- [ ] **딥러닝** 하이퍼파라미터 튜닝
- [ ] **분산 컴퓨팅** 환경에서의 대용량 데이터 처리
- [ ] **MLOps** 파이프라인 구축 및 배포

### 7.4 추가 학습 자료

#### 도서
- "Hands-On Machine Learning" - Aurélien Géron
- "The Elements of Statistical Learning" - Hastie, Tibshirani, Friedman
- "Pattern Recognition and Machine Learning" - Christopher Bishop

#### 온라인 자료
- Scikit-learn 공식 문서: https://scikit-learn.org/
- Kaggle Learn: https://www.kaggle.com/learn
- Fast.ai: https://www.fast.ai/

#### 실습 플랫폼
- **Kaggle**: 경진대회 및 데이터셋
- **Google Colab**: 무료 GPU 환경
- **Papers with Code**: 최신 연구 동향

---

## 마무리

### 주요 성과
- **데이터 전처리**: 범주형 데이터 처리 마스터
- **하이퍼파라미터 튜닝**: 체계적 모델 최적화 방법 습득
- **모델 평가**: 종합적 성능 평가 및 비교 능력 확보
- **실무 역량**: 실제 프로젝트 적용 가능한 기술 스택 구축

### 다음 여정
머신러닝의 핵심 기법들을 익혔으니, 이제 더 복잡하고 실전적인 문제들에 도전해볼 차례입니다. 
