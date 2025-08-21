# 🔥 PyTorch 정리

##### 🗓️ 2025.08.19
##### 📝 Writer : Moon19ht

---

## 📚 목차

1. [PyTorch 고급 실습 개요](#1-pytorch-고급-실습-개요)
2. [캘리포니아 주택 가격 회귀 모델](#2-캘리포니아-주택-가격-회귀-모델)
3. [MPG 연비 예측 회귀 모델](#3-mpg-연비-예측-회귀-모델)
4. [다이아몬드 가격 예측 모델](#4-다이아몬드-가격-예측-모델)
5. [LLM 텍스트 생성 실습](#5-llm-텍스트-생성-실습)
6. [고급 MNIST 분류 모델](#6-고급-mnist-분류-모델)
7. [핵심 기술 및 개념](#7-핵심-기술-및-개념)
8. [실습 성과 및 인사이트](#8-실습-성과-및-인사이트)

---

## 1. PyTorch 고급 실습 개요

### 1.1 학습 목표
0819일 실습은 PyTorch의 고급 기능과 다양한 도메인 적용에 중점을 둔 심화 과정입니다.

- **회귀 문제 해결**: 연속값 예측을 위한 신경망 설계
- **고급 데이터 전처리**: 데이터 누수 방지 및 정규화 기법
- **모델 최적화**: 학습률 스케줄링, 얼리 스토핑, 정규화
- **자연어 처리**: Transformers 라이브러리를 활용한 LLM 사용
- **모듈화 설계**: 재사용 가능한 클래스 기반 구조

### 1.2 실습 데이터셋
- **California Housing**: 회귀 문제 (20,640개 샘플, 8개 특성)
- **MPG Dataset**: 자동차 연비 예측 (392개 샘플, 6개 특성)
- **Diamonds Dataset**: 다이아몬드 가격 예측 (범주형 + 수치형 특성)
- **KoGPT2**: 한국어 텍스트 생성
- **MNIST**: 고급 분류 모델 (완전한 파이프라인)

---

## 2. 캘리포니아 주택 가격 회귀 모델

### 2.1 프로젝트 개요
- **목표**: 캘리포니아 지역 주택 가격 예측
- **데이터**: 20,640개 샘플, 8개 특성
- **특성**: MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude
- **타겟**: MedHouseVal (단위: 10만 달러)

### 2.2 핵심 구현 특징

#### 데이터 누수 방지
```python
# 데이터 누수 방지: 훈련 세트에만 fit, 검증 세트에는 transform만 적용
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train).astype(np.float32)
X_val = scaler.transform(X_val).astype(np.float32)
```

#### 고급 모델 아키텍처
```python
class HousingRegressor(nn.Module):
    def __init__(self, input_size=8, hidden_sizes=(128, 64, 32), p_drop=0.1):
        super().__init__()
        layers = []
        prev = input_size
        
        # 은닉층 구성 (동적 생성)
        for h in hidden_sizes:
            layers += [nn.Linear(prev, h), nn.ReLU(), nn.Dropout(p_drop)]
            prev = h
        
        # 출력층
        layers += [nn.Linear(prev, 1)]
        self.net = nn.Sequential(*layers)
        
        # He 초기화
        self.apply(self._init_weights)
```

#### 고급 훈련 기법
- **학습률 스케줄링**: `ReduceLROnPlateau`
- **얼리 스토핑**: Validation loss 기반 (patience=20)
- **가중치 정규화**: Weight Decay (L2 정규화)
- **드롭아웃**: 과적합 방지

### 2.3 성능 및 결과
- **손실함수**: MSE (Mean Squared Error)
- **평가지표**: MSE, RMSE, MAE, R²
- **특성 중요도**: 순열 중요도 분석
- **시각화**: 학습 곡선, 예측 vs 실제값, 잔차 분석

### 2.4 핵심 학습 포인트
1. **데이터 누수 방지**: 훈련/검증 분할 후 전처리 적용
2. **재현성 보장**: 시드 고정 및 결정적 알고리즘 사용
3. **모델 모니터링**: 실시간 성능 추적 및 저장
4. **다중 평가 지표**: 종합적 성능 분석

---

## 3. MPG 연비 예측 회귀 모델

### 3.1 프로젝트 개요
- **목표**: 자동차 연비(MPG) 예측
- **데이터**: 392개 샘플, 6개 특성
- **특성**: cylinders, displacement, horsepower, weight, acceleration, origin
- **모델**: 객체지향 설계의 완전한 파이프라인

### 3.2 객체지향 설계 패턴

#### 모델 클래스
```python
class MPGRegressor(nn.Module):
    def __init__(self, input_size=6):
        super(MPGRegressor, self).__init__()
        self.layers = nn.Sequential(
            nn.Linear(input_size, 64),  # 입력층
            nn.ReLU(),
            nn.Linear(64, 32),          # 은닉층 1
            nn.ReLU(),
            nn.Linear(32, 32),          # 은닉층 2
            nn.ReLU(),
            nn.Linear(32, 1)            # 출력층
        )
```

#### 데이터 처리 클래스
```python
class MPGDataProcessor:
    def __init__(self, data_path):
        self.data_path = data_path
        self.scaler = StandardScaler()
        
    def load_and_preprocess_data(self):
        # 데이터 로드, 결측값 처리, 정규화
        
    def create_data_loaders(self, X, y, test_size=0.2, batch_size=32):
        # 데이터 분할, 텐서 변환, DataLoader 생성
```

#### 훈련 클래스
```python
class MPGTrainer:
    def __init__(self, model, learning_rate=0.001):
        self.model = model
        self.criterion = nn.MSELoss()
        self.optimizer = optim.Adam(model.parameters(), lr=learning_rate)
```

### 3.3 고급 시각화 및 분석
- **탐색적 데이터 분석**: 특성별 히스토그램, 상관관계 히트맵
- **훈련 모니터링**: 실시간 손실 추적
- **성능 분석**: 실제 vs 예측값, 잔차 분석
- **특성 중요도**: 상관계수 기반 분석

### 3.4 모듈화의 장점
1. **재사용성**: 다른 데이터셋에 쉽게 적용 가능
2. **유지보수성**: 각 기능별 독립적 관리
3. **확장성**: 새로운 기능 추가 용이
4. **테스트 용이성**: 각 클래스별 독립적 테스트

---

## 4. 다이아몬드 가격 예측 모델

### 4.1 프로젝트 개요
- **목표**: 다이아몬드 가격 예측
- **데이터**: 범주형 변수 포함 (cut, color, clarity)
- **특징**: 원핫 인코딩을 통한 범주형 변수 처리

### 4.2 범주형 데이터 처리

#### 원핫 인코딩
```python
# 원핫 인코딩 (범주형 변수 처리)
X = pd.get_dummies(X, drop_first=True)
print(f"원핫 인코딩 후 특성 수: {X.shape[1]}")
```

#### 동적 모델 구조
```python
class DiamondPricePredictor(nn.Module):
    def __init__(self, input_features):
        super(DiamondPricePredictor, self).__init__()
        self.fc1 = nn.Linear(input_features, 128)  # 동적 입력 크기
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 32)
        self.output = nn.Linear(32, 1)
        self.dropout = nn.Dropout(0.2)
```

### 4.3 통합 파이프라인 클래스
```python
class DiamondPriceModel:
    def __init__(self, data_path, test_size=0.2, batch_size=32, learning_rate=0.001):
        # 모든 하이퍼파라미터 중앙 관리
        
    def load_and_preprocess_data(self):
        # 데이터 로드, 원핫 인코딩, 정규화
        
    def build_model(self, input_features):
        # 동적 모델 생성
        
    def train(self, epochs=100):
        # 훈련 루프
        
    def evaluate(self):
        # 모델 평가
        
    def predict(self, X_new):
        # 새로운 데이터 예측
```

### 4.4 핵심 특징
1. **범주형 변수 처리**: 원핫 인코딩을 통한 자동 변환
2. **동적 아키텍처**: 입력 특성 수에 따라 자동 조정
3. **통합 관리**: 전체 파이프라인의 일원화된 관리
4. **다중 평가지표**: MSE, RMSE, MAE 종합 평가

---

## 5. LLM 텍스트 생성 실습

### 5.1 프로젝트 개요
- **목표**: KoGPT2를 이용한 한국어 텍스트 생성
- **모델**: skt/kogpt2-base-v2
- **라이브러리**: Transformers (Hugging Face)

### 5.2 모델 로드 및 설정

#### 모델 초기화
```python
def load_model(model_name="skt/kogpt2-base-v2"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return tokenizer, model

def setup_device(model):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    return device
```

### 5.3 텍스트 생성 파라미터

#### 핵심 파라미터 설명
- **max_length**: 생성할 최대 토큰 수
- **temperature**: 창의성 조절 (0.1-2.0)
  - 낮음(0.3): 보수적, 일관성 있는 생성
  - 높음(1.2): 창의적, 다양한 생성
- **top_k**: 상위 k개 토큰에서만 선택 (품질 향상)
- **repetition_penalty**: 반복 방지 (1.0-3.0)

#### 고급 생성 함수
```python
def generate_text_with_params(tokenizer, model, device, input_text, 
                            max_length=50, temperature=0.9, top_k=50, repetition_penalty=2.0):
    model.eval()
    input_ids = tokenizer.encode(input_text, return_tensors="pt").to(device)
    
    generated_ids = model.generate(
        input_ids,
        max_length=max_length,
        pad_token_id=tokenizer.eos_token_id,
        repetition_penalty=repetition_penalty,
        do_sample=True,
        top_k=top_k,
        temperature=temperature
    )
    
    return tokenizer.decode(generated_ids[0], skip_special_tokens=True)
```

### 5.4 실험 및 비교 분석
- **파라미터 실험**: Temperature와 Top-k 값 변화에 따른 결과 비교
- **다양한 입력**: 여러 주제의 텍스트 생성 실험
- **품질 평가**: 일관성, 창의성, 자연스러움 분석

### 5.5 핵심 학습 포인트
1. **사전 훈련된 모델 활용**: Hugging Face 생태계 이해
2. **생성 파라미터 튜닝**: 품질과 다양성의 균형
3. **토큰화 과정**: 텍스트-토큰-텍스트 변환 과정 이해
4. **GPU 최적화**: 모델과 데이터의 디바이스 관리

---

## 6. 고급 MNIST 분류 모델

### 6.1 프로젝트 개요
- **목표**: 완전한 MNIST 분류 파이프라인 구축
- **특징**: 산업급 코드 구조와 고급 기능 구현
- **확장성**: 실제 이미지 예측까지 포함

### 6.2 완전한 클래스 구조

#### 메인 분류기 클래스
```python
class MNISTClassifier:
    def __init__(self, batch_size=64, learning_rate=0.001, epochs=5):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.5,), (0.5,))
        ])
        
    def prepare_data(self):
        # MNIST 데이터 자동 다운로드 및 로드
        
    def build_model(self):
        # 모델, 손실함수, 옵티마이저 초기화
        
    def train(self):
        # 훈련 루프 + 시각화
        
    def evaluate(self):
        # 클래스별 성능 분석
        
    def predict_image(self, image_path):
        # 실제 이미지 파일 예측
```

### 6.3 고급 기능들

#### 모델 저장/로드
```python
def save_model(self, filepath="mnist_model.pth"):
    torch.save(self.model.state_dict(), filepath)
    
def load_model(self, filepath="mnist_model.pth"):
    self.model.load_state_dict(torch.load(filepath, map_location=self.device))
    self.model.eval()
```

#### 실제 이미지 예측
```python
def predict_image(self, image_path):
    image = Image.open(image_path).convert('L')
    
    predict_transform = transforms.Compose([
        transforms.Resize((28, 28)),
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])
    
    # 예측 + 시각화
```

#### 상세 성능 분석
- **클래스별 정확도**: 각 숫자(0-9)별 성능 분석
- **혼동행렬**: 잘못 분류된 패턴 분석
- **신뢰도 분석**: 예측 확률 분포 시각화

### 6.4 시각화 및 분석 도구
- **데이터 샘플 시각화**: 원본 데이터 확인
- **훈련 과정 모니터링**: 손실 곡선 실시간 표시
- **예측 결과 시각화**: 이미지, 확률, 신뢰도 통합 표시
- **테스트 샘플 분석**: 정답/오답 비교 분석

---

## 7. 핵심 기술 및 개념

### 7.1 고급 PyTorch 기법

#### 모델 설계 패턴
```python
# 동적 네트워크 구성
def build_network(input_size, hidden_sizes, output_size, dropout_rate=0.1):
    layers = []
    prev_size = input_size
    
    for hidden_size in hidden_sizes:
        layers.extend([
            nn.Linear(prev_size, hidden_size),
            nn.ReLU(),
            nn.Dropout(dropout_rate)
        ])
        prev_size = hidden_size
    
    layers.append(nn.Linear(prev_size, output_size))
    return nn.Sequential(*layers)
```

#### 가중치 초기화
```python
@staticmethod
def _init_weights(m):
    if isinstance(m, nn.Linear):
        nn.init.kaiming_uniform_(m.weight, nonlinearity='relu')  # He 초기화
        if m.bias is not None:
            nn.init.zeros_(m.bias)
```

### 7.2 데이터 전처리 고급 기법

#### 데이터 누수 방지 패턴
```python
# 올바른 방법: 훈련 데이터에만 fit
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)  # fit 없이 transform만
```

#### 범주형 변수 처리
```python
# 원핫 인코딩
X_encoded = pd.get_dummies(X, drop_first=True)
# 동적 입력 크기 조정
model = MyModel(input_size=X_encoded.shape[1])
```

### 7.3 모델 최적화 기법

#### 학습률 스케줄링
```python
# ReduceLROnPlateau: 성능 정체 시 학습률 감소
scheduler = optim.lr_scheduler.ReduceLROnPlateau(
    optimizer, mode='min', factor=0.5, patience=5, verbose=True
)
scheduler.step(val_loss)
```

#### 얼리 스토핑
```python
# 검증 손실 기반 조기 종료
if val_loss < best_val_loss:
    best_val_loss = val_loss
    patience_counter = 0
    torch.save(model.state_dict(), 'best_model.pth')
else:
    patience_counter += 1
    
if patience_counter >= patience:
    break  # 훈련 종료
```

### 7.4 모델 평가 및 분석

#### 다중 평가 지표
```python
def calculate_metrics(y_true, y_pred):
    mse = np.mean((y_true - y_pred) ** 2)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    return mse, rmse, mae, r2
```

#### 특성 중요도 분석
```python
def permutation_importance(model, X, y, feature_names, n_repeats=5):
    baseline_score = r2_score(y, model.predict(X))
    importances = []
    
    for i, feature_name in enumerate(feature_names):
        scores = []
        for _ in range(n_repeats):
            X_perm = X.copy()
            np.random.shuffle(X_perm[:, i])
            perm_score = r2_score(y, model.predict(X_perm))
            scores.append(baseline_score - perm_score)
        importances.append(np.mean(scores))
    
    return np.array(importances)
```

---

## 8. 실습 성과 및 인사이트

### 8.1 프로젝트별 성능 요약

| 프로젝트 | 데이터셋 | 모델 타입 | 주요 기법 | 평가 지표 |
|---------|----------|-----------|-----------|-----------|
| 캘리포니아 주택 | California Housing | 회귀 신경망 | 얼리스토핑, 스케줄링 | RMSE, R² |
| MPG 연비 예측 | Auto MPG | 회귀 신경망 | 객체지향 설계 | MSE, MAE |
| 다이아몬드 가격 | Diamonds | 회귀 신경망 | 원핫 인코딩 | MSE, RMSE, MAE |
| 텍스트 생성 | KoGPT2 | Transformer | 생성 파라미터 튜닝 | 정성적 평가 |
| MNIST 분류 | MNIST | 완전연결망 | 완전한 파이프라인 | 정확도, 클래스별 성능 |

### 8.2 핵심 학습 성과

#### 회귀 모델링 마스터
1. **다양한 도메인**: 부동산, 자동차, 보석 등 실제 문제 해결
2. **데이터 누수 방지**: 올바른 전처리 순서 학습
3. **성능 최적화**: 스케줄링, 정규화, 얼리 스토핑
4. **범주형 데이터**: 원핫 인코딩을 통한 혼합 데이터 처리

#### 고급 PyTorch 기법
1. **동적 모델 구성**: 입력 크기에 따른 자동 조정
2. **가중치 초기화**: He 초기화를 통한 학습 안정화
3. **모델 영속성**: 저장/로드를 통한 모델 재사용
4. **디바이스 관리**: CPU/GPU 자동 감지 및 활용

#### 자연어 처리 입문
1. **사전 훈련된 모델**: Transformers 라이브러리 활용
2. **텍스트 생성**: 다양한 파라미터를 통한 품질 조절
3. **토큰화 이해**: 텍스트 처리의 핵심 개념
4. **한국어 특화**: KoGPT2를 통한 한국어 생성

#### 소프트웨어 공학 원칙
1. **객체지향 설계**: 재사용 가능한 클래스 구조
2. **모듈화**: 독립적 기능별 분리
3. **재현성**: 시드 고정 및 결정적 실행
4. **문서화**: 상세한 주석과 설명

### 8.3 실무 적용 인사이트

#### 데이터 과학 관점
- **전처리의 중요성**: 모델 성능의 70%를 좌우
- **검증 전략**: 적절한 분할과 평가 지표 선택
- **특성 엔지니어링**: 도메인 지식과 데이터 탐색의 조화
- **모델 해석**: 예측뿐만 아니라 설명 가능성도 중요

#### 딥러닝 엔지니어링
- **아키텍처 설계**: 문제에 맞는 적절한 복잡도 선택
- **하이퍼파라미터**: 체계적 튜닝 방법론 필요
- **모니터링**: 실시간 성능 추적과 시각화
- **프로덕션**: 모델 배포를 고려한 코드 설계

#### MLOps 관점
- **파이프라인**: 데이터부터 배포까지 자동화
- **버전 관리**: 모델과 데이터의 버전 추적
- **재현성**: 실험 결과의 일관성 보장
- **확장성**: 다른 문제에 쉽게 적용 가능한 구조

### 8.4 다음 단계 학습 방향

#### 고급 아키텍처
- **CNN**: 이미지 처리를 위한 합성곱 신경망
- **RNN/LSTM**: 시계열 데이터와 순차 정보 처리
- **Transformer**: 최신 자연어 처리 아키텍처
- **GAN**: 생성적 적대 신경망

#### 최적화 기법
- **배치 정규화**: 학습 안정성 향상
- **Attention 메커니즘**: 중요한 정보에 집중
- **전이 학습**: 사전 훈련된 모델 활용
- **앙상블**: 여러 모델의 조합으로 성능 향상

#### 실무 도구
- **MLflow**: 실험 관리 및 모델 추적
- **DVC**: 데이터와 모델 버전 관리
- **Docker**: 일관된 실행 환경
- **Kubernetes**: 대규모 모델 배포

---

## 🎯 최종 정리

0819일 PyTorch 고급 실습을 통해 다음과 같은 성과를 달성했습니다:

### 🔧 기술적 성과
1. **회귀 모델링 완전 정복**: 3개의 서로 다른 도메인 문제 해결
2. **고급 PyTorch 기법**: 동적 모델, 고급 최적화, 모델 영속성
3. **자연어 처리 입문**: LLM을 활용한 텍스트 생성
4. **완전한 ML 파이프라인**: 산업급 코드 구조 구현

### 📊 방법론적 성과
1. **데이터 누수 방지**: 올바른 전처리 순서 습득
2. **객체지향 설계**: 재사용 가능한 모듈화 구조
3. **성능 최적화**: 다양한 정규화 및 스케줄링 기법
4. **모델 평가**: 다각도 성능 분석 및 해석

### 🚀 실무 준비
1. **End-to-End 경험**: 문제 정의부터 배포까지 전체 과정
2. **도메인 다양성**: 부동산, 자동차, 보석, 언어 모델
3. **코드 품질**: 가독성, 재사용성, 확장성을 고려한 설계
4. **문제 해결**: 실제 데이터의 복잡성과 도전 과제 경험

PyTorch의 강력함과 유연성을 활용하여 다양한 머신러닝 문제를 해결할 수 있는 실무 역량을 갖추었습니다. 특히 회귀 문제에 대한 깊은 이해와 고급 PyTorch 기법, 그리고 자연어 처리 분야까지 확장한 것이 큰 성과입니다.

---

**📝 참고 자료**
- [PyTorch 공식 문서](https://pytorch.org/docs/)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [scikit-learn 문서](https://scikit-learn.org/stable/)
- [KoGPT2 모델](https://huggingface.co/skt/kogpt2-base-v2)