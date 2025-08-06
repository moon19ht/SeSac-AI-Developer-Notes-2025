# 🧠 Deep Learning 정리

##### 🗓️ 2025.08.05
##### 📝 Writer : Moon19ht

---

## 📚 목차

1. [SECOM 데이터셋 클린 코드 머신러닝 파이프라인](#1-secom-데이터셋-클린-코드-머신러닝-파이프라인)
2. [클린 코드 아키텍처](#2-클린-코드-아키텍처)
3. [전체 데이터 처리 파이프라인](#3-전체-데이터-처리-파이프라인)
4. [모델 성능 결과](#4-모델-성능-결과)
5. [핵심 학습 내용](#5-핵심-학습-내용)
6. [실무 적용 가치](#6-실무-적용-가치)

---

## 1. SECOM 데이터셋 클린 코드 머신러닝 파이프라인

### 📋 프로젝트 개요
- **목표**: 반도체 제조 공정에서 품질 Pass/Fail 이진 분류 예측
- **데이터**: UCI SECOM 데이터셋 (1,567개 샘플, 592개 센서 피처)
- **핵심 특징**: 클린 코드 원칙을 적용한 체계적 ML 파이프라인 구축
- **최고 성능**: Gradient Boosting 97.78% 테스트 정확도

### 🎯 주요 도전 과제
- **극심한 클래스 불균형**: Pass 104개 vs Fail 1,463개 (14:1 비율)
- **높은 결측치 비율**: 최대 91.19% 결측값을 가진 피처 존재
- **고차원 데이터**: 592개의 센서 피처 처리
- **노이즈 많은 센서 데이터**: 제조 공정 특성상 변동성 큰 데이터

---

## 2. 클린 코드 아키텍처

### 🏗️ 설정 관리 시스템
```python
class Config:
    # 데이터 처리 파라미터
    MISSING_DATA_THRESHOLD = 0.2      # 결측치 허용 임계값
    CORRELATION_THRESHOLD = 0.05       # 타겟 상관관계 최소값
    MULTICOLLINEARITY_THRESHOLD = 0.8  # 다중공선성 임계값
    
    # 모델 파라미터
    TEST_SIZE = 0.2
    RANDOM_STATE = 42
    CV_FOLDS = 5
    PCA_COMPONENTS = 24
    
    # 시각화 설정
    FIGURE_SIZE_LARGE = (20, 20)
    FIGURE_SIZE_MEDIUM = (15, 15)
    FIGURE_SIZE_SMALL = (10, 6)
```

### 📦 모듈화된 함수 구조

#### 데이터 처리 모듈
1. **`load_and_explore_data()`**: 데이터 로딩 및 기본 통계 출력
2. **`prepare_features_target()`**: 피처-타겟 분리 및 타겟 인코딩
3. **`clean_missing_data()`**: 결측치 처리 및 데이터 정제
4. **`replace_outliers_iqr()`**: IQR 기반 이상치 처리

#### 피처 엔지니어링 모듈
1. **`select_features_by_correlation()`**: 상관관계 기반 피처 선택
2. **`remove_multicollinear_features()`**: 다중공선성 제거

#### 시각화 모듈
1. **`plot_correlation_heatmap()`**: 상관관계 히트맵
2. **`plot_feature_distributions()`**: 피처 분포 시각화
3. **`plot_boxplots()`**: 이상치 탐지용 박스플롯
4. **`plot_pca_explained_variance()`**: PCA 설명 분산 그래프

#### 모델링 모듈
1. **`get_model_configurations()`**: 모델 및 하이퍼파라미터 설정
2. **`train_and_evaluate_models()`**: 자동화된 모델 훈련 및 평가
3. **`print_model_comparison()`**: 모델 성능 비교 테이블

---

## 3. 전체 데이터 처리 파이프라인

### 🔧 1단계: 데이터 로딩 및 탐색
```python
# 기본 정보 확인
데이터셋 형태: (1567, 592)
메모리 사용량: 7.18 MB
최대 결측 데이터 비율: 91.19%
```

### 🧹 2단계: 데이터 정제
```python
# 정제 과정 결과
원본 형태: (1567, 591)
높은 결측 컬럼 제거 후: (1567, 583)    # 9개 컬럼 제거
Time 컬럼 제거 후: (1567, 582)         # 시계열 불필요
정제 후 총 결측값 수: 0                # 평균값으로 보간
분산이 0인 특성: 116개 발견            # 상수 피처 확인
```

### 🎯 3단계: 피처 선택
```python
# 2단계 피처 선택 과정
상관관계 임계값 0.05 → 86개 특성 선택
다중공선성 제거 → 36개 특성 최종 선택

# 차원 축소율: 592 → 36개 (93.9% 감소)
```

### ⚖️ 4단계: 데이터 전처리
```python
# 전처리 파이프라인
StandardScaler() → 특성 정규화
SMOTE() → 클래스 균형 맞춤 (1463→1463 vs 104→1463)
PCA(24) → 차원 축소 (36→24개 성분)

# 최종 데이터 형태
균형 맞춘 데이터셋: (2926, 24)
24개 PCA 성분으로 설명된 분산: 0.892 (89.2%)
```

### 🤖 5단계: 모델 훈련
```python
# 8개 알고리즘 하이퍼파라미터 튜닝
- RandomForest: {'n_estimators': [20-60], 'max_depth': [None, 10-60]}
- SVM: {'C': [10-60], 'kernel': ['linear', 'rbf']}
- XGBoost: {'n_estimators': [160-300], 'learning_rate': [0.25-0.3]}
- GradientBoosting: {'n_estimators': [90-150], 'learning_rate': [0.5-0.6]}
```

---

## 4. 모델 성능 결과

### 🏆 모델 성능 순위표
| 순위 | 모델 | 테스트 정확도 | 교차검증 점수 | 과적합 정도 |
|------|------|-------------|-------------|-----------|
| **1** | **Gradient Boosting** | **97.78%** | 94.44% | 0.0222 |
| 2 | Random Forest | 97.44% | 95.04% | 0.0256 |
| 3 | SVM | 97.27% | 96.41% | 0.0273 |
| 4 | XGBoost | 96.42% | 94.83% | 0.0358 |
| 5 | KNN | 89.59% | 87.14% | 0.1041 |
| 6 | Decision Tree | 87.37% | 87.44% | 0.1263 |
| 7 | Logistic Regression | 77.65% | 74.06% | -0.0303 |
| 8 | Naive Bayes | 76.62% | 77.86% | 0.0077 |

### 🎖️ 최고 모델 상세 분석
```python
최고 모델: Gradient Boosting
- 테스트 정확도: 97.78%
- 교차검증 점수: 94.44% 
- 최적 파라미터: {
    'learning_rate': 0.6,
    'max_depth': 4, 
    'n_estimators': 150
  }

# 분류 보고서
              precision    recall  f1-score   support
    Fail(0)       1.00      0.96      0.98       293
    Pass(1)       0.96      1.00      0.98       293
    
    accuracy                          0.98       586

# 혼동 행렬 - 거의 완벽한 분류
[[280  13]    # Fail 예측: 280개 정확, 13개 오분류  
 [  0 293]]   # Pass 예측: 293개 모두 정확
```

### 📊 모델별 특성 분석
1. **Tree-based 모델** (RF, GB, XGB): 높은 성능, 약간의 과적합
2. **SVM**: 높은 성능, 안정적 일반화
3. **거리 기반** (KNN): 중간 성능, 높은 과적합
4. **선형 모델** (LR): 낮은 성능, 언더피팅
5. **확률 모델** (NB): 낮은 성능, 가정 위배

---

## 5. 핵심 학습 내용

### 🎨 클린 코드 원칙 적용

#### 1. 단일 책임 원칙 (SRP)
```python
# 각 함수는 하나의 명확한 기능만 수행
def load_and_explore_data() → 데이터 로딩만
def clean_missing_data() → 결측치 처리만  
def select_features_by_correlation() → 피처 선택만
```

#### 2. DRY 원칙 (Don't Repeat Yourself)
```python
# 공통 설정을 Config 클래스로 중앙화
# 반복되는 시각화 로직을 함수로 추상화
# 모델 평가 로직을 재사용 가능한 함수로 구현
```

#### 3. 가독성과 유지보수성
```python
# 의미있는 함수명과 변수명 사용
# 충분한 docstring과 주석 제공
# 논리적 섹션별 코드 구조화
```

### 🔬 고급 데이터 과학 기법

#### 1. 체계적 피처 엔지니어링
- **상관관계 기반 선택**: 타겟과 무관한 피처 제거
- **다중공선성 처리**: 중복 정보 제거로 모델 안정성 향상
- **차원 축소**: PCA로 노이즈 감소 및 계산 효율성 증대

#### 2. 클래스 불균형 처리
- **SMOTE 오버샘플링**: 소수 클래스 합성 생성
- **층화 분할**: 훈련/테스트 세트 균형 유지
- **적절한 평가 지표**: Precision, Recall, F1-score 활용

#### 3. 모델 검증 및 선택
- **5-Fold 교차검증**: 모델 안정성 검증
- **Grid Search**: 체계적 하이퍼파라미터 튜닝
- **다양한 알고리즘 비교**: 앙상블부터 선형 모델까지

### 📈 시각화 및 EDA 기법
```python
# 포괄적 시각화 파이프라인
- 상관관계 히트맵 → 피처 간 관계 파악
- 분포 히스토그램 → 데이터 특성 이해  
- 박스플롯 → 이상치 패턴 확인
- PCA 분산 그래프 → 차원 축소 효과 검증
```

---

## 6. 실무 적용 가치

### 🚀 즉시 적용 가능한 코드 패턴

#### 재사용 가능한 ML 파이프라인
```python
# 설정 기반 유연한 파이프라인
class MLPipeline:
    def __init__(self, config):
        self.config = config
    
    def run_full_pipeline(self, data_path):
        # 1. 데이터 로딩 및 탐색
        df = load_and_explore_data(data_path)
        
        # 2. 데이터 정제
        X_cleaned = clean_missing_data(X)
        
        # 3. 피처 선택
        X_selected = select_features_by_correlation(X_cleaned, y)
        X_final = remove_multicollinear_features(X_selected, y)
        
        # 4. 전처리 및 균형 맞춤
        X_scaled = StandardScaler().fit_transform(X_final)
        X_balanced, y_balanced = SMOTE().fit_resample(X_scaled, y)
        X_pca = PCA(n_components=config.PCA_COMPONENTS).fit_transform(X_balanced)
        
        # 5. 모델 훈련 및 평가
        results = train_and_evaluate_models(X_train, y_train, X_test, y_test)
        
        return results
```

#### 제조업 품질 관리 시스템
```python
# 실시간 품질 예측 API
class QualityPredictionSystem:
    def __init__(self, trained_model, scaler, pca):
        self.model = trained_model
        self.scaler = scaler  
        self.pca = pca
    
    def predict_quality(self, sensor_data):
        # 전처리 파이프라인 적용
        scaled_data = self.scaler.transform(sensor_data)
        pca_data = self.pca.transform(scaled_data)
        
        # 예측 및 신뢰도 계산
        prediction = self.model.predict(pca_data)[0]
        probability = self.model.predict_proba(pca_data)[0].max()
        
        return {
            'quality': 'Pass' if prediction == 1 else 'Fail',
            'confidence': probability,
            'recommendation': self._get_recommendation(probability)
        }
```

### 📊 확장 가능한 개선 방향

#### 1. 고급 피처 엔지니어링
- **도메인 지식 활용**: 센서 간 비율, 트렌드 피처 생성
- **시계열 피처**: 시간창 기반 통계량 추출
- **자동 피처 생성**: Featuretools를 활용한 자동화

#### 2. 앙상블 및 스태킹
- **Voting Classifier**: 상위 모델들의 결합
- **Stacking**: 메타 모델을 통한 성능 향상
- **Dynamic Ensemble**: 데이터 특성에 따른 모델 선택

#### 3. 모델 해석성 및 모니터링
- **SHAP Values**: 예측 근거 설명
- **Feature Importance**: 중요 센서 식별
- **Drift Detection**: 모델 성능 저하 감지
- **A/B Testing**: 모델 개선 효과 검증

### 💼 비즈니스 임팩트

#### 제조업 적용 효과
1. **품질 예측 정확도**: 97.78%로 거의 완벽한 불량 감지
2. **비용 절감**: 
   - 불량품 조기 감지로 재작업 비용 최소화
   - 예방적 유지보수로 설비 다운타임 감소
3. **공정 최적화**:
   - 핵심 센서 36개 식별로 모니터링 효율화
   - 실시간 품질 관리 시스템 구축 가능

#### 확장 적용 분야
- **의료 진단**: 환자 데이터 기반 질병 예측
- **금융 리스크**: 신용평가 및 사기 탐지
- **마케팅**: 고객 이탈 예측 및 세분화
- **에너지**: 설비 고장 예측 및 최적화

---

## 🎯 결론

### 📈 주요 성과
1. **클린 코드 아키텍처**: 유지보수 가능하고 확장성 높은 ML 파이프라인 구축
2. **고성능 모델**: Gradient Boosting 97.78% 정확도 달성
3. **체계적 방법론**: 데이터 처리부터 모델 평가까지 end-to-end 프로세스
4. **실무 적용성**: 바로 사용 가능한 코드 패턴과 함수들

### 💡 핵심 인사이트
1. **코드 품질의 중요성**: 클린 코드가 협업과 유지보수에 미치는 큰 영향
2. **체계적 접근**: 설정 관리와 모듈화를 통한 실험 재현성 확보
3. **균형잡힌 파이프라인**: 성능과 가독성을 동시에 만족하는 설계
4. **확장성 고려**: 새로운 데이터셋과 요구사항에 쉽게 적응 가능한 구조

### 🚀 실무 적용 가치
이번 프로젝트를 통해 **단순한 모델 훈련을 넘어 실제 프로덕션 환경에서 사용 가능한 ML 시스템 구축 방법**을 학습했습니다. 클린 코드 원칙을 적용한 체계적인 접근은 개인 프로젝트뿐만 아니라 팀 단위 협업에서도 큰 가치를 제공할 것입니다.

특히 제조업, 의료, 금융 등 **높은 정확도와 안정성이 요구되는 도메인**에서 이러한 방법론을 활용하면 실질적인 비즈니스 임팩트를 창출할 수 있습니다.