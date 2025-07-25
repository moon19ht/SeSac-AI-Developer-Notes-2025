# 🧠 Deep Learning 정리 

##### 🗓️ 2025.07.23
##### 📝 Writer : Moon19ht

---

## 📚 목차

1. [개요](#개요)
2. [Transfer Learning 이론](#transfer-learning-이론)
3. [VGG19 사전훈련 모델](#vgg19-사전훈련-모델)
4. [투스테이지 방식 구현](#투스테이지-방식-구현)
5. [데이터 전처리 및 분할](#데이터-전처리-및-분할)
6. [특성 추출 과정](#특성-추출-과정)
7. [분류 모델 구축 및 학습](#분류-모델-구축-및-학습)
8. [성능 평가 및 결과](#성능-평가-및-결과)
9. [주요 학습 내용](#주요-학습-내용)
10. [결론 및 향후 과제](#결론-및-향후-과제)

---

## 📖 개요

이번 실습에서는 **Transfer Learning**을 활용하여 개-고양이 이진 분류 모델을 구현했습니다. ImageNet으로 사전훈련된 VGG19 모델을 특성 추출기로 활용하는 투스테이지 방식을 적용했습니다.

### 🎯 학습 목표
- **Transfer Learning** 개념 이해 및 실제 구현
- **사전훈련 모델** 활용 방법 학습
- **투스테이지 방식**과 **인라인 방식** 차이점 이해
- **특성 추출** 기법을 통한 효율적 학습
- **높은 성능** 달성 방법 습득

### 🛠️ 주요 기술 스택
- **프레임워크**: TensorFlow 2.15.1, Keras 2.15.0
- **사전훈련 모델**: VGG19 (ImageNet)
- **언어**: Python
- **라이브러리**: NumPy, Pickle, Matplotlib

### 🏆 주요 성과
- **테스트 정확도**: 97.80% (978/1000)
- **클래스별 정확도**: Cat 97.80%, Dog 97.80%
- **학습 시간**: 대폭 단축 (특성 추출 후 20 에포크)

---

## 🔄 Transfer Learning 이론

### 💡 Transfer Learning이란?
이미 대규모 데이터셋(ImageNet)으로 학습된 모델의 지식을 새로운 작업에 전이하는 기법입니다.

```python
# Transfer Learning의 핵심 아이디어
사전훈련_모델 = VGG19(weights="imagenet", include_top=False)
새로운_작업 = 개_고양이_분류
최종_모델 = 사전훈련_모델 + 새로운_분류층
```

### 🔍 두 가지 Transfer Learning 방식

| 방식 | 투스테이지 (Two-Stage) | 인라인 (Inline) |
|------|----------------------|-----------------|
| **구조** | 특성 추출 → 분류 학습 | 전체 모델 통합 학습 |
| **장점** | 매우 빠른 학습 속도 | 데이터 증강 직접 적용 |
| **단점** | 메모리 사용량 많음 | 상대적으로 느림 |
| **적용** | 소규모 데이터셋 | 중대규모 데이터셋 |

### ⚡ Transfer Learning의 장점
1. **학습 시간 단축**: CNN 부분 재사용으로 빠른 학습
2. **높은 성능**: 풍부한 사전 지식 활용
3. **적은 데이터**: 소규모 데이터셋으로도 효과적
4. **효율성**: 제한된 컴퓨팅 자원으로도 가능

---

## 🏗️ VGG19 사전훈련 모델

### 📊 VGG19 모델 특징
- **학습 데이터**: ImageNet (1,400만 장, 1,000개 클래스)
- **구조**: 16개 Conv 레이어 + 3개 FC 레이어 = 19개 레이어
- **입력 크기**: (180, 180, 3)
- **출력 크기**: (5, 5, 512) → 12,800차원 특성 벡터

### 🔧 모델 로드 및 설정

```python
# VGG19 사전훈련 모델 로드
conv_base = keras.applications.vgg19.VGG19(
    weights="imagenet",        # ImageNet 가중치 사용
    include_top=False,         # 최상위 분류층 제외
    input_shape=(180, 180, 3)  # 입력 이미지 크기
)

print(f"입력 크기: {conv_base.input_shape}")   # (None, 180, 180, 3)
print(f"출력 크기: {conv_base.output_shape}")  # (None, 5, 5, 512)
```

### 🎯 특성 추출 전략
- **레이어 동결**: VGG19의 모든 가중치를 고정
- **특성 벡터**: 마지막 합성곱 블록(block5_pool)에서 추출
- **차원**: 각 이미지당 5×5×512 = 12,800차원 특성

---

## 🔄 투스테이지 방식 구현

### 1️⃣ 1단계: 특성 추출

```python
def get_features_and_labels(dataset):
    """VGG19로 특성 추출"""
    all_features = []
    all_labels = []
    
    for images, labels in dataset:
        # ImageNet 전처리 적용
        preprocessed_images = keras.applications.vgg19.preprocess_input(images)
        
        # VGG19으로 특성 추출
        features = conv_base.predict(preprocessed_images, verbose=0)
        
        all_features.append(features)
        all_labels.append(labels)
    
    return np.concatenate(all_features), np.concatenate(all_labels)
```

### 2️⃣ 2단계: 분류 모델 학습

```python
def create_classification_model():
    """특성을 입력으로 받는 분류 모델"""
    inputs = keras.Input(shape=(5, 5, 512))  # VGG19 출력 크기
    
    # 데이터 증강
    x = data_augmentation(inputs)
    x = layers.Flatten()(x)                  # 12,800차원으로 변환
    x = layers.Dense(256, activation='relu')(x)
    x = layers.Dense(128, activation='relu')(x)
    x = layers.Dropout(0.5)(x)               # 과적합 방지
    outputs = layers.Dense(1, activation="sigmoid")(x)
    
    return keras.Model(inputs, outputs)
```

### 💾 특성 저장 및 재사용

```python
# 특성 추출 및 저장
train_features, train_labels = get_features_and_labels(train_ds)
validation_features, validation_labels = get_features_and_labels(validation_ds)
test_features, test_labels = get_features_and_labels(test_ds)

# pickle로 저장하여 재사용
with open("개고양이특성.bin", "wb") as file:
    pickle.dump([train_features, train_labels, 
                validation_features, validation_labels,
                test_features, test_labels], file)
```

---

## 📁 데이터 전처리 및 분할

### 🔢 데이터 분할 전략

| 데이터셋 | 범위 | 클래스별 샘플 수 | 총 샘플 수 | 용도 |
|----------|------|-----------------|-----------|------|
| **Train** | 0~999 | 1,000개 | 2,000개 | 모델 학습 |
| **Validation** | 1000~1499 | 500개 | 1,000개 | 검증 및 조기 종료 |
| **Test** | 1500~1999 | 500개 | 1,000개 | 최종 성능 평가 |

### 📂 디렉토리 구조

```
cats_and_dogs_small/
├── train/
│   ├── cat/    (1,000장: cat.0.jpg ~ cat.999.jpg)
│   └── dog/    (1,000장: dog.0.jpg ~ dog.999.jpg)
├── validation/
│   ├── cat/    (500장: cat.1000.jpg ~ cat.1499.jpg)
│   └── dog/    (500장: dog.1000.jpg ~ dog.1499.jpg)
└── test/
    ├── cat/    (500장: cat.1500.jpg ~ cat.1999.jpg)
    └── dog/    (500장: dog.1500.jpg ~ dog.1999.jpg)
```

### ⚙️ 데이터 로더 설정

```python
# 데이터셋 로더 생성
train_ds = keras.utils.image_dataset_from_directory(
    new_base_dir / "train",
    image_size=(180, 180),
    batch_size=16,
    label_mode='binary'  # 이진 분류 (0: cat, 1: dog)
)
```

---

## 🔍 특성 추출 과정

### 📊 추출된 특성 정보

| 항목 | 값 |
|------|-----|
| **입력 이미지** | (180, 180, 3) |
| **VGG19 출력** | (5, 5, 512) |
| **특성 차원** | 12,800차원 |
| **Train 특성** | (2000, 5, 5, 512) |
| **Validation 특성** | (1000, 5, 5, 512) |
| **Test 특성** | (1000, 5, 5, 512) |

### ⚡ 전처리 과정

```python
# ImageNet 전처리 (VGG19에 맞춤)
preprocessed_images = keras.applications.vgg19.preprocess_input(images)

# 정규화 방식: [0,255] → [-1,1] (ImageNet 표준)
# RGB 채널별 평균값 차감: [103.939, 116.779, 123.68]
```

### 💾 특성 저장 결과
- **파일명**: `개고양이특성.bin`
- **저장 방식**: Python pickle 형식
- **파일 크기**: 약 491MB
- **재사용**: 한 번 추출 후 반복 활용 가능

---

## 🧠 분류 모델 구축 및 학습

### 🏗️ 모델 아키텍처

```python
Model: "model_1"
_________________________________________________________________
Layer (type)                Output Shape              Param #   
=================================================================
input_4 (InputLayer)        [(None, 5, 5, 512)]       0         
sequential_1 (Sequential)   (None, 5, 5, 512)         0         # 데이터 증강
flatten_1 (Flatten)         (None, 12800)             0         
dense_3 (Dense)             (None, 256)               3,277,056 
dense_4 (Dense)             (None, 128)               32,896    
dropout_1 (Dropout)         (None, 128)               0         
dense_5 (Dense)             (None, 1)                 129       
=================================================================
Total params: 3,310,081 (12.63 MB)
```

### 🎨 데이터 증강 기법

```python
data_augmentation = keras.Sequential([
    layers.RandomFlip("horizontal"),     # 수평 뒤집기
    layers.RandomRotation(0.1),         # ±36도 회전 
    layers.RandomZoom(0.1),             # ±10% 확대/축소
])
```

### ⚙️ 학습 설정

| 설정 항목 | 값 |
|-----------|-----|
| **옵티마이저** | RMSprop |
| **손실 함수** | Binary Crossentropy |
| **평가 지표** | Accuracy |
| **에포크** | 20 |
| **배치 크기** | 32 |
| **콜백** | ModelCheckpoint (최적 모델 저장) |

### 📈 학습 과정 최적화

```python
# 최적 모델 자동 저장
callbacks = [
    keras.callbacks.ModelCheckpoint(
        filepath="특성추출.keras",
        save_best_only=True,        # 최고 성능 모델만 저장
        monitor="val_loss",         # 검증 손실 기준
        verbose=1
    )
]
```

---

## 📊 성능 평가 및 결과

### 🎯 최종 성능

| 지표 | 값 |
|------|-----|
| **테스트 정확도** | 97.80% (978/1000) |
| **고양이 정확도** | 97.80% |
| **개 정확도** | 97.80% |
| **틀린 예측** | 22개 |

### 📈 예측 결과 분석

```python
# 예측 결과 (처음 20개)
예측값: [0 0 0 1 0 1 1 0 0 1 0 1 0 1 1 1 0 0 1 0]
실제값: [0 0 0 1 0 1 1 0 0 1 0 0 0 1 1 1 0 0 1 0]
         # ↑ 여기서 1개 틀림

정확도: 19/20 = 95% (이 배치에서)
```

### 🔍 성능 비교

| 모델 | 정확도 | 학습 시간 | 파라미터 수 |
|------|--------|-----------|------------|
| **CNN (이전)** | 45.50% | 긴 시간 | 1,684,705개 |
| **Transfer Learning** | 97.80% | 짧은 시간 | 3,310,081개 |
| **성능 향상** | +52.30% | -대폭 단축 | +약 2배 |

### 💡 성능 향상 요인
1. **사전훈련된 특성**: ImageNet으로 학습된 풍부한 시각적 특성
2. **적절한 아키텍처**: VGG19의 검증된 CNN 구조
3. **효율적 학습**: 특성 추출 후 분류층만 학습
4. **데이터 증강**: 과적합 방지 및 일반화 성능 향상

---

## 📚 주요 학습 내용

### 1. Transfer Learning 핵심 개념

```python
# 기본 구조
사전훈련_모델 = VGG19(weights="imagenet", include_top=False)
사전훈련_모델.trainable = False  # 가중치 동결

새로운_모델 = Sequential([
    사전훈련_모델,
    새로운_분류층
])
```

### 2. 투스테이지 vs 인라인 방식

| 특징 | 투스테이지 | 인라인 |
|------|------------|---------|
| **특성 추출** | 미리 계산하여 저장 | 실시간 계산 |
| **메모리** | 많이 사용 | 적게 사용 |
| **속도** | 매우 빠름 | 상대적으로 느림 |
| **유연성** | 제한적 | 높음 |

### 3. 특성 추출 기법

```python
# VGG19 특성 추출 과정
원본_이미지 → VGG19_전처리 → VGG19_CNN → 특성벡터(5,5,512)
                ↓
특성벡터 → Flatten → 분류_신경망 → 예측결과
```

### 4. 모델 저장 및 재사용

```python
# 최적 모델 자동 저장
keras.callbacks.ModelCheckpoint(
    filepath="특성추출.keras",
    save_best_only=True,
    monitor="val_loss"
)

# 저장된 모델 로드
model = keras.models.load_model("특성추출.keras")
```

### 5. 성능 최적화 전략

1. **적절한 사전훈련 모델 선택**: VGG19, ResNet, EfficientNet 등
2. **효과적인 특성 추출**: 적절한 레이어에서 특성 추출
3. **최적화된 분류 네트워크**: Dropout, BatchNorm 등 활용
4. **데이터 증강**: 제한된 데이터의 다양성 증대

---

## 🎯 결론 및 향후 과제

### ✅ 완료한 학습 내용
1. **Transfer Learning 이론** 이해 및 실제 적용
2. **VGG19 사전훈련 모델** 활용법 습득  
3. **투스테이지 방식** 구현을 통한 효율적 학습
4. **특성 추출 기법**을 통한 고성능 달성
5. **체계적인 모델 관리** (저장/로드/평가)

### 🏆 주요 성과
- **97.80% 정확도** 달성으로 이전 CNN 대비 52.30% 향상
- **학습 시간 대폭 단축** (특성 추출 후 20에포크만으로 완료)
- **효율적인 자원 활용** (제한된 환경에서도 고성능 달성)
- **재사용 가능한 구조** (특성 한번 추출 후 반복 활용)

### 📈 향후 개선 방향

1. **인라인 방식 구현**
   - VGG19를 전체 모델에 포함하여 end-to-end 학습
   - Fine-tuning으로 VGG19 상위 레이어도 함께 학습
   - 원본 이미지에 직접 데이터 증강 적용

2. **다양한 사전훈련 모델 실험**
   - ResNet50/101: 잔차 연결로 깊은 네트워크
   - EfficientNet: 효율적인 스케일링
   - MobileNet: 경량화 모델
   - Vision Transformer: 최신 어텐션 기반 모델

3. **고급 최적화 기법**
   - Learning Rate Scheduling
   - Gradient Clipping
   - Mixed Precision Training
   - Knowledge Distillation

4. **모델 해석 및 분석**
   - Grad-CAM으로 모델 판단 근거 시각화
   - 특성 맵 분석으로 학습된 패턴 이해
   - 오분류 사례 분석 및 개선 방안 도출

### 🚀 실용적 활용 방안

1. **웹 애플리케이션 개발**
   - Flask/FastAPI로 REST API 서버 구축
   - 실시간 이미지 업로드 및 분류
   - 사용자 친화적 인터페이스 제공

2. **모바일 앱 연동**
   - TensorFlow Lite로 모델 경량화
   - 스마트폰에서 실시간 카메라 분류
   - 오프라인 환경에서도 동작

3. **엣지 디바이스 배포**
   - Raspberry Pi, Jetson Nano 등
   - IoT 환경에서의 실시간 처리
   - 저전력 환경 최적화

### 💡 핵심 인사이트

1. **Transfer Learning의 위력**: 사전훈련된 모델의 지식 전이로 획기적 성능 향상
2. **효율성의 중요성**: 투스테이지 방식으로 학습 시간 대폭 단축
3. **적절한 모델 선택**: 문제에 맞는 사전훈련 모델 선택의 중요성
4. **체계적 접근**: 데이터 분할, 특성 추출, 모델 학습의 단계별 접근

### 📝 마무리

이번 Transfer Learning 실습을 통해 사전훈련된 모델의 강력함을 직접 경험했습니다. 단순 CNN으로는 45.50%에 머물던 정확도가 VGG19 Transfer Learning으로 97.80%까지 향상된 것은 매우 인상적인 결과입니다. 

특히 투스테이지 방식을 통해 학습 시간을 대폭 단축하면서도 높은 성능을 달성할 수 있음을 확인했습니다. 앞으로는 인라인 방식, Fine-tuning, 그리고 다양한 최신 사전훈련 모델들을 활용하여 더욱 발전된 모델을 구축해나가겠습니다.

---

### 📊 부록: 실험 결과 요약

| 항목 | 값 |
|------|-----|
| **사전훈련 모델** | VGG19 (ImageNet) |
| **방식** | 투스테이지 Transfer Learning |
| **데이터셋** | Cats and Dogs (4,000장) |
| **최종 정확도** | 97.80% |
| **학습 시간** | 20 에포크 |
| **모델 크기** | 12.63 MB |
| **성능 향상** | +52.30% (vs 단순 CNN) |