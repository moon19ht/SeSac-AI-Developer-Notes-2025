# 🐍 파이썬(Python) 기초 개념 설명서

##### 🗓️ 2025.04.25
##### 📝 Writer : Moon19ht

---

## 📚 목차

1. [딕셔너리(Dictionary)](#-1-딕셔너리-dictionary)
2. [튜플(Tuple)](#-2-튜플-tuple)
3. [컴프리핸션(Comprehension)](#-3-컴프리핸션-comprehension)
4. [제어문](#-4-제어문)

---

## 1. 딕셔너리 (Dictionary)

**개념**
- 키(key)와 값(value)의 쌍으로 이루어진 자료형
- 순서가 없는(파이썬 3.6 이상부터는 삽입 순서 유지), mutable(변경 가능)한 자료형
- 중복된 키는 허용하지 않음

**생성 방법**
```python
# 기본 생성
my_dict = {"name": "Alice", "age": 25, "city": "Seoul"}

# dict() 함수 사용
my_dict2 = dict(name="Bob", age=30)
```

**주요 메서드**
```python
my_dict["name"]         # 'Alice' — 키로 값 접근
my_dict.get("age")      # 25 — 키가 없을 경우 None 반환 (예외 발생 안 함)
my_dict.keys()          # dict_keys(['name', 'age', 'city'])
my_dict.values()        # dict_values(['Alice', 25, 'Seoul'])
my_dict.items()         # dict_items([('name', 'Alice'), ('age', 25), ('city', 'Seoul')])
my_dict.pop("city")     # 'Seoul' — 삭제하고 값 반환
my_dict.update({"age": 26})  # 값 변경
```

**특징**
- 키는 해시 가능한 불변 타입(str, int, float, tuple 등)만 사용 가능
- 빠른 검색 속도 (해시 기반)

---

## 2. 튜플 (Tuple)

**개념**
- 순서가 있는 자료형으로, immutable(변경 불가능)한 리스트
- 소괄호 `( )`를 사용해서 정의

**생성 방법**
```python
t1 = (1, 2, 3)
t2 = 1, 2, 3            # 괄호 생략 가능 (자동으로 튜플로 인식됨)
t3 = (1,)               # 요소가 하나일 경우 쉼표 필요
```

**주요 연산**
```python
t1[0]                   # 1 — 인덱싱
t1[1:3]                 # (2, 3) — 슬라이싱
t1 + t2                 # 튜플 연결
t1 * 2                  # 반복
len(t1)                 # 길이
```

**특징**
- 리스트보다 메모리 사용이 적고 속도가 빠름
- 수정이 불가능하므로 데이터 보호에 유리
- 딕셔너리의 키나 set의 원소로 사용 가능

---

## 3. 컴프리핸션 (Comprehension)

**개념**
- 간결하고 직관적인 문법으로 컬렉션 생성
- 반복문과 조건문을 조합하여 새로운 리스트, 딕셔너리, 셋을 생성

---

**리스트 컴프리핸션**
```python
# 0부터 9까지 제곱 리스트
squares = [x**2 for x in range(10)]

# 짝수만 필터링
evens = [x for x in range(10) if x % 2 == 0]
```

---

**딕셔너리 컴프리핸션**
```python
# 0~4 숫자와 그 제곱을 key-value로 매핑
square_dict = {x: x**2 for x in range(5)}
```

---

**셋(Set) 컴프리핸션**
```python
# 중복 제거하면서 제곱 저장
square_set = {x**2 for x in [1, 2, 2, 3, 4]}
```

---

**특징**
- 코드 길이를 줄이고 가독성 향상
- 그러나 너무 복잡하면 오히려 가독성 저하되므로 주의 필요

---

## 4. 제어문 

### 제어 구조(Control Structure)

프로그래밍에서 제어 구조는 코드의 실행 흐름을 제어하는 구문이다. 파이썬에서 자주 사용하는 제어 구조는 아래와 같이 나눌 수 있다.

#### 순차 구조 (Sequential Structure)

- 명령문이 위에서 아래로 순서대로 실행된다.
- 가장 기본적인 구조이다.
  
```python
print("1단계 실행")
print("2단계 실행")
print("3단계 실행")
```

---

#### 분기 구조 (Conditional / Branching Structure)

**if 문**

- 조건에 따라 코드를 실행할지 말지를 결정한다.
- 조건의 결과는 반드시 True 또는 False를 반환해야 한다.

```python
if 조건식:
    실행문1
    실행문2
# 들여쓰기가 끝나는 부분이 if 블록의 종료점이다.
```

**if - else 문**

- 조건이 참이면 if 블록, 거짓이면 else 블록 실행

```python
if 조건식:
    실행문
else:
    다른실행문
```

**if - elif - else 문**

- 여러 조건을 순차적으로 확인하고 해당 조건에 맞는 블록을 실행한다.

```python
if 조건1:
    실행문1
elif 조건2:
    실행문2
elif 조건3:
    실행문3
else:
    실행문4
```

---

#### 반복 구조 (Loop Structure)

**for 문**

- 정해진 횟수만큼 반복
- 리스트, 튜플, 문자열 등 시퀀스 자료형에 대해 반복

```python
for 변수 in 반복 가능한 객체(리스트, 튜플 등):
    실행문
```

예:
```python
for i in range(5):  # 0부터 4까지 반복
    print(i)
```

**while 문**

- 조건을 만족하는 동안 반복
- 반복 횟수가 정해지지 않았을 때 사용
- 조건이 처음부터 False라면 한 번도 실행되지 않을 수 있음

```python
while 조건식:
    실행문
```

예:
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

---

### 기타 참고

- `break`: 반복문을 즉시 종료한다.
- `continue`: 현재 반복을 건너뛰고 다음 반복으로 넘어간다.
- `pass`: 아무 동작도 하지 않고 자리를 채워둠 (빈 블록이 필요할 때 사용)
```python
def some_func():
    pass  # 나중에 구현 예정
```

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

## 요약

| 제어 구조 | 설명 |
|-----------|------|
| 순차 구조 | 위에서 아래로 차례대로 실행 |
| 분기 구조 | 조건에 따라 서로 다른 코드 실행 (`if`, `if-else`, `if-elif-else`) |
| 반복 구조 | 조건을 만족할 때까지 또는 정해진 횟수만큼 반복 (`for`, `while`) |

---

## 실무 TIP

- 딕셔너리에서 키가 존재하지 않을 때 get()을 사용하면 예외 없이 None을 반환하므로 안전하게 값을 조회할 수 있다.
- 튜플은 불변(immutable)이므로, 값 변경이 필요하다면 리스트로 변환 후 작업하는 것이 좋다.
- 컴프리핸션은 간단한 경우에만 사용하고, 복잡한 경우에는 for문을 사용하는 것이 가독성에 더 좋다.
- for문에서 enumerate()를 사용하면 인덱스와 값을 동시에 얻을 수 있다.
- 반복문 내에서 break, continue, pass의 차이를 명확히 이해하고 사용하자.
