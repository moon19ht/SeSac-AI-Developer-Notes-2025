# 🧠 Deep Learning 정리

##### 🗓️ 2025.07.17
##### 📝 Writer : Moon19ht

---

## 📚 목차

1. [딥러닝 개요](#1-딥러닝-개요)
2. [딥러닝 구현 환경](#2-딥러닝-구현-환경)
3. [신경망 모델 구조](#3-신경망-모델-구조)
4. [데이터 전처리](#4-데이터-전처리)
5. [모델 컴파일과 학습](#5-모델-컴파일과-학습)
6. [성능 평가와 분석](#6-성능-평가와-분석)
7. [실습 비교 분석](#7-실습-비교-분석)
8. [최적화 기법](#8-최적화-기법)

---

## 1. 딥러닝 개요

### 1.1 딥러닝이란?
- **정의**: 인공신경망을 기반으로 한 머신러닝의 한 분야
- **특징**: 다층 퍼셉트론(Multi-Layer Perceptron, MLP)을 통한 복잡한 패턴 학습
- **장점**: 대용량 데이터에서 뛰어난 성능, 자동 특성 추출
- **단점**: 많은 데이터와 연산 자원이 필요, 해석이 어려움

### 1.2 딥러닝 vs 전통적 머신러닝

| 구분            | 딥러닝                 | 전통적 머신러닝         |
| --------------- | ---------------------- | ----------------------- |
| **데이터 크기** | 대용량 데이터에 유리   | 소량~중간 데이터에 적합 |
| **특성 추출**   | 자동 특성 추출         | 수동 특성 엔지니어링    |
| **해석성**      | 블랙박스 (해석 어려움) | 상대적으로 해석 용이    |
| **연산 자원**   | GPU 등 고성능 필요     | 상대적으로 적은 자원    |
| **학습 시간**   | 상대적으로 오래 걸림   | 빠른 학습               |

---

## 2. 딥러닝 구현 환경

### 2.1 필수 라이브러리

#### TensorFlow/Keras
```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import models, layers
from tensorflow.keras.utils import to_categorical
```

#### 데이터 처리
```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
import numpy as np
```

### 2.2 환경 설정
```python
# 재현 가능한 결과를 위한 랜덤 시드 설정
tf.random.set_seed(1234)

# TensorFlow 버전 확인
print("TensorFlow 버전:", tf.__version__)
```

---

## 3. 신경망 모델 구조

### 3.1 Sequential 모델

#### 기본 구조
```python
model = keras.Sequential([
    layers.Dense(뉴런수, activation='활성화함수'),
    layers.Dense(뉴런수, activation='활성화함수'),
    layers.Dense(출력뉴런수, activation='출력활성화함수')
])
```

#### MNIST 예제 구조
```python
model = keras.Sequential([
    layers.Dense(256, activation='relu'),  # 은닉층 1
    layers.Dense(256, activation='relu'),  # 은닉층 2
    layers.Dense(128, activation='relu'),  # 은닉층 3
    layers.Dense(64, activation='relu'),   # 은닉층 4
    layers.Dense(10, activation='softmax') # 출력층 (10개 클래스)
])
```

#### Iris 예제 구조
```python
network = keras.Sequential([
    layers.Dense(64, activation='relu'),   # 은닉층 1
    layers.Dense(64, activation='relu'),   # 은닉층 2
    layers.Dense(128, activation='relu'),  # 은닉층 3
    layers.Dense(3, activation='softmax')  # 출력층 (3개 클래스)
])
```

### 3.2 활성화 함수

#### ReLU (Rectified Linear Unit)
- **공식**: f(x) = max(0, x)
- **특징**: 계산이 간단하고 기울기 소실 문제 완화
- **용도**: 은닉층에서 주로 사용

#### Softmax
- **공식**: f(xi) = e^xi / Σe^xj
- **특징**: 출력값의 합이 1이 되는 확률 분포 생성
- **용도**: 다중분류 문제의 출력층

#### Sigmoid
- **공식**: f(x) = 1 / (1 + e^-x)
- **특징**: 0과 1 사이의 값 출력
- **용도**: 이진분류 문제의 출력층

### 3.3 출력층 설계 패턴

| 문제 유형    | 출력층 구조                             | 활성화 함수 | 손실 함수                |
| ------------ | --------------------------------------- | ----------- | ------------------------ |
| **회귀**     | `Dense(1)`                              | 없음        | MSE                      |
| **이진분류** | `Dense(1, activation='sigmoid')`        | Sigmoid     | Binary Crossentropy      |
| **다중분류** | `Dense(클래스수, activation='softmax')` | Softmax     | Categorical Crossentropy |

---

## 4. 데이터 전처리

### 4.1 MNIST 데이터 전처리

#### 차원 변환
```python
# 3차원(28×28×1) → 2차원(784×1)로 평면화
train_images = train_images.reshape(train_images.shape[0], 28 * 28)
test_images = test_images.reshape(test_images.shape[0], 28 * 28)
```

#### 정규화 (0~1 스케일링)
```python
# 픽셀 값을 0~255 → 0~1 범위로 변환
train_images = train_images.astype(float) / 255
test_images = test_images.astype(float) / 255
```

### 4.2 Iris 데이터 전처리

#### StandardScaler를 이용한 정규화
```python
scaler = StandardScaler()

# 훈련 데이터로 스케일러 학습 후 변환
X_train_scaled = scaler.fit_transform(X_train)

# 테스트 데이터는 훈련 데이터의 스케일로 변환
X_test_scaled = scaler.transform(X_test)  # fit 없이 transform만!
```

### 4.3 라벨 인코딩

#### 원-핫 인코딩 (One-Hot Encoding)
```python
# 정수 라벨 → 원-핫 인코딩
y_train_encoded = to_categorical(y_train)
y_test_encoded = to_categorical(y_test)

# 예시: [0, 1, 2] → [[1,0,0], [0,1,0], [0,0,1]]
```

### 4.4 손실함수별 라벨 형태

| 손실함수                          | 라벨 형태    | 예시                        |
| --------------------------------- | ------------ | --------------------------- |
| `sparse_categorical_crossentropy` | 정수         | [0, 1, 2]                   |
| `categorical_crossentropy`        | 원-핫 인코딩 | [[1,0,0], [0,1,0], [0,0,1]] |

---

## 5. 모델 컴파일과 학습

### 5.1 모델 컴파일

#### 기본 구조
```python
model.compile(
    optimizer='옵티마이저',
    loss='손실함수',
    metrics=['평가지표']
)
```

#### MNIST 예제
```python
model.compile(
    optimizer='rmsprop',
    loss='sparse_categorical_crossentropy',  # 정수 라벨용
    metrics=['accuracy']
)
```

#### Iris 예제
```python
network.compile(
    optimizer='rmsprop',
    loss='categorical_crossentropy',         # 원-핫 인코딩용
    metrics=['accuracy']
)
```

### 5.2 주요 옵티마이저

| 옵티마이저  | 특징                | 적용 상황               |
| ----------- | ------------------- | ----------------------- |
| **SGD**     | 기본적인 경사하강법 | 간단한 문제             |
| **RMSprop** | 학습률 자동 조정    | 일반적인 딥러닝         |
| **Adam**    | 모멘텀 + RMSprop    | 대부분의 경우 좋은 성능 |

### 5.3 모델 학습

#### 학습 실행
```python
history = model.fit(
    X_train,           # 입력 데이터
    y_train,           # 타겟 데이터
    epochs=100,        # 학습 회수
    batch_size=128,    # 배치 크기
    verbose=1          # 진행상황 출력
)
```

#### 배치 크기 선택 기준
- **너무 크면**: 메모리 부족, 일반화 성능 저하
- **너무 작으면**: 학습 속도 느림, 불안정한 학습
- **권장값**: 32, 64, 128, 256 등의 2의 거듭제곱

---

## 6. 성능 평가와 분석

### 6.1 모델 평가

#### 기본 평가
```python
# 훈련셋 성능
train_loss, train_acc = model.evaluate(X_train, y_train, verbose=0)

# 테스트셋 성능
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
```

### 6.2 과적합 판단

#### 과적합 진단
```python
accuracy_diff = train_acc - test_acc

if accuracy_diff > 0.05:  # 5% 이상 차이
    print("⚠️ 과적합(Overfitting) 가능성")
else:
    print("✅ 적절한 일반화 성능")
```

### 6.3 성능 개선 방법

#### 과적합 방지 기법
1. **Dropout**: 일부 뉴런을 무작위로 비활성화
2. **Early Stopping**: 검증 손실이 증가하면 학습 중단
3. **Regularization**: L1/L2 정규화 추가
4. **Data Augmentation**: 데이터 증강

#### 학습 성능 향상
1. **Batch Normalization**: 배치 정규화로 학습 안정화
2. **Learning Rate Scheduling**: 학습률 동적 조정
3. **더 깊은 네트워크**: 층 수 증가
4. **다른 활성화 함수**: Leaky ReLU, ELU 등

---

## 7. 실습 비교 분석

### 7.1 MNIST vs Iris 비교

| 구분              | MNIST                           | Iris                     |
| ----------------- | ------------------------------- | ------------------------ |
| **데이터 크기**   | 70,000개 (대용량)               | 150개 (소량)             |
| **입력 차원**     | 784 (28×28 이미지)              | 4 (수치형 특성)          |
| **클래스 수**     | 10개 (0~9 숫자)                 | 3개 (꽃 품종)            |
| **데이터 분할**   | 기본 제공                       | train_test_split 사용    |
| **전처리**        | 차원변환 + 0~1 정규화           | StandardScaler 정규화    |
| **라벨 형태**     | 정수 라벨                       | 원-핫 인코딩             |
| **손실함수**      | sparse_categorical_crossentropy | categorical_crossentropy |
| **학습 시간**     | 상대적으로 오래 걸림            | 매우 빠름                |
| **네트워크 크기** | 큰 네트워크 필요                | 작은 네트워크로 충분     |

### 7.2 데이터셋별 적합한 접근법

#### 대용량 데이터 (MNIST 형태)
- 딥러닝의 장점이 잘 드러남
- 복잡한 네트워크 구조 가능
- GPU 사용 권장
- 정규화 기법 필수

#### 소량 데이터 (Iris 형태)
- 전통적 머신러닝도 효과적
- 간단한 네트워크로도 충분
- 과적합 주의 필요
- 특성 엔지니어링 중요

---

## 8. 최적화 기법

### 8.1 하이퍼파라미터 튜닝

#### 주요 하이퍼파라미터
1. **학습률 (Learning Rate)**: 가중치 업데이트 크기
2. **배치 크기 (Batch Size)**: 한 번에 처리할 샘플 수
3. **에포크 (Epochs)**: 전체 데이터셋 반복 횟수
4. **네트워크 구조**: 층 수, 뉴런 수
5. **활성화 함수**: ReLU, Sigmoid, Tanh 등

#### 튜닝 전략
1. **Grid Search**: 모든 조합 시도
2. **Random Search**: 무작위 조합 시도
3. **Bayesian Optimization**: 베이지안 최적화
4. **Early Stopping**: 조기 종료로 최적점 찾기

### 8.2 모델 개선 방향

#### 성능 향상 방법
1. **CNN 사용**: 이미지 데이터에 특화
2. **RNN/LSTM**: 시계열 데이터에 특화
3. **Attention Mechanism**: 중요한 부분에 집중
4. **Transfer Learning**: 사전 훈련된 모델 활용

#### 실무 적용 고려사항
1. **계산 복잡도**: 실시간 추론 가능성
2. **메모리 사용량**: 모바일/임베디드 환경
3. **해석 가능성**: 비즈니스 요구사항
4. **유지보수성**: 모델 업데이트 용이성

---

## 💡 핵심 포인트 정리

### ✅ 딥러닝 모델 개발 단계
1. **데이터 준비**: 수집, 탐색, 전처리
2. **모델 설계**: 네트워크 구조, 활성화 함수 선택
3. **모델 컴파일**: 옵티마이저, 손실함수, 평가지표 설정
4. **모델 학습**: epochs, batch_size 조정하며 훈련
5. **성능 평가**: 과적합 여부 확인, 일반화 성능 검증
6. **모델 개선**: 하이퍼파라미터 튜닝, 정규화 기법 적용

### 🎯 문제 유형별 템플릿

#### 이미지 분류 (MNIST 스타일)
- 데이터: 차원 변환 + 0~1 정규화
- 라벨: 정수 형태 유지
- 손실: sparse_categorical_crossentropy
- 출력: Dense(클래스수, activation='softmax')

#### 수치 데이터 분류 (Iris 스타일)
- 데이터: StandardScaler 정규화
- 라벨: 원-핫 인코딩
- 손실: categorical_crossentropy
- 출력: Dense(클래스수, activation='softmax')

### 📚 다음 학습 방향
1. **CNN (Convolutional Neural Network)**: 이미지 처리 특화
2. **RNN/LSTM**: 시계열, 자연어 처리
3. **고급 정규화**: Dropout, Batch Normalization
4. **전이 학습**: 사전 훈련된 모델 활용
5. **실전 프로젝트**: 실제 데이터셋으로 end-to-end 구현
