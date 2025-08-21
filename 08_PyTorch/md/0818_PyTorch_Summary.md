# 🔥 PyTorch 정리

##### 🗓️ 2025.08.18
##### 📝 Writer : Moon19ht

---

## 📚 목차

1. [PyTorch 기본 개념](#1-pytorch-기본-개념)
2. [Iris 데이터셋 분류 모델](#2-iris-데이터셋-분류-모델)
3. [유방암 데이터셋 이진 분류](#3-유방암-데이터셋-이진-분류)
4. [MNIST 손글씨 분류](#4-mnist-손글씨-분류)
5. [CNN을 이용한 고양이 vs 개 분류](#5-cnn을-이용한-고양이-vs-개-분류)
6. [핵심 개념 정리](#6-핵심-개념-정리)
7. [실습 결과 및 성과](#7-실습-결과-및-성과)

---

## 1. PyTorch 기본 개념

### 1.1 PyTorch 소개
- **정의**: Facebook에서 개발한 오픈소스 딥러닝 프레임워크
- **특징**: 동적 계산 그래프, 직관적인 API, GPU 가속 지원
- **장점**: 연구와 프로덕션 모두에 적합한 유연성

### 1.2 핵심 구성 요소

#### 텐서 (Tensor)
```python
import torch

# 텐서 생성
x = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
y = torch.zeros(2, 3)
z = torch.randn(2, 3)  # 정규분포에서 랜덤 생성
```

#### 모델 정의 (nn.Module)
```python
import torch.nn as nn

class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = nn.Linear(10, 1)
    
    def forward(self, x):
        return self.linear(x)
```

#### 자동 미분 (Autograd)
- `backward()`: 역전파 수행
- `torch.no_grad()`: 그래디언트 계산 비활성화
- `optimizer.zero_grad()`: 그래디언트 초기화

---

## 2. Iris 데이터셋 분류 모델

### 2.1 프로젝트 개요
- **목표**: 붓꽃 품종 분류 (3클래스 분류)
- **데이터**: 150개 샘플, 4개 특성
- **모델**: 다층 퍼셉트론 (MLP)

### 2.2 모델 아키텍처
```python
class IrisClassifier(nn.Module):
    def __init__(self, input_size=4, hidden1_size=16, hidden2_size=8, num_classes=3):
        super(IrisClassifier, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden1_size)    # 4 → 16
        self.fc2 = nn.Linear(hidden1_size, hidden2_size)  # 16 → 8
        self.fc3 = nn.Linear(hidden2_size, num_classes)   # 8 → 3
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.2)
```

### 2.3 주요 구현 사항
- **데이터 전처리**: StandardScaler 정규화
- **손실함수**: CrossEntropyLoss
- **옵티마이저**: Adam (lr=0.01)
- **정규화**: Dropout (0.2)
- **학습률 스케줄링**: StepLR

### 2.4 성능 결과
- **테스트 정확도**: 95-100%
- **모델 파라미터**: 약 400개
- **훈련 에포크**: 100회

### 2.5 핵심 학습 포인트
1. **다중 클래스 분류** 구현
2. **데이터 로더** 활용 (`TensorDataset`, `DataLoader`)
3. **모델 저장/로드** 방법
4. **혼동행렬**과 **분류보고서** 활용
5. **예측 확률** 분석

---

## 3. 유방암 데이터셋 이진 분류

### 3.1 프로젝트 개요
- **목표**: 유방암 진단 (이진 분류)
- **데이터**: 569개 샘플, 30개 특성
- **모델**: 완전연결 신경망

### 3.2 모델 구조
```python
class CancerClassifier(nn.Module):
    def __init__(self, input_size=30, hidden_sizes=[64, 32], output_size=1):
        # 30 → 64 → 32 → 1
        layers = []
        prev_size = input_size
        for hidden_size in hidden_sizes:
            layers.append(nn.Linear(prev_size, hidden_size))
            layers.append(nn.ReLU())
            prev_size = hidden_size
        layers.append(nn.Linear(prev_size, output_size))
        self.network = nn.Sequential(*layers)
```

### 3.3 이진 분류 특화 구현
- **손실함수**: `BCEWithLogitsLoss` (이진 교차 엔트로피)
- **출력**: 단일 뉴런 + Sigmoid 활성화
- **예측**: `torch.round(torch.sigmoid(outputs))`

### 3.4 클래스 기반 설계
1. **CancerDataProcessor**: 데이터 전처리 담당
2. **CancerTrainer**: 훈련 및 평가 담당
3. **모듈화된 설계**: 재사용성과 유지보수성 향상

### 3.5 성능 및 특징
- **정확도**: 90% 이상
- **훈련 안정성**: Adam 옵티마이저로 안정적 수렴
- **메모리 효율성**: 적은 파라미터로 높은 성능

---

## 4. MNIST 손글씨 분류

### 4.1 프로젝트 개요
- **목표**: 손글씨 숫자 인식 (10클래스 분류)
- **데이터**: 70,000개 이미지 (28×28 픽셀)
- **모델**: 완전연결 신경망

### 4.2 Config 클래스 활용
```python
class Config:
    BATCH_SIZE = 64
    LEARNING_RATE = 0.001
    EPOCHS = 5
    INPUT_SIZE = 28 * 28
    HIDDEN_SIZE = 500
    NUM_CLASSES = 10
```

### 4.3 모델 아키텍처
```python
class ImageClassifier(nn.Module):
    def __init__(self):
        super(ImageClassifier, self).__init__()
        self.fc1 = nn.Linear(784, 500)  # 28×28 → 500
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(500, 10)   # 500 → 10
    
    def forward(self, x):
        x = x.reshape(-1, 784)  # 이미지 평탄화
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x
```

### 4.4 데이터 전처리
- **정규화**: `transforms.Normalize((0.5,), (0.5,))`
- **텐서 변환**: `transforms.ToTensor()`
- **자동 다운로드**: `torchvision.datasets.MNIST`

### 4.5 예측 시스템
```python
class MNISTPredictor:
    def predict(self, image_path):
        image = Image.open(image_path).convert('L')
        image_tensor = self.transform(image).unsqueeze(0)
        output = self.model(image_tensor)
        probabilities = torch.nn.functional.softmax(output, dim=1)
        predicted_class = torch.argmax(probabilities, dim=1)
```

### 4.6 성능 결과
- **테스트 정확도**: 95-98%
- **총 파라미터**: 397,510개
- **훈련 시간**: 5 에포크로 충분

---

## 5. CNN을 이용한 고양이 vs 개 분류

### 5.1 프로젝트 개요
- **목표**: 이미지에서 고양이와 개 구분 (이진 분류)
- **데이터**: Kaggle Dogs vs Cats 데이터셋
- **모델**: 합성곱 신경망 (CNN)

### 5.2 데이터 준비
```python
# 데이터셋 서브셋 생성
def make_subset(subset_name, start_index, end_index):
    # 훈련: 0-1000, 검증: 1000-1500, 테스트: 1500-2500
    
# 데이터 증강
train_transforms = transforms.Compose([
    transforms.Resize((180, 180)),
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.RandomRotation(10),
    transforms.RandomAffine(degrees=0, translate=(0.2, 0.2)),
    transforms.ToTensor()
])
```

### 5.3 CNN 모델 구조
```python
class ConvNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_layers = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=3, padding='same'),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
            
            nn.Conv2d(32, 64, kernel_size=3, padding='same'),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
            
            nn.Conv2d(64, 128, kernel_size=3, padding='same'),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
            
            nn.Conv2d(128, 256, kernel_size=3, padding='same'),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
            
            nn.Conv2d(256, 256, kernel_size=3, padding='same'),
            nn.ReLU()
        )
        self.classifier = nn.Sequential(
            nn.Linear(256 * 11 * 11, 1),
            nn.Sigmoid()
        )
```

### 5.4 훈련 전략
- **옵티마이저**: RMSprop (lr=1e-4)
- **손실함수**: BCELoss
- **조기 종료**: Validation loss 기반
- **모델 체크포인트**: 최적 모델 저장

### 5.5 데이터 증강 효과
1. **RandomHorizontalFlip**: 좌우 반전
2. **RandomRotation**: 회전 변환
3. **RandomAffine**: 평행이동
4. **과적합 방지**: 일반화 성능 향상

---

## 6. 핵심 개념 정리

### 6.1 PyTorch 워크플로우

#### 1단계: 데이터 준비
```python
# 데이터 변환 정의
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean, std)
])

# 데이터셋 로드
dataset = datasets.MNIST(root='./data', transform=transform, download=True)
dataloader = DataLoader(dataset, batch_size=64, shuffle=True)
```

#### 2단계: 모델 정의
```python
class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.layers = nn.Sequential(...)
    
    def forward(self, x):
        return self.layers(x)
```

#### 3단계: 손실함수와 옵티마이저
```python
criterion = nn.CrossEntropyLoss()  # 또는 BCELoss
optimizer = optim.Adam(model.parameters(), lr=0.001)
```

#### 4단계: 훈련 루프
```python
for epoch in range(epochs):
    for inputs, labels in dataloader:
        optimizer.zero_grad()  # 그래디언트 초기화
        outputs = model(inputs)  # 순전파
        loss = criterion(outputs, labels)  # 손실 계산
        loss.backward()  # 역전파
        optimizer.step()  # 가중치 업데이트
```

### 6.2 주요 손실함수 비교

| 손실함수 | 용도 | 특징 |
|---------|------|------|
| `CrossEntropyLoss` | 다중 클래스 분류 | Softmax + NLLLoss |
| `BCELoss` | 이진 분류 | Sigmoid 출력과 함께 사용 |
| `BCEWithLogitsLoss` | 이진 분류 | Sigmoid + BCE (수치적 안정성) |
| `MSELoss` | 회귀 | 평균 제곱 오차 |

### 6.3 옵티마이저 특성

| 옵티마이저 | 특징 | 적용 사례 |
|-----------|------|-----------|
| `SGD` | 기본적, 모멘텀 지원 | 간단한 모델 |
| `Adam` | 적응적 학습률, 빠른 수렴 | 대부분의 경우 |
| `RMSprop` | RNN에 효과적 | 순환 신경망 |
| `AdamW` | Weight Decay 개선 | Transformer |

### 6.4 활성화 함수 비교

| 활성화 함수 | 수식 | 특징 |
|------------|------|------|
| `ReLU` | max(0, x) | 가장 일반적, 기울기 소실 해결 |
| `Sigmoid` | 1/(1+e^(-x)) | 이진 분류 출력층 |
| `Tanh` | (e^x - e^(-x))/(e^x + e^(-x)) | -1~1 출력 |
| `Softmax` | e^xi / Σe^xj | 다중 클래스 확률 분포 |

---

## 7. 실습 결과 및 성과

### 7.1 프로젝트별 성능 요약

| 프로젝트 | 데이터셋 | 모델 타입 | 정확도 | 파라미터 수 |
|---------|----------|-----------|---------|-------------|
| Iris 분류 | Iris (150) | MLP | 95-100% | ~400 |
| 유방암 진단 | Breast Cancer (569) | MLP | 90%+ | ~3,000 |
| MNIST | MNIST (70K) | MLP | 95-98% | ~400K |
| 고양이 vs 개 | Dogs vs Cats | CNN | 80-85% | ~30M |

### 7.2 학습한 핵심 기술

#### 데이터 처리
- **정규화**: StandardScaler, Normalize transforms
- **데이터 증강**: 회전, 반전, 이동
- **배치 처리**: DataLoader 활용
- **계층화 분할**: stratify 매개변수

#### 모델 설계
- **MLP**: 완전연결층 기반 분류
- **CNN**: 합성곱층을 이용한 이미지 처리
- **정규화**: Dropout으로 과적합 방지
- **모듈화**: 클래스 기반 설계 패턴

#### 훈련 최적화
- **학습률 스케줄링**: StepLR
- **조기 종료**: Validation loss 모니터링
- **체크포인트**: 최적 모델 저장
- **GPU 활용**: CUDA 자동 감지

#### 평가 및 분석
- **혼동행렬**: 분류 성능 시각화
- **분류보고서**: Precision, Recall, F1-score
- **예측 확률**: 모델 신뢰도 분석
- **시각화**: matplotlib을 이용한 결과 표시

### 7.3 실습을 통한 인사이트

#### 모델 복잡도와 성능
- **간단한 데이터**: 작은 MLP로도 충분한 성능
- **이미지 데이터**: CNN이 MLP보다 효과적
- **파라미터 수**: 성능과 반드시 비례하지 않음

#### 데이터 전처리의 중요성
- **정규화**: 훈련 안정성과 수렴 속도 향상
- **데이터 증강**: 과적합 방지와 일반화 성능 향상
- **배치 크기**: 메모리와 성능의 균형점 필요

#### 하이퍼파라미터 튜닝
- **학습률**: 너무 크면 발산, 너무 작으면 느린 수렴
- **에포크 수**: 과적합 방지를 위한 적절한 조절
- **배치 크기**: GPU 메모리와 성능 고려

### 7.4 다음 단계 학습 방향

#### 고급 아키텍처
- **ResNet**: 잔차 연결을 통한 깊은 네트워크
- **Transformer**: Attention 메커니즘
- **GAN**: 생성적 적대 신경망

#### 최적화 기법
- **Learning Rate Scheduling**: 코사인, 웜업
- **Regularization**: BatchNorm, LayerNorm
- **Transfer Learning**: 사전 훈련된 모델 활용

#### 프로덕션 배포
- **모델 경량화**: Quantization, Pruning
- **TorchScript**: 모델 직렬화
- **ONNX**: 다른 프레임워크와 호환성

---

## 🎯 최종 정리

이번 PyTorch 실습을 통해 딥러닝의 전체 파이프라인을 경험했습니다:

1. **기초 구축**: PyTorch 기본 구조와 텐서 조작
2. **다양한 문제**: 분류 문제를 통한 점진적 학습
3. **실전 적용**: 실제 데이터셋으로 모델 구현
4. **성능 최적화**: 하이퍼파라미터 튜닝과 정규화
5. **결과 분석**: 정량적/정성적 평가 방법

PyTorch의 직관적인 API와 동적 계산 그래프의 장점을 활용하여, 연구와 프로덕션 모두에 적용 가능한 딥러닝 모델을 구현할 수 있는 기초를 다졌습니다.

---

**📝 참고 자료**
- [PyTorch 공식 문서](https://pytorch.org/docs/)
- [PyTorch 튜토리얼](https://pytorch.org/tutorials/)
- [torchvision 문서](https://pytorch.org/vision/stable/index.html)