# 🧩 파이썬(Python) 심화

##### 🗓️ 2025.05.09
##### 📝 Writer : Moon19ht

---

## 📚 목차

- [🧩 파이썬(Python) 심화](#-파이썬python-심화)
        - [🗓️ 2025.05.09](#️-20250509)
        - [📝 Writer : Moon19ht](#-writer--moon19ht)
  - [📚 목차](#-목차)
  - [📌 1. 파일 읽고 쓰기 (Text File I/O)](#-1-파일-읽고-쓰기-text-file-io)
    - [✅ 파일 열기 모드](#-파일-열기-모드)
    - [✅ 텍스트 파일 쓰기](#-텍스트-파일-쓰기)
    - [✅ 텍스트 파일 읽기](#-텍스트-파일-읽기)
  - [📌 2. `.bin` 파일과 바이너리 모드](#-2-bin-파일과-바이너리-모드)
    - [✅ 예시](#-예시)
  - [📌 3. `pickle` 모듈](#-3-pickle-모듈)
    - [✅ 주요 함수](#-주요-함수)
  - [📌 4. 직렬화 (Serialization)](#-4-직렬화-serialization)
    - [✅ 예시: 객체 직렬화](#-예시-객체-직렬화)
  - [📌 5. 역직렬화 (Deserialization)](#-5-역직렬화-deserialization)
    - [✅ 예시: 객체 역직렬화](#-예시-객체-역직렬화)
  - [🔚 마무리](#-마무리)
  - [✅ 주의사항](#-주의사항)
  - [⏭️ 다음으로는...](#️-다음으로는)

---

## 📌 1. 파일 읽고 쓰기 (Text File I/O)

### ✅ 파일 열기 모드

| 모드 | 설명 |
|------|------|
| `'r'` | 읽기 전용 (기본값) |
| `'w'` | 쓰기 전용 (기존 내용 삭제) |
| `'a'` | 이어쓰기 (append) |
| `'x'` | 파일이 없을 때만 쓰기 |
| `'b'` | 바이너리 모드 (텍스트가 아닌 데이터 처리 시 사용) |
| `'t'` | 텍스트 모드 (텍스트 처리 시 사용, 기본값) |

### ✅ 텍스트 파일 쓰기
```python
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("Hello, Python!\n")
    f.write("파일 입출력 예제입니다.\n")
```

### ✅ 텍스트 파일 읽기
```python
with open("example.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
```

---

## 📌 2. `.bin` 파일과 바이너리 모드

- `.bin`은 관례적으로 **이진(binary) 데이터 파일** 확장자
- 텍스트 외에 숫자, 객체, 이미지 등 **비가시적(binary) 데이터** 저장
- `open()` 함수에 `'rb'`, `'wb'` 모드를 사용

### ✅ 예시
```python
with open("data.bin", "wb") as f:
    f.write(b'\x00\x01\x02\x03')  # 16진수 바이트 직접 저장

with open("data.bin", "rb") as f:
    data = f.read()
    print(data)  # 출력: b'\x00\x01\x02\x03'
```

---

## 📌 3. `pickle` 모듈

- Python 객체를 **바이트 형식으로 변환(직렬화)하고 복원(역직렬화)**하는 내장 모듈
- 리스트, 딕셔너리, 클래스 인스턴스 등을 바이너리로 저장/복원 가능
- 확장자: `.pkl`, `.bin`, `.dat` 등

### ✅ 주요 함수

| 함수 | 설명 |
|------|------|
| `pickle.dump(obj, file)` | 객체를 파일에 직렬화 |
| `pickle.load(file)` | 파일에서 객체를 역직렬화 |
| `pickle.dumps(obj)` | 객체를 바이트 스트림으로 직렬화 |
| `pickle.loads(bytes)` | 바이트 스트림을 객체로 복원 |

---

## 📌 4. 직렬화 (Serialization)

- **객체 → 바이트 스트림(Binary)** 으로 변환
- 전송하거나 저장 가능하도록 변환
- `pickle` 외에도 `json`, `marshal`, `dill` 등 다양한 직렬화 방법 존재

### ✅ 예시: 객체 직렬화
```python
import pickle

data = {"name": "Alice", "score": 95, "passed": True}

with open("student.pkl", "wb") as f:
    pickle.dump(data, f)  # 객체를 파일에 직렬화
```

---

## 📌 5. 역직렬화 (Deserialization)

- **바이트 스트림 → 객체**로 복원
- 저장된 바이트 데이터를 객체로 복원하여 프로그램 내에서 활용
### ✅ 예시: 객체 역직렬화
```python
import pickle

with open("student.pkl", "rb") as f:
    loaded_data = pickle.load(f)

print(loaded_data)
# 출력: {'name': 'Alice', 'score': 95, 'passed': True}
```

---

## 🔚 마무리

| 개념 | 설명 | 주요 함수/모드 |
|------|------|----------------|
| 파일 입출력 | 텍스트 또는 바이너리 파일 처리 | `open()`, `'r'`, `'w'`, `'b'` |
| .bin 파일 | 이진 데이터 저장 파일 | `'wb'`, `'rb'` |
| `pickle` | 객체 직렬화/역직렬화 모듈 | `dump()`, `load()` |
| 직렬화 | 객체 → 바이트 저장 | `pickle.dump`, `pickle.dumps` |
| 역직렬화 | 바이트 → 객체 복원 | `pickle.load`, `pickle.loads` |

---

## ✅ 주의사항

- `pickle`은 **보안에 취약**할 수 있음 → 신뢰되지 않은 소스의 파일은 `pickle.load()`로 절대 열지 말 것
- JSON은 범용성과 가독성이 좋지만, Python 고유 객체(예: set, tuple, 사용자 정의 클래스)는 직렬화 불가 → 복잡한 구조에는 `pickle` 사용이 더 적절

---

## ⏭️ 다음으로는...
- class 메소드, 스테틱 메소드, 싱글톤 패턴, 데코레이터, 클로저 ...

---

[⏮️ 이전 문서](./0508%20Python정리.md) [다음 문서 ⏭️](./0512%20Python정리.md)