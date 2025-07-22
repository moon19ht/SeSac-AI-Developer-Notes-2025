# 🧠 Deep Learning 정리

##### 🗓️ 2025.07.21
##### 📝 Writer : Moon19ht

---

## 📚 목차

1. [CNN(합성곱 신경망) 기초](#1-cnn합성곱-신경망-기초)
2. [Fashion-MNIST 이미지 분류](#2-fashion-mnist-이미지-분류)
3. [일반 신경망 vs CNN 성능 비교](#3-일반-신경망-vs-cnn-성능-비교)
4. [실전 프로젝트: 꽃 분류 시스템](#4-실전-프로젝트-꽃-분류-시스템)
5. [딥러닝 모델 최적화 기법](#5-딥러닝-모델-최적화-기법)
6. [실무 적용 가이드](#6-실무-적용-가이드)

---

## 1. CNN(합성곱 신경망) 기초

### 1.1 CNN의 핵심 개념

**CNN(Convolutional Neural Network)**은 이미지 처리에 특화된 딥러닝 모델입니다.

#### 주요 구성 요소

1. **합성곱층(Conv2D)**
   - 이미지의 특징(feature) 추출
   - 필터(커널)을 사용하여 공간적 패턴 감지
   - 가중치 공유로 매개변수 수 감소

2. **풀링층(Pooling)**
   - 특징맵 크기 축소 (다운샘플링)
   - 과대적합 방지 및 계산량 감소
   - MaxPooling, AveragePooling 등

3. **완전연결층(Dense)**
   - 추출된 특징으로 최종 분류 수행
   - 일반적인 신경망과 동일한 구조

#### CNN의 장점

- **공간적 정보 보존**: 이미지의 2D 구조 유지
- **매개변수 효율성**: 가중치 공유로 적은 매개변수 사용
- **평행이동 불변성**: 객체 위치에 관계없이 인식 가능
- **계층적 특징 학습**: 저수준 → 고수준 특징 순차적 학습

### 1.2 기본 CNN 아키텍처

```python
# 기본 CNN 모델 구조 예시
model = models.Sequential([
    layers.Rescaling(1./255, input_shape=(28, 28, 1)),  # 정규화
    layers.Conv2D(32, (3, 3), activation='relu'),       # 특징 추출
    layers.Conv2D(64, (3, 3), activation='relu'),       # 특징 추가 추출
    layers.MaxPooling2D((2, 2)),                        # 다운샘플링
    layers.Flatten(),                                    # 1차원 변환
    layers.Dense(128, activation='relu'),                # 분류기
    layers.Dense(64, activation='relu'),                 # 분류기
    layers.Dense(10, activation='softmax')               # 출력층
])
```

---

## 2. Fashion-MNIST 이미지 분류

### 2.1 Fashion-MNIST 데이터셋

**Fashion-MNIST**는 Zalando의 의류 이미지 데이터셋으로, 기존 MNIST의 대안입니다.

#### 데이터셋 특징

- **이미지 크기**: 28×28 픽셀 (그레이스케일)
- **클래스 수**: 10개
- **훈련 데이터**: 60,000개
- **테스트 데이터**: 10,000개

#### 클래스 정보

| 레이블 | 클래스명 | 한국어 |
|--------|----------|---------|
| 0 | T-shirt/top | 티셔츠/탑 |
| 1 | Trouser | 바지 |
| 2 | Pullover | 풀오버 |
| 3 | Dress | 드레스 |
| 4 | Coat | 코트 |
| 5 | Sandal | 샌들 |
| 6 | Shirt | 셔츠 |
| 7 | Sneaker | 스니커즈 |
| 8 | Bag | 가방 |
| 9 | Ankle boot | 앵클부츠 |

### 2.2 모델 성능 분석

#### 실습 결과

- **최종 훈련 정확도**: 98.51%
- **최종 테스트 정확도**: 90.03%
- **일반화 갭**: 5.68%p

#### 성능 개선 방안

1. **정규화 강화**: Dropout, BatchNormalization 추가
2. **데이터 증강**: 회전, 이동, 확대/축소
3. **조기 종료**: EarlyStopping 콜백 활용
4. **학습률 스케줄링**: 적응적 학습률 조정

---

## 3. 일반 신경망 vs CNN 성능 비교

### 3.1 CIFAR-10 실험 설계

**CIFAR-10** 컬러 이미지 데이터셋을 사용한 비교 실험

#### 데이터셋 특징

- **이미지 크기**: 32×32×3 (RGB)
- **클래스 수**: 10개
- **훈련 데이터**: 50,000개
- **테스트 데이터**: 10,000개

#### 클래스 정보

0. airplane (비행기), 1. automobile (자동차), 2. bird (새)
3. cat (고양이), 4. deer (사슴), 5. dog (개)
6. frog (개구리), 7. horse (말), 8. ship (배), 9. truck (트럭)

### 3.2 모델 비교 결과

#### 성능 지표 비교

| 항목 | Dense 모델 | CNN 모델 | 개선도 |
|------|------------|----------|--------|
| **매개변수 수** | 411,146개 | 1,634,058개 | +297% |
| **훈련 시간** | 0.71분 | 8.02분 | +7.3분 |
| **훈련 정확도** | 48.83% | 88.62% | +39.79%p |
| **테스트 정확도** | 46.78% | 62.37% | +15.59%p |
| **일반화 갭** | 2.05%p | 26.25%p | +24.20%p |

#### 주요 발견사항

1. **CNN의 우수한 특징 추출**: 컬러 이미지에서 CNN이 현저히 높은 성능
2. **매개변수 효율성**: Dense 모델이 더 적은 매개변수로 빠른 학습
3. **과대적합 경향**: CNN에서 더 심각한 과대적합 발생 (정규화 필요)
4. **학습 곡선**: CNN이 더 빠르게 수렴하는 경향

### 3.3 모델 선택 가이드

#### 일반 신경망 사용 권장 상황

- 테이블 형태의 구조화된 데이터
- 작은 이미지나 단순한 패턴
- 빠른 프로토타이핑이 필요한 경우
- 모델 해석가능성이 중요한 경우

#### CNN 사용 권장 상황

- 이미지 분류, 객체 탐지
- 컴퓨터 비전 프로젝트
- 공간적 구조가 중요한 데이터
- 높은 성능이 우선인 경우

---

## 4. 실전 프로젝트: 꽃 분류 시스템

### 4.1 프로젝트 개요

**목표**: Daisy(데이지) vs Dandelion(민들레) 이진 분류 시스템 구현

#### 기술 스택

- **프레임워크**: TensorFlow/Keras
- **모델**: CNN (Convolutional Neural Network)
- **데이터**: 실제 꽃 이미지 (80×80×3)

### 4.2 데이터 파이프라인

#### 데이터 구조

```markdown
flowers/
├── train/
│   ├── daisy/      (529개 이미지)
│   └── dandelion/  (746개 이미지)
└── test/
    ├── daisy/      (77개 이미지)
    └── dandelion/  (105개 이미지)
```

#### 전처리 과정

1. **이미지 유효성 검사**: gif, png, jpeg, jpg 형식 확인
2. **크기 정규화**: 80×80 픽셀로 리사이즈
3. **레이블 인코딩**: daisy=0, dandelion=1
4. **데이터 저장**: NPZ 압축 형식으로 직렬화

### 4.3 모델 아키텍처

```python
# 꽃 분류 CNN 모델
model = models.Sequential([
    layers.Input(shape=(80, 80, 3)),
    layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(32, (3, 3), activation='relu', padding='same'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(32, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(1, activation='sigmoid')  # 이진 분류
])
```

### 4.4 고급 학습 기법

#### 콜백 함수 활용

1. **조기 종료 (EarlyStopping)**
   ```python
   EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
   ```

2. **학습률 스케줄링 (ReduceLROnPlateau)**
   ```python
   ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=3)
   ```

3. **모델 체크포인트 (ModelCheckpoint)**
   ```python
   ModelCheckpoint(filepath='best_model.h5', save_best_only=True)
   ```

### 4.5 성능 평가 결과

#### 최종 성능 지표

- **테스트 정확도**: ~80-85% (10 에포크 기준)
- **일반화 성능**: 양호한 수준
- **학습 시간**: 약 5-10분 (CPU 환경)

---

## 5. 딥러닝 모델 최적화 기법

### 5.1 정규화 기법

#### 1. Dropout

```python
layers.Dropout(0.3)  # 30% 뉴런을 무작위로 제거
```

- **효과**: 과대적합 방지
- **권장값**: 0.2 ~ 0.5

#### 2. Batch Normalization

```python
layers.BatchNormalization()  # 배치 정규화
```

- **효과**: 학습 안정성 향상, 빠른 수렴
- **위치**: 활성화 함수 이전에 배치

#### 3. L1/L2 정규화

```python
layers.Dense(128, kernel_regularizer=tf.keras.regularizers.l2(0.01))
```

### 5.2 데이터 증강 (Data Augmentation)

```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(
    rotation_range=30,        # 회전
    width_shift_range=0.3,    # 수평 이동
    height_shift_range=0.3,   # 수직 이동
    horizontal_flip=True,     # 수평 뒤집기
    zoom_range=0.3,          # 확대/축소
    brightness_range=[0.8, 1.2]  # 밝기 조절
)
```

### 5.3 최적화 알고리즘

#### 주요 옵티마이저 비교

| 옵티마이저 | 특징 | 권장 용도 |
|------------|------|-----------|
| **SGD** | 기본적, 안정적 | 간단한 모델 |
| **Adam** | 적응적 학습률, 빠른 수렴 | 대부분의 CNN |
| **RMSprop** | 학습률 자동 조정 | 순환 신경망 |
| **AdamW** | Adam + 가중치 감쇠 | 최신 모델 |

---

## 6. 실무 적용 가이드

### 6.1 모델 배포 체크리스트

#### 배포 전 검증사항

- [ ] **다양한 해상도 테스트**: 여러 크기의 이미지로 검증
- [ ] **메모리 사용량 분석**: 프로덕션 환경에서의 리소스 요구사항
- [ ] **추론 속도 벤치마크**: 실시간 처리 가능 여부 확인
- [ ] **엣지 케이스 처리**: 흐릿한 이미지, 관련 없는 객체 등
- [ ] **A/B 테스트**: 기존 시스템 대비 성능 검증

### 6.2 모델 관리 시스템

#### 버전 관리

```python
# 모델 정보 저장 예시
model_info = {
    'model_name': 'flower_classifier_v1',
    'training_time': '2025-07-21T15:30:00',
    'test_accuracy': 0.8352,
    'parameters': 1634058,
    'framework': 'TensorFlow 2.19.0'
}
```

#### 모니터링 지표

- **성능 지표**: 정확도, 정밀도, 재현율, F1-점수
- **시스템 지표**: 메모리 사용량, CPU 사용률, 응답 시간
- **비즈니스 지표**: 사용자 만족도, 오류율

### 6.3 확장 가능한 아키텍처

#### 마이크로서비스 패턴

```markdown
Web Interface → API Gateway → Model Service → Database
                     ↓
               Monitoring Service
```

#### 성능 최적화 전략

1. **모델 경량화**: TensorFlow Lite, ONNX 변환
2. **GPU 활용**: CUDA, cuDNN 최적화
3. **배치 처리**: 여러 이미지 동시 처리
4. **캐싱**: 결과 캐싱으로 응답 속도 향상

---

## 7. 향후 학습 방향

### 7.1 고급 CNN 아키텍처

#### 1. ResNet (잔차 네트워크)

- **핵심 개념**: Skip Connection으로 깊은 네트워크 학습
- **장점**: 기울기 소실 문제 해결
- **응용**: 이미지 분류, 객체 탐지

#### 2. DenseNet (밀집 연결 네트워크)

- **핵심 개념**: 모든 층이 서로 연결
- **장점**: 특징 재사용, 매개변수 효율성
- **응용**: 의료 이미지 분석

#### 3. EfficientNet (효율적 네트워크)

- **핵심 개념**: 깊이, 너비, 해상도의 균형적 스케일링
- **장점**: 높은 성능과 효율성
- **응용**: 모바일 환경, 실시간 처리

### 7.2 전이 학습 (Transfer Learning)

#### 사전 훈련된 모델 활용

```python
# ImageNet 사전 훈련 모델 사용 예시
base_model = tf.keras.applications.VGG16(
    weights='imagenet',  # ImageNet 가중치 로드
    include_top=False,   # 분류층 제외
    input_shape=(224, 224, 3)
)

# 커스텀 분류층 추가
model = tf.keras.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(128, activation='relu'),
    layers.Dense(num_classes, activation='softmax')
])
```

### 7.3 최신 기술 동향

#### 1. Vision Transformer (ViT)

- **개념**: Attention 메커니즘을 이미지에 적용
- **장점**: 글로벌 특징 학습, 높은 성능
- **단점**: 대용량 데이터 필요

#### 2. 자율 주행 / 의료 이미지 분석

- **응용 분야**: 실제 산업 적용 사례
- **요구 사항**: 높은 정확도, 실시간 처리
- **도전 과제**: 안전성, 해석가능성

#### 3. 생성형 AI (Generative AI)

- **GAN**: 생성적 적대 신경망
- **Diffusion Models**: 확산 모델
- **응용**: 이미지 생성, 스타일 변환

### 7.4 추천 학습 경로

#### 초급 → 중급

1. **기본 CNN 마스터**: Fashion-MNIST, CIFAR-10 완벽 이해
2. **전이 학습 실습**: ImageNet 모델 활용
3. **실전 프로젝트**: 개인 데이터셋으로 분류기 구축

#### 중급 → 고급

1. **고급 아키텍처**: ResNet, DenseNet 구현
2. **객체 탐지**: YOLO, R-CNN 계열 학습
3. **세그멘테이션**: U-Net, DeepLab 실습

#### 고급 → 전문가

1. **연구 논문 구현**: 최신 논문 재현
2. **커스텀 손실 함수**: 도메인 특화 최적화
3. **오픈소스 기여**: TensorFlow, PyTorch 생태계 참여

---

## 🎯 정리 및 핵심 포인트

### 주요 학습 성과

1. **CNN 기초 이해**: 합성곱층, 풀링층, 완전연결층의 역할과 구조
2. **실전 적용 경험**: Fashion-MNIST, CIFAR-10, 꽃 분류 프로젝트
3. **성능 최적화**: 정규화, 데이터 증강, 콜백 활용
4. **모델 비교 분석**: 일반 신경망 vs CNN의 장단점 이해

### 핵심 교훈

1. **적절한 도구 선택**: 문제에 맞는 모델 아키텍처 선택의 중요성
2. **실험적 검증**: 이론과 실제 성능 간의 차이 확인
3. **지속적 개선**: 초기 결과에 만족하지 않고 최적화 추구
4. **실무 관점**: 연구실 환경과 프로덕션 환경의 차이 고려

---

*"모든 모델은 틀렸지만, 일부는 유용하다."* - 조지 박스

**Happy Deep Learning! 🚀✨**