# 🧠 Deep Learning 정리

##### 🗓️ 2025.07.31
##### 📝 Writer : Moon19ht

---

## 📚 목차

1. [자연어 처리 기초](#자연어-처리-기초)
2. [텍스트 벡터화 구현](#텍스트-벡터화-구현)
3. [Keras TextVectorization 활용](#keras-textvectorization-활용)
4. [IMDB 감성 분석 프로젝트](#imdb-감성-분석-프로젝트)
5. [핵심 개념 정리](#핵심-개념-정리)
6. [실무 적용 방안](#실무-적용-방안)

---

## 자연어 처리 기초

### 🎯 자연어 처리란?
자연어 처리(Natural Language Processing, NLP)는 인간의 언어를 컴퓨터가 이해하고 처리할 수 있도록 하는 인공지능 분야입니다.

### 📊 주요 응용 분야
- **감성 분석**: 텍스트의 감정, 의견 분석
- **기계 번역**: 언어 간 자동 번역
- **질의 응답**: 자연어 질문에 대한 답변 생성
- **텍스트 요약**: 긴 문서의 핵심 내용 추출
- **개체명 인식**: 인명, 지명, 기관명 등 식별

### 🔧 텍스트 전처리 과정
1. **표준화(Standardization)**: 대소문자 통일, 구두점 제거
2. **토큰화(Tokenization)**: 문장을 단어 단위로 분할
3. **어휘 사전 구축(Vocabulary Building)**: 고유 단어 집합 생성
4. **수치화(Numerization)**: 텍스트를 숫자로 변환

---

## 텍스트 벡터화 구현

### 💡 벡터화의 필요성
머신러닝 모델은 숫자만 처리할 수 있기 때문에, 텍스트를 숫자 벡터로 변환하는 과정이 필수적입니다.

### 🏗️ MyVectorize 클래스 구현

#### 주요 메서드
```python
class MyVectorize:
    def standardize(self, text):
        """텍스트 표준화: 소문자 변환, 구두점 제거"""
        text = text.lower()
        return "".join(c for c in text if c not in string.punctuation)
    
    def tokenize(self, text):
        """토큰화: 공백 기준으로 단어 분할"""
        return text.split()
    
    def make_vocabulary(self, dataset):
        """어휘 사전 구축: 특수 토큰과 단어 매핑"""
        self.vocabulary = {"": 0, "[UNK]": 1}  # 패딩, 미등록 단어
        # 데이터셋 순회하며 어휘 사전 구축
    
    def encode(self, text):
        """텍스트를 숫자 시퀀스로 인코딩"""
        # 미등록 단어는 [UNK] 토큰(1)으로 처리
    
    def decode(self, int_sequence):
        """숫자 시퀀스를 텍스트로 디코딩"""
        # 역방향 매핑으로 복원
```

#### 특수 토큰 처리
- **패딩 토큰("")**: 인덱스 0, 시퀀스 길이 맞춤용
- **미등록 단어 토큰("[UNK]")**: 인덱스 1, 어휘 사전에 없는 단어 처리

### 📈 구현의 장단점
**장점:**
- 구현 원리 이해 용이
- 완전한 제어 가능
- 외부 의존성 최소화

**단점:**
- 성능 제한 (Python 기반)
- 고급 기능 부족
- 메모리 효율성 낮음

---

## Keras TextVectorization 활용

### ⚡ TextVectorization의 장점
- **TensorFlow 최적화**: GPU 가속 지원
- **배치 처리**: 대용량 데이터 효율적 처리
- **다양한 출력 모드**: int, binary, count, tf-idf
- **모델 통합**: Keras 레이어로 직접 연결

### 🔧 커스텀 전처리 함수
```python
def custom_standardization_fn(text):
    """커스텀 표준화 함수"""
    lower_text = tf.strings.lower(text)
    return tf.strings.regex_replace(lower_text, f"[{re.escape(string.punctuation)}]", "")

def custom_split_fn(text):
    """커스텀 토큰화 함수"""
    return tf.strings.split(text)
```

### 📊 출력 모드 비교
```python
# Int 모드: 정수 시퀀스
vectorizer_int = TextVectorization(output_mode="int")

# Binary 모드: 단어 존재 여부 (0 또는 1)
vectorizer_binary = TextVectorization(output_mode="binary")

# Count 모드: 단어 빈도수
vectorizer_count = TextVectorization(output_mode="count")

# TF-IDF 모드: 가중치 적용
vectorizer_tfidf = TextVectorization(output_mode="tf_idf")
```

### 🏗️ 모델 통합 예제
```python
model = Sequential([
    text_vectorization,  # 전처리 레이어
    Embedding(input_dim=len(vocabulary), output_dim=16),
    LSTM(32),
    Dense(1, activation='sigmoid')
])
```

---

## IMDB 감성 분석 프로젝트

### 📊 프로젝트 개요
- **데이터셋**: Stanford AI Lab의 IMDB 영화 리뷰 (50,000개)
- **문제 유형**: 이진 분류 (긍정/부정 감성 분석)
- **기술 스택**: TensorFlow/Keras, TextVectorization, Dense Neural Network
- **벡터화 방식**: Multi-hot encoding (Bag of Words)

### 🗂️ 데이터 구조
```
aclImdb/
├── train/
│   ├── pos/          # 긍정 리뷰 (12,500개)
│   └── neg/          # 부정 리뷰 (12,500개)
├── val/              # 검증용 (5,000개)
│   ├── pos/          
│   └── neg/          
└── test/
    ├── pos/          # 긍정 리뷰 (12,500개)
    └── neg/          # 부정 리뷰 (12,500개)
```

### 🔄 데이터 파이프라인
1. **데이터 다운로드**: 스트리밍 방식으로 메모리 효율적 처리
2. **압축 해제**: tar.gz 형식 안전 해제
3. **데이터 분할**: train/validation 분할 (80:20 비율)
4. **벡터화**: TextVectorization으로 multi-hot encoding
5. **모델 훈련**: Dense 신경망으로 이진 분류

### 🧠 모델 아키텍처
```python
def getModel(max_tokens=20000, hidden_dim=16):
    inputs = keras.Input(shape=(max_tokens,))        # 입력층: 20,000차원
    x = layers.Dense(hidden_dim, activation='relu')(inputs)  # 은닉층: 16개 뉴런
    x = layers.Dropout(0.5)(x)                       # 드롭아웃: 과적합 방지
    outputs = layers.Dense(1, activation='sigmoid')(x)      # 출력층: 이진 분류
    
    model = keras.Model(inputs, outputs)
    model.compile(
        optimizer="rmsprop",
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )
    return model
```

### 📈 성능 결과
- **테스트 정확도**: 87.42%
- **훈련 시간**: 약 30초 (10 에포크)
- **모델 크기**: 1.22MB (320,033 파라미터)

---

## 핵심 개념 정리

### 🎯 주요 벡터화 기법

#### 1. Bag of Words (BoW)
```
"I love this movie" → [0, 1, 1, 0, 1, 0, ...]
```
- **장점**: 구현 간단, 해석 용이
- **단점**: 단어 순서 무시, 희소 벡터

#### 2. TF-IDF
```
TF-IDF = TF(단어 빈도) × IDF(역문서 빈도)
```
- **장점**: 중요한 단어에 가중치 부여
- **단점**: 여전히 순서 정보 없음

#### 3. Word Embeddings
```
"king" - "man" + "woman" ≈ "queen"
```
- **장점**: 의미론적 관계 표현
- **단점**: 사전 훈련 필요

### 🔧 최적화 기법
- **데이터 캐싱**: `dataset.cache()` 활용
- **멀티프로세싱**: `num_parallel_calls=4`
- **배치 처리**: 메모리 효율적 처리
- **조기 종료**: 과적합 방지

### 📊 성능 평가 지표
- **정확도(Accuracy)**: 전체 예측 중 맞춘 비율
- **손실(Loss)**: 이진 교차 엔트로피
- **검증 성능**: 과적합 모니터링

---

## 실무 적용 방안

### 🏢 산업별 활용 사례

#### 1. 전자상거래
```python
# 제품 리뷰 자동 분석
review_sentiment = model.predict("This product is amazing!")
if review_sentiment > 0.5:
    update_product_rating(positive=True)
```

#### 2. 소셜 미디어 모니터링
```python
# 브랜드 멘션 감성 분석
brand_mentions = collect_social_posts("brand_name")
sentiment_scores = model.predict(brand_mentions)
generate_sentiment_report(sentiment_scores)
```

#### 3. 고객 서비스
```python
# 문의 내용 우선순위 분류
inquiry_sentiment = model.predict(customer_message)
if inquiry_sentiment < 0.3:  # 매우 부정적
    escalate_to_manager(inquiry_id)
```

### 🚀 확장 가능한 아키텍처
```
사용자 입력 → API Gateway → 
전처리 서버 → ML 모델 서버 → 
결과 캐싱 → 클라이언트 응답
```

### 📈 성능 개선 로드맵

#### Phase 1: 기본 성능 향상
- TF-IDF 벡터화 적용
- N-gram 확장 (bigram, trigram)
- 하이퍼파라미터 튜닝
- 정규화 강화

#### Phase 2: 고급 모델 도입
- 임베딩 레이어 활용
- 순환 신경망 (RNN/LSTM)
- 합성곱 신경망 (CNN)
- 어텐션 메커니즘

#### Phase 3: 최신 기법 적용
- 사전 훈련 모델 (BERT, RoBERTa)
- 전이 학습 활용
- 멀티모달 접근
- 설명 가능한 AI

### 🔬 추가 실험 방향
- **데이터 증강**: 동의어 치환, 백번역
- **앙상블 학습**: 다양한 모델 조합
- **도메인 특화**: 의료, 금융, 법률 텍스트
- **실시간 시스템**: 웹 인터페이스 + API

---

## 📚 참고 자료

### 핵심 논문
- Maas et al. (2011): "Learning Word Vectors for Sentiment Analysis"
- Mikolov et al. (2013): "Efficient Estimation of Word Representations"
- Vaswani et al. (2017): "Attention Is All You Need"

### 실무 자료
- [TensorFlow Text Guide](https://www.tensorflow.org/text)
- [Hugging Face Transformers](https://huggingface.co/transformers)
- [Papers With Code NLP](https://paperswithcode.com/area/natural-language-processing)

### 한국어 NLP 자료
- KoBERT, KoGPT: 한국어 사전 훈련 모델
- 한국어 Embedding: FastText, Word2Vec
- 형태소 분석기: KoNLPy, Mecab

---

**🎉 학습 완료!** 자연어 처리의 기본 개념부터 실제 프로젝트 구현까지 완전한 NLP 파이프라인을 구축하는 방법을 학습했습니다.