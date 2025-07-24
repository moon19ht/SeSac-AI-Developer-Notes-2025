# 📊 Machine Learning 이론

##### 🗓️ 2025.07.02
##### 📝 Writer : Moon19ht

---

## 📚 목차

1. [DataFrame 심화](#dataframe-심화)
2. [외부 파일 읽기/쓰기](#외부-파일-읽기쓰기)
3. [파일 경로 처리](#파일-경로-처리)
4. [CSV 파일 처리](#csv-파일-처리)
5. [Excel 파일 처리](#excel-파일-처리)
6. [DataFrame API 활용](#dataframe-api-활용)
7. [조건부 데이터 검색](#조건부-데이터-검색)
8. [통계 함수 활용](#통계-함수-활용)
9. [실습 예제](#실습-예제)
10. [핵심 요약](#핵심-요약)

---

## DataFrame 심화

### DataFrame의 특징
- 판다스가 제공하는 2차원 배열 형태의 데이터 타입
- 하나의 타입으로만 구성되지 않고, 각 열이 각기 다른 타입으로 구성 가능
- 별도의 구조체나 클래스를 만들지 않고도 사용자 데이터를 취급하기 쉬운 객체
- 많은 통계 관련 함수들을 제공
- 각 열과 행에 대해 자유롭게 접근 가능

### 판다스가 지원하는 파일 형식
- **CSV**: 쉼표로 구분된 값 (Comma-Separated Values)
- **Excel**: Microsoft Excel 파일 (.xlsx, .xls)
- **JSON**: JavaScript Object Notation
- **XML**: eXtensible Markup Language
- **HTML**: HyperText Markup Language
- **SQL**: 데이터베이스 연결
- **기타**: TSV, 고정폭 파일 등

---

## 외부 파일 읽기/쓰기

### 외부 파일 처리의 중요성
- 실제 데이터 분석에서는 외부에서 제공되는 데이터를 활용
- 다양한 소스에서 수집된 데이터를 효율적으로 처리
- 분석 결과를 다른 시스템에서 활용할 수 있도록 저장

---

## 파일 경로 처리

### 경로 표현 방식

#### 1. 절대 경로
- 루트(/) 또는 드라이브(C:)부터 모든 경로를 기술
- 예: `C:/pandas_workspace/uni_10/data/score.csv`

#### 2. 상대 경로
- 현재 애플리케이션이 실행 중인 폴더를 기준으로 경로 배정
- `.` (도트): 현재 폴더
- `..` (도트 두 개): 상위 폴더
- 예: `./data/score.csv`

### 파이썬에서의 경로 처리 주의사항

#### 역슬래시(\) 문제 해결 방법
1. **이스케이프 문자 사용**: `c:\\pandas_workspace\\data\\score.csv`
2. **원시 문자열 사용**: `r"c:\pandas_workspace\data\score.csv"`
3. **슬래시 사용**: `c:/pandas_workspace/data/score.csv` (권장)

#### 경로 선택 권장사항
- 절대 경로보다는 상대 경로 사용을 권장
- 폴더 이동 시 경로 수정 필요 없음
- 프로젝트 이식성 향상

---

## CSV 파일 처리

### CSV 파일의 특징
- 데이터를 쉼표(,)로 구분하는 텍스트 파일
- 특정 프로그램 없이 일반 에디터로 작성 가능
- Excel에서도 편집 가능
- 빅데이터에서 가장 많이 사용하는 데이터 저장 형태

### CSV 파일 읽기

#### 기본 읽기
```python
import pandas as pd
data = pd.read_csv("./data/score.csv")
```

#### 주요 옵션
- `header`: 제목 줄 설정
  - `None`: 제목 줄이 없음
  - `3`: 4번째 줄이 제목 줄
- `encoding`: 문자 인코딩 설정
- `sep`: 구분자 설정 (기본값: 쉼표)

### CSV 파일 읽기 예제

#### 1. 기본 CSV 파일 읽기
```python
# 파일명: exam10_1.py
import pandas as pd

data = pd.read_csv("./data/score.csv")
print("컬럼명:", data.columns)
print("인덱스:", data.index)

# 총점, 평균 구하기
data['total'] = data['kor'] + data['eng'] + data['mat']
data['avg'] = data['total'] / 3
print(data)
```

#### 2. 제목 줄이 없는 CSV 파일 처리
```python
# 파일명: exam10_2.py
import pandas as pd

# 제목 줄이 없을 경우 header=None
data = pd.read_csv("./data/score_noheader.csv", header=None)
print("컬럼명:", data.columns)

# 직접 컬럼명 부여
data.columns = ['name', 'kor', 'eng', 'mat']
print("컬럼 부여 후:", data.columns)
print(data)

# 총점, 평균 구하기
data['total'] = data['kor'] + data['eng'] + data['mat']
data['avg'] = data['total'] / 3
print(data)
```

#### 3. 제목 줄이 특정 위치에 있는 경우
```python
# 파일명: exam10_3.py
import pandas as pd

# header가 4번째 줄에 있음 (인덱스 3)
data = pd.read_csv("./data/score_header.csv", header=3)
print("컬럼명:", data.columns)
print("인덱스:", data.index)

# 총점, 평균 구하기
data['total'] = data['kor'] + data['eng'] + data['mat']
data['avg'] = data['total'] / 3
print(data)

# CSV 파일로 저장
# Excel에서 열어보려면 cp949 인코딩 필요
# index=False로 인덱스 저장 안 함
data.to_csv("score_result.csv", mode='w', encoding="cp949", index=False)
```

---

## Excel 파일 처리

### Excel 파일의 장점
- 별도의 COM 라이브러리나 다른 라이브러리 설치 불필요
- 판다스에서 직접 지원
- 복잡한 데이터 구조 처리 가능

### Excel 파일 읽기/쓰기 예제
```python
# 파일명: exam10_4.py
import pandas as pd

# Excel 파일 읽기
data = pd.read_excel("./data/score.xlsx")
data['total'] = data['kor'] + data['eng'] + data['mat']
data['avg'] = data['total'] / 3
print(data)

# Excel 파일로 저장
data.to_excel("score_result1.xlsx")           # 인덱스 포함
data.to_excel("score_result2.xlsx", index=False)  # 인덱스 제외
```

### Excel 저장 시 옵션
- `index=False`: 인덱스 필드 출력 안 함
- `index=True` (기본값): 인덱스 필드도 함께 출력

---

## DataFrame API 활용

### 기본 정보 확인 API

#### 1. head() / tail()
```python
# 파일명: exam10_5.py
import pandas as pd

data = pd.read_csv("./data/auto-mpg.csv")

print("앞에서부터 5개 미리 보기")
print(data.head())

print("뒤에서부터 5개 미리 보기")
print(data.tail())

print("앞에서부터 10개 미리 보기")
print(data.head(10))
```

#### 2. shape
```python
print(data.shape)  # 데이터프레임의 차원 (행, 열)
row, col = data.shape
print("행의 개수:", row)
print("열의 개수:", col)
```

#### 3. info()
```python
# 파일명: exam10_6.py
import pandas as pd

data = pd.read_csv("./data/auto-mpg.csv")
print("데이터의 기본 구조")
print(data.info())
```

**info() 함수 제공 정보:**
- 데이터 타입
- 각 컬럼별 데이터 개수
- 메모리 사용량
- 인덱스 정보

#### 4. describe()
```python
print("데이터의 요약 정보 확인")
print(data.describe())
```

**describe() 함수 제공 정보:**
- count: 데이터 개수
- mean: 평균값
- std: 표준편차
- min: 최솟값
- 25%, 50%, 75%: 사분위수
- max: 최댓값

---

## 조건부 데이터 검색

### 기본 조건 검색
```python
# 파일명: exam10_7.py
import pandas as pd

data = pd.read_csv("./data/auto-mpg.csv")

# 단일 조건 검색
print("실린더 개수가 4개인 데이터")
print(data[data.cylinders == 4])

print("연비가 27 이상인 데이터")
print(data[data.mpg >= 27])

print("모델 연도가 70년인 데이터")
print(data[data['model-year'] == 70])
```

### 복합 조건 검색

#### 주의사항
- 파이썬의 `and`, `or` 연산자는 사용 불가
- numpy의 논리 함수를 사용해야 함

#### numpy 논리 함수 사용
```python
import numpy as np

# 두 가지 조건을 동시에 만족하는 데이터
print("모델 연도가 70년이고 연비가 25 이상인 데이터")
print(data[np.logical_and(data['model-year'] == 70, data['mpg'] >= 25)])

# 두 가지 조건 중 하나라도 만족하는 데이터
print("모델 연도가 70년이거나 연비가 30 이상인 데이터")
print(data[np.logical_or(data['model-year'] == 70, data['mpg'] >= 30)])
```

#### 오류 예시
```python
# 이렇게 사용하면 에러 발생
# data[data['model-year']==70 and data['mpg']>=25]
# ValueError: The truth value of a Series is ambiguous.
```

---

## 통계 함수 활용

### DataFrame의 통계 함수들
DataFrame의 각 열은 Series 타입으로, 다양한 통계 함수를 제공합니다.

#### 기본 통계 함수
- `mean()`: 평균값
- `max()`: 최댓값
- `min()`: 최솟값
- `median()`: 중간값
- `std()`: 표준편차
- `var()`: 분산
- `quantile()`: 사분위수
- `value_counts()`: 고유값 개수

### 통계 함수 활용 예제
```python
# 파일명: exam10_8.py
import pandas as pd

data = pd.read_csv("./data/auto-mpg.csv")

# 각 데이터별 고유 개수
print("모델 연도별 개수")
print(data['model-year'].value_counts())

# 기본 통계량
print("연비 평균:", data['mpg'].mean())
print("연비 최댓값:", data['mpg'].max())
print("연비 최솟값:", data['mpg'].min())
print("연비 중간값:", data['mpg'].median())
print("연비 분산:", data['mpg'].var())
print("연비 표준편차:", data['mpg'].std())

# 사분위수
print("1사분위수:", data['mpg'].quantile(0.25))
print("2사분위수:", data['mpg'].quantile(0.5))
print("3사분위수:", data['mpg'].quantile(0.75))
```

### 통계 개념 설명

#### 표준편차 (Standard Deviation)
- 집단의 성격을 알아내기 위해 사용
- 값이 클수록 데이터가 평균에서 멀리 분포
- 값이 작을수록 데이터가 평균 주변에 모여 있음

#### 분산 (Variance)
- 집단 내 값의 흩어짐 정도를 나타내는 척도
- 표준편차의 제곱

#### 사분위수 (Quantile)
- 데이터를 크기 순으로 정렬했을 때의 위치값
- 1사분위수(25%), 2사분위수(50%, 중간값), 3사분위수(75%)

#### 중간값 (Median)
- 데이터를 크기 순으로 정렬했을 때 중간에 위치한 값
- 평균값과 달리 극값의 영향을 받지 않음

---

## 실습 예제

### 과제: Iris 데이터셋 분석
`data/iris.csv` 파일을 읽어서 다음 작업을 수행하세요.

#### 문제
1. iris 데이터셋의 필드 개수와 각 필드의 타입 확인
2. 맨 앞의 데이터 7개 출력
3. iris 데이터셋의 통계량 확인
4. variety가 'Setosa'인 데이터의 통계량 출력
5. 각 variety별 sepal.length 값의 평균값 출력
6. 꽃의 종류가 'Setosa'이면서 sepal.length가 5cm 이상인 데이터 개수 출력

#### 해답
```python
# 파일명: homework10.py
import pandas as pd
import numpy as np

# 데이터 로드
data = pd.read_csv("./data/iris.csv")

# 1) 필드 정보 확인
print("=== 1. 데이터셋 필드 정보 ===")
print(data.info())

# 2) 앞의 7개 데이터 출력
print("\n=== 2. 앞의 7개 데이터 ===")
print(data.head(7))

# 3) 통계량 요약 정보
print("\n=== 3. 통계량 요약 ===")
print(data.describe())

# 4) variety가 'Setosa'인 데이터의 통계량
print("\n=== 4. Setosa 데이터 통계량 ===")
setosa_data = data[data['variety'] == 'Setosa']
print(setosa_data.describe())

# 5) 각 variety별 sepal.length 평균
print("\n=== 5. 각 variety별 sepal.length 평균 ===")
setosa_avg = data[data['variety'] == 'Setosa']['sepal.length'].mean()
print(f"Setosa 평균: {setosa_avg}")

versicolor_avg = data[data['variety'] == 'Versicolor']['sepal.length'].mean()
print(f"Versicolor 평균: {versicolor_avg}")

virginica_avg = data[data['variety'] == 'Virginica']['sepal.length'].mean()
print(f"Virginica 평균: {virginica_avg}")

# 6) Setosa이면서 sepal.length >= 5인 데이터 개수
print("\n=== 6. Setosa이면서 sepal.length >= 5인 데이터 ===")
condition_data = data[np.logical_and(data['variety'] == 'Setosa', 
                                   data['sepal.length'] >= 5)]
print(f"조건을 만족하는 데이터 개수: {len(condition_data)}")
print(condition_data)
```

---

## 핵심 요약

### DataFrame
- 판다스에서 제공하는 데이터 구조 중 가장 많이 사용
- CSV, Excel, JSON 등 다양한 파일 형식을 DataFrame 객체로 직접 변환 가능
- for문을 사용하지 않고도 조건식으로 데이터에 접근 가능
- 복합 조건 사용 시 파이썬의 논리 연산자 대신 numpy의 논리 함수 사용 필요

### 주요 DataFrame API

#### 데이터 탐색
- `head()`: 앞에서부터 기본 5개 데이터 출력
- `tail()`: 뒤에서부터 기본 5개 데이터 출력
- `info()`: 각 필드의 종류, 데이터 타입, 데이터 개수 등의 정보 출력
- `describe()`: 기본 통계값(max, min, mean, quantile, std 등) 출력

#### 파일 입출력
- `read_csv()`: CSV 파일 읽기
- `read_excel()`: Excel 파일 읽기
- `to_csv()`: CSV 파일로 저장
- `to_excel()`: Excel 파일로 저장

#### 통계 함수
- `mean()`, `max()`, `min()`, `median()`: 기본 통계량
- `std()`, `var()`: 표준편차, 분산
- `quantile()`: 사분위수
- `value_counts()`: 고유값 개수

### 주요 주의사항
- 파일 경로 설정 시 역슬래시(`\`) 처리 주의
- 복합 조건 검색 시 numpy 논리 함수 사용
- 파일 저장 시 인코딩 옵션 고려
- 상대 경로 사용 권장
