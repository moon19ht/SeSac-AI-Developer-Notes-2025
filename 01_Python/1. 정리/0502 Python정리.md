# 🐍 파이썬(Python) 기초 개념 설명서

##### 🗓️ 2025.05.02
##### 📝 Writer : Moon19ht

---

## 📚 목차


- [🔚 마무리](#-마무리)
- [⏭️ 다음으로는...](#️-다음으로는)
- [⏮️ 이전 문서](./0430%20Python정리.md) [다음 문서 ⏭️](./0507%20Python정리.md)

---

## 📌 1. `set()` 함수

### ✅ 정의
- **중복을 허용하지 않는** 집합 자료형
- 순서가 없으며, 빠른 검색과 집합 연산 가능

### ✅ 주요 특징
- 중복 제거
- 합집합, 교집합, 차집합 등의 집합 연산 지원
- `list` → `set`으로 변환 가능

### ✅ 예시
```python
s = set([1, 2, 3, 2, 1])
print(s)  # 출력: {1, 2, 3}

# 요소 추가
s.add(4)

# 요소 제거
s.remove(2)

# 집합 연산
a = set([1, 2, 3])
b = set([2, 3, 4])

print(a | b)  # 합집합: {1, 2, 3, 4}
print(a & b)  # 교집합: {2, 3}
print(a - b)  # 차집합: {1}
```

---

## 📌 2. 2차원 배열 (리스트의 리스트)

### ✅ 개념
- Python에는 다차원 배열 자료형이 없으므로 **리스트 안에 리스트**를 사용
- 행과 열 개념으로 데이터 구성 가능

### ✅ 생성 방법
```python
# 3행 4열의 2차원 배열 (모두 0으로 초기화)
rows, cols = 3, 4
matrix = [[0]*cols for _ in range(rows)]
```

### ✅ 접근 및 수정
```python
matrix[0][1] = 5  # 1행 2열에 5 대입

# 전체 출력
for row in matrix:
    print(row)
```

### ✅ 예시
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2])  # 출력: 6
```

---

## 📌 3. 컴퓨터와 숫자 야구 게임 만들기

### ✅ 게임 규칙
- 컴퓨터가 1~9 사이의 서로 다른 임의의 세 숫자를 생성
- 사용자는 3자리 숫자를 추측
- 각 라운드마다 **Strike** (자리수와 숫자 모두 맞춤), **Ball** (숫자만 맞춤)을 판정
- 3스트라이크면 게임 종료

### ✅ 게임 흐름
1. 컴퓨터 숫자 생성 (중복 X)
2. 사용자 입력
3. 스트라이크/볼 판단
4. 반복

### ✅ 예시 코드
```python
import random

def generate_numbers():
    return random.sample(range(1, 10), 3)

def check_guess(answer, guess):
    strike = ball = 0
    for i in range(3):
        if guess[i] == answer[i]:
            strike += 1
        elif guess[i] in answer:
            ball += 1
    return strike, ball

def play_game():
    answer = generate_numbers()
    attempts = 0

    print("🎮 숫자 야구 게임 시작!")
    while True:
        guess = input("세 자리 숫자를 입력하세요 (예: 1 2 3): ")
        guess = list(map(int, guess.strip().split()))

        if len(set(guess)) != 3 or any(not 1 <= n <= 9 for n in guess):
            print("❌ 1~9 사이의 서로 다른 숫자 3개를 입력해주세요.")
            continue

        attempts += 1
        strike, ball = check_guess(answer, guess)
        print(f"🔍 결과: {strike} Strike, {ball} Ball")

        if strike == 3:
            print(f"🎉 정답입니다! 시도 횟수: {attempts}번")
            break

play_game()
```

> ⚠ 입력 예외 처리, 중복 숫자 방지, 반복 루프 구성 등 실전 로직 포함

---

## 🔚 마무리

| 주제              | 핵심 내용                                  |
|-------------------|---------------------------------------------|
| `set()`           | 중복 제거, 집합 연산 가능, 순서 없음         |
| 2차원 배열        | 리스트의 리스트, `matrix[row][col]` 접근     |
| 숫자 야구 게임    | 랜덤 숫자 생성 + 사용자 추측 + 반복판정 로직 |

---

## ⏭️ 다음으로는...
- 

---

[⏮️ 이전 문서](./0430%20Python정리.md) [다음 문서 ⏭️](./0507%20Python정리.md)