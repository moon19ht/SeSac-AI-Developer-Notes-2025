# 머신러닝 모델 성능(적중률) 향상을 위한 실전 절차 및 예제

---

이 문서는 머신러닝 프로젝트에서 모델의 성능(적중률 등)을 높이기 위한 전체 실무 절차와 핵심 예제, 실전 팁을 체계적으로 정리한 자료입니다. 데이터 분석, 모델 개발, 실무 적용까지 단계별로 참고할 수 있습니다.

## 목차

1. [문제 정의 및 목표 설정](#1-문제-정의-및-목표-설정)
2. [데이터 수집 및 이해 (EDA)](#2-데이터-수집-및-이해-eda)
3. [데이터 전처리](#3-데이터-전처리)
4. [특징 공학 (Feature Engineering)](#4-특징-공학-feature-engineering)
5. [모델 선택 및 학습](#5-모델-선택-및-학습)
6. [하이퍼파라미터 튜닝](#6-하이퍼파라미터-튜닝)
7. [모델 평가](#7-모델-평가)
8. [앙상블 (선택 사항)](#8-앙상블-선택-사항)
9. [모델 배포 및 모니터링](#9-모델-배포-및-모니터링)
10. [차원 축소(Dimensionality Reduction) 실전 예제](#10-차원-축소dimensionality-reduction-실전-예제)
11. [실전 요약 및 TIP](#11-실전-요약-및-tip)

---

## 1. 문제 정의 및 목표 설정
- **무엇을 예측/분류할 것인가?** (예: 고객 이탈, 이미지 분류, 가격 예측 등)
- **성능 지표 선정:** Accuracy, Precision, Recall, F1, ROC AUC, RMSE, MAE 등. 불균형 데이터에서는 Accuracy만으로 판단하지 않음.
- **비즈니스 가치:** 모델 성능 향상이 실제로 어떤 가치를 주는지 명확히 이해

---

## 2. 데이터 수집 및 이해 (EDA)
- **관련 데이터 최대한 수집:** 내부/외부 데이터 모두 고려
- **탐색적 데이터 분석(EDA):**
    - 분포, 통계량, 고유값, 상관관계, 이상치, 결측치, 불균형 여부 등 시각화
    - 도메인 지식 활용

---

## 3. 데이터 전처리
- **결측치 처리:** 삭제, 평균/중앙값/최빈값 대체, 예측 모델 등
- **이상치 처리:** 박스플롯, Z-score 등으로 탐지 후 제거/대체/변환
- **범주형 인코딩:**
    - 순서 없음: One-Hot Encoding
    - 순서 있음: Label Encoding/순서 매핑
- **스케일링:**
    - 정규화(Min-Max), 표준화(StandardScaler)
    - Gradient Descent 기반 모델에서 필수
- **노이즈 제거:** 오타, 중복 등 정리

#### TIP
- 전처리 단계에서 데이터 품질이 모델 성능에 큰 영향을 미칩니다.
- 파이프라인(sklearn의 Pipeline 등)으로 전처리 과정을 자동화하면 실무에 유리합니다.

---

## 4. 특징 공학 (Feature Engineering)
- **새로운 특징 생성:** 날짜/시간 파생, 컬럼 조합, 비율 등
- **차원 축소:** PCA, t-SNE, ICA 등 (과적합 방지, 시각화, 학습 효율)
- **특징 선택:** 중요 변수만 남기기 (필터, 래퍼, 임베디드 방법)

#### TIP
- 도메인 지식이 반영된 파생변수 생성이 성능 향상에 매우 효과적입니다.
- 차원 축소는 시각화, 과적합 방지, 연산 효율에 모두 유리합니다.

---

## 5. 모델 선택 및 학습
- **다양한 알고리즘 시도:** 선형/비선형, 트리, SVM, 신경망 등
- **데이터 분할:**
    - Train/Validation/Test
    - 교차 검증(K-Fold 등)으로 일반화 성능 신뢰도 향상

#### TIP
- 단일 모델에 집착하지 말고 여러 모델을 비교 실험하세요.
- 교차 검증은 데이터가 적을수록 더욱 중요합니다.

---

## 6. 하이퍼파라미터 튜닝
- **Grid Search:** 모든 조합 시도
- **Random Search:** 무작위 샘플링
- **Bayesian Optimization:** 이전 결과 기반 탐색
- **AutoML:** 자동화된 튜닝/특징 엔지니어링/모델 선택

#### TIP
- 하이퍼파라미터 튜닝은 모델 성능의 마지막 한 끗을 결정합니다.
- 실무에서는 Random Search, Optuna, AutoML 등 자동화 도구 활용이 많습니다.

---

## 7. 모델 평가
- **지표 사용:** Accuracy, Precision, Recall, F1, RMSE 등
- **과적합/과소적합 진단:**
    - 과적합: 학습 성능↑, 테스트 성능↓
    - 과소적합: 학습/테스트 모두 성능↓
    - 학습 곡선(Learning Curve)으로 진단

#### TIP
- 평가 지표는 문제 특성(불균형, 회귀/분류 등)에 따라 다르게 선택해야 합니다.
- 혼동행렬, ROC Curve, 학습곡선 등 시각화도 적극 활용하세요.

---

## 8. 앙상블 (선택 사항)
- **배깅(Bagging):** 여러 모델 병렬 학습 후 평균/투표 (랜덤포레스트 등)
- **부스팅(Boosting):** 순차적 학습, 이전 오류 보완 (XGBoost, LightGBM 등)
- **스태킹(Stacking):** 여러 모델 예측을 메타 모델에 입력

#### TIP
- 단일 모델로 성능 한계에 도달했다면 앙상블을 적극 고려하세요.
- 실무에서는 LightGBM, XGBoost, CatBoost 등 부스팅 계열이 많이 쓰입니다.

---

## 9. 모델 배포 및 모니터링
- **실제 환경 적용:** 학습/검증 완료 모델을 서비스에 배포
- **지속적 모니터링:** 데이터/개념 드리프트 감지, 성능 저하 시 재학습
- **피드백 루프:** 실제 데이터와 피드백을 수집해 개선

#### TIP
- 배포 후에도 모델 성능이 유지되는지 지속적으로 모니터링해야 합니다.
- 데이터/업무 환경 변화에 따라 주기적 재학습이 필요합니다.

---

## 10. 차원 축소(Dimensionality Reduction) 실전 예제

### 차원 축소란?
- 데이터셋의 특징(feature) 수를 줄이는 과정입니다.
- 특징이 너무 많으면 학습 시간이 길어지고, 과적합 위험이 증가하며, 시각화가 어려워집니다.
- 차원 축소는 핵심 정보를 보존하면서 효율적인 학습과 시각화를 돕습니다.

### 예제 1: 주성분 분석(PCA) - Iris 데이터셋

```python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# 1. 데이터 로드 및 준비
iris = load_iris()
X = iris.data
y = iris.target

# 2. 데이터 스케일링
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. PCA (4차원 -> 2차원)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# 4. 데이터프레임 생성
import numpy as np
df_pca = pd.DataFrame(data=X_pca, columns=['PC1', 'PC2'])
df_pca['target'] = y

# 5. 시각화
plt.figure(figsize=(8, 6))
for target, color in zip(np.unique(y), ['r', 'g', 'b']):
    indices = df_pca['target'] == target
    plt.scatter(df_pca.loc[indices, 'PC1'], df_pca.loc[indices, 'PC2'], c=color, s=50)
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('PCA of Iris Dataset')
plt.legend(iris.target_names)
plt.grid()
plt.show()

# 분산 비율 확인
print('설명된 분산 비율:', pca.explained_variance_ratio_)
print('총 분산:', sum(pca.explained_variance_ratio_))
```

#### TIP
- PCA는 스케일링 필수(StandardScaler 등)
- n_components로 축소 차원 지정
- explained_variance_ratio_로 정보 보존 정도 확인

---

### 예제 2: t-SNE - MNIST 숫자 데이터셋

```python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import time

# 1. 데이터 로드
digits = load_digits()
X = digits.data
y = digits.target

# 2. 스케일링
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. t-SNE (64차원 -> 2차원)
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000, random_state=42)
start = time.time()
X_tsne = tsne.fit_transform(X_scaled)
print(f"t-SNE 소요 시간: {time.time() - start:.2f}초")

# 4. 데이터프레임 생성
df_tsne = pd.DataFrame(data=X_tsne, columns=['tSNE1', 'tSNE2'])
df_tsne['target'] = y

# 5. 시각화
plt.figure(figsize=(10, 8))
colors = plt.cm.get_cmap('jet', 10)
for i in range(10):
    indices = df_tsne['target'] == i
    plt.scatter(df_tsne.loc[indices, 'tSNE1'], df_tsne.loc[indices, 'tSNE2'], color=colors(i), label=str(i), s=10, alpha=0.7)
plt.xlabel('t-SNE 1')
plt.ylabel('t-SNE 2')
plt.title('t-SNE of MNIST Digits')
plt.legend(title='Digit')
plt.grid(True)
plt.show()
```

#### TIP
- t-SNE는 비선형 구조 시각화에 강력, 계산 비용 높으므로 소규모/샘플 데이터에 적합
- perplexity, learning_rate 등 하이퍼파라미터 튜닝 필요

---

## 11. 실전 요약 및 TIP

| 단계 | 핵심 내용 |
|------|-----------------------------|
| 문제 정의 | 목표, 지표, 비즈니스 가치 명확화 |
| 데이터 수집/EDA | 분포, 이상치, 결측치, 불균형 등 탐색 |
| 전처리 | 결측/이상치, 인코딩, 스케일링, 노이즈 제거 |
| 특징 공학 | 파생변수, 차원축소, 변수선택 등 |
| 모델/학습 | 다양한 알고리즘, 데이터 분할, 교차검증 |
| 튜닝 | 하이퍼파라미터, AutoML 등 |
| 평가 | 지표, 과적합/과소적합 진단, 학습곡선 |
| 앙상블 | 배깅, 부스팅, 스태킹 등 |
| 배포/모니터링 | 실서비스 적용, 성능 모니터링, 피드백 |

---

> **TIP:** 각 단계별로 실무에서는 데이터 품질, 피처 엔지니어링, 하이퍼파라미터 튜닝, 배포 자동화 등에서 성능 차이가 크게 발생합니다. 반복적 실험과 분석, 도메인 전문가와의 협업이 중요합니다.