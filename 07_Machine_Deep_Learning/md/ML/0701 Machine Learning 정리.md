# 📊 Machine Learning 이론

##### 🗓️ 2025.07.01
##### 📝 Writer : Moon19ht

---

## 📚 목차

1. [판다스 소개](#1-판다스-소개)
2. [판다스 설치](#2-판다스-설치)
3. [판다스 데이터 타입](#3-판다스-데이터-타입)
4. [Series 상세](#4-series-상세)
5. [DataFrame 상세](#5-dataframe-상세)
6. [Panel 상세](#6-panel-상세)
7. [판다스 연산](#7-판다스-연산)
8. [실습 예제](#8-실습-예제)
9. [핵심 요약](#9-핵심-요약)

---

## 1. 판다스(Pandas) 소개

### 1.1 데이터셋의 중요성
- 수집된 데이터들은 각자 동일하거나 다른 형태의 데이터들로 구성
- 데이터셋은 다양한 형태의 데이터들을 하나의 구조로 만들어서 관리나 분석을 용이하게 함
- 파이썬에서는 데이터셋을 관리하기 위해 pandas 라이브러리를 제공

### 1.2 판다스(pandas) 라이브러리란?
- 데이터 분석(Data Analysis)을 위해 널리 사용되는 파이썬 라이브러리 패키지
- 클래스를 별도로 만들지 않고도 pandas 라이브러릴 이용하여 데이터를 읽고 쓸 수 있습니다.
- 파이썬에 제공하는 통계관련 패키지들에서도 자주 사용하는 라이브러리 입니다.
- 아나콘다(Anaconda)를 이용해 파이썬을 설치하셨다면 이미 pandas 패키지는 설치되어 있습니다.
- 만일 별도로 파이썬만 설치되어 있다면, pandas 를 별도로 설치해야 합니다.
- 머신러닝이나 딥러닝에서는 numpy나 pandas 라이브러를 이용해서 파이썬이 제공하는 기본 타입들을 데이터 분석에 사용하기 쉽도록 제공하고 있습니다.

### 1.3 판다스 라이브러리 구성
- 클래스와 여러가지의 내장함수로 구성되어있습니다.
- 제공하는 데이터 타입은 Series(1차원), Dataframe(2차원), Panel(3차원)입니다
- 판다스를 이용해 list나 dict 타입등을 판다스에서 사용하는 데이터 구조로 변환할 수 있습니다.
- 데이터 분석에서 사용하는 데이터 타입은 파이썬에 제공하는 list나 dict 타입을 그냥 사용하기에는 무리가 있습니다.
- pandas 는 csv파일을 읽고 쓰거나, excel 파일을 읽고 쓰기 쉽도록 구성되어 있습니다.

---

## 2. 판다스 설치

### 2.1 아나콘다 사용 시
- 아나콘다(Anaconda)를 이용해 파이썬을 설치했다면 이미 pandas 패키지가 설치되어 있음

### 2.2 별도 설치 시
```bash
pip install pandas
```

### 2.3 설치 문제 해결
- pip 명령이 작동하지 않는 경우: 환경변수에 경로 지정 필요
- 권한 부족 시: 관리자 권한으로 콘솔창 실행

### 2.4 사용법
```python
import pandas as pd
```

---

## 3. 판다스 데이터 타입

| 타입 | 차원 | 설명 |
|------|------|------|
| Series | 1차원 | 배열/리스트와 같은 시퀀스 데이터 |
| DataFrame | 2차원 | 행과 열로 이루어진 테이블 형태 |
| Panel | 3차원 | 3개의 축을 가진 데이터 구조 (현재 사용 안함) |

---

## 4. Series 상세

### 4.1 Series란?
- pandas가 제공하는 1차원 구조의 타입
- 배열/리스트와 같은 일련의 시퀀스(연속된) 데이터를 저장
- 인덱스와 값 쌍으로 구성되어 dict 타입과 유사

### 4.2 인덱스 구조
- 인덱스는 자기와 짝을 이루는 데이터의 값과 주소를 저장
- 데이터 값의 검색, 정렬, 선택, 결합 등을 용이하게 함
- 별도의 레이블 인덱스를 지정하지 않으면 0부터 시작하는 인덱스가 자동 부여

### 4.3 Series 생성 예제
```python
# 파일명: exam9_1.py
import pandas as pd

# 파이썬 list를 사용하여 Series 만들기
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print(type(series))
print(series)

# 직접 index 부여하기 (dict 타입 사용)
data2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
series2 = pd.Series(data2)
print(series2)
```

### 4.4 Series 데이터 접근 방법
- **기본 접근**: `변수명[인덱스]`
- **슬라이싱**: `변수명[시작:끝]`
- **레이블 접근**: `변수명['레이블명']`

```python
# 파일명: exam9_4.py
import pandas as pd

data = [10, 20, 30, 40, 50, 60]
s = pd.Series(data)

print(s[0])         # 0번째 데이터 출력
s[1] = 200          # 1번째 데이터 수정
print(s[:5])        # 처음부터 4번째까지 출력
print(s[2:5])       # 2번째부터 4번째까지 출력
print(s[3:])        # 3번째부터 끝까지 출력

# 레이블 인덱스 사용
data = {'one': '일', 'two': '이', 'three': '삼', 'four': '사', 'five': '오'}
series = pd.Series(data)
print(series['one'])
print(series['one':'three'])
```

---

## 5. DataFrame 상세

### 5.1 DataFrame이란?
- pandas가 제공하는 2차원 구조의 타입
- 데이터를 행과 열로 이루어진 테이블 형태로 저장
- R 통계언어에서 비롯된 구조
- 열은 각자 다른 타입으로 구성될 수 있음
- 관계형 데이터베이스, Excel, CSV 형식의 데이터를 다루는데 최적화

### 5.2 DataFrame 생성 예제
```python
# 파일명: exam9_2.py
import pandas as pd

data = {
    'name': ['홍길동', '임꺽정', '장길산', '홍경래'],
    'kor': [90, 80, 70, 70],
    'eng': [99, 98, 97, 46],
    'mat': [90, 70, 70, 60],
}
df = pd.DataFrame(data)
print("타입:", type(df))
print(df)
```

### 5.3 DataFrame 데이터 접근 방법
- **iloc 함수**: 행과 열의 인덱스 번호를 이용해 접근
- **loc 함수**: 행의 인덱스와 열의 컬럼명을 이용해 접근

```python
# 파일명: exam9_5.py
import pandas as pd

data = {
    'name': ['홍길동', '임꺽정', '장길산', '홍경래', '이상민', '김수경'],
    'kor': [90, 80, 70, 70, 60, 70],
    'eng': [99, 98, 97, 46, 77, 56],
    'mat': [90, 70, 70, 60, 88, 99],
}
df = pd.DataFrame(data)

# 기본 정보 출력
print(df.head())          # 앞의 다섯 행만 출력
print(df['name'])         # 특정 열만 출력
print(df.columns)         # 컬럼 이름 출력

# iloc 함수 사용
print(df.iloc[0, 0])      # 0,0번에 해당하는 데이터
print(df.iloc[3, 2])      # 3번째 행의 2번째 열
print(df.iloc[2:4, 2])    # 2~3번 행의 2번째 열
print(df.iloc[2:4, 2:4])  # 2~3번 행의 2~3번째 열

# loc 함수 사용
print(df.loc[0, 'name'])           # 0번째 행의 name 필드
print(df.loc[3, 'eng'])            # 3번째 행의 eng 필드
print(df.loc[:, 'name':'eng'])     # 모든 행의 name부터 eng까지
```

---

## 6. Panel 상세

### 6.1 Panel이란?
- 3차원 자료구조 (현재는 사용하지 않음)
- Axis 0 (items), Axis 1 (major_axis), Axis 2 (minor_axis) 등 3개의 축을 가짐
- Axis 0은 2차원 DataFrame에 해당
- Axis 1은 DataFrame의 행(row), Axis 2는 DataFrame의 열(column)에 해당

### 6.2 Panel 예제
```python
# 파일명: exam9_6.py
import pandas as pd

data = {
    'class1': {
        'name': ['박동석', '권다윤', '김민제'],
        'height': [173, 177, 183]
    },
    'class2': {
        'name': ['김민수', '이용희', '임미영'],
        'height': [179, 167, 180]
    }
}

panel = pd.Panel(data)  # 경고 메시지 발생 (미래 버전에서 제거 예정)
print(panel)

# 데이터 접근
df = panel['class1']
print(df.iloc[0, 0])
```

---

## 7. 판다스 연산

### 7.1 연산 프로세스
pandas 객체의 산술연산은 다음 3단계를 거침:
1. 행, 열 인덱스를 기준으로 모든 원소를 정렬
2. 동일한 위치에 있는 원소끼리 일대일 대응
3. 일대일 대응된 원소끼리 연산 처리 (대응 원소가 없으면 NaN 처리)

### 7.2 Series 연산 예제

#### 7.2.1 기본 연산
```python
# 파일명: exam9_7.py
import pandas as pd

data1 = {'kor': 90, 'eng': 70, 'mat': 80}
data2 = {'kor': 90, 'eng': 70, 'mat': 80}
data3 = {'kor': 90, 'eng': 70, 'mat': 80}
data4 = {'eng': 90, 'mat': 70, 'kor': 80}  # 인덱스 순서가 달라도 자동 정렬

series1 = pd.Series(data1)
series2 = pd.Series(data2)
series3 = pd.Series(data3)
series4 = pd.Series(data4)

result1 = series1 + series2 + series3 + series4
result2 = result1 / 4

print("총점:", result1)
print("평균:", result2)
```

#### 7.2.2 NaN 처리
```python
# 파일명: exam9_8.py
import pandas as pd

# 인덱스가 없을 경우 NaN 처리
data1 = {'kor': 90, 'mat': 80}
data2 = {'kor': 90, 'eng': 70}
data3 = {'kor': 90, 'eng': 70, 'mat': 80}

series1 = pd.Series(data1)
series2 = pd.Series(data2)
series3 = pd.Series(data3)

result1 = series1 + series2 + series3
print(result1)  # NaN 값 포함
```

#### 7.2.3 fill_value 옵션 사용
```python
# 파일명: exam9_9.py
import pandas as pd

data1 = {'kor': 90, 'mat': 80}
data2 = {'kor': 90, 'eng': 70}
data3 = {'kor': 90, 'eng': 70, 'mat': 80}

series1 = pd.Series(data1)
series2 = pd.Series(data2)
series3 = pd.Series(data3)

# fill_value=0으로 NaN 대신 0 사용
result1 = series1.add(series2, fill_value=0).add(series3, fill_value=0)
print(result1)
```

### 7.3 DataFrame 연산

#### 7.3.1 기본 연산과 새 필드 추가
```python
# 파일명: exam9_10.py
import pandas as pd

# Series를 결합하여 DataFrame 만들기
data1 = {'kor': 90, 'eng': 70, 'mat': 80}
data2 = {'kor': 90, 'eng': 70, 'mat': 80}
data3 = {'kor': 90, 'eng': 70, 'mat': 80}

data = pd.DataFrame()
data = data.append(data1, ignore_index=True)
data = data.append(data2, ignore_index=True)
data = data.append(data3, ignore_index=True)

# 새 필드 추가
data['total'] = data.kor + data.eng + data.mat
data['avg'] = data.total / 3
print(data)
```

#### 7.3.2 행 추가와 삭제
```python
# 파일명: exam9_12.py
import pandas as pd

data = {
    'fruits': ['망고', '딸기', '수박', '파인애플'],
    'price': [2500, 5000, 10000, 7000],
    'count': [5, 2, 2, 4],
}
df = pd.DataFrame(data)

# 새로운 행 추가 (반드시 반환값을 받아야 함)
df = df.append({'fruits': '사과', 'price': 3500, 'count': 10}, ignore_index=True)
print(df)

# 특정 필드 삭제 (axis=1: 열, axis=0: 행)
df2 = df.drop("price", axis=1)
print(df2)

# 특정 행 삭제
df3 = df.drop(0, axis=0)
print(df3)
```

---

## 8. 실습 예제

### 과제 1: 데이터프레임 만들기
다음 테이블 데이터를 DataFrame 객체로 만들고, 새로운 데이터 (10, 20, 30, 40)를 추가한 후 total 필드를 만들어 각 필드의 합을 구하세요.

```python
# 파일명: homework9.py
import pandas as pd

data = {
    'X1': [2.9, 2.4, 2, 2.3, 3.2],
    'X2': [9.2, 8.7, 7.2, 8.5, 9.6],
    'X3': [13.2, 11.5, 10.8, 12.3, 12.6],
    'X4': [2, 3, 4, 3, 2]
}

df = pd.DataFrame(data)
print(df)

# 새로운 행 추가
df = df.append({'X1': 10, 'X2': 20, 'X3': 30, 'X4': 40}, ignore_index=True)

# total 필드 추가
df['total'] = df.X1 + df.X2 + df.X3 + df.X4
print(df)
```

---

## 9. 핵심 요약

### 9.1 Series
- 판다스에서 1차원 데이터를 지원하는 데이터 타입
- 인덱스를 활용해 데이터에 접근
- 인덱스는 자동으로 부여되거나 dict 타입으로 사용자가 지정 가능
- 조건식을 통한 데이터 필터링 가능: `data[조건식]`

### 9.2 DataFrame
- 판다스에서 2차원 데이터를 지원하는 데이터 타입
- 테이블 구조로 행과 열을 가짐
- 가장 많이 사용하는 데이터 타입
- 각 열과 행은 하나의 Series 타입으로 볼 수 있음
- **iloc 함수**: 열번호와 행번호를 이용한 접근
- **loc 함수**: 컬럼명과 행명을 이용한 접근
- CSV 파일이나 Excel 파일 처리에 용이

### 9.3 Panel
- 판다스에서 3차원 데이터를 지원하는 데이터 타입
- 현재는 사용하지 않음 (미래 버전에서 제거 예정)

### 9.4 연산 특징
- 벡터 연산 수행
- 인덱스 기준 자동 정렬
- 일대일 대응 연산
- 대응 원소가 없으면 NaN 처리
- fill_value 옵션으로 기본값 설정 가능
