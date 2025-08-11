# 🧠 Deep Learning 정리

##### 🗓️ 2025.08.08
##### 📝 Writer : Moon19ht

---

## 📚 목차

1. [프로젝트 개요](#프로젝트-개요)
2. [환경 및 라이브러리](#환경-및-라이브러리)
3. [데이터셋 준비(NSMC)](#데이터셋-준비nsmc)
4. [데이터 로딩(Keras Dataset)](#데이터-로딩keras-dataset)
5. [한국어 전처리 파이프라인(Okt)](#한국어-전처리-파이프라인okt)
6. [텍스트 벡터화(TextVectorization)](#텍스트-벡터화textvectorization)
7. [사전 훈련 임베딩(FastText) 구성](#사전-훈련-임베딩fasttext-구성)
8. [모델 구조(BiLSTM)](#모델-구조bilstm)
9. [훈련 설정 및 콜백](#훈련-설정-및-콜백)
10. [평가 및 시각화](#평가-및-시각화)
11. [예측 사용 방법](#예측-사용-방법)
12. [재현(실행) 순서](#재현실행-순서)
13. [개선 방향](#개선-방향)

---

## 프로젝트 개요

네이버 영화 리뷰 데이터셋(NSMC)을 이용해 한국어 감성(긍정/부정) 분류 모델을 구현했습니다. 한국어 형태소 분석(Okt)과 사전 훈련 임베딩(FastText)을 결합하고, 양방향 LSTM(Bidirectional LSTM)으로 문맥 정보를 학습합니다. 프레임워크는 TensorFlow/Keras를 사용했습니다.

---

## 환경 및 라이브러리

- **주요 라이브러리**: TensorFlow/Keras, Korpora, KoNLPy(Okt), gensim(KeyedVectors), NumPy, Matplotlib
- **권장 설치**:
  ```bash
  pip install tensorflow Korpora konlpy gensim matplotlib
  ```
  노트북 최초 셀에 임포트와 버전 출력이 포함되어 있습니다.

---

## 데이터셋 준비(NSMC)

- Korpora로 NSMC를 다운로드/로드합니다: `Korpora.fetch("nsmc")`, `Korpora.load("nsmc")`
- Keras의 `text_dataset_from_directory`에 맞춰 폴더 구조를 생성하는 함수 `create_korean_dataset`를 제공합니다.
- 생성되는 디렉터리 구조(`korean_imdb`):
  ```
  korean_imdb/
    train/
      pos/  neg/
    val/
      pos/  neg/
    test/
      pos/  neg/
  ```
- 검증 세트는 훈련 데이터에서 각 1,000개를 분리해 구성합니다.

---

## 데이터 로딩(Keras Dataset)

- 배치 크기 `batch_size=32`
- `keras.utils.text_dataset_from_directory`로 `train/`, `val/`, `test/` 각각을 로드합니다.
- `label_mode="binary"`로 이진 분류에 맞는 라벨 형식 사용.

---

## 한국어 전처리 파이프라인(Okt)

- `clean_text`: 한글/영문/숫자/공백만 남기고 소문자화하는 정규식 정제.
- `Okt.morphs`로 형태소 단위 토큰화 후 공백으로 결합.
- TensorFlow 파이프라인과 연결을 위해 `tf.py_function`을 사용한 래퍼(`tf_korean_preprocess_fn`)로 `tf.data.Dataset`에 매핑합니다.

---

## 텍스트 벡터화(TextVectorization)

- 설정: `max_tokens=10,000`, `output_sequence_length=20`, `standardize=None`, `split="whitespace"`.
- 전처리된 훈련 데이터로 `adapt`하여 어휘 사전을 구축합니다.
- 성능을 위해 `cache().prefetch(tf.data.AUTOTUNE)` 적용.

---

## 사전 훈련 임베딩(FastText) 구성

- FastText 한국어 벡터(`cc.ko.300.vec`)를 상위 50,000개 토큰만 로드하여 메모리 절약.
- `vectorizer.get_vocabulary()` 기반으로 임베딩 행렬을 구성합니다.
- 파일이 없으면 임베딩 차원 300으로 랜덤 초기화합니다.

---

## 모델 구조(BiLSTM)

- 입력: 정수 인덱스 시퀀스.
- 임베딩: 사전 훈련 가중치 사용 시 `embeddings_initializer=Constant(embedding_matrix)`, `trainable=False`, `mask_zero=True`.
- 본체: `Bidirectional(LSTM(32))` + `Dropout(0.5)`.
- 출력: `Dense(1, activation='sigmoid')`.
- 컴파일: `optimizer='rmsprop'`, `loss='binary_crossentropy'`, `metrics=['accuracy']`.

---

## 훈련 설정 및 콜백

- 에폭: 10
- 콜백
  - `ModelCheckpoint("korean_rnn_model.keras", save_best_only=True, monitor='val_accuracy', mode='max')`
  - `EarlyStopping(monitor='val_accuracy', patience=3, restore_best_weights=True)`
- 학습 이력은 `korean_rnn_history.pkl`로 저장합니다.

---

## 평가 및 시각화

- `model.evaluate(test_ds_vectorized)`로 테스트 성능 평가.
- 학습/검증 정확도와 손실을 Matplotlib으로 시각화합니다.
- 노트북 기준 기대 성능(데이터/환경에 따라 변동): 테스트 정확도 약 85–90%.

---

## 예측 사용 방법

- `predict_sentiment(texts: list[str]) -> np.ndarray`를 제공.
- 입력 문장을 동일 전처리(Okt 형태소 분석) 후 `TextVectorization`으로 벡터화하고 모델 예측 확률을 반환합니다.
- 임계값 0.5 기준으로 긍/부정 판단을 출력 예시와 함께 제공합니다.

---

## 재현(실행) 순서

1) 라이브러리 임포트 확인 및 환경 점검

2) NSMC 다운로드 및 로드

3) `create_korean_dataset()` 실행하여 `korean_imdb` 디렉터리 생성(이미 있으면 스킵 가능)

4) `text_dataset_from_directory`로 train/val/test 로드

5) 전처리 파이프라인(`tf_korean_preprocess_fn`)을 모든 데이터셋에 적용 후 `vectorizer.adapt`

6) 데이터 벡터화 및 `cache/prefetch` 적용

7) 사전 훈련 임베딩(`cc.ko.300.vec`)을 루트에 두고 로드(없으면 랜덤 초기화)

8) 모델 구성/컴파일 → 학습(콜백 포함)

9) 테스트 평가 및 학습 곡선 시각화

10) `predict_sentiment`로 샘플 문장 예측 확인

---

## 개선 방향

1. **더 큰 모델**: BERT/KoBERT 등 Transformer 기반 모델 적용
2. **데이터 증강**: 역번역, 패러프레이징 등으로 일반화 성능 향상
3. **앙상블**: 서로 다른 아키텍처 결합으로 안정적 성능 확보
4. **하이퍼파라미터 최적화**: 그리드/베이지안 탐색
5. **도메인 특화**: 영화 외 도메인 데이터 병합 및 파인튜닝
