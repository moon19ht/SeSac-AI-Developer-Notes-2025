# 🧠 Deep Learning 정리

##### 🗓️ 2025.08.01
##### 📝 Writer : Moon19ht

---

## 📚 목차

1. [핵심 학습 목표](#핵심-학습-목표)
2. [Part I: 텍스트 벡터화 직접 구현](#part-i-텍스트-벡터화-직접-구현)
3. [Part II: Keras TextVectorization 활용](#part-ii-keras-textvectorization-활용)
4. [Part III: IMDB 감성 분석 프로젝트](#part-iii-imdb-감성-분석-프로젝트)
5. [구현 방법 비교 분석](#구현-방법-비교-분석)
6. [핵심 개념 정리](#핵심-개념-정리)
7. [발전 방향 및 차세대 기법](#발전-방향-및-차세대-기법)
8. [학습 성과 및 다음 단계](#학습-성과-및-다음-단계)
9. [참고 자료](#참고-자료)
10. [마무리](#마무리)

---

## 🎯 핵심 학습 목표

1. **텍스트 벡터화 이해**: 자연어를 컴퓨터가 처리 가능한 숫자로 변환하는 방법 학습
2. **실무 수준 NLP 파이프라인 구축**: 데이터 수집부터 모델 배포까지 전체 과정 경험
3. **Keras TextVectorization 활용**: 최적화된 텍스트 전처리 도구 사용법 습득
4. **감성 분석 모델 개발**: IMDB 데이터로 실제 이진 분류 모델 구현

---

## 📖 Part I: 텍스트 벡터화 직접 구현

### 1.1 MyVectorize 클래스 설계

직접 구현한 벡터화 시스템의 핵심 구조:

```python
class MyVectorize:
    def standardize(self, text):
        # 소문자 변환 + 구두점 제거
        text = text.lower()
        return "".join(c for c in text if c not in string.punctuation)
    
    def tokenize(self, text):
        # 공백 기준 단어 분할
        return text.split()
    
    def make_vocabulary(self, dataset):
        # 어휘 사전 구축 (특수 토큰 포함)
        self.vocabulary = {"": 0, "[UNK]": 1}
        # 데이터셋 순회하며 어휘 확장
    
    def encode(self, text):
        # 텍스트 → 숫자 시퀀스 변환
        return [self.vocabulary.get(token, 1) for token in tokens]
    
    def decode(self, int_sequence):
        # 숫자 시퀀스 → 텍스트 복원
        return " ".join(self.inverse_vocabulary.get(i, "[UNK]") for i in int_sequence)
```

### 1.2 핵심 처리 단계

**1단계: 표준화 (Standardization)**
- 대소문자 통일 → 일관성 확보
- 구두점 제거 → 노이즈 감소
- 예시: `"Hello, World!"` → `"hello world"`

**2단계: 토큰화 (Tokenization)**
- 공백 기준 단어 분할
- 예시: `"hello world"` → `["hello", "world"]`

**3단계: 어휘 사전 구축 (Vocabulary Building)**
- 특수 토큰: `""` (패딩), `"[UNK]"` (미등록 단어)
- 동적 사전 확장
- 양방향 매핑 지원

**4단계: 인코딩/디코딩 (Encoding/Decoding)**
- 텍스트 ↔ 숫자 시퀀스 상호 변환
- 미등록 단어는 `[UNK]` 토큰으로 처리

### 1.3 테스트 결과 분석

**테스트 데이터셋**:
```
1. "I write, erase, reqrite"
2. "Erase again, and then"  
3. "A poppy blooms"
4. "Dog is pretty"
```

**어휘 사전 구축 결과** (총 15개 단어):
- 특수 토큰: `""` (0), `"[UNK]"` (1)
- 일반 단어: `"i"` (2), `"write"` (3), `"erase"` (4) 등

**인코딩 예시**:
- `"I write erase"` → `[2, 3, 4]`
- 미등록 단어 포함시 → `[2, 1, 1, 7, 1]` (`[UNK]` = 1)

---

## 📊 Part II: Keras TextVectorization 활용

### 2.1 고급 벡터화 시스템

**TensorFlow 기반 최적화**:
```python
text_vectorization = TextVectorization(
    output_mode="int",  # 정수 시퀀스 출력
    standardize=custom_standardization_fn,  # 커스텀 전처리
    split=custom_split_fn  # 커스텀 토큰화
)
```

### 2.2 주요 개선 사항

**성능 최적화**:
- TensorFlow 백엔드 활용 → 189.5 문장/초 처리 속도
- GPU 가속 지원
- 배치 처리 내장 지원
- 메모리 효율적 구현

**기능 확장성**:
- 다양한 출력 모드: `int`, `binary`, `count`, `tf_idf`
- 빈도 기반 어휘 자동 정렬
- 어휘 크기 제한 기능 (`max_tokens`)
- 커스텀 전처리 함수 지원

### 2.3 출력 모드 비교

**테스트 문장**: `"I write erase rewrite"`

| 모드     | 출력 결과                | 특징                 |
| -------- | ------------------------ | -------------------- |
| `int`    | `[9, 3, 2, 5]`           | 단어 인덱스 시퀀스   |
| `binary` | `[0, 1, 1, 0, 1, ...]`   | 단어 존재 여부 (0/1) |
| `count`  | `[0, 1, 1, 0, 1, ...]`   | 단어 빈도 카운트     |
| `tf_idf` | `[0, 0.847, 1.099, ...]` | TF-IDF 가중치        |

### 2.4 딥러닝 모델 통합

**원시 텍스트 직접 처리**:
```python
model = Sequential([
    text_vectorization,  # 전처리 레이어
    Embedding(len(vocabulary), 16),
    LSTM(32),
    Dense(1, activation='sigmoid')
])

# 원시 텍스트를 모델에 직접 입력 가능
model.predict(["I love this movie"])
```

---

## 🎬 Part III: IMDB 감성 분석 프로젝트

### 3.1 프로젝트 개요

**데이터셋 특징**:
- **규모**: 50,000개 영화 리뷰 (훈련 25,000 + 테스트 25,000)
- **균형**: 긍정/부정 비율 50:50
- **품질**: 실제 IMDb 사용자 리뷰, 극단적 점수만 필터링

**기술 스택**:
- TensorFlow/Keras 딥러닝 프레임워크
- TextVectorization 텍스트 전처리
- Multi-hot encoding (Bag of Words)
- Dense Neural Network

### 3.2 데이터 처리 파이프라인

**1단계: 데이터 다운로드 및 준비**
```python
def download_imdb_dataset():
    # 스트리밍 다운로드로 메모리 효율성 확보
    # 진행률 표시 및 네트워크 오류 처리
    # 기존 파일 검증으로 중복 다운로드 방지
```

**2단계: 압축 해제 및 구조 검증**
```
aclImdb/
├── train/pos/    # 긍정 리뷰 12,500개
├── train/neg/    # 부정 리뷰 12,500개  
├── test/pos/     # 긍정 리뷰 12,500개
└── test/neg/     # 부정 리뷰 12,500개
```

**3단계: 검증 데이터 분할**
- 원본 train(25,000) → train(20,000) + validation(5,000)
- 클래스별 균등 분할로 편향 방지
- 무레이블 데이터 자동 제거

### 3.3 텍스트 벡터화 설정

**Multi-hot Encoding 방식**:
```python
text_vectorization = TextVectorization(
    max_tokens=20000,        # 상위 20,000개 단어만 사용
    output_mode="multi_hot"  # Bag of Words 방식
)
# → 각 리뷰를 20,000차원 이진 벡터로 변환
```

**벡터화 결과**:
- 입력 형태: `(batch_size, 20000)` float32 텐서
- 각 차원: 해당 단어 존재 여부 (0 또는 1)
- 희소 벡터: 대부분 값이 0인 고차원 벡터

### 3.4 모델 아키텍처

**Dense Neural Network**:
```python
def getModel(max_tokens=20000, hidden_dim=16):
    inputs = keras.Input(shape=(max_tokens,))       # 20,000차원 입력
    x = layers.Dense(hidden_dim, activation='relu')(inputs)  # 은닉층 16뉴런
    x = layers.Dropout(0.5)(x)                      # 드롭아웃 50%
    outputs = layers.Dense(1, activation='sigmoid')(x)      # 출력층 1뉴런
    return keras.Model(inputs, outputs)
```

**모델 특징**:
- 총 파라미터: 320,033개 (1.22MB)
- 입력층: 20,000차원 (어휘 사전 크기)
- 은닉층: 16뉴런 + ReLU 활성화
- 정규화: 드롭아웃 0.5로 과적합 방지
- 출력층: 시그모이드로 확률 출력

### 3.5 훈련 및 성능 결과

**훈련 설정**:
- 옵티마이저: RMSprop
- 손실 함수: Binary Crossentropy
- 배치 크기: 32
- 에포크: 10회

**성능 지표**:
- **테스트 정확도**: 87.42%
- **검증 정확도**: 최고 88.86% (에포크 6)
- **훈련 최적화**: 캐싱으로 첫 에포크 후 빠른 처리

**학습 패턴 분석**:
- 에포크 1-3: 빠른 성능 향상
- 에포크 4-6: 최고 성능 달성
- 에포크 7-10: 과적합 징후 (검증 손실 증가)

---

## 🔍 구현 방법 비교 분석

### 직접 구현 vs Keras TextVectorization

| 특징            | 직접 구현 (MyVectorize)      | Keras TextVectorization    |
| --------------- | ---------------------------- | -------------------------- |
| **구현 복잡도** | 높음 (모든 기능 직접 구현)   | 낮음 (내장 기능 활용)      |
| **성능**        | 파이썬 기반, 상대적으로 느림 | TensorFlow 최적화, 빠름    |
| **메모리 효율** | 기본적인 수준                | 매우 효율적                |
| **배치 처리**   | 별도 구현 필요               | 내장 지원                  |
| **GPU 가속**    | 지원하지 않음                | 완전 지원                  |
| **어휘 정렬**   | 삽입 순서                    | 빈도 기반 자동 정렬        |
| **출력 모드**   | 정수 시퀀스만                | int, binary, count, tf-idf |
| **모델 통합**   | 별도 연결 작업 필요          | Keras 레이어로 직접 연결   |

### 사용 권장 사항

**✅ Keras TextVectorization 권장**:
- 딥러닝 모델과 통합 사용
- 대용량 데이터 처리
- 성능이 중요한 운영 환경
- 다양한 벡터화 방식 필요

**✅ 직접 구현 권장**:
- 학습 및 이해 목적
- 매우 특수한 전처리 로직
- 외부 의존성 최소화
- 완전한 제어가 필요한 경우

---

## 💡 핵심 개념 정리

### 1. 텍스트 벡터화 이론

**왜 벡터화가 필요한가?**
- 머신러닝 모델은 **숫자**만 처리 가능
- 텍스트를 수치적 표현으로 변환하는 과정 필수
- 의미론적 관계를 수학적으로 표현

**주요 벡터화 기법**:

1. **Bag of Words (BoW)** - 본 프로젝트 사용
   ```
   "I love this movie" → [0, 1, 1, 0, 1, 0, ...]
   ```
   - 장점: 구현 간단, 해석 용이
   - 단점: 단어 순서 무시, 희소 벡터

2. **TF-IDF**
   ```
   TF-IDF = TF(단어 빈도) × IDF(역문서 빈도)
   ```
   - 장점: 중요한 단어에 가중치 부여
   - 단점: 여전히 순서 정보 없음

3. **Word Embeddings**
   ```
   "king" - "man" + "woman" ≈ "queen"
   ```
   - 장점: 의미론적 관계 표현
   - 단점: 사전 훈련 필요

### 2. 감성 분석 응용 분야

**🏢 산업별 활용**:
- **전자상거래**: 제품 리뷰 자동 분석
- **소셜 미디어**: 브랜드 멘션 모니터링
- **고객 서비스**: 문의 우선순위 분류
- **금융**: 뉴스 감성으로 시장 동향 예측

**📊 분류 유형**:
- **이진 분류**: 긍정/부정 (본 프로젝트)
- **다중 분류**: 매우 긍정/긍정/중립/부정/매우 부정
- **세밀한 감정**: 기쁨, 슬픔, 분노, 두려움 등

### 3. 실무 고려사항

**데이터 품질 관리**:
- HTML 태그 제거 필요
- 균형 잡힌 클래스 분포 확인
- 적절한 데이터 분할 (train/val/test)

**성능 최적화**:
- 캐싱으로 전처리 비용 절약
- 배치 처리로 처리량 향상
- GPU 활용으로 학습 가속화

**모델 해석성**:
- Bag of Words: 어떤 단어가 예측에 영향을 줬는지 추적 가능
- 가중치 분석으로 중요 특성 파악
- 비즈니스 로직과 연결 가능

---

## 🚀 발전 방향 및 차세대 기법

### 단계적 성능 개선 로드맵

**Phase 1: 기본 성능 향상** (즉시 적용 가능)
- TF-IDF 벡터화로 단어 중요도 반영
- N-gram 확장으로 단어 조합 패턴 인식
- 하이퍼파라미터 튜닝 (학습률, 배치 크기)
- 정규화 강화 (Batch Normalization, L2 Regularization)

**Phase 2: 고급 모델 도입** (중기 목표)
- 임베딩 레이어로 밀집 벡터 표현
- RNN/LSTM으로 순서 정보 활용
- CNN으로 지역적 패턴 인식
- 어텐션 메커니즘으로 중요 단어 집중

**Phase 3: 최신 기법 적용** (장기 목표)
- 사전 훈련 모델 (BERT, RoBERTa, GPT)
- 전이 학습으로 도메인 특화 파인튜닝
- 멀티모달 (텍스트 + 이미지 + 메타데이터)
- 설명 가능한 AI로 모델 결정 근거 제시

### 실무 확장 전략

**프로덕션 배포**:
```
사용자 입력 → API Gateway → 
전처리 서버 → ML 모델 서버 → 
결과 캐싱 → 클라이언트 응답
```

**모델 업데이트 파이프라인**:
```
1. 새로운 데이터 수집
2. 자동 재훈련 파이프라인
3. A/B 테스트로 성능 검증
4. 점진적 모델 배포
```

---

## 📝 학습 성과 및 다음 단계

### 🎓 획득한 핵심 역량

**기술적 역량**:
1. **완전한 NLP 파이프라인**: 텍스트 데이터 → 예측 결과
2. **대용량 데이터 처리**: 효율적인 I/O 및 메모리 관리
3. **실무 코딩 스킬**: 오류 처리, 로깅, 모니터링
4. **모델 평가 및 개선**: 성능 측정 및 최적화 전략

**개념적 이해**:
- 텍스트 벡터화의 다양한 방법론
- 딥러닝 모델과 전처리의 통합
- 성능 최적화를 위한 다양한 기법
- 실무 적용시 고려해야 할 사항들

### 🎯 추천 다음 학습 단계

**1. 심화 NLP 기법**
- Transformer 아키텍처 이해
- BERT, GPT 등 사전 훈련 모델 활용
- 한국어 NLP 특화 기법 (KoBERT, KoGPT)

**2. MLOps 및 배포**
- Docker 컨테이너화
- Kubernetes 오케스트레이션  
- CI/CD 파이프라인 구축

**3. 성능 최적화**
- 모델 압축 및 양자화
- 추론 속도 최적화
- 분산 학습 시스템

### 💼 실습 프로젝트 제안

**초급 프로젝트**:
1. 다른 언어 데이터셋 적용 (한국어 리뷰 분석)
2. 다양한 벡터화 방법 비교 연구
3. 웹 인터페이스로 실시간 감성 분석 시스템

**중급 프로젝트**:
4. 멀티클래스 감정 분류 (기쁨, 슬픔, 분노 등)
5. 도메인 특화 모델 (의료, 금융, 법률 텍스트)
6. 설명 가능한 AI 구현 (어떤 단어가 예측에 영향?)

**고급 프로젝트**:
7. 실시간 소셜 미디어 감성 모니터링
8. 다국어 감성 분석 시스템
9. 대화형 챗봇에 감성 분석 통합

---

## 🔗 참고 자료

### 핵심 논문
- **Maas et al. (2011)**: "Learning Word Vectors for Sentiment Analysis" - IMDB 데이터셋 원논문
- **Mikolov et al. (2013)**: "Efficient Estimation of Word Representations" - Word2Vec
- **Vaswani et al. (2017)**: "Attention Is All You Need" - Transformer 아키텍처

### 실무 자료
- **TensorFlow Text Guide**: https://www.tensorflow.org/text
- **Hugging Face Transformers**: https://huggingface.co/transformers  
- **Papers With Code NLP**: https://paperswithcode.com/area/natural-language-processing

### 한국어 NLP 자료
- **KoBERT, KoGPT**: 한국어 사전 훈련 모델
- **한국어 Embedding**: FastText, Word2Vec 한국어 버전
- **형태소 분석기**: KoNLPy, Mecab, Okt

---

## 🎉 마무리

이번 실습을 통해 자연어 처리의 전체 파이프라인을 경험하고, 텍스트 데이터를 활용한 실제 머신러닝 프로젝트를 완성했습니다. 

**주요 성과**:
- ✅ 텍스트 벡터화 원리 완전 이해
- ✅ 실무 수준의 코드 품질과 최적화 기법 습득
- ✅ 87.42% 정확도의 감성 분석 모델 구축
- ✅ 확장 가능한 아키텍처 설계 경험

이제 여러분은 텍스트 데이터를 다루는 실무 프로젝트에 바로 참여할 수 있는 역량을 갖추었습니다. 계속해서 새로운 기법을 학습하고, 더 복잡하고 흥미로운 NLP 프로젝트에 도전해보세요! 🚀

**다음 목표**: Transformer 기반 모델 (BERT, GPT)을 활용한 고급 NLP 프로젝트 도전! 💪