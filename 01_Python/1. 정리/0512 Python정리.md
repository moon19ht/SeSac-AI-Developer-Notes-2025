# 🧩 파이썬(Python) 심화

##### 🗓️ 2025.05.12
##### 📝 Writer : Moon19ht

---

## 📚 목차

- [🧩 파이썬(Python) 심화](#-파이썬python-심화)
        - [🗓️ 2025.05.12](#️-20250512)
        - [📝 Writer : Moon19ht](#-writer--moon19ht)
  - [📚 목차](#-목차)
  - [📌 1. 클래스 메소드 (`@classmethod`)](#-1-클래스-메소드-classmethod)
    - [✅ 개념](#-개념)
    - [✅ 문법](#-문법)
    - [✅ 호출 방법](#-호출-방법)
  - [📌 2. 스태틱 메소드 (`@staticmethod`)](#-2-스태틱-메소드-staticmethod)
    - [✅ 개념](#-개념-1)
    - [✅ 문법](#-문법-1)
    - [✅ 호출 방법](#-호출-방법-1)
  - [📌 3. 싱글톤 패턴 (Singleton Pattern)](#-3-싱글톤-패턴-singleton-pattern)
    - [✅ 개념](#-개념-2)
    - [✅ 예시](#-예시)
    - [✅ 사용 예시](#-사용-예시)
  - [📌 4. 데코레이터 (Decorator)](#-4-데코레이터-decorator)
    - [✅ 개념](#-개념-3)
    - [✅ 문법](#-문법-2)
    - [✅ 출력 결과](#-출력-결과)
  - [📌 5. 클로저 (Closure)](#-5-클로저-closure)
    - [✅ 개념](#-개념-4)
    - [✅ 예시](#-예시-1)
  - [📚 클래스 메소드 vs 스태틱 메소드](#-클래스-메소드-vs-스태틱-메소드)
  - [🔚 마무리](#-마무리)
  - [⏭️ 다음으로는...](#️-다음으로는)

---

## 📌 1. 클래스 메소드 (`@classmethod`)

### ✅ 개념
- 클래스 자체를 인자로 받는 메소드
- 인스턴스가 아닌 **클래스 레벨에서 동작**
- 주로 **클래스 속성에 접근하거나 클래스 기반 로직(예: 팩토리 메서드)** 에서 사용

### ✅ 문법
```python
class MyClass:
    count = 0

    @classmethod
    def increase_count(cls):
        cls.count += 1
```

### ✅ 호출 방법
```python
MyClass.increase_count()
```

---

## 📌 2. 스태틱 메소드 (`@staticmethod`)

### ✅ 개념
- 클래스와 인스턴스 **어느 것도 받지 않는** 메소드
- 일반 함수와 동일하지만, **클래스 이름공간에 논리적으로 속하는 경우** 정의

### ✅ 문법
```python
class Math:
    @staticmethod
    def add(x, y):
        return x + y
```

### ✅ 호출 방법
```python
Math.add(3, 5)  # 8
```

---

## 📌 3. 싱글톤 패턴 (Singleton Pattern)

### ✅ 개념
- 클래스의 인스턴스가 **단 하나만** 존재하도록 보장하는 패턴
- 전역 상태 유지, 설정 객체 등에 유용

### ✅ 예시
```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

### ✅ 사용 예시
```python
a = Singleton()
b = Singleton()
print(a is b)  # True
```

---

## 📌 4. 데코레이터 (Decorator)

### ✅ 개념
- 함수를 **변경하지 않고** 기능을 추가할 수 있는 **함수**
- 다른 함수를 인자로 받고, 새로운 함수를 반환

### ✅ 문법
```python
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def greet():
    print("Hello")

greet()
```

### ✅ 출력 결과
```
Before
Hello
After
```

---

## 📌 5. 클로저 (Closure)

### ✅ 개념
- 내부 함수가 외부 함수의 지역 변수에 접근하는 함수 구조
- 외부 함수가 종료되어도 변수 상태를 **기억**

### ✅ 예시
```python
def outer(x):
    def inner(y):
        return x + y
    return inner

add5 = outer(5)
print(add5(10))  # 15
```

> `x`는 `outer()`의 지역 변수이지만, `inner()` 내부에서 계속 참조 가능 (렉시컬 스코프)

---

## 📚 클래스 메소드 vs 스태틱 메소드

| 구분 | 클래스 메소드 | 스태틱 메소드 |
|------|----------------|----------------|
| 정의 방식 | `@classmethod` | `@staticmethod` |
| 첫 인자 | `cls` (클래스) | 없음 |
| 목적 | 클래스 상태를 변경하거나 접근 | 유틸리티 함수 정의 |
| 사용 예 | 팩토리 메서드, 설정값 변경 | 수학 계산, 유틸 함수 등 |

---

## 🔚 마무리

| 개념 | 설명 | 키워드 |
|------|------|--------|
| 클래스 메소드 | 클래스 속성 접근 | `@classmethod`, `cls` |
| 스태틱 메소드 | 독립적인 유틸리티 함수 | `@staticmethod` |
| 싱글톤 패턴 | 하나의 인스턴스만 생성 | `__new__`, `_instance` |
| 데코레이터 | 함수 기능을 감싸서 확장 | `@decorator` |
| 클로저 | 외부 스코프 변수에 접근 가능한 내부 함수 | 함수 중첩, 렉시컬 스코프 |

---

## ⏭️ 다음으로는...
- 상속, 다중 상속, 다이아몬드 상속, 패키지, 내장 함수, 표준 라이브러리, 멀티 프로세싱...

---

[⏮️ 이전 문서](./0509%20Python정리.md) [다음 문서 ⏭️](./0513%20Python정리.md)