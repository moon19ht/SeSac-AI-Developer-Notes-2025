# 🧠 Deep Learning 정리 

##### 🗓️ 2025.07.22
##### 📝 Writer : Moon19ht

---

## 📚 목차

1. [개요](#개요)
2. [프로젝트 1: 개와 고양이 이진 분류](#프로젝트-1-개와-고양이-이진-분류)
3. [프로젝트 2: 꽃 이미지 다중 분류](#프로젝트-2-꽃-이미지-다중-분류)
4. [CNN 아키텍처 비교](#cnn-아키텍처-비교)
5. [데이터 증강 기법](#데이터-증강-기법)
6. [주요 학습 내용](#주요-학습-내용)
7. [결론 및 향후 과제](#결론-및-향후-과제)

---

## 📖 개요

이번 실습에서는 **Convolutional Neural Network(CNN)**을 활용한 이미지 분류 모델을 두 가지 프로젝트로 구현했습니다.

### 🎯 학습 목표
- **CNN 기본 구조** 이해 및 구현
- **이진 분류**와 **다중 클래스 분류** 비교
- **데이터 증강(Data Augmentation)** 기법 적용
- **TensorFlow/Keras** 프레임워크 활용
- **모델 성능 최적화** 방법 학습

### 🛠️ 주요 기술 스택
- **프레임워크**: TensorFlow 2.19.0, Keras 3.10.0
- **언어**: Python 3.11.13
- **라이브러리**: NumPy, Matplotlib, PIL, OS

---

## 🐱🐶 프로젝트 1: 개와 고양이 이진 분류

### 📊 프로젝트 개요
- **목표**: 개와 고양이 이미지를 구분하는 이진 분류 모델
- **데이터**: 25,000장 → 4,000장 사용 (학습용 2,000장, 검증용 1,000장, 테스트용 1,000장)
- **이미지 크기**: 180×180×3 (RGB)
- **배치 크기**: 16

### 🏗️ 모델 아키텍처

```python
# 입력: (180, 180, 3)
Sequential([
    # 데이터 증강 + 정규화
    Rescaling(1./255),
    RandomFlip("horizontal"),
    RandomRotation(0.1),
    RandomZoom(0.1),
    
    # CNN 블록들
    Conv2D(32, (3,3), activation='relu'),  # 첫 번째 특징 추출
    MaxPooling2D((2,2)),
    
    Conv2D(64, (3,3), activation='relu'),  # 중간 수준 특징
    MaxPooling2D((2,2)),
    
    Conv2D(32, (3,3), activation='relu'),  # 고수준 특징
    MaxPooling2D((2,2)),
    
    # 분류 레이어들
    Flatten(),
    Dropout(0.5),                          # 과적합 방지
    Dense(128, activation='relu'),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')         # 이진 분류 출력
])
```

### ⚙️ 모델 설정
- **옵티마이저**: Adam
- **손실 함수**: Binary Crossentropy
- **평가 지표**: Accuracy
- **에포크**: 50
- **총 파라미터**: 1,684,705개

### 📈 학습 결과
- **최종 학습 정확도**: 51.13%
- **최종 검증 정확도**: 45.50%
- **모델 크기**: 19.34 MB

### 💡 특징
- **점진적 필터 증가**: 32 → 64 → 32 (파라미터 수 조절)
- **Sigmoid 활성화**: 0~1 확률 출력으로 이진 분류
- **Dropout 0.5**: 과적합 방지를 위한 정규화

---

## 🌸 프로젝트 2: 꽃 이미지 다중 분류

### 📊 프로젝트 개요
- **목표**: 5가지 꽃 종류 분류 (daisy, dandelion, rose, sunflower, tulip)
- **데이터**: 총 2,746장 → Train(50%), Validation(25%), Test(25%) 분할
- **이미지 크기**: 180×180×3 (RGB)
- **배치 크기**: 16

### 🔄 데이터 전처리 과정

```python
# 1단계: 이미지 리네이밍
def rename_images_in_class_folder(src_class_dir, class_name, dest_dir):
    # 'class_name.index.ext' 형식으로 리네이밍
    
# 2단계: 데이터 분할
def ImageCopy(renamed_dataset_dir, base_dir):
    # Train:Validation:Test = 50:25:25 비율로 분할
```

### 📁 데이터 분할 결과

| 클래스 | Train | Validation | Test | 총계 |
|---------|--------|------------|------|------|
| **Daisy** | 250개 | 125개 | 126개 | 501개 |
| **Dandelion** | 323개 | 161개 | 162개 | 646개 |
| **Rose** | 248개 | 124개 | 125개 | 497개 |
| **Sunflower** | 247개 | 123개 | 125개 | 495개 |
| **Tulip** | 303개 | 151개 | 153개 | 607개 |

### 🏗️ 모델 아키텍처

```python
# 입력: (180, 180, 3)
Sequential([
    # 전처리 + 데이터 증강
    Rescaling(1./255),
    RandomFlip("horizontal"),
    RandomRotation(0.1),
    RandomZoom(0.1),
    
    # CNN 블록들
    Conv2D(32, (3,3), activation='relu'),
    MaxPooling2D((2,2)),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D((2,2)),
    Conv2D(32, (3,3), activation='relu'),
    MaxPooling2D((2,2)),
    
    # 분류 레이어들
    Flatten(),
    Dropout(0.5),
    Dense(128, activation='relu'),
    Dense(64, activation='relu'),
    Dense(5, activation='softmax')         # 5클래스 분류 출력
])
```

### ⚙️ 모델 설정
- **옵티마이저**: Adam
- **손실 함수**: Sparse Categorical Crossentropy
- **평가 지표**: Accuracy
- **에포크**: 30

### 💡 특징
- **Softmax 활성화**: 5개 클래스에 대한 확률 분포 출력
- **체계적 데이터 관리**: 리네이밍 → 분할 → 구조화
- **다중 클래스 분류**: 정수 라벨 사용

---

## 🔍 CNN 아키텍처 비교

### 공통점
| 요소 | 설명 |
|------|------|
| **기본 구조** | Conv2D → MaxPooling2D → Conv2D → MaxPooling2D → Conv2D → MaxPooling2D |
| **필터 패턴** | 32 → 64 → 32 (동일한 점진적 패턴) |
| **활성화 함수** | ReLU (은닉층), Dropout(0.5) |
| **완전연결층** | Dense(128) → Dense(64) |
| **이미지 크기** | 180×180×3 |
| **데이터 증강** | RandomFlip, RandomRotation, RandomZoom |

### 차이점
| 항목 | 개와 고양이 분류 | 꽃 이미지 분류 |
|------|------------------|----------------|
| **문제 유형** | 이진 분류 | 다중 클래스 분류 |
| **출력층** | Dense(1, sigmoid) | Dense(5, softmax) |
| **손실 함수** | Binary Crossentropy | Sparse Categorical Crossentropy |
| **클래스 수** | 2개 (cats, dogs) | 5개 (꽃 종류) |
| **라벨 형태** | 0 또는 1 | 0, 1, 2, 3, 4 |

---

## 🎨 데이터 증강 기법

### 적용된 증강 기법들

```python
data_augmentation = keras.Sequential([
    layers.Rescaling(1./255),              # 픽셀 정규화 (0~255 → 0~1)
    layers.RandomFlip("horizontal"),        # 수평 뒤집기 (50% 확률)
    layers.RandomRotation(0.1),            # ±36도 회전
    layers.RandomZoom(0.1),                # ±10% 확대/축소
])
```

### 📊 증강 기법의 효과

| 기법 | 목적 | 효과 |
|------|------|------|
| **RandomFlip** | 좌우 대칭성 학습 | 방향에 무관한 특징 추출 |
| **RandomRotation** | 회전 불변성 | 다양한 각도의 객체 인식 |
| **RandomZoom** | 크기 적응성 | 다양한 크기의 객체 대응 |
| **Rescaling** | 수치 안정성 | 학습 수렴 속도 향상 |

### 💡 데이터 증강의 장점
- **🛡️ 과적합 방지**: 제한된 데이터로 다양한 변형 생성
- **📈 일반화 성능**: 실제 환경의 다양한 조건 대응
- **⚡ 실시간 처리**: GPU에서 빠른 변형 생성
- **💾 메모리 효율**: 원본 데이터 크기 유지

---

## 📚 주요 학습 내용

### 1. CNN 기본 구조 이해
```python
# 합성곱층: 특징 추출
Conv2D(filters, kernel_size, activation='relu')

# 풀링층: 다운샘플링
MaxPooling2D(pool_size)

# 완전연결층: 분류 결정
Dense(units, activation)
```

### 2. 이진 분류 vs 다중 분류

| 항목 | 이진 분류 | 다중 분류 |
|------|-----------|-----------|
| **출력 뉴런** | 1개 | 클래스 수만큼 |
| **활성화 함수** | Sigmoid | Softmax |
| **손실 함수** | Binary Crossentropy | Categorical/Sparse Categorical Crossentropy |
| **출력 해석** | 확률 (0~1) | 확률 분포 (합=1) |

### 3. 모델 최적화 기법
- **Dropout**: 과적합 방지를 위한 정규화
- **Adam Optimizer**: 적응적 학습률 조정
- **Data Augmentation**: 데이터 다양성 증대
- **Batch Processing**: 메모리 효율적 학습

### 4. TensorFlow/Keras 활용
```python
# 데이터셋 로딩
train_ds = keras.utils.image_dataset_from_directory(
    directory, validation_split=0.2, subset="training"
)

# 모델 컴파일
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 모델 학습
history = model.fit(train_ds, validation_data=val_ds, epochs=50)

# 모델 저장
model.save('model.keras')
```

---

## 🎯 결론 및 향후 과제

### ✅ 완료한 학습 내용
1. **CNN 기본 구조** 이해 및 구현
2. **이진 분류와 다중 분류** 모델 설계
3. **데이터 증강 기법** 적용 및 효과 확인
4. **체계적인 데이터 전처리** 방법 학습
5. **모델 학습 및 저장** 프로세스 마스터

### 📈 성능 개선 방향
1. **하이퍼파라미터 튜닝**
   - 학습률, 배치 크기, 에포크 수 최적화
   - 다양한 옵티마이저 실험

2. **모델 아키텍처 개선**
   - 더 깊은 네트워크 구조
   - ResNet, EfficientNet 등 사전 훈련 모델 활용
   - 전이학습(Transfer Learning) 적용

3. **데이터 품질 향상**
   - 더 많은 데이터 수집
   - 데이터 불균형 해결
   - 고급 데이터 증강 기법 적용

### 🚀 다음 단계
1. **모델 평가**
   - Test 데이터셋으로 최종 성능 평가
   - Confusion Matrix 분석
   - 잘못 분류된 사례 분석

2. **실용적 활용**
   - 웹 애플리케이션 개발
   - REST API 구축
   - 실시간 이미지 분류 시스템

3. **고급 기법 학습**
   - Transfer Learning
   - Object Detection
   - Semantic Segmentation

### 💡 핵심 인사이트
- **데이터 전처리의 중요성**: 체계적인 데이터 관리가 모델 성능에 큰 영향
- **데이터 증강의 효과**: 제한된 데이터로도 과적합 방지 가능
- **모델 구조의 균형**: 복잡도와 성능 사이의 적절한 균형점 찾기
- **실험적 접근**: 다양한 하이퍼파라미터와 구조 실험의 필요성

---

### 📝 마무리
이번 실습을 통해 CNN의 기본 원리부터 실제 구현까지 전체 파이프라인을 경험했습니다. 특히 이진 분류와 다중 분류 문제를 모두 다루면서 각각의 특징과 차이점을 명확히 이해할 수 있었습니다. 앞으로는 더 복잡한 모델과 고급 기법들을 활용하여 실제 문제 해결 능력을 향상시켜 나가겠습니다.

