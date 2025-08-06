# 🧠 Deep Learning 정리

##### 🗓️ 2025.08.06
##### 📝 Writer : Moon19ht

---

## 📚 목차

1. [의료비용 예측 딥러닝 모델 (0806_DL_Practice_1)](#1-의료비용-예측-딥러닝-모델)
2. [Fashion-MNIST 이미지 분류 모델 (0806_DL_Practice_2)](#2-fashion-mnist-이미지-분류-모델)
3. [핵심 개념 정리](#3-핵심-개념-정리)
4. [실습 비교 분석](#4-실습-비교-분석)

---

## 1. 의료비용 예측 딥러닝 모델

### 📋 프로젝트 개요
- **목표**: 개인의 특성(나이, BMI, 흡연여부 등)을 기반으로 의료비용을 예측하는 **회귀 모델**
- **데이터셋**: insurance.csv (보험 데이터)
- **모델 유형**: 완전연결 신경망 (Fully Connected Neural Network)
- **문제 유형**: 회귀 문제 (연속형 값 예측)

### 🎯 주요 특징
- **입력 특성**: age, sex, bmi, children, smoker, region
- **출력**: charges (의료비용, 연속형 값)
- **전처리**: 범주형 변수 원핫인코딩 + 수치형 변수 표준화

### 🏗️ 모델 아키텍처

```python
# 네트워크 구조
Input Layer (9개 특성)
    ↓
Dense(128, ReLU) - 첫 번째 은닉층
    ↓  
Dense(64, ReLU)  - 두 번째 은닉층
    ↓
Dense(1)         - 출력층 (회귀이므로 활성화 함수 없음)
```

#### 모델 설정
- **옵티마이저**: RMSprop (학습률: 0.001)
- **손실 함수**: MSE (Mean Squared Error)
- **평가 지표**: MAE (Mean Absolute Error)
- **조기 종료**: val_loss 기준, patience=10

### 📊 데이터 전처리 과정

#### 1. 범주형 변수 원핫인코딩
```python
categorical_features = ['sex', 'smoker', 'region']
df_encoded = pd.get_dummies(df, columns=categorical_features, drop_first=True)
```

#### 2. 수치형 변수 표준화 (Z-score)
```python
numerical_features = ['age', 'bmi', 'children']
# 각 특성을 (x - μ) / σ 로 표준화
```

#### 3. 데이터 분할
- **훈련/테스트**: 80% / 20%
- **검증 데이터**: 훈련 데이터의 20% (전체의 16%)

### 🎯 주요 기능 구현

#### 1. 모듈화된 함수 설계
```python
def load_insurance_data()          # 데이터 로딩
def preprocess_insurance_data()    # 전처리
def create_medical_cost_model()    # 모델 생성
def train_model()                  # 모델 훈련
def evaluate_and_visualize_model() # 평가 및 시각화
```

#### 2. 시각화 기능
- **타겟 분포**: 히스토그램, 박스플롯
- **훈련 히스토리**: 손실/MAE 그래프
- **예측 성능**: 산점도, 잔차 플롯, 오차 분포

#### 3. 성능 평가
- **MSE, MAE, RMSE** 계산
- **결정계수 (R²)** 측정
- **오차율** 분석 (MAE/평균 비율)

### 🔑 핵심 코드 패턴

#### 회귀 모델 구성
```python
model = keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=(input_shape,)),
    layers.Dense(64, activation='relu'),
    layers.Dense(1)  # 회귀: 출력층에 활성화 함수 없음
])

model.compile(
    optimizer='rmsprop',
    loss='mse',      # 회귀: MSE 손실
    metrics=['mae']  # 회귀: MAE 지표
)
```

---

## 2. Fashion-MNIST 이미지 분류 모델

### 📋 프로젝트 개요
- **목표**: Fashion-MNIST 데이터셋을 사용한 의류 이미지 **10-class 분류**
- **데이터셋**: Fashion-MNIST (28x28 흑백 이미지)
- **모델 유형**: Convolutional Neural Network (CNN)
- **문제 유형**: 다중 클래스 분류 문제

### 🎯 주요 특징
- **입력**: 28×28×1 픽셀 이미지 (흑백)
- **출력**: 10개 클래스 확률 (T-shirt, Trouser, Pullover 등)
- **클래스**: 10가지 의류 카테고리

### 🏗️ CNN 모델 아키텍처

```python
# 네트워크 구조
Input (28, 28, 1)
    ↓
Conv2D(32, 3x3, ReLU) → MaxPooling2D(2x2)  # 특징 추출 블록 1
    ↓
Conv2D(64, 3x3, ReLU) → MaxPooling2D(2x2)  # 특징 추출 블록 2  
    ↓
Flatten()                                   # 1D 변환
    ↓
Dense(64, ReLU) → Dense(32, ReLU)          # 완전연결층
    ↓
Dense(10, Softmax)                         # 출력층 (분류)
```

#### 모델 설정
- **옵티마이저**: Adam
- **손실 함수**: Sparse Categorical Crossentropy
- **평가 지표**: Accuracy
- **조기 종료**: val_loss 기준, patience=5

### 📊 데이터 전처리 과정

#### 1. 정규화 (픽셀 값 스케일링)
```python
X_train = X_train.astype("float32") / 255.0  # 0-255 → 0-1
X_test = X_test.astype("float32") / 255.0
```

#### 2. 차원 확장 (CNN용)
```python
X_train = np.expand_dims(X_train, -1)  # (28, 28) → (28, 28, 1)
X_test = np.expand_dims(X_test, -1)
```

#### 3. 레이블 처리
- **원핫인코딩 불필요**: `sparse_categorical_crossentropy` 사용
- 정수형 레이블 그대로 사용 (0~9)

### 🎯 주요 기능 구현

#### 1. 모듈화된 함수 설계
```python
def load_data()            # 데이터 로딩
def preprocessing()        # 전처리
def getModel()            # CNN 모델 생성
def train_model()         # 모델 훈련
def evaluate_model()      # 평가 및 분석
```

#### 2. 데이터 증강 옵션
```python
data_augmentation = keras.Sequential([
    layers.RandomFlip("horizontal"),
    layers.RandomRotation(0.1),
    layers.RandomZoom(0.2)
])
```

#### 3. 성능 평가
- **기본 지표**: 테스트 손실, 정확도
- **혼동 행렬**: 클래스별 분류 성능
- **분류 보고서**: 정밀도, 재현율, F1-점수

### 🔑 핵심 코드 패턴

#### CNN 분류 모델 구성
```python
model = keras.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    layers.MaxPooling2D((2,2)),
    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D((2,2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(32, activation='relu'),
    layers.Dense(10, activation='softmax')  # 분류: softmax 활성화
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',  # 다중분류: sparse categorical
    metrics=['accuracy']                     # 분류: accuracy 지표
)
```

---

## 3. 핵심 개념 정리

### 🧠 딥러닝 모델 유형 비교

| 구분 | 회귀 모델 | 분류 모델 |
|------|-----------|-----------|
| **문제 유형** | 연속형 값 예측 | 클래스 예측 |
| **출력층** | Dense(1) | Dense(클래스 수) |
| **활성화 함수** | 없음 (선형) | Softmax |
| **손실 함수** | MSE, MAE | CrossEntropy |
| **평가 지표** | MSE, MAE, R² | Accuracy, Precision, Recall |

### 🔧 전처리 방법

#### 회귀 문제 (의료비용 예측)
- **범주형 변수**: 원핫인코딩
- **수치형 변수**: 표준화 (Z-score)
- **타겟**: 그대로 사용 (연속형)

#### 분류 문제 (Fashion-MNIST)
- **이미지**: 정규화 (0-1 스케일)
- **차원**: CNN용 차원 확장
- **레이블**: 정수형 유지 (sparse categorical)

### 🏗️ 네트워크 아키텍처

#### 완전연결 신경망 (Dense Network)
- **용도**: 테이블 형태 데이터
- **구조**: Dense 레이어만 사용
- **특징**: 모든 뉴런이 연결됨

#### 합성곱 신경망 (CNN)
- **용도**: 이미지 데이터
- **구조**: Conv2D + MaxPooling + Dense
- **특징**: 지역적 패턴 인식

### ⚙️ 하이퍼파라미터 설정

#### 공통 설정
```python
# 훈련 설정
RANDOM_SEED = 42
TEST_SIZE = 0.2
VALIDATION_SPLIT = 0.2
MAX_EPOCHS = 100

# 조기 종료
EarlyStopping(monitor='val_loss', patience=5~10)
```

#### 옵티마이저 선택
- **RMSprop**: 회귀 문제에 적합
- **Adam**: 분류 문제에 널리 사용

### 📊 모델 평가 방법

#### 회귀 모델 평가
```python
# 수치적 지표
MSE = np.mean((y_true - y_pred)**2)
MAE = np.mean(np.abs(y_true - y_pred))
RMSE = np.sqrt(MSE)
R2 = 1 - SS_res / SS_tot

# 시각화
- 예측 vs 실제값 산점도
- 잔차 플롯
- 오차 분포 히스토그램
```

#### 분류 모델 평가
```python
# 수치적 지표
accuracy = np.mean(y_true == y_pred)
precision = tp / (tp + fp)
recall = tp / (tp + fn)
f1_score = 2 * (precision * recall) / (precision + recall)

# 시각화
- 혼동 행렬 (Confusion Matrix)
- 클래스별 성능 보고서
- 정확도 그래프
```

---

## 4. 실습 비교 분석

### 📊 두 실습의 차이점

| 구분 | 의료비용 예측 | Fashion-MNIST 분류 |
|------|---------------|-------------------|
| **데이터 유형** | 테이블형 (구조화 데이터) | 이미지 (비구조화 데이터) |
| **입력 차원** | 1D (9개 특성) | 3D (28×28×1 이미지) |
| **네트워크** | 완전연결 (Dense) | 합성곱 (CNN) |
| **문제 유형** | 회귀 | 다중 클래스 분류 |
| **출력** | 1개 연속값 | 10개 클래스 확률 |
| **전처리** | 원핫인코딩 + 표준화 | 정규화 + 차원 확장 |

### 🎯 공통 패턴

#### 1. 모듈화된 설계
```python
# 공통 파이프라인 패턴
def load_data()        # 데이터 로딩
def preprocess()       # 전처리
def create_model()     # 모델 생성
def train_model()      # 훈련
def evaluate_model()   # 평가
```

#### 2. 훈련 설정
```python
# 공통 콜백
early_stopping = EarlyStopping(
    monitor='val_loss',
    patience=5~10,
    restore_best_weights=True
)

# 공통 검증
validation_split=0.2
```

#### 3. 결과 저장
```python
# 모델 저장
model.save("model_name.keras")

# 히스토리 저장  
pickle.dump(history.history, f)
```

### 🔑 핵심 학습 포인트

#### 1. **문제 유형별 모델 설계**
- 회귀: Dense 네트워크, MSE 손실, 선형 출력
- 분류: CNN, CrossEntropy 손실, Softmax 출력

#### 2. **데이터 전처리의 중요성**
- 테이블 데이터: 범주형 인코딩, 수치형 정규화
- 이미지 데이터: 픽셀 정규화, 차원 조정

#### 3. **성능 평가 방법**
- 회귀: MSE, MAE, R², 잔차 분석
- 분류: Accuracy, Precision, Recall, 혼동행렬

#### 4. **코드 구조화**
- 함수 모듈화로 재사용성 향상
- 설정값 분리로 유지보수성 향상
- 시각화를 통한 결과 해석

### 📚 다음 학습 방향

1. **모델 개선 기법**
   - 드롭아웃, 배치 정규화
   - 하이퍼파라미터 튜닝
   - 교차 검증

2. **고급 아키텍처**
   - ResNet, DenseNet
   - Transfer Learning
   - Ensemble Methods

3. **실제 프로젝트 적용**
   - 실제 데이터셋 활용
   - 배포 고려사항
   - 성능 최적화

---

### 💡 핵심 요약

이번 실습을 통해 딥러닝의 두 가지 주요 문제 유형인 **회귀**와 **분류**를 모두 경험해보았습니다:

- **회귀 모델**: 의료비용 예측 → 연속형 값 예측
- **분류 모델**: Fashion-MNIST → 이미지 카테고리 분류

각각의 문제 유형에 맞는 **모델 아키텍처**, **손실 함수**, **평가 지표**를 선택하고, **전처리 방법**과 **성능 평가 기법**을 적절히 적용하는 것이 성공적인 딥러닝 프로젝트의 핵심입니다.