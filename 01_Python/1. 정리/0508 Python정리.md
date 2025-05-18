# 🐍 파이썬(Python) 기초 개념 설명서

##### 🗓️ 2025.05.08
##### 📝 Writer : Moon19ht

---

## 📚 목차

- [� 파이썬(Python) 기초 개념 설명서](#-파이썬python-기초-개념-설명서)
        - [🗓️ 2025.05.08](#️-20250508)
        - [📝 Writer : Moon19ht](#-writer--moon19ht)
  - [📚 목차](#-목차)
  - [📌 1. 객체지향 - 클래스 (사용자가 만드는 데이터 타입)](#-1-객체지향---클래스-사용자가-만드는-데이터-타입)
  - [📌 2. 추상화 - 클래스](#-2-추상화---클래스)
  - [📌 3. 은닉화 (Encapsulation)](#-3-은닉화-encapsulation)
  - [📌 4. 상속성 (Inheritance)](#-4-상속성-inheritance)
  - [📌 5. 다형성 (Polymorphism)](#-5-다형성-polymorphism)
  - [📌 6. 🎮 객체지향 숫자 야구 게임 예제 (with 주석)](#-6--객체지향-숫자-야구-게임-예제-with-주석)
  - [📌 7. 📊 객체지향 성적 처리 시스템 예제](#-7--객체지향-성적-처리-시스템-예제)
  - [🔚 마무리](#-마무리)
  - [⏭️ 다음으로는...](#️-다음으로는)

---

## 📌 1. 객체지향 - 클래스 (사용자가 만드는 데이터 타입)

- `int`, `str`, `float`처럼 **클래스**도 하나의 데이터 타입
- 클래스 기반 객체는 **힙(Heap) 메모리**에 생성되며, 변수는 객체의 **참조값(주소)**를 저장
- 객체 내부 요소 접근은 `.`(dot) 연산자 사용
- 생성자 메서드 이름은 `__init__`이며, **첫 번째 인자**로 **self**를 사용
    - self는 객체 자기 자신을 가리킴
    - 꼭 `self`일 필요는 없지만, 관례적으로 사용

---

## 📌 2. 추상화 - 클래스

- 사용자는 **내부 구현을 몰라도 객체를 사용할 수 있음**
- 복잡한 내부 구조는 숨기고 필요한 기능만 외부에 제공
- 추상화가 잘 될수록 사용은 쉬워지지만, 개발은 어려워짐
- 소프트웨어 설계에서 추상화를 위한 **디자인 패턴**이 존재 (예: 23가지 GoF 패턴 등)

---

## 📌 3. 은닉화 (Encapsulation)

- **데이터 보호**를 위한 접근 제한
- 다른 언어에서는 `private`, `public` 키워드로 접근 권한을 설정
- Python은 기본적으로 **모든 멤버가 public**
    - 변수나 함수 앞에 `__`(언더스코어 2개)를 붙이면 **비공개(private)** 속성

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # 직접 접근은 제한됨

    def get_salary(self):
        return self.__salary
```

---

## 📌 4. 상속성 (Inheritance)

- 부모 클래스의 속성과 메서드를 자식 클래스가 **물려받아 재사용**
- 코드 중복 제거 및 구조화에 유리

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()  # 부모 클래스 메서드 사용
```

---

## 📌 5. 다형성 (Polymorphism)

- 같은 이름의 메서드가 **클래스마다 다른 동작을 함**
- 파이썬에서는 메서드 오버로딩이 명시적으로 지원되지 않지만, 매개변수 기본값과 `*args`, `**kwargs` 등을 통해 **유연한 동작** 구현 가능

```python
class Person:
    def __init__(self, name="Unknown"):
        self.name = name
```

---

## 📌 6. 🎮 객체지향 숫자 야구 게임 예제 (with 주석)

```python
import random

class Player:
    def get_input(self):
        while True:
            guess = input("세 개의 숫자 입력 (공백으로 구분): ")
            guess = list(map(int, guess.strip().split()))
            if len(guess) == 3 and len(set(guess)) == 3 and all(1 <= x <= 9 for x in guess): # 중복 없이 3자리 숫자, 1~9 사이
                return guess
            print("❌ 입력 오류: 1~9 사이의 중복되지 않는 숫자 3개를 입력하세요.")

class Computer:
    def generate_numbers(self):
        return random.sample(range(1, 10), 3)

class BaseballGame:
    def __init__(self):
        self.computer = Computer()
        self.player = Player()
        self.answer = self.computer.generate_numbers()

    def get_score(self, guess):
        strike = sum([1 for i in range(3) if guess[i] == self.answer[i]])
        ball = len(set(guess) & set(self.answer)) - strike
        return strike, ball

    def play(self):
        print("⚾ 숫자 야구 게임 시작!")
        attempts = 0
        while True:
            guess = self.player.get_input()
            attempts += 1
            strike, ball = self.get_score(guess)
            print(f"결과: {strike} Strike, {ball} Ball")

            if strike == 3:
                print(f"🎉 정답입니다! 시도 횟수: {attempts}")
                break

if __name__ == "__main__":
    game = BaseballGame()
    game.play()
```

---

## 📌 7. 📊 객체지향 성적 처리 시스템 예제

```python
class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def total(self):
        return self.kor + self.eng + self.math

    def average(self):
        return self.total() / 3

    def __str__(self):
        return f"{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total()}\t{self.average():.2f}"

class GradeManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_all(self):
        print("이름\t국어\t영어\t수학\t총점\t평균")
        for student in self.students:
            print(student)

if __name__ == "__main__":
    gm = GradeManager()
    gm.add_student(Student("홍길동", 90, 85, 95))
    gm.add_student(Student("김철수", 80, 75, 70))
    gm.show_all()
```

---

## 🔚 마무리

| 개념 | 설명 |
|------|------|
| 클래스 | 사용자 정의 데이터 타입 |
| 추상화 | 내부 구현을 숨기고 인터페이스만 제공 |
| 은닉화 | 접근 제어로 데이터 보호 |
| 상속 | 코드 재사용 및 계층 구조 |
| 다형성 | 동일 인터페이스, 다양한 구현 |
| 모듈 | 연관된 클래스와 함수를 묶어 재사용 가능한 단위 (.py 파일) |
| 게임 예제 | 클래스로 역할 분리 및 구조화된 로직 구현 |
| 성적처리 예제 | 데이터, 로직 분리로 유지보수성 향상 |

---

## ⏭️ 다음으로는...
- 파일 읽고 쓰기, 직렬화, 역직렬화 등...

---

[⏮️ 이전 문서](./0507%20Python정리.md) [다음 문서 ⏭️](./0509%20Python정리.md)