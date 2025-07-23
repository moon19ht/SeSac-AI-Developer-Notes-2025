# 🧠 Deep Learning 정리

##### 🗓️ 2025.07.22
##### 📝 Writer : Moon19ht

---

## 📚 목차

1. [🐱🐶 프로젝트 개요](#-프로젝트-개요)
2. [📚 라이브러리 및 환경 설정](#-라이브러리-및-환경-설정)
3. [📁 데이터 준비 및 전처리](#-데이터-준비-및-전처리)
4. [🔄 데이터 증강(Data Augmentation)](#-데이터-증강data-augmentation)
5. [🧠 CNN 모델 아키텍처](#-cnn-모델-아키텍처)
6. [⚙️ 모델 컴파일 및 학습](#️-모델-컴파일-및-학습)
7. [📊 학습 결과 분석](#-학습-결과-분석)
8. [💾 모델 저장 및 활용](#-모델-저장-및-활용)
9. [🔍 핵심 개념 정리](#-핵심-개념-정리)
10. [💡 개선 방안](#-개선-방안)

---

## 🐱🐶 프로젝트 개요

### 🎯 목표
- **Convolutional Neural Network(CNN)**을 사용한 개와 고양이 이미지 **이진 분류**
- **데이터 증강** 기법을 통한 과대적합 방지
- **체계적인 딥러닝 프로젝트** 수행 과정 학습

### 📊 데이터셋 정보
- **데이터 소스**: Kaggle cats_and_dogs 데이터셋
- **총 데이터**: 25,000장 → **4,000장 사용** (실습 최적화)
- **이미지 크기**: **180×180×3** (RGB)
- **클래스**: 2개 (고양이, 개)

### 📁 데이터 분할 전략
```
📁 데이터 구조
├── 📚 train/          (학습용: 2,000장)
│   ├── 🐱 cats/       (1,000장)
│   └── 🐶 dogs/       (1,000장)
├── 🧪 test/           (테스트용: 1,000장)
│   ├── 🐱 cats/       (500장)
│   └── 🐶 dogs/       (500장)
└── ✅ validation/     (검증용: 1,000장)
    ├── 🐱 cats/       (500장)
    └── 🐶 dogs/       (500장)
```

---

## 📚 라이브러리 및 환경 설정

### 🔧 주요 라이브러리
```python
# 딥러닝 프레임워크
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import models, layers

# 데이터 처리 및 시각화
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 파일 시스템
import os
import shutil
```

### ⚙️ 환경 설정
```python
# 재현 가능한 결과를 위한 시드 설정
RANDOM_SEED = 42
random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)
tf.random.set_seed(RANDOM_SEED)

# GPU 메모리 증가 설정
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    for gpu in gpus:
        tf.config.experimental.set_memory_growth(gpu, True)
```

### 📋 프로젝트 설정 클래스
```python
class Config:
    # 데이터셋 설정
    ORIGINAL_DATASET_DIR = "../../data/cats_and_dogs/train"
    BASE_DIR = "../../data/cats_and_dogs_small"
    
    # 데이터 분할 설정
    TRAIN_SAMPLES_PER_CLASS = 1000
    TEST_SAMPLES_PER_CLASS = 500
    VALIDATION_SAMPLES_PER_CLASS = 500
    
    # 이미지 및 학습 설정
    IMAGE_SIZE = (180, 180)
    BATCH_SIZE = 16
    CHANNELS = 3
    EPOCHS = 50
    VALIDATION_SPLIT = 0.2
    
    # 클래스 정보
    CLASS_NAMES = ['cats', 'dogs']
```

---

## 📁 데이터 준비 및 전처리

### 🔄 데이터 준비 과정
1. **📂 디렉토리 구조 생성**: 학습/테스트/검증 폴더 체계적 구성
2. **📋 파일 복사**: 원본에서 각 디렉토리로 이미지 분할 복사
3. **✅ 무결성 검증**: 복사된 파일 수 확인 및 데이터 검증

### 🛠️ 주요 함수들

#### 원본 데이터셋 검증
```python
def validate_original_dataset():
    """원본 데이터셋의 존재와 구조를 검증"""
    # 디렉토리 존재 확인
    # 파일 개수 및 형식 검증
    # 기본적인 jpg 파일 비율 확인
    return is_valid, total_count, message
```

#### 디렉토리 구조 생성
```python
def create_directory_structure():
    """데이터셋을 위한 디렉토리 구조 생성"""
    # 기존 디렉토리 안전 삭제
    # 필요한 모든 디렉토리 생성
    # 권한 및 접근성 확인
    return success
```

#### 클래스별 파일 복사
```python
def copy_class_files(class_name, start_idx, end_idx, dest_dir, dataset_type):
    """특정 클래스의 파일들을 지정된 범위로 복사"""
    # 파일명 생성 및 존재 확인
    # 진행률 표시와 함께 복사 수행
    # 성공/실패 통계 반환
    return success_count, failed_count, failed_files
```

---

## 🔄 데이터 증강(Data Augmentation)

### 🎯 데이터 증강의 목적
- **📈 데이터 다양성 증대**: 제한된 데이터로 더 많은 변형 생성
- **🛡️ 과대적합 방지**: 모델이 특정 패턴에 과도하게 의존하는 것 방지
- **🎨 일반화 성능 향상**: 다양한 조건의 이미지에 대한 견고성 증가
- **⚡ 실시간 처리**: 학습 중 동적으로 변형 적용

### 🛠️ 적용된 증강 기법

| 🎨 기법 | 📝 설명 | ⚙️ 설정값 | 🎯 효과 |
|---|---|---|---|
| **📏 Rescaling** | 픽셀 정규화 | `1/255` (0~1 범위) | 수치 안정성 |
| **🔄 RandomFlip** | 수평 뒤집기 | `horizontal` | 좌우 대칭성 학습 |
| **🌀 RandomRotation** | 무작위 회전 | `±36도 (0.1×2π)` | 회전 불변성 확보 |
| **🔍 RandomZoom** | 확대/축소 | `±10%` | 크기 변화 적응성 |

### 💻 구현 코드
```python
def create_data_augmentation():
    """데이터 증강을 위한 Sequential 모델 생성"""
    augmentation_layers = [
        # 픽셀 값 정규화 (0~255 → 0~1)
        layers.Rescaling(1./255, input_shape=(*Config.IMAGE_SIZE, Config.CHANNELS)),
        
        # 수평 뒤집기 (50% 확률)
        layers.RandomFlip("horizontal"),
        
        # 무작위 회전 (±36도)
        layers.RandomRotation(0.1),
        
        # 무작위 확대/축소 (±10%)
        layers.RandomZoom(0.1),
    ]
    
    return keras.Sequential(augmentation_layers, name="data_augmentation_pipeline")
```

---

## 🧠 CNN 모델 아키텍처

### 🏗️ 모델 구조 개요
```
📥 입력 (180×180×3)
    ↓
📏 데이터 증강 + 정규화
    ↓
🔄 Conv2D(32, 3×3) + ReLU → MaxPool(2×2)  [89×89×32]
    ↓
🔄 Conv2D(64, 3×3) + ReLU → MaxPool(2×2)  [43×43×64]  
    ↓
🔄 Conv2D(32, 3×3) + ReLU → MaxPool(2×2)  [20×20×32]
    ↓
📦 Flatten                               [12,800]
    ↓
🚫 Dropout(0.5)                         [12,800]
    ↓
🧠 Dense(128) + ReLU                     [128]
    ↓
🧠 Dense(64) + ReLU                      [64]
    ↓
📤 Dense(1) + Sigmoid                    [1]
```

### 🎯 설계 원칙

| 🏷️ 구성요소 | 🎯 목적 | ⚙️ 설정 | 📊 특징 |
|---|---|---|---|
| **🔄 Conv2D 블록** | 특징 추출 | 3×3 필터, ReLU | 점진적 특징 학습 |
| **📉 MaxPooling** | 다운샘플링 | 2×2 윈도우 | 차원 축소, 위치불변성 |
| **🚫 Dropout** | 과적합 방지 | 50% 뉴런 차단 | 일반화 성능 향상 |
| **🧠 Dense** | 분류 결정 | ReLU → Sigmoid | 최종 확률 출력 |

### 💻 모델 구현
```python
def create_cnn_model():
    """개와 고양이 이진 분류를 위한 CNN 모델 생성"""
    model = models.Sequential(name="CatsDogs_CNN")
    
    # 데이터 증강 레이어
    model.add(data_augmentation)
    
    # 합성곱 블록 1: 기본 특징 추출
    model.add(layers.Conv2D(32, (3, 3), activation='relu', name='conv2d_block1'))
    model.add(layers.MaxPooling2D((2, 2), name='maxpool_block1'))
    
    # 합성곱 블록 2: 중간 수준 특징 추출
    model.add(layers.Conv2D(64, (3, 3), activation='relu', name='conv2d_block2'))
    model.add(layers.MaxPooling2D((2, 2), name='maxpool_block2'))
    
    # 합성곱 블록 3: 고수준 특징 추출
    model.add(layers.Conv2D(32, (3, 3), activation='relu', name='conv2d_block3'))
    model.add(layers.MaxPooling2D((2, 2), name='maxpool_block3'))
    
    # Flatten 및 Dense 레이어
    model.add(layers.Flatten(name='flatten'))
    model.add(layers.Dropout(0.5, name='dropout_regularization'))
    model.add(layers.Dense(128, activation='relu', name='dense_features'))
    model.add(layers.Dense(64, activation='relu', name='dense_abstract'))
    model.add(layers.Dense(1, activation='sigmoid', name='binary_output'))
    
    return model
```

### 📊 모델 정보
- **총 파라미터 수**: 1,684,705개
- **예상 메모리 사용량**: 6.43 MB
- **총 레이어 수**: 12개

---

## ⚙️ 모델 컴파일 및 학습

### 🔧 컴파일 설정
```python
model.compile(
    optimizer='adam',           # 적응적 학습률 옵티마이저
    loss='binary_crossentropy', # 이진 분류 손실함수
    metrics=['accuracy']        # 평가 지표
)
```

### 📂 데이터셋 로딩
- **Korean path 문제 해결**: 커스텀 데이터셋 생성 함수 구현
- **배치 처리**: 16개씩 배치로 처리
- **데이터 검증**: 형태, 타입, 값 범위 확인

### 🏋️ 학습 과정
```python
history = model.fit(
    train_ds,              # 학습 데이터셋
    validation_data=val_ds, # 검증 데이터셋
    epochs=50,             # 50 에포크
    verbose=1              # 학습 과정 출력
)
```

---

## 📊 학습 결과 분석

### 📈 최종 성능 지표
- **학습 정확도**: 51.13%
- **검증 정확도**: 45.50%
- **학습 손실**: 0.6930
- **검증 손실**: 0.6955

### 🔍 결과 분석
#### ⚠️ 문제점
1. **낮은 정확도**: 약 50% 수준으로 랜덤 추측과 유사
2. **학습 정체**: 에포크가 진행되어도 성능 개선 없음
3. **그래디언트 소실**: 손실이 약 0.693에서 고정 (ln(2) ≈ 0.693)

#### 🎯 원인 분석
1. **데이터 양 부족**: 클래스당 1000장으로 CNN 학습에 부족
2. **모델 복잡도**: 데이터 대비 과도한 파라미터 수
3. **학습률 문제**: 적절하지 않은 학습률 설정
4. **데이터 품질**: 데이터 전처리 과정에서의 문제

### 📊 시각화 코드
```python
plt.figure(figsize=(12, 4))

# 정확도 그래프
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy')

# 손실 그래프
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
```

---

## 💾 모델 저장 및 활용

### 💾 모델 저장
```python
model_path = "../../data/models/catanddog.keras"
model.save(model_path)
```

### 📋 저장된 모델 정보
- **파일 크기**: 19.34 MB
- **형식**: Keras 네이티브 형식 (.keras)
- **포함 내용**: 모델 구조 + 가중치 + 옵티마이저 상태

### 🔄 모델 로딩 및 사용
```python
# 모델 로딩
loaded_model = keras.models.load_model(model_path)

# 예측 수행
predictions = loaded_model.predict(test_images)
predicted_classes = (predictions > 0.5).astype(int)
```

---

## 🔍 핵심 개념 정리

### 1. 🧠 Convolutional Neural Network (CNN)
- **합성곱층(Conv2D)**: 특징 추출을 위한 필터 적용
- **풀링층(MaxPooling)**: 차원 축소 및 위치 불변성 확보
- **완전연결층(Dense)**: 최종 분류 결정

### 2. 🔄 데이터 증강(Data Augmentation)
- **목적**: 데이터 다양성 증대, 과대적합 방지
- **실시간 적용**: 학습 중 동적으로 변형 생성
- **성능 향상**: 일반화 능력 개선

### 3. 🚫 정규화 기법
- **Dropout**: 뉴런 임의 비활성화로 과대적합 방지
- **Batch Normalization**: 내부 공변량 변화 감소
- **L1/L2 정규화**: 가중치 크기 제한

### 4. 📊 이진 분류
- **Sigmoid 활성화**: 0~1 범위의 확률 출력
- **Binary Crossentropy**: 이진 분류에 적합한 손실함수
- **임계값**: 0.5를 기준으로 클래스 결정

---

## 💡 개선 방안

### 🔧 모델 아키텍처 개선
1. **전이학습(Transfer Learning)**
   ```python
   base_model = tf.keras.applications.VGG16(
       weights='imagenet',
       include_top=False,
       input_shape=(180, 180, 3)
   )
   ```

2. **더 깊은 네트워크**
   - ResNet, EfficientNet 등 사용
   - Skip connection 및 attention mechanism 적용

3. **배치 정규화 추가**
   ```python
   model.add(layers.Conv2D(32, (3, 3), activation='relu'))
   model.add(layers.BatchNormalization())
   model.add(layers.MaxPooling2D((2, 2)))
   ```

### 📊 데이터 개선
1. **데이터 양 증가**
   - 전체 25,000장 활용
   - 외부 데이터셋 추가 수집

2. **고급 데이터 증강**
   ```python
   # 더 다양한 증강 기법
   layers.RandomContrast(0.2),
   layers.RandomBrightness(0.2),
   layers.RandomRotation(0.2),
   layers.RandomTranslation(0.1, 0.1),
   ```

3. **데이터 품질 향상**
   - 이미지 해상도 증가
   - 불량 이미지 제거
   - 클래스 균형 조정

### ⚙️ 하이퍼파라미터 튜닝
1. **학습률 스케줄링**
   ```python
   lr_scheduler = tf.keras.callbacks.ReduceLROnPlateau(
       monitor='val_loss',
       factor=0.2,
       patience=5,
       min_lr=0.0001
   )
   ```

2. **Early Stopping**
   ```python
   early_stopping = tf.keras.callbacks.EarlyStopping(
       monitor='val_loss',
       patience=10,
       restore_best_weights=True
   )
   ```

3. **옵티마이저 변경**
   - AdamW, RMSprop 실험
   - 학습률 범위 조정

### 🎯 평가 및 분석 개선
1. **다양한 평가 지표**
   - Precision, Recall, F1-score
   - Confusion Matrix
   - ROC-AUC

2. **모델 해석성**
   - Grad-CAM 시각화
   - Feature Map 분석
   - 오분류 사례 분석

---

## 📚 참고 자료

### 📖 이론적 배경
- **CNN 기초**: "Deep Learning" by Ian Goodfellow
- **전이학습**: "Transfer Learning for Computer Vision"
- **데이터 증강**: "Data Augmentation Techniques"

### 🔗 유용한 링크
- [TensorFlow 공식 문서](https://www.tensorflow.org/)
- [Keras 가이드](https://keras.io/guides/)
- [CNN 시각화 도구](https://poloclub.github.io/cnn-explainer/)

### 💻 실습 환경
- **Python**: 3.11.13
- **TensorFlow**: 2.19.0
- **Keras**: 3.10.0
- **NumPy**: 2.1.3

---

## 🎯 학습 목표 달성 평가

### ✅ 달성한 목표
- CNN 모델 구조 설계 및 구현
- 데이터 전처리 파이프라인 구축
- 데이터 증강 기법 적용
- 모델 학습 및 저장 과정 완료
- 시각화를 통한 결과 분석

### 🔄 추가 학습이 필요한 영역
- 전이학습 활용법
- 고급 정규화 기법
- 하이퍼파라미터 최적화
- 모델 성능 평가 및 해석

### 🚀 다음 단계
1. **전이학습 프로젝트**: 사전 훈련된 모델 활용
2. **객체 탐지**: YOLO, R-CNN 등 학습
3. **생성 모델**: GAN, VAE 실습
4. **실제 배포**: Flask/Django를 통한 웹 서비스 구현

---

*"작은 성공도 성공이다. 오늘의 실습을 통해 딥러닝의 전체 과정을 경험했다는 것이 가장 큰 성과!"* 🎉