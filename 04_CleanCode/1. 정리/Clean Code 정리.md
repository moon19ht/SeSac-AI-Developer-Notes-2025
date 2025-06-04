# 🧹 CleanCode 설명서

##### 🗓️ 2025.05.29
##### 📝 Writer : Moon19ht

---

클린 코드는 읽기 쉽고, 유지보수가 쉬우며, 오류가 적은 코드를 의미합니다.

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

## 3. 주석은 오해 방지용으로만

```python
# 나쁜 예시
x = 10  # x에 10을 할당

# 좋은 예시
max_retry_count = 10  # 최대 재시도 횟수
```
- 코드 자체가 명확하다면 불필요한 주석은 피합니다.

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

# 사용 예시
v1 = Vector(1, 2)
v2 = Vector(3, 4)
result = v1 + v2  # Vector(4, 6)
```

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

---


