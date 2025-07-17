# 📊 Machine Learning 이론

##### 🗓️ 2025.07.10
##### 📝 Writer : Moon19ht

---

## 📚 목차

1. [군집분석(클러스터링)](#1-군집분석클러스터링)
2. [주성분분석(PCA)](#2-주성분분석pca)
3. [K-Fold 교차검증](#3-k-fold-교차검증)
4. [성능 비교 및 분석](#4-성능-비교-및-분석)
5. [실무 적용 가이드](#5-실무-적용-가이드)

---

## 1. 군집분석(클러스터링)

### 군집분석이란?
- **비지도학습**의 대표적인 방법 중 하나
- 결과(라벨)를 주지 않고 데이터만으로 분류 수행
- 일반적으로 군집의 개수는 사전에 지정해야 함

### K-Means 클러스터링

#### 기본 원리
- 데이터를 K개의 군집으로 분할
- 각 군집의 중심점(centroid)을 기준으로 분류
- 반복적으로 중심점을 업데이트하여 최적화

#### 주요 매개변수
```python
from sklearn.cluster import KMeans

kmeans = KMeans(
    n_clusters=3,      # 군집 개수
    random_state=42    # 재현 가능한 결과
)
```

### 가우시안(정규) 분포
- `np.random.normal(평균, 표준편차, 형태)` 사용
- 예: `np.random.normal(173, 10, 100)` - 평균 173, 표준편차 10인 100개 데이터
- 인공 데이터 생성을 통한 알고리즘 검증

### 실습 결과

#### 인공 데이터 군집분석
- **3개 가우시안 분포**에서 생성된 데이터
- **150개 샘플** (각 군집당 50개)
- **정확한 분류** 성공: 중심점이 명확히 분리됨

#### Iris 데이터셋 군집분석
- **5개 군집**으로 강제 분할 (실제 클래스는 3개)
- 원래 군집 개수보다 많이 설정하면 **강제로 세분화**
- 원래 군집 개수보다 적게 설정하면 **정보 손실** 발생

### 군집 개수 결정 방법
1. **엘보우 방법(Elbow Method)**: 최적 K값 찾기
2. **실루엣 방법(Silhouette Analysis)**: 군집 품질 평가
3. **전문가적 견해**: 도메인 지식 활용

---

## 2. 주성분분석(PCA)

### PCA의 개념
- **Principal Component Analysis**: 고차원 데이터를 저차원으로 축소
- **차원의 저주** 해결: 특성이 많을 때 성능 저하 방지
- **비지도 학습**: 라벨 없이 데이터의 패턴 찾기

### PCA의 필요성

#### 고차원 데이터 문제
- **이미지 데이터**: 80×80×3 = 19,200개 특성
- **계산 복잡도 증가**: 학습 시간 및 메모리 사용량 증가
- **과적합 위험**: 특성 수가 샘플 수보다 많을 때

#### 다중공선성 문제
- **높은 상관관계**: 특성들 간의 강한 연관성
- **유방암 데이터셋 예시**: 
  - mean radius ↔ mean perimeter: 0.998
  - mean radius ↔ mean area: 0.987

### PCA 과정

#### 1단계: 데이터 표준화
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

#### 2단계: PCA 적용
```python
from sklearn.decomposition import PCA
pca = PCA(n_components=10)
X_pca = pca.fit_transform(X_scaled)
```

#### 3단계: 설명 분산 확인
```python
explained_variance = pca.explained_variance_ratio_
print(f"누적 설명 분산: {explained_variance.sum():.2%}")
```

### 실습 결과 분석

#### 손글씨 데이터셋 (Digits)
- **원본**: 64차원 (8×8 픽셀)
- **PCA 후**: 10차원 (84% 차원 축소)
- **설명 분산**: 58.87%

#### 성능 비교 (로지스틱 회귀)
| 방법 | 차원 | 훈련 정확도 | 테스트 정확도 |
|------|------|-------------|---------------|
| 원본 데이터 | 64 | 1.0000 | 0.9733 |
| 표준화 | 64 | 0.9985 | 0.9711 |
| PCA | 10 | 0.9005 | 0.8933 |

### PCA 시각화

#### 2D 시각화
- **PC1 + PC2**: 가장 중요한 두 성분
- **색상별 클래스**: 각 숫자별 분포 확인
- **누적 설명 분산**: 약 21.59%

#### 3D 시각화
- **PC1 + PC2 + PC3**: 세 번째 성분 추가
- **더 명확한 분리**: 클래스 간 경계 개선
- **누적 설명 분산**: 약 30.04%

### PCA의 장단점

#### 장점
- **차원 축소**: 저장 공간 절약, 계산 속도 향상
- **노이즈 제거**: 중요하지 않은 특성 제거
- **시각화**: 고차원 데이터를 2D/3D로 표현
- **다중공선성 해결**: 상관관계 높은 특성들 처리
- **과적합 방지**: 특성 수 감소로 일반화 성능 향상

#### 단점
- **해석 어려움**: 새로운 특성(주성분)의 의미 파악 어려움
- **정보 손실**: 일부 분산 정보 손실
- **선형 변환 한계**: 비선형 관계 포착 제한
- **스케일링 필수**: 사전 데이터 표준화 필요

---

## 3. K-Fold 교차검증

### 교차검증의 목적
- **과대적합 방지**: 모델이 특정 데이터에만 잘 맞는 것을 방지
- **일반화 성능 향상**: 다양한 데이터에 대해 모델 성능 평가
- **안정적인 성능 측정**: 여러 번 검증하여 평균적인 성능 측정

### 교차검증 방법들

#### 1. K-Fold 교차검증
```python
from sklearn.model_selection import KFold

kfold = KFold(n_splits=5, shuffle=False)
```
- 데이터를 K개 그룹으로 나누어 검증
- 각 그룹을 한 번씩 테스트셋으로 사용
- **클래스 분포를 고려하지 않음**

#### 2. Stratified K-Fold
```python
from sklearn.model_selection import StratifiedKFold

stratified_kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
```
- 클래스 분포를 고려한 K-Fold
- 각 폴드에서 클래스 비율을 균등하게 유지
- **분류 문제에서 권장**

#### 3. cross_val_score 함수
```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, y, scoring="accuracy", cv=5)
```
- **한 줄로 교차검증 수행**: 복잡한 반복문 없이 간단하게 처리
- **다양한 평가 지표**: accuracy, precision, recall, f1 등
- **자동 평균 계산**: 각 폴드의 결과를 자동으로 평균

### K-Fold 동작 원리 (K=5 예시)
```
전체 데이터: [1] [2] [3] [4] [5]

1회: 훈련셋[1,2,3,4] → 테스트셋[5]
2회: 훈련셋[2,3,4,5] → 테스트셋[1]  
3회: 훈련셋[3,4,5,1] → 테스트셋[2]
4회: 훈련셋[4,5,1,2] → 테스트셋[3]
5회: 훈련셋[5,1,2,3] → 테스트셋[4]

최종 성능: 5회 점수의 평균
```

### 실습 결과 비교

#### Iris 데이터셋 성능 (의사결정나무)
| 방법 | 평균 정확도 | 표준편차 | 최고 정확도 | 최저 정확도 |
|------|-------------|----------|-------------|-------------|
| K-Fold | 0.9133 | 0.0833 | 1.0 | 0.8 |
| Stratified K-Fold | 0.9533 | 0.0340 | 1.0 | 0.9 |
| cross_val_score | 0.9533 | 0.0340 | 1.0 | 0.9 |

#### 다양한 모델 성능 비교
| 모델 | 평균 정확도 | 표준편차 |
|------|-------------|----------|
| Decision Tree | 0.9533 | 0.0340 |
| Random Forest | 0.9667 | 0.0211 |
| SVM | 0.9667 | 0.0211 |
| K-NN | 0.9733 | 0.0249 |

### K-Fold vs Stratified K-Fold 차이점

#### 일반 K-Fold 문제점
- **클래스 분포 불균등**: 순서대로 분할하여 특정 폴드에 특정 클래스만 포함
- **성능 변동 큰**: 표준편차 0.0833으로 불안정
- **편향된 평가**: 일부 폴드에서 극단적인 결과

#### Stratified K-Fold 장점
- **클래스 분포 균등**: 각 폴드에서 클래스 비율을 원본과 동일하게 유지
- **안정적 성능**: 표준편차 0.0340으로 일관된 결과
- **공정한 평가**: 모든 폴드에서 균등한 조건

---

## 4. 성능 비교 및 분석

### 비지도학습 vs 지도학습 성능

#### PCA 차원축소 효과
- **차원 축소율**: 64차원 → 10차원 (84% 축소)
- **성능 유지**: 테스트 정확도 97.33% → 89.33% (약 8% 감소)
- **효율성 개선**: 학습 속도 향상, 메모리 사용량 감소

#### 교차검증 안정성
- **Stratified K-Fold**: 가장 안정적이고 신뢰할 수 있는 결과
- **표준편차 개선**: 0.0833 → 0.0340 (약 59% 향상)
- **실무 권장**: 분류 문제에서 필수적으로 사용

### 모델별 특성 분석

#### 앙상블 모델 우수성
- **Random Forest**: 다수의 결정나무로 안정적 성능
- **SVM**: 복잡한 결정 경계 학습 가능
- **K-NN**: 단순하지만 효과적인 지역적 패턴 학습

#### 단일 모델 한계
- **Decision Tree**: 과적합 위험, 불안정한 성능
- **개선 방안**: 앙상블 기법 적용, 정규화 적용

---

## 5. 실무 적용 가이드

### 군집분석 활용 가이드

#### 적용 분야
- **고객 세분화**: 마케팅 전략 수립
- **이미지 세그멘테이션**: 컴퓨터 비전
- **유전자 분석**: 바이오인포매틱스
- **시장 분석**: 경쟁 그룹 식별

#### 주의사항
```python
# 1. 스케일링 필수
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 2. 적절한 K값 선택
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3, random_state=42)

# 3. 결과 검증
from sklearn.metrics import silhouette_score
score = silhouette_score(X_scaled, labels)
```

### PCA 적용 가이드

#### 사용 시점
1. **고차원 데이터**: 특성 수가 샘플 수보다 많을 때
2. **상관관계 높음**: 다중공선성 문제 발생 시
3. **시각화 필요**: 고차원 데이터를 2D/3D로 표현
4. **계산 효율성**: 학습 시간 단축 필요 시

#### 실무 템플릿
```python
# 1. 데이터 표준화
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 2. PCA 적용
pca = PCA(n_components=0.95)  # 95% 분산 유지
X_pca = pca.fit_transform(X_scaled)

# 3. 결과 확인
print(f"원본 차원: {X.shape[1]}")
print(f"축소 차원: {X_pca.shape[1]}")
print(f"설명 분산: {pca.explained_variance_ratio_.sum():.2%}")
```

### 교차검증 적용 가이드

#### 상황별 교차검증 선택
```python
# 분류 문제 (클래스 불균형 고려)
from sklearn.model_selection import StratifiedKFold
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# 회귀 문제 (연속값 예측)
from sklearn.model_selection import KFold
cv = KFold(n_splits=5, shuffle=True, random_state=42)

# 시계열 데이터
from sklearn.model_selection import TimeSeriesSplit
cv = TimeSeriesSplit(n_splits=5)

# 그룹 데이터
from sklearn.model_selection import GroupKFold
cv = GroupKFold(n_splits=5)
```

#### 적절한 K값 선택
- **K=5 또는 K=10**: 일반적으로 권장
- **작은 데이터셋**: K=5 또는 Leave-One-Out
- **큰 데이터셋**: K=3 또는 Hold-out 검증

### 종합 워크플로우

#### 1단계: 탐색적 데이터 분석
```python
# 데이터 기본 정보
print(f"데이터 크기: {X.shape}")
print(f"결측치: {pd.DataFrame(X).isnull().sum().sum()}")

# 상관관계 분석 (PCA 필요성 판단)
corr_matrix = pd.DataFrame(X).corr()
high_corr = (corr_matrix.abs() > 0.8).sum().sum()
```

#### 2단계: 전처리 및 차원축소
```python
# 스케일링
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# PCA (필요시)
if X.shape[1] > 50:  # 고차원인 경우
    pca = PCA(n_components=0.95)
    X_final = pca.fit_transform(X_scaled)
else:
    X_final = X_scaled
```

#### 3단계: 모델 평가
```python
# 교차검증을 통한 모델 비교
models = {
    'RandomForest': RandomForestClassifier(random_state=42),
    'SVM': SVC(random_state=42),
    'KNN': KNeighborsClassifier()
}

for name, model in models.items():
    scores = cross_val_score(model, X_final, y, cv=5, scoring='accuracy')
    print(f"{name}: {scores.mean():.4f} (±{scores.std():.4f})")
```

### 핵심 권장사항

1. **항상 Stratified K-Fold 사용** (분류 문제)
2. **PCA 전 반드시 스케일링 적용**
3. **군집 개수는 도메인 지식과 통계적 방법 병행**
4. **교차검증으로 모델 선택 및 성능 평가**
5. **재현 가능한 결과를 위해 random_state 설정**

### 주의사항

1. **데이터 누수 방지**: 테스트 데이터로 전처리하지 않기
2. **과적합 모니터링**: 훈련-검증 성능 차이 확인
3. **계산 비용 고려**: 대용량 데이터에서는 샘플링 고려
4. **해석 가능성**: PCA 후 특성 의미 파악 어려움 인지

### 결론

**0710 실습을 통해 학습한 세 가지 핵심 기법**:
- **군집분석**: 패턴 발견을 위한 비지도학습
- **주성분분석**: 효율적인 차원축소와 시각화
- **교차검증**: 신뢰할 수 있는 모델 평가

이 기법들은 실무에서 **데이터 전처리, 탐색적 분석, 모델 검증**에 필수적으로 사용되는 도구들입니다.
