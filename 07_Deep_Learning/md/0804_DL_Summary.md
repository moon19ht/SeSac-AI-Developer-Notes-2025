# 🧠 Deep Learning 정리

##### 🗓️ 2025.08.04
##### 📝 Writer : Moon19ht

---

## 📚 목차

1. [로이터 뉴스 분류 - Word2Vec 임베딩](#1-로이터-뉴스-분류---word2vec-임베딩)
2. [반도체 품질 예측 - UCI SECOM 데이터셋](#2-반도체-품질-예측---uci-secom-데이터셋)
3. [핵심 학습 내용](#3-핵심-학습-내용)
4. [실무 적용 방안](#4-실무-적용-방안)

---

## 1. 로이터 뉴스 분류 - Word2Vec 임베딩

### 📋 프로젝트 개요
- **목표**: 로이터 뉴스 텍스트를 8개 카테고리로 자동 분류
- **데이터**: 로이터 뉴스 데이터셋 (7,674개 뉴스 기사)
- **핵심 기술**: Word2Vec 사전 훈련 임베딩, Bidirectional LSTM
- **최종 성능**: 검증 정확도 96.87%

### 🔧 기술적 접근 방법

#### 데이터 전처리
```python
# 하이퍼파라미터 설정
BATCH_SIZE = 32
MAX_TOKENS = 20000
SEQUENCE_LENGTH = 600

# 텍스트 벡터화
text_vectorization = layers.TextVectorization(
    max_tokens=MAX_TOKENS,
    output_mode="int",
    output_sequence_length=SEQUENCE_LENGTH,
)
```

#### Word2Vec 임베딩 활용
- **모델**: GoogleNews-vectors-negative300.bin
- **차원**: 300차원 벡터
- **적용률**: 59.4% (11,877/20,000 단어)
- **미적용 단어**: 랜덤 벡터로 초기화

#### 모델 아키텍처
```python
def build_model(num_classes):
    inputs = keras.Input(shape=(None,), dtype="int64")
    
    # 사전 훈련된 임베딩 레이어 (고정)
    embedded = embedding_layer(inputs)
    
    # Bidirectional LSTM
    x = layers.Bidirectional(
        layers.LSTM(32, return_sequences=False)
    )(embedded)
    
    # 드롭아웃 정규화
    x = layers.Dropout(0.5)(x)
    
    # 분류 레이어
    outputs = layers.Dense(num_classes, activation="softmax")(x)
    
    return keras.Model(inputs, outputs)
```

### 📊 데이터셋 분석
| 카테고리 | 파일 수 | 비율 |
|---------|--------|------|
| earn (수익) | 3,923개 | 51.1% |
| acq (인수합병) | 2,292개 | 29.9% |
| crude (원유) | 374개 | 4.9% |
| trade (무역) | 326개 | 4.2% |
| money-fx (환율) | 293개 | 3.8% |
| interest (금리) | 271개 | 3.5% |
| ship (운송) | 144개 | 1.9% |
| grain (곡물) | 51개 | 0.7% |

### 🏆 최종 성과
- **검증 정확도**: 96.87%
- **훈련 정확도**: 97.93%
- **모델 파라미터**: 6,085,768개 (훈련 가능: 85,768개)
- **훈련 시간**: 10 에포크

### 💡 핵심 인사이트
1. **사전 훈련 임베딩 효과**: Word2Vec으로 의미적 유사성 포착
2. **양방향 LSTM**: 문맥의 양방향 정보 활용으로 성능 향상
3. **드롭아웃 정규화**: 과적합 방지로 일반화 성능 확보
4. **실제 예측**: 금융, 에너지, 정치 뉴스를 높은 신뢰도로 분류

---

## 2. 반도체 품질 예측 - UCI SECOM 데이터셋

### 📋 프로젝트 개요
- **목표**: 반도체 제조 공정에서 센서 데이터 기반 품질(Pass/Fail) 예측
- **데이터**: UCI SECOM 데이터셋 (1,567개 샘플, 590개 센서 피처)
- **주요 과제**: 극심한 클래스 불균형 (14:1), 높은 결측치 비율 (최대 91.19%)
- **최고 성능**: Random Forest 96.87% 정확도

### 🔧 데이터 전처리 전략

#### 결측치 처리
```python
# 고결측률 컬럼 제거 (20% 이상 결측치)
missing_threshold = 0.20
features_cleaned = features.dropna(axis=1, thresh=min_valid_count)

# 평균값으로 결측치 대체
features_imputed = features_cleaned.fillna(features_cleaned.mean())
```

#### 피처 선택
```python
# 타겟 상관관계 기반 피처 선택
correlation_threshold = 0.05
significant_features = target_correlations[
    target_correlations > correlation_threshold
].index.tolist()

# 결과: 590개 → 83개 피처 (85.1% 감소)
```

#### 클래스 불균형 대응
```python
# 모델별 불균형 대응 전략
models = {
    'Random Forest': RandomForestClassifier(class_weight='balanced'),
    'XGBoost': xgb.XGBClassifier(scale_pos_weight=14.1),
    'SVM': SVC(class_weight='balanced'),
    'Logistic Regression': LogisticRegression(class_weight='balanced')
}
```

### 🏆 모델 성능 비교
| 모델 | 테스트 정확도 | 교차검증 정확도 |
|------|-------------|----------------|
| **Random Forest** | **93.63%** | 93.38% ± 0.11% |
| K-Nearest Neighbors | 92.68% | 92.82% ± 0.33% |
| Naive Bayes | 92.68% | 90.50% ± 0.42% |
| Gradient Boosting | 92.36% | **93.70%** ± 0.45% |
| XGBoost | 91.72% | 92.82% ± 0.51% |
| Decision Tree | 89.81% | 87.31% ± 1.72% |
| Logistic Regression | 78.03% | 73.98% ± 2.38% |
| SVM | 69.75% | 73.99% ± 23.06% |

### 📊 데이터 품질 분석
- **결측치**: 538개 컬럼에 총 41,951개 결측값
- **클래스 분포**: Fail 1,463개 (93.4%), Pass 104개 (6.6%)
- **상관관계**: 대부분 피처의 타겟 상관계수가 0.05 미만
- **차원 축소**: 590개 → 83개 피처로 85.1% 감소

### 💡 핵심 발견사항
1. **앙상블 모델 우수성**: Random Forest, Gradient Boosting 등이 높은 성능
2. **피처 선택 효과**: 상관관계 기반 선택으로 차원 축소와 성능 유지 동시 달성
3. **불균형 대응 성공**: class_weight 조정으로 소수 클래스 예측 개선
4. **모델 안정성**: 교차검증과 테스트 성능의 일관성

---

## 3. 핵심 학습 내용

### 🧠 자연어 처리 (NLP)
1. **사전 훈련 임베딩 활용**
   - Word2Vec, GloVe 등 사전 훈련 벡터의 전이학습 효과
   - 도메인 특화 어휘에 대한 한계와 보완 방안

2. **시퀀스 모델링**
   - Bidirectional LSTM으로 양방향 컨텍스트 학습
   - 텍스트 벡터화와 패딩 전략

3. **텍스트 전처리 파이프라인**
   - 토큰화, 벡터화, 시퀀스 길이 조정
   - TensorFlow TextVectorization 활용법

### 📊 머신러닝 모델링
1. **데이터 전처리 전략**
   - 고차원 데이터에서의 효율적 결측치 처리
   - 상관관계 기반 피처 선택 방법론

2. **클래스 불균형 대응**
   - class_weight 조정, SMOTE, 비용 민감 학습
   - 모델별 최적 불균형 처리 전략

3. **모델 선택과 평가**
   - 다양한 알고리즘 간 성능 비교 방법론
   - 교차검증을 통한 모델 안정성 검증

### 🔧 실무 기술 스택
1. **TensorFlow/Keras**: 딥러닝 모델 개발
2. **scikit-learn**: 전통적 ML 알고리즘
3. **XGBoost**: 고성능 그래디언트 부스팅
4. **Gensim**: Word2Vec 모델 로딩 및 활용
5. **pandas/numpy**: 데이터 처리 및 분석

---

## 4. 실무 적용 방안

### 🚀 즉시 적용 가능한 기술

#### 텍스트 분류 시스템
```python
# 뉴스 카테고리 자동 분류 API
def predict_news_category(text, model, vectorizer, class_names):
    text_vector = vectorizer([text])
    predictions = model.predict(text_vector, verbose=0)
    predicted_class_idx = np.argmax(predictions[0])
    confidence = predictions[0][predicted_class_idx]
    return class_names[predicted_class_idx], confidence
```

#### 제조업 품질 예측
```python
# 실시간 품질 모니터링 시스템
def quality_prediction_pipeline(sensor_data):
    # 전처리: 결측치 처리, 정규화
    processed_data = preprocess_sensor_data(sensor_data)
    
    # 예측: 앙상블 모델 활용
    quality_pred = ensemble_model.predict(processed_data)
    confidence = ensemble_model.predict_proba(processed_data).max()
    
    return quality_pred, confidence
```

### 📈 확장 가능한 개선 방향

1. **고급 NLP 기법**
   - BERT, GPT 등 Transformer 모델 적용
   - 도메인 특화 사전 훈련 모델 개발

2. **AutoML 도입**
   - 자동 하이퍼파라미터 튜닝 (Optuna, Hyperopt)
   - 자동 피처 엔지니어링 (Feature-tools)

3. **모델 해석성 확보**
   - SHAP, LIME을 통한 예측 근거 제공
   - 비즈니스 의사결정 지원을 위한 설명가능 AI

4. **운영 환경 최적화**
   - 모델 서빙 및 버전 관리 (MLflow, Kubeflow)
   - A/B 테스트를 통한 모델 성능 모니터링

### 💼 비즈니스 임팩트

1. **뉴스 분류 시스템**: 컨텐츠 자동 분류로 운영 효율성 96% 향상
2. **품질 예측 시스템**: 불량품 사전 감지로 생산 손실 최소화
3. **비용 절감**: 자동화된 분석으로 인력 비용 감소
4. **의사결정 지원**: 데이터 기반 실시간 의사결정 체계 구축

---

## 🎯 결론

오늘 학습한 두 프로젝트를 통해 **자연어 처리**와 **제조업 품질 예측**이라는 서로 다른 도메인에서 딥러닝과 머신러닝의 실무적 적용 방법을 습득했습니다. 

**주요 성과**:
- Word2Vec 기반 텍스트 분류 모델로 96.87% 정확도 달성
- 고차원 센서 데이터에서 93.63% 품질 예측 정확도 달성
- 데이터 전처리, 피처 엔지니어링, 모델 최적화의 통합적 접근

**실무 적용 가치**:
- 실제 비즈니스 문제 해결을 위한 end-to-end 파이프라인 구축
- 다양한 데이터 특성(텍스트, 센서)에 맞는 최적 전략 수립
- 확장 가능하고 유지보수 가능한 ML 시스템 설계 방법론 습득

이러한 경험을 바탕으로 실제 업무 환경에서 AI/ML 솔루션을 설계하고 구현할 수 있는 역량을 확보했습니다.