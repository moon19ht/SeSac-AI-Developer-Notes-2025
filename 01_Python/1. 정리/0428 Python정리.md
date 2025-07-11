# 🐍 파이썬(Python) 기초 개념 설명서

##### 🗓️ 2025.04.28
##### 📝 Writer : Moon19ht

---

## 📚 목차

- [📌 1. 이중 for문](#1--이중-for문)
- [📌 2. 누적 합 출력 (1+2+...+n)](#2--누적-합-출력-12n---이중-for문-응용)
- [📌 3. 별 출력하기](#3--별-출력하기---이중-for문-응용)
- [📌 4. while문](#4--while문)
- [📌 5. 함수 사용](#5--함수-사용)
- [🔚 마무리](#-마무리)

---

## 📌 1. 이중 for문

### ✅ 기본 개념
- 중첩 for문은 하나의 for문 안에 또 다른 for문을 넣는 구조입니다.
- 예: 바깥 루프가 M번, 안쪽 루프가 N번 수행되면 전체 반복 횟수는 `M x N`입니다.
- **2중 루프까지 사용하는 것이 일반적입니다.**

### ✅ 예제1: 1~100까지 출력 (10개씩 한 줄에)
```python
for i in range(10):
    for j in range(10):
        print(i*10+j+1, end=' ')
    print()
```

## 📌 2. 누적 합 출력 (1+2+...+n) - 이중 for문 응용

### ✅ 기본 for문
```python
for i in range(1, 11):
    total = 0
    expr = ""
    for j in range(1, i+1):
        total += j
        if j == 1:
            expr = "1"
        else:
            expr += " + " + str(j)
    print(f"{expr} -> {total}")
```

### ✅ join + sum 활용
```python
for i in range(1, 11):
    nums = range(1, i+1)
    expr = " + ".join(map(str, nums))
    print(f"{expr} -> {sum(nums)}")
```

### ✅ 수학 공식 이용 (등차수열의 합)
```python
for i in range(1, 11):
    expr = " + ".join(str(j) for j in range(1, i+1))
    total = i * (i + 1) // 2
    print(f"{expr} -> {total}")
```

## 📌 3. 별 출력하기 - 이중 for문 응용

### ✅ 삼각형
```python
for i in range(1, 11):
    print("*" * i)
```

### ✅ 마름모(다이아몬드)
```python
n = 5
# 위쪽
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2*i + 1)) # 정중앙 정렬용 좌우 여백
# 아래쪽
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2*i + 1))  # 정중앙 정렬용 좌우 여백
```

### 💡 원리 요약
- 위쪽: 공백 `n - i - 1`개 + 별 `2*i + 1`개
- 아래쪽: 위의 반대 순서로 반복

## 📌 4. while문

### ✅ 기본 문법
```python
i = 1
while i <= 10:
    print(i)
    i += 1
```

### ✅ 예제: 합이 1000을 넘는 최소 자연수
```python
total = 0
i = 0
while total < 1000:
    i += 1
    total += i
print(i)
```

## 📌 5. 함수 사용

### 📌 함수(Function)란?
- **함수(Function)** 는 특정 기능을 수행하는 코드 묶음으로, 반복되는 작업을 간결하고 효율적으로 처리하기 위해 사용됩니다.
- 과거의 스파게티 코드처럼 복잡하게 얽힌 코드에서 벗어나, 기능별로 모듈화하여 구조적으로 관리할 수 있게 해줍니다.
- 함수는 **입력값(매개변수)** 을 받아 **결과값(return)** 을 반환하며, 파이썬에서는 `def` 키워드로 정의합니다.

### ✅ 함수와 프로시저의 차이
- 프로시저(Procedure) : 값을 반환하지 않고 작업만 수행
- 함수(Function) : 작업 후 결과값을 반환함

### ✅ 함수의 장점
- 코드 재사용성 증가 → 유지보수 편리
- 반복 작업을 구조화하여 코드 가독성 향상
- 구조적/객체지향 프로그래밍에서 필수 개념

### ✅ 작성 시 유의사항
- 일반적으로 함수는 15줄 이하, A4 한 페이지 이내가 이상적 (가독성 기준)
- 반환값은 하나만 명시하지만, 여러 값을 `tuple` 형태로 묶어 반환 가능

### ✅ 함수 정의 및 호출
```python
def print_line():
    print("=" * 30)

print_line()
```

### ✅ N까지의 합을 반환하는 함수
```python
def sigma(limit):
    s = 0
    for i in range(1, limit+1):
        s += i
    return s

print(sigma(10))     # 55
print(sigma(100))    # 5050
print(sigma(1000))   # 500500
```

---

## 🔚 마무리
- 반복문은 일정한 패턴의 작업을 자동으로 수행하게 해주며, 특히 이중 for문은 표 형태의 출력이나 누적 계산 등에서 유용합니다. 
- 함수는 반복되는 코드 블록을 하나로 묶어 재사용성과 가독성을 높이고, 필요한 값을 반환해 프로그램의 흐름을 깔끔하게 만듭니다. 
- 반복문과 함수는 파이썬의 구조적 프로그래밍과 문제 해결에 있어 기본이자 핵심 도구입니다.
