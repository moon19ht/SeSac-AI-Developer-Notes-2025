# 🧩 파이썬(Python) 심화

##### 🗓️ 2025.05.13
##### 📝 Writer : Moon19ht

---

## 📚 목차

1. [상속 (Inheritance)](#1-상속-inheritance)
2. [다중 상속 (Multiple Inheritance)](#2-다중-상속-multiple-inheritance)
3. [다이아몬드 상속 (Diamond Inheritance)](#3-다이아몬드-상속-diamond-inheritance)
4. [패키지 (Package)](#4-패키지-package)
5. [내장 함수 (Built-in Functions)](#5-내장-함수-built-in-functions)
6. [표준 라이브러리 (Standard Library)](#6-표준-라이브러리-standard-library)
7. [멀티 프로세싱 (Multiprocessing)](#7-멀티-프로세싱-multiprocessing)

---

## 1. 상속 (Inheritance)

### 개념
- 기존 클래스의 기능을 **재사용하고 확장** 할 수 있는 객체지향의 핵심 개념
- **부모 클래스(Parent)** 의 속성과 메서드를 **자식 클래스(Child)** 가 물려받음

### 문법 및 예시
```python
class Animal:
    def speak(self):
        print("동물이 소리를 냅니다.")

class Dog(Animal):  # Animal을 상속받음
    def bark(self):
        print("멍멍!")

d = Dog()
d.speak()  # 부모 클래스의 메서드 사용
d.bark()
```

#### TIP
- 상속받은 메서드를 오버라이딩(재정의)할 수 있습니다.
- super()를 사용하면 부모 클래스의 메서드를 명시적으로 호출할 수 있습니다.

---

## 2. 다중 상속 (Multiple Inheritance)

### 개념
- 두 개 이상의 클래스로부터 **속성과 메서드**를 동시에 상속받을 수 있음
- 순서에 따라 **MRO(Method Resolution Order)** 적용

### 예시
```python
class A:
    def do_a(self):
        print("A 동작")

class B:
    def do_b(self):
        print("B 동작")

class C(A, B):
    pass

c = C()
c.do_a()
c.do_b()
```

> `C`는 `A`, `B` 모두를 상속받아 두 클래스의 기능을 동시에 사용할 수 있음.

#### TIP
- 다중 상속은 복잡성을 높일 수 있으므로 설계에 주의하세요.
- MRO는 클래스명.__mro__로 확인할 수 있습니다.

---

## 3. 다이아몬드 상속 (Diamond Inheritance)

### 개념
- 상속 구조가 **마름모 형태**로 구성되어, **같은 조상 클래스가 중복 상속되는 구조**
- Python은 **MRO(Method Resolution Order)** 규칙에 따라 중복을 해결

### 예시
```python
class A:
    def whoami(self):
        print("A")

class B(A):
    def whoami(self):
        print("B")

class C(A):
    def whoami(self):
        print("C")

class D(B, C):
    pass

d = D()
d.whoami()  # 출력: B → MRO에 따라 좌측 우선
```

> `D -> B -> C -> A` 순으로 메서드 탐색 (좌측 클래스 우선)

#### TIP
- 다이아몬드 상속 구조에서는 super()와 MRO를 잘 이해하고 사용해야 예기치 않은 동작을 방지할 수 있습니다.

---

## 4. 패키지 (Package)

### 개념
- 여러 개의 모듈을 **폴더 단위로 구조화한 단위**
- 폴더에 `__init__.py` 파일이 존재하면 Python은 해당 폴더를 패키지로 인식

### 구조 예시
```
my_package/
├── __init__.py
├── module1.py
└── module2.py
```

### 사용 예시
```python
from my_package import module1
module1.function()
```

> `__init__.py`를 통해 패키지 초기화 로직 정의 가능

#### TIP
- 패키지 내 상대 경로 import는 from . import module 형식으로 사용합니다.
- 패키지 구조를 잘 설계하면 대규모 프로젝트 관리가 쉬워집니다.

---

## 5. 내장 함수 (Built-in Functions)

### 개념
- Python 인터프리터에 **기본 내장**된 함수
- import 없이 바로 사용 가능

### 주요 함수 예시

| 함수 | 설명 |
|------|------|
| `len()` | 길이 반환 |
| `type()` | 자료형 확인 |
| `range()` | 반복 가능한 수열 생성 |
| `print()` | 출력 |
| `input()` | 사용자 입력 |
| `sum()` | 합계 계산 |
| `max()`, `min()` | 최대/최소값 반환 |

#### TIP
- 내장 함수 전체 목록은 `dir(__builtins__)`로 확인할 수 있습니다.
- 내장 함수는 오버라이딩(동일 이름 함수 정의) 시 주의해야 합니다.

---

## 6. 표준 라이브러리 (Standard Library)

### 개념
- Python에서 기본 제공하는 모듈들의 집합
- **추가 설치 없이** `import`만으로 사용 가능

### 주요 표준 라이브러리

| 모듈 | 용도 |
|------|------|
| `math` | 수학 연산 |
| `datetime` | 날짜/시간 처리 |
| `os` | 운영체제 기능 |
| `sys` | 시스템 인자, 환경 |
| `random` | 난수 생성 |
| `json` | JSON 처리 |
| `collections` | 고급 자료구조 |
| `re` | 정규 표현식 |
| `itertools` | 반복자 처리 도구 |

### 예시
```python
import math
print(math.sqrt(16))  # 4.0

import datetime
print(datetime.datetime.now())
```

#### TIP
- 표준 라이브러리 공식 문서: https://docs.python.org/ko/3/library/index.html
- 외부 패키지와 이름이 겹치지 않도록 주의하세요.

---

## 7. 멀티 프로세싱 (Multiprocessing)

### 개념
- CPU 코어를 활용하여 **동시에 여러 작업을 병렬 처리**
- `threading`은 GIL(Global Interpreter Lock)로 인해 병렬성이 제한되지만, `multiprocessing`은 **각 프로세스가 별도 메모리 공간에서 병렬 실행**되어 CPU를 효율적으로 활용 가능

### 모듈: `multiprocessing`

### 예시
```python
from multiprocessing import Process

def worker(name):
    print(f"{name} 작업 중...")

if __name__ == "__main__":
    p1 = Process(target=worker, args=("프로세스 1",))
    p2 = Process(target=worker, args=("프로세스 2",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
```

> `start()`는 프로세스 실행 시작, `join()`은 해당 프로세스가 끝날 때까지 대기

#### TIP
- 멀티프로세싱은 데이터 공유가 어렵고, 프로세스 간 통신(Queue, Pipe 등)이 필요할 수 있습니다.
- 대용량 데이터 처리, CPU 집약적 작업에 적합합니다.

---

## 정리 

| 개념 | 설명 | 키워드 |
|------|------|--------|
| 상속 | 부모 클래스 기능 재사용 | `class Child(Parent)` |
| 다중 상속 | 여러 부모 클래스 상속 | `class C(A, B)` |
| 다이아몬드 상속 | 중복 상속 경로를 명확하게 결정 | `MRO`, `super()` |
| 패키지 | 모듈 묶음 폴더 | `__init__.py`, `import` |
| 내장 함수 | 기본 제공 함수 | `len()`, `sum()` |
| 표준 라이브러리 | 기본 제공 모듈 | `math`, `datetime`, `os` |
| 멀티 프로세싱 | CPU 병렬 작업 처리 | `multiprocessing`, `Process`, `start()`, `join()` |
