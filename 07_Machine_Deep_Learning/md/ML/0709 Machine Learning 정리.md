# 📊 Machine Learning 이론

##### 🗓️ 2025.07.09
##### 📝 Writer : Moon19ht

---

## 📚 목차

1. [지도학습 vs 비지도학습](#1-지도학습-vs-비지도학습)
2. [데이터 스케일링](#2-데이터-스케일링)
3. [서포트벡터머신(SVM)](#3-서포트벡터머신svm)
4. [이상치 탐지 및 처리](#4-이상치-탐지-및-처리)
5. [데이터 전처리 종합실습](#5-데이터-전처리-종합실습)
6. [성능 비교 및 분석](#6-성능-비교-및-분석)
7. [실무 적용 가이드](#7-실무-적용-가이드)

---

## 1. 지도학습 vs 비지도학습

### 지도학습 (Supervised Learning)
- **정의**: 출력결과(정답)를 알고 있을 때 사용하는 학습 방식
- **특징**: 레이블이 있는 데이터로 학습
- **사이킷런 패턴**: `fit()` → `predict()`
- **예시**: 분류, 회귀

### 비지도학습 (Unsupervised Learning)
- **정의**: 결과를 모르는 상태에서 패턴을 찾는 학습 방식
- **특징**: 라벨링이 없는 데이터 사용
- **사이킷런 패턴**: `fit()` → `transform()`
- **활용**: 지도학습 전단계 데이터 분석용으로 많이 사용
- **예시**: 군집화, 차원축소, 연관규칙분석

### 분류 vs 군집의 차이점
- **분류**: "기린일 확률 0.7, 병아리일 확률 0.3입니다"
- **군집**: "클래스1일 확률 0.7, 클래스2일 확률 0.3입니다"

---

## 2. 데이터 스케일링

### 스케일링의 필요성
- 서로 다른 단위와 범위를 가진 특성들을 통일
- 모델 성능 향상과 학습 안정성 확보
- 특히 거리 기반 알고리즘에서 필수적

### 스케일링 종류

#### 1. StandardScaler (표준화)
```python
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
scaled_data = ss.fit_transform(data)
```
- **특징**: 평균 0, 표준편차 1로 변환
- **사용 시기**: 
  - 데이터가 정규분포를 따른다고 가정할 때
  - 모델이 스케일링에 민감할 때
  - SVM, 로지스틱 회귀, 딥러닝에 유용
- **단점**: 이상치에 민감

#### 2. RobustScaler (로버스트 스케일링)
```python
from sklearn.preprocessing import RobustScaler
rb = RobustScaler()
scaled_data = rb.fit_transform(data)
```
- **특징**: 중위값과 IQR 사용
- **사용 시기**: 데이터에 이상치가 많을 때
- **장점**: StandardScaler 대신 사용 가능한 안정적 방법

#### 3. MinMaxScaler (최소-최대 정규화)
```python
from sklearn.preprocessing import MinMaxScaler
mm = MinMaxScaler()
scaled_data = mm.fit_transform(data)
```
- **특징**: 특성값을 0~1 범위로 변환
- **사용 시기**: 
  - 특성값의 범위가 명확히 0~1 사이에 와야 할 때
  - 이미지 데이터, 특정 신경망에서 사용

#### 4. Normalizer (정규화)
```python
from sklearn.preprocessing import Normalizer
nm = Normalizer()
scaled_data = nm.fit_transform(data)
```
- **특징**: 벡터의 크기를 1로 만듦
- **사용 시기**: 
  - 주로 텍스트 분석에 유용
  - 클러스터링(군집분석)에 사용

---

## 3. 서포트벡터머신(SVM)

### SVM의 핵심 개념
- **기본 아이디어**: 평면에 선을 그어 데이터를 분류
- **고차원 매핑**: 평면에서 분리가 어려운 경우 고차원 공간으로 변환
- **마진 최대화**: 클래스 간 경계를 최대한 멀리 설정

### 스케일링의 중요성

#### 유방암 데이터셋 실험 결과
| 모델 | 스케일링 | 훈련 정확도 | 테스트 정확도 |
|------|----------|-------------|---------------|
| 로지스틱 회귀 | 없음 | 94.6% | 94.4% |
| 로지스틱 회귀 | 적용 | 99.1% | 96.5% |
| SVM | 없음 | 90.4% | 93.7% |
| SVM | 적용 | 99.1% | 96.5% |

### 주요 발견사항
1. **SVM은 스케일링에 매우 민감**
2. **로지스틱 회귀는 상대적으로 덜 민감하지만 수렴 속도 개선**
3. **스케일링 적용 시 두 모델 모두 성능 향상**

### 수렴 문제 해결 방법
```python
# 방법 1: max_iter 증가
LogisticRegression(max_iter=1000)

# 방법 2: 데이터 스케일링 (권장)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

---

## 4. 이상치 탐지 및 처리

### IQR 방법을 이용한 이상치 탐지

#### 계산 공식
- **Q1**: 25% 분위수
- **Q3**: 75% 분위수  
- **IQR**: Q3 - Q1
- **하한 경계**: Q1 - 1.5 × IQR
- **상한 경계**: Q3 + 1.5 × IQR

#### 실습 예제 결과
```python
# 처리 전: 평균 24.50, 표준편차 39.90
# 처리 후: 평균 8.10, 표준편차 5.95
```

### 이상치 처리 전략
1. **제거**: 완전히 삭제
2. **대체**: 경계값으로 변경 (Winsorizing)
3. **변환**: 로그 변환 등을 통한 완화

---

## 5. 데이터 전처리 종합실습

### 실습 데이터셋별 특징

#### 1. Iris 데이터셋
- **특징**: 깨끗한 데이터, 결측치 없음
- **크기**: 150개 샘플, 4개 특성
- **목표**: 3종류 붓꽃 분류
- **전처리**: 불필요
- **성능**: 훈련 97.1%, 테스트 93.3%

#### 2. Penguins 데이터셋  
- **특징**: 결측치 존재, 범주형 데이터 포함
- **크기**: 333개 샘플, 6개 특성
- **목표**: 3종류 펭귄 분류
- **전처리**: 라벨 인코딩 + 결측치 제거
- **성능**: 훈련 99.1%, 테스트 99.0%

#### 3. Diamonds 데이터셋
- **특징**: 복잡한 범주형 변수 다수
- **크기**: 53,940개 샘플, 9개 특성
- **목표**: 5종류 다이아몬드 컷 분류
- **전처리**: 자동화된 라벨 인코딩
- **성능**: 훈련 54.3%, 테스트 54.0%

### 라벨 인코딩 기법

#### 수동 매핑 방식
```python
island_mapping = {'Torgersen': 1, 'Dream': 2, 'Biscoe': 3}
df['island_label'] = df['island'].map(island_mapping)
```

#### 자동화된 매핑 함수
```python
def get_label_map(df, field):
    unique_values = df[field].unique()
    label_map = {item: index + 1 for index, item in enumerate(unique_values)}
    return label_map
```

---

## 6. 성능 비교 및 분석

### 종합 실험 결과

| 데이터셋 | 훈련 정확도 | 테스트 정확도 | 성능 차이 | 전처리 복잡도 |
|----------|-------------|---------------|-----------|---------------|
| Iris | 0.971 | 0.933 | 0.038 | 낮음 |
| Penguins | 0.991 | 0.990 | 0.001 | 중간 |
| Diamonds | 0.543 | 0.540 | 0.003 | 높음 |

### 핵심 인사이트
1. **데이터 품질이 모델 성능에 결정적 영향**
2. **적절한 전처리는 성공적인 머신러닝의 핵심**
3. **과적합 위험도**: Iris > Penguins ≈ Diamonds
4. **전처리 복잡도와 성능은 반드시 비례하지 않음**

---

## 7. 실무 적용 가이드

### 머신러닝 프로젝트 체크리스트

#### 데이터 탐색 단계
- [ ] 데이터 크기 및 구조 파악 (`shape`, `info()`)
- [ ] 기술 통계 확인 (`describe()`)
- [ ] 결측치 현황 조사 (`isnull().sum()`)
- [ ] 타겟 변수 분포 확인 (`value_counts()`)
- [ ] 범주형/수치형 변수 구분

#### 데이터 전처리 단계
- [ ] **결측치 처리**: 제거 vs 대체 전략 결정
- [ ] **이상치 탐지**: 박스플롯, IQR 방법 활용
- [ ] **범주형 인코딩**: 라벨 인코딩 vs 원핫 인코딩
- [ ] **스케일링**: 필요시 StandardScaler 적용
- [ ] **특성 선택**: 관련성 높은 특성 선별

#### 모델링 단계
- [ ] **데이터 분할**: train_test_split with stratify
- [ ] **모델 선택**: 문제 유형에 적합한 알고리즘
- [ ] **하이퍼파라미터**: max_iter, random_state 설정

#### 평가 및 개선 단계
- [ ] **성능 지표**: 정확도, 정밀도, 재현율
- [ ] **과적합 확인**: 훈련-테스트 성능 차이 < 0.1
- [ ] **예측 샘플**: 실제 예측 결과 확인

### 재사용 가능한 함수 템플릿

#### 범주형 데이터 자동 인코딩
```python
def preprocess_categorical_data(df, categorical_columns):
    """범주형 데이터 자동 라벨 인코딩"""
    df_encoded = df.copy()
    mappings = {}
    
    for col in categorical_columns:
        unique_values = df[col].unique()
        mapping = {val: idx+1 for idx, val in enumerate(unique_values)}
        df_encoded[f'{col}_label'] = df_encoded[col].map(mapping)
        mappings[col] = mapping
    
    return df_encoded, mappings
```

#### 모델 성능 평가 표준화
```python
def evaluate_model(model, X_train, X_test, y_train, y_test, dataset_name):
    """모델 성능 평가 표준화"""
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)
    gap = train_score - test_score
    
    print(f"=== {dataset_name} 결과 ===")
    print(f"훈련 정확도: {train_score:.4f}")
    print(f"테스트 정확도: {test_score:.4f}")
    print(f"성능 차이: {gap:.4f}")
    print(f"과적합: {'위험' if gap > 0.1 else '양호'}")
    
    return train_score, test_score, gap
```

### 핵심 권장사항

1. **항상 데이터 탐색(EDA)부터 시작**
2. **전처리 과정을 함수화하여 재사용성 향상**
3. **훈련-테스트 성능 차이 0.1 이하 유지**
4. **SVM과 같은 거리 기반 알고리즘에서는 반드시 스케일링 적용**
5. **결측치 처리 전략을 신중하게 결정**
6. **범주형 데이터는 적절한 인코딩 기법 선택**

### 주의사항

1. **데이터 누수 방지**: 테스트 데이터로 전처리하지 않기
2. **랜덤 시드 고정**: 재현 가능한 결과를 위해 random_state 설정
3. **레이블 매핑 보존**: 인코딩 매핑 정보 저장 및 관리
4. **성능 모니터링**: 지속적인 과적합 여부 확인

### 결론

"별짓 다해도 데이터가 많아야 한다!" - 데이터의 품질과 양이 머신러닝 성공의 핵심 요소입니다.
