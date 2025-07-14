# 🧹 CleanCode 설명서

##### 🗓️ 2025.05.29
##### 📝 Writer : Moon19ht

---

## 📚 목차

1. [의미 있는 이름 사용](#1-의미-있는-이름-사용)
2. [함수는 하나의 일만 하게](#2-함수는-하나의-일만-하게)
3. [주석보다는 코드로 설명](#3-주석보다는-코드로-설명)
4. [일관된 형식과 들여쓰기](#4-일관된-형식과-들여쓰기)
5. [오류 처리](#5-오류-처리)
6. [클래스와 객체](#6-클래스와-객체)
7. [연산자 오버로딩과 매직 메서드](#7-연산자-오버로딩과-매직-메서드)
8. [반복자(Iterator)와 제너레이터 활용](#8-반복자iterator와-제너레이터-활용)
9. [테스트와 자동화](#9-테스트와-자동화)
10. [코드 포맷팅과 스타일](#10-코드-포맷팅과-스타일)

---

**클린 코드는 읽기 쉽고, 유지보수가 쉬우며, 오류가 적은 코드를 의미합니다. 실무에서는 협업, 테스트, 확장성까지 고려한 코드 품질이 중요합니다.**

## 1. 의미 있는 이름 사용

```python
# 나쁜 예시
def f(a):
    return a * 2

# 좋은 예시
def double(number):
    return number * 2
```
- 함수와 변수 이름은 역할을 명확히 드러내야 합니다.
- 이름에는 축약어, 모호한 단어 대신 구체적이고 일관된 네이밍을 사용하세요.
- 예: `user_list` (O), `ul` (X)

#### TIP
- 불필요한 접두사/접미사(예: get, set, data 등) 남용을 피하세요.
- 네이밍 컨벤션(스네이크 케이스, 카멜 케이스 등)을 프로젝트 전체에서 통일하세요.

---

## 2. 함수는 하나의 일만 하게

```python
# 나쁜 예시
def process_data(data):
    clean = [d.strip() for d in data]
    print(clean)
    return len(clean)

# 좋은 예시
def clean_data(data):
    return [d.strip() for d in data]

def print_data(data):
    print(data)

def count_data(data):
    return len(data)
```
- 함수는 한 가지 책임만 가져야 하며, 여러 작업을 분리해야 합니다.
- 함수가 여러 동작(입력, 처리, 출력 등)을 동시에 하면 테스트와 재사용이 어렵습니다.

#### TIP
- 함수 길이가 길어지면 분리할 수 있는 부분이 없는지 점검하세요.
- 함수명은 동사+명사(예: `save_file`, `send_email`)로 작성하면 의도가 명확해집니다.

---

## 3. 주석은 오해 방지용으로만

```python
# 나쁜 예시
x = 10  # x에 10을 할당

# 좋은 예시
max_retry_count = 10  # 최대 재시도 횟수
```
- 코드 자체가 명확하다면 불필요한 주석은 피합니다.
- 주석은 "왜"(의도, 예외 상황 등)를 설명할 때만 사용하세요.

#### TIP
- 코드 변경 시 주석도 반드시 함께 수정하세요.
- TODO, FIXME, NOTE 등 주석 태그를 일관되게 사용하면 협업에 도움이 됩니다.

---

## 4. Magic Number 대신 상수 사용

```python
# 나쁜 예시
if score > 60:
    print("합격")

# 좋은 예시
PASS_SCORE = 60
if score > PASS_SCORE:
    print("합격")
```
- 의미 없는 숫자 대신 상수를 사용해 의도를 명확히 합니다.
- 상수는 파일 상단 또는 별도 설정 파일에 모아 관리하세요.

#### TIP
- 상수명은 대문자+언더스코어로 작성합니다(예: `MAX_SIZE`).
- Magic String(의미 없는 문자열)도 상수로 관리하세요.

---

## 5. 에러 처리는 구체적으로

```python
# 나쁜 예시
try:
    result = 10 / x
except:
    print("에러 발생")

# 좋은 예시
try:
    result = 10 / x
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
```
- 예외 처리는 구체적으로 작성해 예기치 않은 오류를 방지합니다.
- 모든 예외를 포괄적으로 처리하면 버그를 찾기 어렵고, 디버깅이 힘들어집니다.

#### TIP
- 필요하다면 `except Exception as e:`로 에러 메시지를 로깅하세요.
- finally 블록을 활용해 자원 정리(파일 닫기 등)를 잊지 마세요.

---

## 6. 리플렉션(Reflection) 활용

- 리플렉션을 사용하면 동적으로 객체의 속성이나 메서드에 접근할 수 있습니다.
- 코드의 유연성과 재사용성을 높이지만, 남용은 피해야 합니다.

```python
class User:
    def __init__(self, name):
        self.name = name

user = User("Alice")
# 나쁜 예시: 직접 속성 접근
print(user.name)

# 좋은 예시: getattr 사용
print(getattr(user, "name", "Unknown"))
```

#### TIP
- 리플렉션은 동적 속성 접근, ORM, 플러그인 시스템 등에서 유용합니다.
- 잘못 사용하면 코드 추적이 어려워지고, IDE 자동완성/정적 분석이 힘들어집니다.

---

## 7. 연산자 중복(Operator Overloading)

- 연산자 중복을 통해 객체 간 연산을 직관적으로 표현할 수 있습니다.
- 의미에 맞는 연산자만 오버라이드해야 가독성이 높아집니다.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# 사용 예시
v1 = Vector(1, 2)
v2 = Vector(3, 4)
result = v1 + v2  # Vector(4, 6)
print(result)
```
- `__str__`, `__repr__`, `__eq__`, `__lt__` 등도 상황에 맞게 구현하면 객체 사용성이 높아집니다.

#### TIP
- 연산자 오버로딩은 수학적/논리적 의미가 명확할 때만 사용하세요.
- 오버라이드 시 타입 체크(예: isinstance)로 예외 상황을 방지하세요.

---

## 8. 반복자(Iterator)와 제너레이터 활용

- 반복자와 제너레이터를 사용하면 메모리 효율적이고, 읽기 쉬운 코드를 작성할 수 있습니다.

```python
# 나쁜 예시: 리스트로 모든 값을 메모리에 저장
squares = [x * x for x in range(1000000)]

# 좋은 예시: 제너레이터 사용
def generate_squares():
    for x in range(1000000):
        yield x * x

for square in generate_squares():
    if square > 100:
        break
    print(square)
```
- 제너레이터는 대용량 데이터 처리, 스트림 처리, 파이프라인 구현 등에 적합합니다.

#### TIP
- `yield from`을 사용하면 중첩 제너레이터를 간결하게 연결할 수 있습니다.
- 반복자 프로토콜(`__iter__`, `__next__`)을 직접 구현하면 커스텀 반복 객체도 만들 수 있습니다.

---

## 9. 테스트와 자동화

- 테스트 코드를 작성하면 코드 품질과 유지보수성이 크게 향상됩니다.
- 단위 테스트는 `unittest`, `pytest` 등 프레임워크를 활용하세요.

```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
```

#### TIP
- 테스트 함수명은 `test_`로 시작하세요.
- CI(지속적 통합) 도구와 연동하면 배포 전 자동 테스트가 가능합니다.

---

## 10. 코드 포맷팅과 스타일

- 코드 스타일을 통일하면 협업과 리뷰가 쉬워집니다.
- `black`, `flake8`, `isort` 등 자동화 도구를 활용하세요.

#### TIP
- 들여쓰기는 4칸, 한 줄 최대 79~100자 권장
- 불필요한 공백, 중복 코드, 미사용 변수는 제거하세요.

---

## 마무리 및 실전 TIP

- 클린 코드는 "나"가 아닌 "팀"과 "미래의 나"를 위한 투자입니다.
- 리뷰, 리팩터링, 문서화, 테스트를 습관화하세요.
- 실무에서는 코드리뷰, 협업툴, 자동화 테스트, 배포 파이프라인 등과 연계해 품질을 높입니다.
