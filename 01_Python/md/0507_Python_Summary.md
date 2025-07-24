# 🐍 파이썬(Python) 기초 개념 설명서

##### 🗓️ 2025.05.07
##### 📝 Writer : Moon19ht

---

## 📚 목차

1. [`class` (클래스)](#1-class-클래스)
2. [모듈 (Module)](#2-모듈-module)
3. [객체지향으로 짜는 가위바위보 게임](#3-객체지향으로-짜는-가위바위보-게임)

---

## 1. `class` (클래스)

### 정의
- 클래스는 **객체를 생성하기 위한 설계도**
- 속성(데이터)과 메서드(함수)를 포함함
- 사용자 정의 자료형을 만드는 핵심 도구

### 구조
```python
class ClassName:
    def __init__(self, 매개변수):
        self.속성 = 매개변수

    def method(self):
        # 동작 정의
```

### 예시
```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}!")

p = Person("Alice")
p.greet()  # 출력: Hello, I am Alice!
```

#### TIP
- 클래스명은 대문자로 시작하는 것이 관례입니다.
- `__init__`은 생성자 메서드로, 객체가 생성될 때 자동으로 호출됩니다.
- self는 인스턴스 자신을 가리키며, 반드시 첫 번째 인자로 선언해야 합니다.

---

## 2. 모듈 (Module)

### 정의
- `.py` 파일 하나가 모듈
- 변수, 함수, 클래스 등을 정의하고 재사용 가능
- `import`를 통해 불러올 수 있음

### 사용 방법
#### 1) `mymodule.py` 라는 파일 생성
```python
def add(a, b):
    return a + b
```

#### 2) 다른 파일에서 import
```python
import mymodule
print(mymodule.add(3, 4))  # 출력: 7
```

> 모듈을 모아놓은 폴더 = **패키지(package)** (디렉토리에 `__init__.py` 포함)

#### TIP
- 표준 라이브러리(예: `math`, `os`, `sys`)도 모두 모듈입니다.
- 모듈 경로가 다를 경우 `sys.path`를 수정하거나, 같은 폴더에 두어야 import가 가능합니다.

---

## 3. 객체지향으로 짜는 가위바위보 게임

### 클래스 기반 구성
- `Player`: 사용자 입력 처리
- `Computer`: 랜덤 선택
- `Game`: 전체 흐름 제어

---

### 전체 코드
```python
import random

class Player:
    def get_choice(self):
        while True:
            choice = input("가위, 바위, 보 중 하나를 선택하세요: ")
            if choice in ['가위', '바위', '보']:
                return choice
            print("올바른 선택이 아닙니다.")

class Computer:
    def get_choice(self):
        return random.choice(['가위', '바위', '보'])

class Game:
    def __init__(self):
        self.player = Player()
        self.computer = Computer()

    def decide_winner(self, user, comp):
        if user == comp:
            return "무승부"
        wins = {
            '가위': '보',
            '바위': '가위',
            '보': '바위'
        }
        return "플레이어 승!" if wins[user] == comp else "컴퓨터 승!"

    def play(self):
        print("가위바위보 게임 시작!")
        user_choice = self.player.get_choice()
        comp_choice = self.computer.get_choice()

        print(f"플레이어: {user_choice}")
        print(f"컴퓨터: {comp_choice}")
        print(f"결과: {self.decide_winner(user_choice, comp_choice)}")

if __name__ == "__main__":
    game = Game()
    game.play()
```

#### TIP
- 입력값 검증을 통해 예외 상황을 방지할 수 있습니다.
- 게임 로직을 함수/클래스로 분리하면 유지보수와 확장성이 좋아집니다.
- 실무에서는 테스트 코드와 예외 처리를 추가하는 것이 좋습니다.

---

## 클래스 설계 요약

| 클래스 | 책임(Role)            | 주요 메서드          |
|--------|------------------------|-----------------------|
| `Player`   | 사용자로부터 입력 받기  | `get_choice()`        |
| `Computer` | 랜덤하게 선택하기     | `get_choice()`        |
| `Game`     | 전체 게임 흐름 제어   | `play()`, `decide_winner()` |

---

## 정리

| 개념     | 핵심 설명 |
|----------|-----------|
| 클래스   | 객체를 만들기 위한 청사진 (설계도) |
| 모듈     | 함수/클래스를 모아놓은 `.py` 파일 |
| OOP 가위바위보 | 클래스 분리 → 역할 나누기 → 재사용성/유지보수 향상 |
