# 📊 Machine Learning 이론

##### 🗓️ 2025.07.03
##### 📝 Writer : Moon19ht

---

## 📚 목차

1. [누락 데이터 처리](#누락-데이터-처리)
2. [중복 데이터 처리](#중복-데이터-처리)
3. [데이터 정규화](#데이터-정규화)
4. [데이터 타입 변환](#데이터-타입-변환)
5. [구간 나누기](#구간-나누기)
6. [원핫 인코딩](#원핫-인코딩)
7. [실습 예제](#실습-예제)
8. [핵심 요약](#핵심-요약)

---

## 누락 데이터 처리

### 누락 데이터의 영향
머신러닝과 딥러닝에서 데이터 누락은 전체 예측 결과에 큰 영향을 미칩니다. 보다 예측력이 높고 신뢰성 있는 결과를 얻으려면 누락된 데이터에 대한 적절한 처리가 필요합니다.

### 누락 데이터 확인 함수

#### 1. isnull() 함수
데이터가 NaN이면 True, 아니면 False를 반환합니다.

```python
import pandas as pd
import numpy as np

# NaN은 numpy를 사용해 직접 입력 가능
s = pd.Series([1, 2, 3, 4, np.nan])
print(s.isnull())
```

#### 2. sum() 함수와 조합
isnull() 결과에 sum() 함수를 사용하면 NaN 값의 개수를 확인할 수 있습니다.

```python
print("NaN 값 개수:", s.isnull().sum())
```

### 누락 데이터 처리 방법

#### 1. 삭제 방법 (dropna)
```python
# 파일명: exam11_1.py
import pandas as pd

data = pd.read_csv("./data/data.csv")
print("컬럼명:", data.columns)
print("인덱스:", data.index)
print(data.info())

# 누락된 데이터 확인
print(data['height'].value_counts(dropna=False))
print(data['height'].isnull())    # NaN이면 True
print(data['height'].notnull())   # NaN이 아니면 True

# null 값 개수 확인
print("height 필드 NaN 개수:", data['height'].isnull().sum())

# 데이터 삭제
print("삭제 전 데이터 개수:", data.shape)
data = data.dropna(subset=['height'], how='any', axis=0)
print("삭제 후 데이터 개수:", data.shape)

# 인덱스 재설정
data = data.reset_index(drop=True)
print(data)
```

#### dropna 함수 주요 매개변수
- `subset`: 특정 필드들에서 NaN 값이 있는 행 삭제
- `how`: 
  - `'any'`: 하나라도 NaN이 있으면 삭제
  - `'all'`: 모두 NaN일 때만 삭제
- `axis`: 
  - `0`: 행 삭제
  - `1`: 열 삭제
- `thresh`: 지정된 개수만큼 NaN이 없는 행/열 삭제
- `inplace`: True로 설정하면 원본 데이터 수정

#### 2. 대체 방법 (fillna)
누락 데이터가 많아서 삭제 시 분석이 어려운 경우, 대체값을 사용하는 것이 더 나은 방법입니다.

```python
# 파일명: exam11_2.py
import pandas as pd

data = pd.read_csv("./data/data.csv")

# 누락 데이터 확인
print("height 필드 NaN 개수:", data['height'].isnull().sum())
print("weight 필드 NaN 개수:", data['weight'].isnull().sum())

# 평균값으로 대체
mean_height = data['height'].mean()
mean_weight = data['weight'].mean()

data['height'].fillna(mean_height, inplace=True)
data['weight'].fillna(mean_weight, inplace=True)

print("대체 후 height 필드 NaN 개수:", data['height'].isnull().sum())
print("대체 후 weight 필드 NaN 개수:", data['weight'].isnull().sum())
print(data)
```

#### 대체값 선택 기준
- **평균값**: 데이터가 정규분포를 따르는 경우
- **중간값**: 이상치가 많거나 편향된 분포를 가진 경우
- **최빈값**: 범주형 데이터의 경우

---

## 중복 데이터 처리

### 중복 데이터의 문제
- 분석 결과 왜곡
- 모델 성능 저하
- 처리 시간 증가

### 중복 데이터 확인 및 제거

```python
# 파일명: exam11_3.py
import pandas as pd

data = {
    'passenger_code': ['A101', 'A102', 'A103', 'A101', 'A104', 'A101', 'A103'],
    'target': ['광주', '서울', '부산', '광주', '대구', '광주', '부산'],
    'price': [25000, 27000, 45000, 25000, 35000, 27000, 45000]
}

df = pd.DataFrame(data)
print("원본 데이터:")
print(df)

# 중복 데이터 확인
print("\n중복 데이터 확인:")
duplicated_data = df['passenger_code'].duplicated()
print(duplicated_data)

# 전체 행이 중복인 경우 제거
print("\n전체 행 중복 제거:")
df2 = df.drop_duplicates()
print(df2)

# 특정 컬럼값이 중복인 경우 제거
print("\n특정 컬럼 중복 제거:")
df3 = df.drop_duplicates(subset=['passenger_code'])
print(df3)

# 두 개 컬럼 조합이 중복인 경우 제거
print("\n두 컬럼 조합 중복 제거:")
df4 = df.drop_duplicates(subset=['passenger_code', 'target'])
print(df4)
```

### 중복 처리 함수
- `duplicated()`: 중복 여부 확인 (첫 번째는 False, 나머지는 True)
- `drop_duplicates()`: 중복 행 제거
- `subset`: 특정 컬럼 기준으로 중복 제거

---

## 데이터 정규화

### 정규화의 필요성
머신러닝과 딥러닝에서 데이터의 단위나 범위가 크게 다를 경우 예측 성능에 영향을 미칩니다. 정규화를 통해 데이터를 같은 스케일로 조정할 수 있습니다.

### 정규화 공식
```
정규화 값 = (원본 값 - 최솟값) / (최댓값 - 최솟값)
```

### 정규화 및 단위 변환 예제

```python
# 파일명: exam11_4.py
import pandas as pd

data = pd.read_csv('./data/auto-mpg.csv')
print(data.info())
print(data.head())

# 컬럼명 변경
data.columns = ['mpg', 'cyl', 'disp', 'power', 'weight', 'acce', 'model']
print(data.head())

# 정규화 적용
data['mpg2'] = (data['mpg'] - data['mpg'].min()) / (data['mpg'].max() - data['mpg'].min())
print(data.head())

# 단위 환산 (MPG를 KPL로 변환)
mpg_unit = 1.60934 / 3.78541  # 마일을 km로, 갤런을 리터로
data['kpl'] = (data['mpg'] * mpg_unit).round(2)
print(data.head())
```

### 정규화 방법
1. **Min-Max 정규화**: 0~1 사이로 변환
2. **Z-score 정규화**: 평균 0, 표준편차 1로 변환
3. **Robust 정규화**: 중간값과 IQR 사용

---

## 데이터 타입 변환

### 타입 변환의 필요성
- 숫자형 데이터가 문자열로 저장된 경우
- 문자열 데이터를 범주형으로 변환해야 하는 경우
- 잘못된 데이터가 포함된 경우

### 타입 변환 예제

```python
# 파일명: exam11_5.py
import pandas as pd
import numpy as np

data = pd.read_csv('./data/auto-mpg.csv')
data.columns = ['mpg', 'cyl', 'disp', 'power', 'weight', 'acce', 'model']

print("데이터 타입 확인:")
print(data.dtypes)
print("고유값 확인:")
print(data['disp'].unique())

# 잘못된 데이터를 NaN으로 변환
data['disp'].replace('?', np.nan, inplace=True)
print("잘못된 데이터 변환 후:")
print(data.head())

# NaN 포함 행 삭제
data.dropna(subset=['disp'], axis=0, inplace=True)

# 타입 변환
print("변환 전 타입:")
print(data.dtypes)

data['disp'] = data['disp'].astype('float')
data['model'] = data['model'].astype('category')

print("변환 후 타입:")
print(data.dtypes)
```

### 주요 타입 변환 함수
- `astype()`: 데이터 타입 변환
- `replace()`: 특정 값을 다른 값으로 대체
- `'category'`: 범주형 데이터로 변환

---

## 구간 나누기

### 구간 나누기의 필요성
연속적 데이터를 불연속 데이터로 변환해야 할 때 사용합니다:
- 등급 시스템 구축
- 범주별 분석
- 복잡한 연속 데이터 단순화

### 구간 나누기 예제

```python
# 파일명: exam11_6.py
import pandas as pd
import numpy as np

data = pd.read_csv('./data/auto-mpg.csv')
data.columns = ['mpg', 'cyl', 'disp', 'power', 'weight', 'acce', 'model']

# 데이터 전처리
data['disp'].replace('?', np.nan, inplace=True)
data.dropna(subset=['disp'], axis=0, inplace=True)
data['disp'] = data['disp'].astype('float')
data['model'] = data['model'].astype('category')

# power 필드 누락 데이터 처리
print("power 필드 NaN 개수:", data['power'].isnull().sum())
data.dropna(subset=['power'], inplace=True)

# 구간 나누기
count, bin_dividers = np.histogram(data['power'], bins=4)
print("구간 경계값:", bin_dividers)

bin_names = ["D", "C", "B", "A"]
data["grade"] = pd.cut(x=data['power'], 
                       bins=bin_dividers,
                       labels=bin_names, 
                       include_lowest=True)

print("구간 나누기 결과:")
print(data[['power', 'grade']].head(10))
```

### 구간 나누기 함수
- `np.histogram()`: 구간 경계값 계산
- `pd.cut()`: 연속 데이터를 구간으로 나누기
- `include_lowest=True`: 최솟값 포함
- `bins`: 구간 개수 또는 경계값 배열
- `labels`: 각 구간에 붙일 라벨명

---

## 원핫 인코딩

### 원핫 인코딩의 필요성
머신러닝과 딥러닝은 수치 데이터만 처리할 수 있습니다. 범주형 데이터를 수치형으로 변환하기 위해 원핫 인코딩을 사용합니다.

### 원핫 인코딩 개념
4개의 카테고리 A, B, C, D가 있을 때:
- A: [1, 0, 0, 0]
- B: [0, 1, 0, 0]
- C: [0, 0, 1, 0]
- D: [0, 0, 0, 1]

### 원핫 인코딩 구현

```python
# 파일명: exam11_7.py
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

# 이전 예제에서 구간 나누기 완료된 데이터 사용
data = pd.read_csv('./data/auto-mpg.csv')
data.columns = ['mpg', 'cyl', 'disp', 'power', 'weight', 'acce', 'model']

# 데이터 전처리 (이전 단계들)
data['disp'].replace('?', np.nan, inplace=True)
data.dropna(subset=['disp'], axis=0, inplace=True)
data['disp'] = data['disp'].astype('float')
data.dropna(subset=['power'], inplace=True)

# 구간 나누기
count, bin_dividers = np.histogram(data['power'], bins=4)
bin_names = ["D", "C", "B", "A"]
data["grade"] = pd.cut(x=data['power'], 
                       bins=bin_dividers,
                       labels=bin_names, 
                       include_lowest=True)

# 원핫 인코딩
Y_class = np.array(data['grade']).reshape(-1, 1)
enc = OneHotEncoder()
enc.fit(Y_class)
Y_class_onehot = enc.transform(Y_class).toarray()

print("원핫 인코딩 결과:")
print(Y_class_onehot[:10])

# 원핫 인코딩 복원
Y_class_recovery = np.argmax(Y_class_onehot, axis=1).reshape(-1, 1)
print("복원된 인덱스:")
print(Y_class_recovery[:10])
```

### 원핫 인코딩 과정
1. **reshape(-1, 1)**: 1차원 배열을 2차원으로 변환
2. **OneHotEncoder()**: 인코더 객체 생성
3. **fit()**: 인코더 훈련
4. **transform()**: 원핫 인코딩 수행
5. **toarray()**: 희소 행렬을 밀집 행렬로 변환

### 원핫 인코딩 복원
- `np.argmax()`: 가장 큰 값의 인덱스 반환
- `axis=1`: 행 방향으로 최댓값 찾기

---

## 실습 예제

### 과제: Iris 데이터셋 종합 처리
`data/iris.csv` 파일을 사용하여 다음 작업을 수행하세요:

1. 누락된 데이터 확인 및 평균값으로 대체
2. sepal.length, sepal.width, petal.width 필드 정규화
3. petal.length 필드를 3개 구간으로 나누어 A, B, C 등급 부여
4. 등급을 원핫 인코딩으로 변환

### 해답

```python
# 파일명: homework11.py
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

# 1. 데이터 로드 및 누락 데이터 확인
data = pd.read_csv('./data/iris.csv')
print("=== 1. 누락 데이터 확인 ===")
print(data.isnull().sum())

# 2. 누락 데이터 평균값으로 대체
print("\n=== 2. 누락 데이터 대체 ===")
mean_values = {
    'sepal.length': data['sepal.length'].mean(),
    'sepal.width': data['sepal.width'].mean(),
    'petal.length': data['petal.length'].mean(),
    'petal.width': data['petal.width'].mean()
}

for column, mean_value in mean_values.items():
    data[column].fillna(mean_value, inplace=True)

print("대체 후 누락 데이터 확인:")
print(data.isnull().sum())

# 3. 정규화 함수 정의 및 적용
def normalize(column_name):
    max_val = data[column_name].max()
    min_val = data[column_name].min()
    return (data[column_name] - min_val) / (max_val - min_val)

print("\n=== 3. 정규화 적용 ===")
data['sepal.length'] = normalize('sepal.length')
data['sepal.width'] = normalize('sepal.width')
data['petal.width'] = normalize('petal.width')
print("정규화 완료")
print(data.head())

# 4. 구간 나누기
print("\n=== 4. 구간 나누기 ===")
count, bin_dividers = np.histogram(data['petal.length'], bins=3)
print("구간 경계값:", bin_dividers)

bin_names = ["A", "B", "C"]
data["petal_grade"] = pd.cut(x=data['petal.length'], 
                             bins=bin_dividers,
                             labels=bin_names, 
                             include_lowest=True)

print("구간 나누기 결과:")
print(data[['petal.length', 'petal_grade']].head())

# 5. 원핫 인코딩
print("\n=== 5. 원핫 인코딩 ===")
Y_class = np.array(data['petal_grade']).reshape(-1, 1)
enc = OneHotEncoder()
enc.fit(Y_class)
Y_class_onehot = enc.transform(Y_class).toarray()

print("원핫 인코딩 결과 (처음 10개):")
print(Y_class_onehot[:10])

# 인코딩 복원
Y_class_recovery = np.argmax(Y_class_onehot, axis=1).reshape(-1, 1)
print("\n복원된 인덱스 (처음 10개):")
print(Y_class_recovery[:10])
```

---

## 핵심 요약

### 데이터 누락치 처리 절차
1. **확인**: `isnull()` 함수로 누락 데이터 확인
2. **개수 파악**: `isnull().sum()`으로 누락 데이터 개수 확인
3. **처리 방법 선택**:
   - 누락 건수가 적을 경우: `dropna()`로 삭제
   - 누락 건수가 많을 경우: `fillna()`로 대체 (평균값, 중간값 등)

### 중복 데이터 처리
- `duplicated()`: 중복 여부 확인
- `drop_duplicates()`: 중복 행 제거
- `subset` 매개변수로 특정 컬럼 기준 중복 제거 가능

### 데이터 변환 기법
1. **정규화**: 데이터 스케일 통일
   - Min-Max 정규화: `(x - min) / (max - min)`
   - Z-score 정규화: `(x - mean) / std`

2. **타입 변환**: `astype()` 함수 사용
   - 숫자형: `'int'`, `'float'`
   - 범주형: `'category'`

3. **구간 나누기**: 연속형 → 범주형 변환
   - `np.histogram()`: 구간 경계값 계산
   - `pd.cut()`: 구간 나누기 실행

4. **원핫 인코딩**: 범주형 → 수치형 변환
   - `OneHotEncoder`: sklearn 라이브러리 사용
   - `reshape(-1, 1)`: 1차원 → 2차원 변환 필요

### 데이터 타입 분류
- **연속형**: 평균값이 중요, 수치적 연산 가능
- **범주형(불연속형)**: 개수가 중요, 원핫 인코딩 필요

### 주요 주의사항
- 문자열 데이터는 반드시 범주형으로 변환 후 사용
- 원핫 인코딩 시 데이터 차원 확인
- 정규화는 알고리즘 특성에 따라 선택적 적용
- 누락 데이터 처리 시 데이터 분포 고려

이러한 데이터 전처리 과정은 머신러닝과 딥러닝 모델의 성능을 크게 좌우하는 핵심 단계입니다.


