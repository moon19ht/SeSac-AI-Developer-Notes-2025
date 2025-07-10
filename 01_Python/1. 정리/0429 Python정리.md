# 🐍 파이썬(Python) 기초 개념 설명서

##### 🗓️ 2025.04.29
##### 📝 Writer : Moon19ht

---

## 📚 목차


- [📌 1. 함수의 매개변수 (Function Parameters)](#-1-함수의-매개변수-function-parameters)
- [📌 2. lambda 함수 (익명 함수)](#-2-lambda-함수-익명-함수)
- [📌 3. filter() 함수](#-3-filter-함수)
- [📌 4. map() 함수](#-4-map-함수)
- [📌 5. sort() 메서드](#-5-sort-메서드)
- [📌 6. sorted() 함수](#-6-sorted-함수)
- [🔚 마무리](#-마무리)

---

## 📌 1. 함수의 매개변수 (Function Parameters)

Python 함수는 다양한 방식으로 매개변수를 받을 수 있습니다.

### ✅ 기본 구조
```python
def greet(name):
    print(f"Hello, {name}!")
```

### 매개변수 종류
| 구분 | 설명 | 예시 |
|------|------|------|
| 위치 인자 (Positional) | 순서대로 값을 전달 | `greet("Alice")` |
| 키워드 인자 (Keyword) | 이름으로 지정하여 전달 | `greet(name="Bob")` |
| 기본값 인자 (Default) | 기본값 지정 가능 | `def greet(name="Guest")` |
| 가변 인자 (`*args`) | 개수가 정해지지 않은 인자 | `def func(*args):` |
| 키워드 가변 인자 (`**kwargs`) | 키워드로 전달된 가변 인자 | `def func(**kwargs):` |

---

## 📌 2. lambda 함수 (익명 함수)

한 줄로 정의하는 **간단한 익명 함수**

### ✅ 기본 문법
```python
lambda 인자1, 인자2: 표현식
```

### ✅ 예시
```python
add = lambda x, y: x + y
print(add(3, 5))  # 출력: 8
```

> ❗ 일반적으로 `map()`, `filter()` 같은 고차 함수에서 자주 사용됨.

---

## 📌 3. filter() 함수

조건에 맞는 요소만 걸러내는 함수

### ✅ 문법
```python
filter(함수, 반복가능한 객체)
```

### ✅ 예시
```python
nums = [1, 2, 3, 4, 5]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)  # 출력: [2, 4]
```

---

## 📌 4. map() 함수

각 요소에 함수를 적용한 결과를 반환

### ✅ 문법
```python
map(함수, 반복가능한 객체)
```

### ✅ 예시
```python
nums = [1, 2, 3]
squared = list(map(lambda x: x ** 2, nums))
print(squared)  # 출력: [1, 4, 9]
```

---

## 📌 5. sort() 메서드

리스트를 제자리에서 정렬

### ✅ 문법
```python
리스트.sort(key=함수, reverse=Boolean)
```

### ✅ 예시
```python
names = ['Charlie', 'Alice', 'Bob']
names.sort()
print(names)  # 출력: ['Alice', 'Bob', 'Charlie']
```

> `sort()`는 **원본을 직접 변경**하며 `None`을 반환함.

---

## 📌 6. sorted() 함수

정렬된 **새 리스트** 를 반환

### ✅ 문법
```python
sorted(반복가능한 객체, key=함수, reverse=Boolean)
```

### ✅ 예시
```python
names = ['Charlie', 'Alice', 'Bob']
sorted_names = sorted(names)
print(sorted_names)  # 출력: ['Alice', 'Bob', 'Charlie']
```

> `sorted()`는 원본을 변경하지 않음.


---

## 🔚 마무리

| 함수 | 주요 특징 | 반환 방식 | 원본 변경 여부 |
|------|-----------|-----------|----------------|
| `lambda` | 간단한 익명 함수 | 함수 객체 | - |
| `filter()` | 조건에 맞는 요소 필터링 | filter 객체 → list로 변환 | ❌ |
| `map()` | 각 요소 함수 적용 | map 객체 → list로 변환 | ❌ |
| `sort()` | 리스트 제자리 정렬  | `None` 반환 | ✅ |
| `sorted()` | 정렬된 새 리스트 반환 | 새 리스트 반환 | ❌ |
