# 🧠 Deep Learning 정리 

##### 🗓️ 2025.07.24
##### 📝 Writer : Moon19ht

---

## 📚 목차

1. [개요](#개요)
2. [인라인 방식 Transfer Learning](#인라인-방식-transfer-learning)
3. [프로젝트 1: 개-고양이 이진 분류](#프로젝트-1-개-고양이-이진-분류)
4. [프로젝트 2: 꽃 이미지 다중 분류](#프로젝트-2-꽃-이미지-다중-분류)
5. [이진 분류 vs 다중 분류 심화 비교](#이진-분류-vs-다중-분류-심화-비교)
6. [인라인 vs 투스테이지 방식 비교](#인라인-vs-투스테이지-방식-비교)
7. [실시간 데이터 증강의 효과](#실시간-데이터-증강의-효과)
8. [성능 분석 및 결과](#성능-분석-및-결과)
9. [주요 학습 내용](#주요-학습-내용)
10. [결론 및 향후 과제](#결론-및-향후-과제)

---

## 📖 개요

이번 실습에서는 **인라인(Inline) 방식의 Transfer Learning**을 통해 두 가지 서로 다른 분류 문제를 해결했습니다. VGG19 사전훈련 모델을 전체 파이프라인에 통합하여 **end-to-end 학습**을 구현하고, **이진 분류**와 **다중 분류**의 차이점을 심도 있게 분석했습니다.

### 🎯 학습 목표
- **인라인 방식** Transfer Learning 구현 및 이해
- **이진 분류**와 **다중 분류** 모델 설계 차이점 파악
- **실시간 데이터 증강** 효과 체험
- **End-to-End 학습** 파이프라인 구축
- **투스테이지 vs 인라인** 방식 비교 분석

### 🛠️ 주요 기술 스택
- **프레임워크**: TensorFlow 2.15.1, Keras 2.15.0
- **사전훈련 모델**: VGG19 (ImageNet)
- **언어**: Python
- **라이브러리**: NumPy, Matplotlib, Pickle

### 🏆 주요 성과
- **이진 분류**: 개-고양이 97.30% 검증 정확도
- **다중 분류**: 꽃 5종 82.20% 테스트 정확도
- **실시간 증강**: 원본 이미지에 직접 적용 성공
- **End-to-End**: 입력부터 출력까지 통합 파이프라인

---

## 🔄 인라인 방식 Transfer Learning

### 💡 인라인 방식이란?
VGG19 사전훈련 모델을 전체 모델의 일부로 포함시켜 **하나의 통합된 파이프라인**으로 학습하는 방식입니다.

```python
# 인라인 방식의 핵심 구조
inputs = keras.Input(shape=(180, 180, 3))

# 1단계: 실시간 데이터 증강
x = data_augmentation(inputs)

# 2단계: VGG19 전처리
x = keras.applications.vgg19.preprocess_input(x)

# 3단계: VGG19 특성 추출 (동결)
x = conv_base(x)

# 4단계: 분류 네트워크
x = layers.Flatten()(x)
outputs = layers.Dense(클래스_수, activation="활성화함수")(x)

model = keras.Model(inputs, outputs)
```

### 🔍 인라인 vs 투스테이지 방식 비교

| 특성 | 인라인 방식 | 투스테이지 방식 |
|------|-------------|-----------------|
| **구조** | VGG19 포함 통합 모델 | 특성 추출 → 분류 학습 |
| **데이터 증강** | 원본 이미지에 직접 적용 | 추출된 특성에만 적용 |
| **학습 속도** | 상대적으로 느림 | 매우 빠름 |
| **메모리 사용** | 효율적 (배치별 처리) | 많음 (모든 특성 저장) |
| **과적합 방지** | 우수 (실시간 증강) | 보통 (제한적 증강) |
| **실무 활용도** | 높음 (일반적 방식) | 낮음 (프로토타이핑) |
| **모델 배포** | 간단 (단일 모델) | 복잡 (2단계 처리) |
| **확장성** | 대용량 데이터 적합 | 메모리 제약 존재 |

### ⚡ 인라인 방식의 장점
1. **실시간 증강**: 매 에포크마다 다른 증강된 이미지로 학습
2. **과적합 방지**: 데이터 다양성 증가로 일반화 성능 향상
3. **End-to-End**: 입력부터 출력까지 하나의 파이프라인
4. **실무적합성**: 실제 서비스 배포에 적합한 구조

---

## 🐱🐶 프로젝트 1: 개-고양이 이진 분류

### 📊 프로젝트 개요
- **목표**: VGG19 인라인 방식으로 개와 고양이 구분
- **데이터**: 각 클래스 1,000장 (Train), 500장 (Val), 500장 (Test)
- **방식**: 이진 분류 (Binary Classification)
- **총 데이터**: 4,000장

### 🏗️ 모델 아키텍처

```python
# 이진 분류 모델 구조
Model: "VGG19_Inline_Model"
_________________________________________________________________
Layer (type)                Output Shape              Param #   
=================================================================
input_layer (InputLayer)    [(None, 180, 180, 3)]     0         
data_augmentation           (None, 180, 180, 3)       0         
vgg19_preprocessing         (None, 180, 180, 3)       0         
vgg19 (Functional)          (None, 5, 5, 512)         20,024,384
flatten (Flatten)           (None, 12800)             0         
dense_256 (Dense)           (None, 256)               3,277,056 
dense_128 (Dense)           (None, 128)               32,896    
dense_64 (Dense)            (None, 64)                8,256     
output (Dense)              (None, 1)                 65        
=================================================================
Total params: 23,342,657 (89.05 MB)
Trainable params: 3,318,273 (12.66 MB)
Non-trainable params: 20,024,384 (76.39 MB)
```

### ⚙️ 이진 분류 설정

| 설정 항목 | 값 | 설명 |
|-----------|-----|------|
| **출력층** | Dense(1, activation="sigmoid") | 0~1 확률값 출력 |
| **손실 함수** | binary_crossentropy | 이진 분류 최적화 |
| **라벨 형태** | 0 (cat), 1 (dog) | 이진 정수 라벨 |
| **예측 방법** | predictions > 0.5 | 임계값 기반 분류 |
| **옵티마이저** | rmsprop | 적응적 학습률 |

### 🎨 데이터 증강 설정

```python
data_augmentation = keras.Sequential([
    layers.RandomFlip("horizontal"),      # 수평 뒤집기
    layers.RandomRotation(0.2),          # ±72도 회전
    layers.RandomZoom(0.4),              # ±40% 확대/축소
])
```

### 📈 학습 결과
- **훈련 정확도**: 94.30%
- **검증 정확도**: 97.30%
- **에포크**: 10회
- **학습 시간**: 인라인 방식 특성상 상대적으로 긴 시간

---

## 🌸 프로젝트 2: 꽃 이미지 다중 분류

### 📊 프로젝트 개요
- **목표**: 5가지 꽃 종류 분류 (daisy, dandelion, rose, sunflower, tulip)
- **데이터**: 총 2,746장 → Train(50%), Val(25%), Test(25%) 분할
- **방식**: 다중 분류 (Multi-Class Classification)
- **클래스**: 5개 (알파벳 순서로 자동 라벨링)

### 📁 데이터 분할 결과

| 클래스 | Train | Validation | Test | 총계 |
|---------|--------|------------|------|------|
| **Daisy** | 250개 | 125개 | 126개 | 501개 |
| **Dandelion** | 323개 | 161개 | 162개 | 646개 |
| **Rose** | 248개 | 124개 | 125개 | 497개 |
| **Sunflower** | 247개 | 123개 | 125개 | 495개 |
| **Tulip** | 303개 | 151개 | 153개 | 607개 |

### 🏗️ 다중 분류 모델 아키텍처

```python
# 다중 분류 모델 구조
Model: "VGG19_Flower_Classifier"
_________________________________________________________________
Layer (type)                Output Shape              Param #   
=================================================================
input_layer (InputLayer)    [(None, 180, 180, 3)]     0         
data_augmentation           (None, 180, 180, 3)       0         
vgg19_preprocessing         (None, 180, 180, 3)       0         
vgg19 (Functional)          (None, 5, 5, 512)         20,024,384
flatten (Flatten)           (None, 12800)             0         
dense_256 (Dense)           (None, 256)               3,277,056 
dense_128 (Dense)           (None, 128)               32,896    
dense_64 (Dense)            (None, 64)                8,256     
output_5_classes (Dense)    (None, 5)                 325       
=================================================================
Total params: 23,342,661 (89.05 MB)
Trainable params: 3,318,277 (12.66 MB)
Non-trainable params: 20,024,384 (76.39 MB)
```

### ⚙️ 다중 분류 설정

| 설정 항목 | 값 | 설명 |
|-----------|-----|------|
| **출력층** | Dense(5, activation="softmax") | 5개 클래스 확률 분포 |
| **손실 함수** | sparse_categorical_crossentropy | 정수 라벨 다중 분류 |
| **라벨 형태** | 0,1,2,3,4 (daisy→tulip) | 정수 인덱스 |
| **예측 방법** | np.argmax(predictions, axis=1) | 최대 확률 클래스 선택 |
| **옵티마이저** | adam | 안정적 학습률 조정 |

### 🏷️ 클래스 라벨 매핑

```python
# Keras 자동 라벨링 (알파벳 순서)
클래스_매핑 = {
    0: 'daisy',
    1: 'dandelion', 
    2: 'rose',
    3: 'sunflower',
    4: 'tulip'
}
```

### 📈 학습 결과
- **훈련 정확도**: 89.13%
- **검증 정확도**: 81.43%
- **테스트 정확도**: 82.20%
- **에포크**: 10회

### 🔍 예측 분석 예시

```python
# 첫 번째 배치 예측 결과 (처음 10개)
✅ 실제: dandelion | 예측: dandelion (신뢰도: 1.000)
❌ 실제: sunflower | 예측: tulip (신뢰도: 0.986)
✅ 실제: daisy | 예측: daisy (신뢰도: 0.987)
✅ 실제: rose | 예측: rose (신뢰도: 0.937)
✅ 실제: dandelion | 예측: dandelion (신뢰도: 0.997)
```

---

## 🔍 이진 분류 vs 다중 분류 심화 비교

### 📊 기술적 차이점

| 구분 | 이진 분류 (개-고양이) | 다중 분류 (꽃 5종) |
|------|---------------------|-------------------|
| **클래스 수** | 2개 | 5개 |
| **출력층 구조** | Dense(1, sigmoid) | Dense(5, softmax) |
| **출력 해석** | 단일 확률값 (0~1) | 5개 확률의 합=1 |
| **손실 함수** | binary_crossentropy | sparse_categorical_crossentropy |
| **라벨 형태** | 0 또는 1 | 0, 1, 2, 3, 4 |
| **예측 방법** | predictions > 0.5 | np.argmax(predictions) |
| **난이도** | 상대적으로 쉬움 | 상대적으로 어려움 |
| **혼동 가능성** | 2개 클래스 간만 | 5개 클래스 간 다양한 혼동 |

### 🎯 수학적 차이점

#### 이진 분류
```python
# Sigmoid 활성화
output = 1 / (1 + e^(-x))  # 0~1 범위

# Binary Crossentropy 손실
loss = -[y*log(p) + (1-y)*log(1-p)]

# 예측
prediction = 1 if output > 0.5 else 0
```

#### 다중 분류
```python
# Softmax 활성화  
output_i = e^(x_i) / Σ(e^(x_j))  # 모든 출력의 합=1

# Sparse Categorical Crossentropy 손실
loss = -log(p_true_class)

# 예측
prediction = argmax(outputs)
```

### 📈 성능 비교 분석

| 지표 | 이진 분류 | 다중 분류 | 분석 |
|------|-----------|-----------|------|
| **검증 정확도** | 97.30% | 81.43% | 이진 분류가 높음 |
| **클래스당 정확도** | 97.30% (균등) | 약 82% (불균등) | 다중 분류에서 클래스별 차이 |
| **과적합 정도** | 낮음 | 보통 | 클래스 수 증가에 따른 복잡도 상승 |
| **학습 안정성** | 높음 | 보통 | 이진 분류가 더 안정적 |

---

## 🎨 실시간 데이터 증강의 효과

### 💡 인라인 방식에서의 데이터 증강

```python
# 실시간 데이터 증강 파이프라인
data_augmentation = keras.Sequential([
    layers.RandomFlip("horizontal"),      # 50% 확률로 수평 뒤집기
    layers.RandomRotation(0.2),          # ±72도 범위 회전
    layers.RandomZoom(0.4),              # ±40% 확대/축소
])

# 매 배치마다 다른 변형 적용
for epoch in range(epochs):
    for batch in dataset:
        augmented_batch = data_augmentation(batch)  # 실시간 변형
        # 학습 진행...
```

### 📊 데이터 증강 효과 분석

| 효과 | 설명 | 이진 분류 결과 | 다중 분류 결과 |
|------|------|---------------|---------------|
| **과적합 방지** | 매번 다른 이미지로 학습 | 훈련 94.3% vs 검증 97.3% | 훈련 89.1% vs 검증 81.4% |
| **일반화 성능** | 다양한 변형에 강건 | 높은 검증 성능 | 안정적인 테스트 성능 |
| **데이터 다양성** | 제한된 데이터 효과적 활용 | 4,000장 → 무한 변형 | 2,746장 → 무한 변형 |
| **학습 속도** | 실시간 처리로 느림 | 에포크당 약 1분 | 에포크당 약 1.5분 |

### 🔄 투스테이지 vs 인라인 데이터 증강 비교

| 특성 | 투스테이지 방식 | 인라인 방식 |
|------|----------------|-------------|
| **증강 시점** | 특성 추출 후 제한적 | 원본 이미지에 직접 |
| **증강 효과** | 제한적 (이미 추출된 특성) | 최대 (픽셀 레벨 변형) |
| **다양성** | 낮음 | 높음 |
| **과적합 방지** | 보통 | 우수 |

---

## 📊 성능 분석 및 결과

### 🏆 전체 성능 요약

| 프로젝트 | 분류 유형 | 클래스 수 | 데이터 수 | 검증 정확도 | 테스트 정확도 |
|----------|-----------|-----------|-----------|-------------|---------------|
| **개-고양이** | 이진 분류 | 2개 | 4,000장 | 97.30% | - |
| **꽃 분류** | 다중 분류 | 5개 | 2,746장 | 81.43% | 82.20% |

### 📈 성능 향상 요인

#### 이진 분류 (개-고양이) 고성능 원인
1. **단순한 문제**: 2개 클래스만 구분
2. **명확한 차이**: 개와 고양이는 시각적으로 뚜렷한 차이
3. **충분한 데이터**: 각 클래스당 2,000장의 학습 데이터
4. **VGG19 적합성**: ImageNet의 동물 특성이 잘 전이됨

#### 다중 분류 (꽃) 상대적 저성능 원인
1. **복잡한 문제**: 5개 클래스 간 구분
2. **유사한 특성**: 일부 꽃들 간 시각적 유사성
3. **클래스 불균형**: 646개(dandelion) vs 495개(sunflower)
4. **세밀한 분류**: 꽃의 종류 구분은 더 정교한 특성 필요

### 🎯 성능 개선 방향

#### 이진 분류 개선 방안
1. **Fine-tuning**: VGG19 상위 레이어도 함께 학습
2. **앙상블**: 여러 모델의 예측 결합
3. **Test 평가**: 실제 테스트 성능 측정

#### 다중 분류 개선 방안
1. **데이터 증강 강화**: 클래스별 특성에 맞는 증강
2. **클래스 가중치**: 불균형 데이터 보정
3. **Confusion Matrix**: 혼동되는 클래스 쌍 분석
4. **더 깊은 네트워크**: ResNet, EfficientNet 등 시도

---

## 📚 주요 학습 내용

### 1. 인라인 Transfer Learning 구현

```python
# 핵심 구현 패턴
def create_inline_model():
    # 1. 사전훈련 모델 로드 및 동결
    conv_base = VGG19(weights="imagenet", include_top=False)
    conv_base.trainable = False
    
    # 2. 데이터 증강 레이어
    data_augmentation = keras.Sequential([...])
    
    # 3. 전체 모델 통합
    inputs = keras.Input(shape=(180, 180, 3))
    x = data_augmentation(inputs)
    x = preprocess_input(x)
    x = conv_base(x)
    outputs = classification_head(x)
    
    return keras.Model(inputs, outputs)
```

### 2. 분류 문제별 설정 차이

```python
# 이진 분류 설정
model.compile(
    loss="binary_crossentropy",
    optimizer="rmsprop",
    metrics=["accuracy"]
)

# 다중 분류 설정  
model.compile(
    loss="sparse_categorical_crossentropy",
    optimizer="adam", 
    metrics=["accuracy"]
)
```

### 3. 실시간 데이터 전처리 파이프라인

```python
# 이미지 → 증강 → 전처리 → 특성추출 → 분류
원본_이미지 → RandomFlip/Rotation/Zoom → VGG19_preprocessing → VGG19_CNN → 분류층
```

### 4. 모델 최적화 기법

```python
# 최적 모델 자동 저장
callbacks = [
    keras.callbacks.ModelCheckpoint(
        filepath="best_model_weights.h5",
        save_weights_only=True,
        save_best_only=True,
        monitor="val_accuracy",
        mode='max'
    )
]
```

### 5. 성능 평가 및 분석

```python
# 다중 분류 예측 분석
predictions = model.predict(test_data)
predicted_classes = np.argmax(predictions, axis=1)
confidence_scores = np.max(predictions, axis=1)

# 클래스별 성능 분석
for i, (true_class, pred_class, confidence) in enumerate(zip(true_labels, predicted_classes, confidence_scores)):
    status = "✅" if true_class == pred_class else "❌"
    print(f"{status} 실제: {class_names[true_class]} | 예측: {class_names[pred_class]} (신뢰도: {confidence:.3f})")
```

---

## 🎯 결론 및 향후 과제

### ✅ 완료한 학습 내용
1. **인라인 Transfer Learning** 마스터: VGG19 통합 파이프라인 구축
2. **이진 vs 다중 분류** 차이점 이해: 출력층, 손실함수, 평가 방법
3. **실시간 데이터 증강** 활용: 과적합 방지 및 성능 향상
4. **End-to-End 학습** 구현: 입력부터 출력까지 통합 처리
5. **성능 분석** 기법: 클래스별 정확도, 신뢰도 분석

### 🏆 주요 성과

#### 기술적 성과
- **인라인 방식** 성공적 구현으로 실무 적용 가능한 모델 개발
- **97.30% 이진 분류** 달성으로 높은 성능 입증
- **82.20% 다중 분류** 달성으로 복잡한 문제 해결 능력 확보
- **실시간 증강** 적용으로 과적합 효과적 방지

#### 방법론적 성과
- **투스테이지 vs 인라인** 방식 비교를 통한 깊은 이해
- **분류 문제 유형별** 접근법 차이 학습
- **VGG19 활용법** 다양한 도메인 적용 경험

### 📈 향후 개선 방향

#### 1. 모델 아키텍처 개선
```python
# Fine-tuning 구현
conv_base.trainable = True
# 상위 레이어만 학습 허용
for layer in conv_base.layers[:-4]:
    layer.trainable = False
```

#### 2. 고급 데이터 증강
```python
# 더 정교한 증강 기법
advanced_augmentation = keras.Sequential([
    layers.RandomCrop(160, 160),     # 랜덤 크롭
    layers.RandomBrightness(0.2),    # 밝기 조절
    layers.RandomContrast(0.2),      # 대비 조절
])
```

#### 3. 다양한 사전훈련 모델 실험
- **ResNet50/101**: 깊은 잔차 네트워크
- **EfficientNet**: 효율적 스케일링
- **Vision Transformer**: 어텐션 기반 모델
- **MobileNet**: 경량화 모델 (모바일 배포용)

#### 4. 고급 평가 및 해석
```python
# Confusion Matrix 생성
from sklearn.metrics import classification_report, confusion_matrix

# Grad-CAM 시각화 (모델 해석)
# 어떤 부분을 보고 판단하는지 시각화

# 클래스별 성능 분석
# 어떤 클래스가 어떤 클래스와 혼동되는지 분석
```

### 🚀 실용적 활용 방안

#### 1. 웹 애플리케이션 개발
```python
# Flask/FastAPI 서버
@app.route('/predict', methods=['POST'])
def predict_image():
    image = preprocess_image(request.files['image'])
    prediction = model.predict(image)
    return jsonify({'class': class_names[np.argmax(prediction)]})
```

#### 2. 모바일 앱 배포
- **TensorFlow Lite** 변환으로 모델 경량화
- **Android/iOS** 앱에서 실시간 카메라 분류
- **Edge 디바이스** 배포 (Raspberry Pi, Jetson Nano)

#### 3. 클라우드 서비스
- **AWS SageMaker**, **Google AI Platform** 배포
- **REST API** 형태로 서비스 제공
- **배치 처리** 시스템 구축

### 💡 핵심 인사이트

#### 1. 방법론 선택의 중요성
- **투스테이지**: 빠른 프로토타이핑, 소규모 데이터
- **인라인**: 실무 배포, 고성능 요구, 대규모 데이터

#### 2. 분류 문제별 접근법
- **이진 분류**: Sigmoid, BCE, 임계값 기반 예측
- **다중 분류**: Softmax, SCE, 최대 확률 기반 예측

#### 3. 데이터 증강의 위력
- **실시간 적용**으로 무한한 데이터 다양성 확보
- **과적합 방지**와 **일반화 성능** 동시 향상

#### 4. Transfer Learning의 효과
- **VGG19 ImageNet 지식**이 다양한 도메인에 효과적 전이
- **적절한 동결**과 **분류층 설계**가 성능 좌우

### 📝 마무리

이번 실습을 통해 **인라인 방식 Transfer Learning**의 강력함과 **이진/다중 분류**의 차이점을 실제 구현을 통해 체험했습니다. 특히 **실시간 데이터 증강**이 과적합 방지에 미치는 강력한 효과와, **End-to-End 학습**이 실무 배포에 가져다주는 편의성을 확인할 수 있었습니다.

앞으로는 **Fine-tuning**, **고급 증강 기법**, **다양한 사전훈련 모델** 등을 활용하여 더욱 정교하고 실용적인 딥러닝 모델을 구축해나가겠습니다.

---

### 📊 부록: 실험 결과 비교표

| 항목 | 이진 분류 (개-고양이) | 다중 분류 (꽃 5종) |
|------|---------------------|-------------------|
| **사전훈련 모델** | VGG19 (ImageNet) | VGG19 (ImageNet) |
| **방식** | 인라인 Transfer Learning | 인라인 Transfer Learning |
| **데이터 수** | 4,000장 | 2,746장 |
| **클래스 수** | 2개 | 5개 |
| **검증 정확도** | 97.30% | 81.43% |
| **테스트 정확도** | - | 82.20% |
| **총 파라미터** | 23,342,657개 | 23,342,661개 |
| **훈련 파라미터** | 3,318,273개 | 3,318,277개 |
| **모델 크기** | 89.05 MB | 89.05 MB |
| **에포크** | 10회 | 10회 |
| **학습 시간** | 약 10분 | 약 15분 |