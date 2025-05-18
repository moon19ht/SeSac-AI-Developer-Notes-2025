# 🧩 파이썬(Python) 심화

##### 🗓️ 2025.05.14
##### 📝 Writer : Moon19ht

---

## 📚 목차

- [📌 1. 정규표현식 (Regular Expression)](#-1-정규표현식-regular-expression)
- [📌 2. 가상환경 (Virtual Environment)](#-2-가상환경-virtual-environment)
- [🔚 마무리](#-마무리)
- [⏭️ 다음으로는...](#️-다음으로는)
- [⏮️ 이전 문서](./0513%20Python정리.md) [다음 문서 ⏭️](./0514%20Python정리.md)

---

## 📌 1. 정규표현식 (Regular Expression)

### ✅ 개념
- 정규표현식(Regex)은 **문자열에서 특정한 규칙(패턴)을 검색, 추출, 대체**할 때 사용하는 문법
- Python에서는 `re` 모듈을 사용

### ✅ 주요 패턴 기호

| 패턴 | 의미 |
|------|------|
| `.` | 줄바꿈 제외 임의의 한 문자 (`\n` 제외) |
| `^` | 문자열 시작 |
| `$` | 문자열 끝 |
| `*` | 0회 이상 반복 |
| `+` | 1회 이상 반복 |
| `?` | 0회 또는 1회 반복 |
| `{n}` | n회 반복 |
| `{n,m}` | n~m회 반복 |
| `[]` | 문자 집합 |
| `\d` | 숫자 (`[0-9]`) |
| `\w` | 단어 문자 (`[a-zA-Z0-9_]`) |
| `\s` | 공백 문자 |
| `|` | OR 연산자 (ex: `a|b`) |
| `()` | 그룹 |

---

### ✅ 기본 사용법
```python
import re

pattern = r"\d{3}-\d{4}-\d{4}"  # 전화번호 패턴
text = "문의는 010-1234-5678 로 주세요."

match = re.search(pattern, text)
if match:
    print(match.group())  # 출력: 010-1234-5678
```

---

### ✅ 주요 함수

| 함수 | 설명 |
|------|------|
| `re.search()` | 문자열 전체에서 첫 매칭 찾기 |
| `re.match()` | 문자열의 **시작 위치**에서만 매칭 찾기 |
| `re.fullmatch()` | 문자열 전체가 정규식과 일치할 때만 매칭 |
| `re.findall()` | 모든 매칭 결과 리스트 반환 |
| `re.sub()` | 문자열 치환 |
| `re.compile()` | 정규표현식 객체 생성 |

### ✅ 예제: 이메일 검증
```python
email = "user@example.com"
if re.fullmatch(r"[\w\.-]+@[\w\.-]+\.\w+", email):
    print("✅ 유효한 이메일")
else:
    print("❌ 잘못된 이메일")
```

---

## 📌 2. 가상환경 (Virtual Environment)

### ✅ 개념
- 프로젝트마다 독립적인 Python 실행 환경을 제공
- **패키지 충돌 방지**, **버전 관리**, **깨끗한 테스트 환경** 제공
- Python 내장 모듈: `venv`

---

### ✅ 가상환경 생성 및 사용

#### 1. 가상환경 생성
```bash
python3 -m venv venv_name  # 일부 시스템에서는 python 대신 python3 사용
```

#### 2. 가상환경 활성화

| 운영체제 | 명령어 |
|----------|--------|
| Windows  | `venv_name\Scripts\activate` |
| macOS/Linux | `source venv_name/bin/activate` |

#### 3. 가상환경 비활성화
```bash
deactivate
```

---

### ✅ 패키지 설치 및 관리
```bash
pip install requests
pip freeze > requirements.txt  # 현재 환경의 패키지 목록 저장

# 다른 환경에서 동일하게 설치
pip install -r requirements.txt
```

---

### ✅ 예시 디렉토리 구조
```
my_project/
├── venv/                # 가상환경 폴더
├── requirements.txt     # 설치된 패키지 목록
├── main.py              # 프로젝트 코드
```

> `venv/` 폴더는 `.gitignore`에 추가해 Git에 포함되지 않도록 해야 함

---

## 🔚 마무리

| 항목 | 설명 |
|------|------|
| 정규표현식 | 문자열 패턴 검색 및 치환 도구 |
| 정규식 모듈 | `import re` |
| 주요 함수 | `search`, `match`, `findall`, `sub` |
| 가상환경 | 프로젝트별 독립 실행 환경 |
| 가상환경 도구 | `venv`, `pip`, `requirements.txt` |

---

## ✅ 실전 팁

- 정규표현식은 문자열 파싱, 검증, 스크래핑에 매우 유용
- 가상환경은 협업 시 필수! `venv` 또는 `.venv` 폴더는 **`.gitignore`에 반드시 포함**

---

## ⏭️ 다음으로는...

- SQL 기초, MySQL 등 ... 

---

[⏮️ 이전 문서](./0513%20Python정리.md) [다음 문서 ⏭️](./0514%20Python정리.md)