# 🐍 파이썬(Python) 기초 개념 설명서

##### 🗓️ 2025.04.24
##### 📝 Writer : Moon19ht

---

## 📚 목차

1. [기초 문법](#-1-파이썬의-기초-문법)
2. [변수(Variable)](#-2-변수-variable)
3. [문자열(String)](#-3-문자열-string)
4. [리스트(List)](#-4-리스트-list)
5. [자료형(Type)](#-5-자료형)

---

## 1. 파이썬의 기초 문법

**출력**

```python
print("Hello, World!")
```
- 출력을 하고자 할 때 `print()` 함수를 사용한다.
- `print()` 함수는 문자열을 인자로 받아 출력한다.
- 기본적으로 줄바꿈이 포함된다.
- 인자를 여러 개 받을 수 있으며, 쉼표(,)로 구분하여 여러 값을 출력할 수 있다.

**사칙연산**
```python
a = 10
b = 5
print(a + b)  # 덧셈
print(a - b)  # 뺄셈
print(a * b)  # 곱셈
print(a / b)  # 나눗셈
print(a // b)  # 몫
print(a % b)  # 나머지
```
- 사칙연산은 +, -, *, /, //, % 연산자를 사용한다.
- // 연산자는 몫을, % 연산자는 나머지를 반환한다.

**입력받기**
```python
name = input("Enter your name: ")
print("Hello, " + name)
```
- `input()` 함수로 사용자 입력을 받을 수 있다.
- 입력값은 항상 문자열(str) 타입으로 반환된다.

---

## 2. 변수 (Variable)

### 변수란?
> 컴퓨터의 기억 공간에 이름을 붙인 것. 이름을 붙이면 값을 저장하고, 나중에 그 값을 다시 꺼내 쓸 수 있다.

### 왜 이름이 필요할까?
1. 사람은 숫자보다 단어를 기억하기 쉽기 때문이다.
2. 메모리 주소를 직접 지정하는 것은 위험하다.  
   → 해당 주소가 비어있는지, 시스템적으로 중요한 공간인지 알 수 없기 때문이다.

---

## 변수 이름 규칙

### 사용할 수 있는 문자
- 영문 대소문자 (A~Z, a~z)
- 숫자 (0~9)
- 언더바(_)

### 주의사항
- 변수는 숫자로 시작할 수 없다.
  - `3a` (불가능)
  - `a3` (가능)
- 예약어(파이썬 키워드)는 사용할 수 없다.
  - 예: `int = 4` (불가능)
  - 예: `inta = 4` (가능)

---

## 변수 이름 작성 스타일

| 스타일 | 예시 | 특징 |
|--------|------|------|
| 스네이크 표기법 | `student_name` | 단어와 단어 사이를 `_`로 구분 |
| 카멜 표기법 | `studentName` | 두 번째 단어부터 첫 글자를 대문자로 |
| 헝가리안 표기법 | `szStudentName` | 타입 정보를 앞에 붙임 (`sz`: string) <br>※ 현대에는 거의 사용되지 않음 |

> 좋은 변수 이름을 짓는 습관
- 의미 있는 이름을 사용하세요.
- 길더라도 어떤 값을 저장하는지 쉽게 유추할 수 있도록 작성하세요.

---

## 값 할당 및 출력

### 리터럴 (Literal)
> 코드에 직접 적힌 값 그 자체

```python
5       # 정수 리터럴
4.5     # 실수 리터럴
"Hello" # 문자열 리터럴
```

### 변수에 값 저장 (할당)
```python
a = 4       # a라는 변수에 4를 저장
a = 5       # a의 값을 5로 변경
print(a)    # 변수 a의 값을 출력
```

---

## 스크립트 vs 인터프린터 vs 컴파일러

| 구분 | 설명 | 예시 |
|------|------|------|
| 스크립트 | 특정 환경에서 해석되어 실행되는 언어 | 웹스크립트, 자바스크립트, VB스크립트 등 |
| 인터프린터 언어 | 한 줄씩 번역하고 바로 실행하는 방식 | 파이썬, 자바스크립트 |
| 컴파일러 언어 | 전체 코드를 한 번에 번역하여 실행 파일로 만드는 방식 | C, C++, Java |

### 인터프린터 특징
- 즉시 실행 → 실습과 교육용으로 적합
- 실행은 빠르나 에러 메시지는 단순 → 디버깅 속도 느림

### 컴파일러 특징
- 에러가 없을 때만 실행 가능
- 에러 메시지 다양 → 디버깅 능력이 빠르게 향상됨
- 변수, 함수 선언 필수 → 문법에 엄격함

---

## 3. 문자열 (String)

- 문자열은 문자들의 집합이다. 예: 'a', "hello"
- 여러 줄 문자열은 작은따옴표 세 개 또는 큰따옴표 세 개를 연속해서 사용할 수 있다.

```python
text = "Hello, Python"
```

---

### 문자열 인덱싱과 슬라이싱

- 인덱싱: 문자열에서 특정 위치의 문자 추출
- 슬라이싱: 문자열의 일부분을 잘라냄

```python
text = "Python"
print(text[0])    # 'P'
print(text[-1])   # 'n'
print(text[1:4])  # 'yth'
```

---

### 문자열 함수

| 함수 | 설명 | 예시 |
|------|------|------|
| `len(s)` | 문자열 길이 반환 | `len("apple") → 5` |
| `lower()` | 소문자로 변환 | `"PY".lower() → "py"` |
| `upper()` | 대문자로 변환 | `"py".upper() → "PY"` |
| `strip()` | 앞뒤 공백 제거 | `"  hi  ".strip() → "hi"` |
| `replace(a, b)` | a를 b로 치환 | `"hello".replace("l", "r") → "herro"` |
| `split(sep)` | 구분자로 나누기 | `"a,b,c".split(",") → ['a', 'b', 'c']` |
| `join(list)` | 리스트 요소를 연결 | `" ".join(['a','b']) → "a b"` |
| `find(x)` | x의 첫 등장 인덱스 | `"banana".find("a") → 1` |
| `count(x)` | x의 등장 횟수 | `"banana".count("a") → 3` |

---

## 4. 리스트 (List)

여러 개의 데이터를 순서대로 저장하는 자료형으로, 대괄호 `[]` 사용

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])     # apple
print(fruits[-1])    # cherry
```

---

### 리스트 인덱싱과 슬라이싱

```python
print(fruits[0])    # 'apple'
print(fruits[-1])   # 'cherry'
print(fruits[1:])   # ['banana', 'cherry']
```

---

### 리스트 함수

| 함수 | 설명 | 예시 |
|------|------|------|
| `append(x)` | 마지막에 추가 | `fruits.append("orange")` |
| `insert(i, x)` | i 위치에 x 삽입 | `fruits.insert(1, "grape")` |
| `remove(x)` | 첫 x 제거 | `fruits.remove("banana")` |
| `pop(i)` | i 위치 값 반환 후 제거 | `fruits.pop(0)` |
| `sort()` | 오름차순 정렬 | `fruits.sort()` |
|`replace(a, b)` | 문자열 치환 | `"hi".replace("h", "y")` → `"yi"` |
| `len(lst)` | 리스트 길이 | `len(fruits)` |
| `in` | 포함 여부 확인 | `"apple" in fruits → True` |

---

### 리스트 컴프리헨션 (List Comprehension)

짧은 문법으로 리스트 생성 가능

```python
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
```

---

## 5. 자료형 (Type)

### 정수 (int)  
소수점 이하가 없는 숫자. (예: `10`, `-5`, `1000000`)

- 저장 크기와 범위:  
  - 4Byte = 32bit  
  - 부호 있음(signed): -21억 ~ +21억 (`-2^31 ~ 2^31-1`)  
  - 부호 없음(unsigned): 0 ~ 42억 (`0 ~ 2^32-1`)  
  - 즉, `int`만으로는 600조를 담기엔 부족함

- 음수 표현 방식 (컴퓨터 내부):
  1. 부호 비트 사용: `0 → 양수`, `1 → 음수`
  2. 1의 보수: `0 → 1`, `1 → 0`
  3. 2의 보수 (표준 방식):  
     1의 보수 + 1 = 2의 보수  
     → 이 방식 덕분에 덧셈기 하나로 `+, -, *, /` 연산 가능

### 실수 (float)
소수점이 있는 수 (예: `3.14`, `-0.001`, `1e+20`)

- 구조:  
  실수는 지수부(exponent) + 가수부(mantissa)로 구성  
  똑같은 4Byte라도 훨씬 더 큰 수 / 작은 수 저장 가능

- 주의 사항:
  - 정수 / 정수 → 파이썬에서는 실수 결과
    ```python
    3 / 2  # 결과: 1.5
    ```
  - 정수 // 정수 → 몫만 취함
    ```python
    3 // 2  # 결과: 1
    ```
  - `%` 연산자 → 나머지 계산
    ```python
    5 % 2  # 결과: 1
    ```

### 문자형 (char)

- 파이썬에는 `char` 타입이 따로 존재하지 않는다.
- `'A'`, `'가'`, `'1'` 등 한 글자도 문자열(`str`)로 취급된다.
- 문자열의 길이가 1인 경우가 문자처럼 사용될 뿐이다.

### 문자열 (string)

- 문자열 생성: 큰따옴표 `"..."` 또는 작은따옴표 `'...'`
- 여러 줄 문자열: `"""..."""` 또는 `'''...'''`

```python
s = """
동해물과 백두산이
마르고 닳도록 
하느님이 보우하사 
우리 나라 만세
"""
```

### 주석(Comment)

- 한 줄 주석: `#` 사용
- 여러 줄 주석처럼 사용할 수 있는 문법은 작은따옴표 세 개(`'''`) 또는 큰따옴표 세 개(`"""`)를 연속해서 사용하는 방식이다.
- 단, 이 방법은 실제로는 실행 시 문자열 객체로 처리되며, 함수나 클래스 바로 아래에 쓰일 경우 docstring으로 동작함

```python
"""
이 코드는
여러 줄 주석처럼 사용됩니다
"""
```

---

## 정리

| 구분     | 파이썬 표현     | 설명                                  |
|----------|----------------|---------------------------------------|
| 정수     | `int`          | 소수점 없는 수                        |
| 실수     | `float`        | 지수와 가수 형태로 표현된 실수       |
| 문자열   | `str`          | 문자 집합 (한 글자도 문자열로 처리됨) |
| 주석     | `#`            | 코드 설명용, 실행되지 않음            |

---

## 추가 : 2진수, 8진수, 10진수, 16진수 변환

### 1. 컴퓨터는 이진수 체계를 사용한다

> 예시:  
> `1100001100101100011111111111100000`

이진수는 컴퓨터 내부에서 정보를 표현하는 가장 기본적인 방식이다.  
모든 데이터는 0과 1로 표현된다.

---

### 2. 8진수와의 변환 관계

8진수는 3비트씩 묶어서 변환한다.

| 2진수 | 8진수 |
|-------|-------|
| 000   | 0     |
| 001   | 1     |
| 010   | 2     |
| 011   | 3     |
| 100   | 4     |
| 101   | 5     |
| 110   | 6     |
| 111   | 7     |

**예시 변환:**

이진수:   1100001100101100011111111111100000  
3비트:   001 100 001 100 101 100 011 111 111 111 000  
8진수:    1    4    1    4    5    4    3    7    7    7    0

---

### 3. 16진수와의 변환 관계

16진수는 4비트씩 묶어서 변환한다.

| 2진수 | 16진수 |
|-------|--------|
| 0000  | 0      |
| 0001  | 1      |
| 0010  | 2      |
| 0011  | 3      |
| 0100  | 4      |
| 0101  | 5      |
| 0110  | 6      |
| 0111  | 7      |
| 1000  | 8      |
| 1001  | 9      |
| 1010  | A      |
| 1011  | B      |
| 1100  | C      |
| 1101  | D      |
| 1110  | E      |
| 1111  | F      |

**예시 변환:**

이진수:   1100001100101100011111111111100000  
4비트:   0001 1000 0110 0101 1000 1111 1111 1110 0000  
16진수:    1    8    6    5    8    F    F    E    0

---

### 4. 2진수와 10진수의 변환

#### 2진수 → 10진수

각 자리의 값을 2의 거듭제곱으로 계산하여 모두 더한다.

> 예시:  
> `1101` →  
> `(1×2³) + (1×2²) + (0×2¹) + (1×2⁰)` = `8 + 4 + 0 + 1` = 13

#### 10진수 → 2진수

2로 계속 나누고, 나머지를 거꾸로 읽는다.

> 예시:  
> `13 ÷ 2 = 6 ...1`  
> `6 ÷ 2 = 3 ...0`  
> `3 ÷ 2 = 1 ...1`  
> `1 ÷ 2 = 0 ...1`  
> → 거꾸로 읽으면: 1101

---

### 요약

- 2진수는 컴퓨터의 기본 표현 방식
- 8진수: 3비트씩 묶어서 표현
- 16진수: 4비트씩 묶어서 표현
- 10진수와는 자리수마다 2의 거듭제곱으로 계산

---

## 실무 TIP

- input() 함수로 입력받은 값은 항상 문자열(str) 타입이므로, 숫자로 사용하려면 int(), float() 등으로 변환해야 한다.
- print() 함수에서 end, sep 파라미터를 활용하면 출력 형식을 다양하게 지정할 수 있다.
- 리스트, 문자열 등은 인덱스가 0부터 시작한다는 점에 주의.
- 변수명은 의미 있게, 일관성 있게 작성하는 습관을 들이자.
- 파이썬의 동적 타이핑 특성상 변수에 다양한 타입의 값을 할당할 수 있지만, 일관성 있게 사용하는 것이 좋다.
