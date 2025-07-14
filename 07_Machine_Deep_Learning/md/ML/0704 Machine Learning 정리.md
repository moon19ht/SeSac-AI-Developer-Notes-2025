# 📊 Machine Learning 이론

##### 🗓️ 2025.07.04
##### 📝 Writer : Moon19ht

---

## 📚 목차

1. [형태소 분석 기초](#형태소-분석-기초)
2. [KoNLPy 설치와 설정](#konlpy-설치와-설정)
3. [형태소 분석 모듈 활용](#형태소-분석-모듈-활용)
4. [말뭉치와 사전](#말뭉치와-사전)
5. [텍스트 시각화 기초](#텍스트-시각화-기초)
6. [워드클라우드 생성](#워드클라우드-생성)
7. [한글 폰트 설정](#한글-폰트-설정)
8. [고급 워드클라우드](#고급-워드클라우드)
9.  [실습 예제](#실습-예제)
10. [문제 풀이](#문제-풀이)
11. [핵심 요약](#핵심-요약)

---

## 형태소 분석 기초

### 형태소 분석의 중요성
> "모든 자연언어 처리 분야에서 가장 중요하면서도 기본적으로 필요한 것이 그 언어의 형태소 분석이라 할 수 있고, 형태소 분석이 완결된 후에야 비로소 구문 분석과 의미분석을 거쳐 기계번역이라든지 자연언어 이해 시스템을 비롯한 모든 자연언어 관련 분야에 응용될 수 있다" - 강승식

### 핵심 개념

#### 형태소(Morpheme)
언어에 있어서 **최소 의미 단위**를 말합니다.

#### 형태소 분석(Morphological Analysis)
형태소보다 단위가 큰 언어 단위인 어절 혹은 문장을 최소 의미 단위인 형태소로 분절하는 과정입니다.

#### 품사 태깅(POS Tagging)
형태소의 뜻과 문맥을 고려하여 품사(Part-of-Speech) 정보를 마크업하는 작업입니다.

**예시:**
```
"가방에 들어가신다" → 가방/NNG + 에/JKM + 들어가/VV + 시/EPH + ㄴ다/EFN
```

### 형태소 분석의 활용
- 문장을 의미 있는 작은 단위로 분해
- 주로 명사나 동사 중심으로 필요한 단어들을 추출
- 텍스트 마이닝, 감정 분석, 정보 검색에 활용
- 자연어 처리 시스템의 기초 단계

---

## KoNLPy 설치와 설정

### KoNLPy란?
KoNLPy(Korean Natural Language Processing in Python)는 한국어 자연어 처리를 위한 파이썬 라이브러리입니다.

### 설치 사전 요구사항

#### 1. Java Development Kit (JDK) 설치
KoNLPy는 Java 기반의 형태소 분석기를 사용하므로 JDK가 필요합니다.

**설치 방법:**
1. OpenJDK 다운로드: https://github.com/ojdkbuild/ojdkbuild
2. 설치 후 환경변수 설정
   - `JAVA_HOME`: JDK 설치 경로 (예: `C:\Program Files\Java\jdk1.8.0_161`)

#### 2. KoNLPy 설치
```bash
# Anaconda Prompt를 관리자 권한으로 실행
pip install konlpy
```

#### 3. 설치 확인
```python
from konlpy.corpus import kolaw  # 오류가 없으면 설치 완료
```

### 설치 문제 해결

#### 환경변수 설정 문제
1. **내 컴퓨터** → **속성** → **고급 시스템 설정** → **환경 변수**
2. 시스템 변수에서 **새로 만들기**
   - 변수 이름: `JAVA_HOME`
   - 변수 값: JDK 설치 경로

#### Anaconda 권한 문제
- Anaconda Prompt를 **관리자 권한**으로 실행
- 시스템 권한이 필요한 라이브러리 설치 시 필수

---

## 형태소 분석 모듈 활용

### 지원되는 형태소 분석기

| 분석기 | 사용 가능 여부 | 특징 |
|--------|----------------|------|
| Hannanum | ✅ | 상당히 정확, 빠른 처리 |
| Kkma | ✅ | 세종말뭉치 기반, 높은 정확도 |
| Okt (Twitter) | ✅ | 속도 빠름, 신조어 처리 |
| Komoran | ❌ | 일부 버전에서 작동 안함 |
| Mecab | ⚠️ | Windows 7에서 지원 안함 |

### 성능 비교표
| 기준 | Hannanum | Kkma | Okt |
|------|----------|------|-----|
| 속도 | 보통 | 느림 | 빠름 |
| 정확도 | 높음 | 매우 높음 | 보통 |
| 신조어 처리 | 보통 | 낮음 | 높음 |

### 1. Kkma 모듈
세종말뭉치를 기반으로 한 형태소 분석기로 높은 정확도를 제공합니다.

```python
# 파일명: exam15_1.py
from konlpy.tag import Kkma
from konlpy.utils import pprint

text = """
오픈소스를 이용하여 형태소 분석을 배워봅시다. 
형태소 분석을 지원하는 라이브러리가 많습니다.
각자 어떻게 분석하는지 살펴보겠습니다.
이건 Kkma 모듈입니다.
"""

kkma = Kkma()

print("=== 문장 분리 ===")
sentences = kkma.sentences(text)
print(sentences)

print("\n=== 형태소 분리 ===")
morphs = kkma.morphs(text)
print(morphs)

print("\n=== 명사 추출 ===")
nouns = kkma.nouns(text)
print(nouns)

print("\n=== 품사 태깅 ===")
pos_tags = kkma.pos(text)
print(pos_tags)
```

#### Kkma 주요 메서드
| 메서드 | 설명 |
|--------|------|
| `sentences()` | 문장 단위로 분리 |
| `morphs()` | 형태소 단위로 분리 |
| `nouns()` | 명사만 추출 |
| `pos()` | 품사 태깅 |

### 2. Hannanum 모듈
KAIST에서 개발된 형태소 분석기로 빠르고 정확한 분석을 제공합니다.

```python
# 파일명: exam15_2.py
from konlpy.tag import Hannanum

text = """
오픈소스를 이용하여 형태소 분석을 배워봅시다. 
형태소 분석을 지원하는 라이브러리가 많습니다.
각자 어떻게 분석하는지 살펴보겠습니다.
이건 Hannanum 모듈입니다.
"""

hannanum = Hannanum()

print("=== 형태소 분석 ===")
analyzed = hannanum.analyze(text)
print(analyzed)

print("\n=== 형태소 분리 ===")
morphs = hannanum.morphs(text)
print(morphs)

print("\n=== 명사 추출 ===")
nouns = hannanum.nouns(text)
print(nouns)

print("\n=== 품사 태깅 ===")
pos_tags = hannanum.pos(text)
print(pos_tags)
```

### 3. Okt (구 Twitter) 모듈
속도가 빠르고 신조어 처리에 특화된 형태소 분석기입니다.

```python
# 파일명: exam15_3.py
from konlpy.tag import Okt

text = """
오픈소스를 이용하여 형태소 분석을 배워봅시다. 
형태소 분석을 지원하는 라이브러리가 많습니다.
각자 어떻게 분석하는지 살펴보겠습니다.
이건 Okt 모듈입니다.
"""

okt = Okt()

print("=== 형태소 분리 ===")
morphs = okt.morphs(text)
print(morphs)

print("\n=== 명사 추출 ===")
nouns = okt.nouns(text)
print(nouns)

print("\n=== 품사 태깅 ===")
pos_tags = okt.pos(text)
print(pos_tags)

print("\n=== 정규화 ===")
normalized = okt.normalize("안녕하세욬ㅋㅋㅋㅋㅋㅋ")
print(f"정규화 결과: {normalized}")

print("\n=== 어구 추출 ===")
phrases = okt.phrases(text)
print(phrases)
```

### 파일 기반 형태소 분석
```python
# 파일명: exam15_4.py
from konlpy.tag import Kkma, Hannanum, Okt

# 파일 읽기
with open("./data/data1.txt", "r", encoding="utf-8") as file:
    text = file.read()

print("원본 텍스트:")
print(text[:200] + "...")

# 각 분석기별 비교
analyzers = {
    "Kkma": Kkma(),
    "Hannanum": Hannanum(),
    "Okt": Okt()
}

for name, analyzer in analyzers.items():
    print(f"\n=== {name} 분석 결과 ===")
    nouns = analyzer.nouns(text)
    print(f"추출된 명사 개수: {len(nouns)}")
    print(f"상위 10개 명사: {nouns[:10]}")
```

---

## 말뭉치와 사전

### 말뭉치(Corpus)란?
언어 연구를 위해 텍스트를 컴퓨터가 읽을 수 있는 형태로 모아 놓은 언어 자료입니다.

### 말뭉치의 중요성
- 통계 분석 및 가설 검증에 사용
- 특정 언어 영역 내에서 언어 규칙 발생의 검사와 정당성 입증
- 분석할 도메인에 맞는 말뭉치 선택이 중요
  - 법률 관련 텍스트 → 법률 말뭉치
  - 의학 관련 텍스트 → 의학 말뭉치

### KoNLPy 제공 말뭉치

#### 1. kolaw - 한국 법률 말뭉치
```python
from konlpy.corpus import kolaw

# 헌법 파일 읽기
constitution = kolaw.open('constitution.txt').readlines()
print("헌법 처음 3줄:")
for i, line in enumerate(constitution[:3]):
    print(f"{i+1}: {line.strip()}")
```

#### 2. kobill - 대한민국 국회 의안 말뭉치
```python
from konlpy.corpus import kobill

# 의안 파일 읽기 (파일명은 의안 번호)
bill = kobill.open('1809890.txt').readlines()
print("의안 처음 5줄:")
for i, line in enumerate(bill[:5]):
    print(f"{i+1}: {line.strip()}")
```

### 사전과 형태소 분석기 매칭

| 분석기 | 기반 말뭉치 | 특징 |
|--------|-------------|------|
| Hannanum | KAIST 말뭉치 | 공학적 접근 |
| Kkma | 세종 말뭉치 | 언어학적 정확도 |
| Mecab | 세종 말뭉치 | 빠른 처리 |

### 말뭉치 활용 예제
```python
# 파일명: exam15_5.py
from konlpy.corpus import kolaw, kobill

# 한국 법률 말뭉치
print("=== 한국 법률 말뭉치 (헌법) ===")
constitution_lines = kolaw.open('constitution.txt').readlines()
print(f"총 줄 수: {len(constitution_lines)}")
print("처음 3줄:")
for line in constitution_lines[:3]:
    print(line.strip())

print("\n=== 국회 의안 말뭉치 ===")
bill_lines = kobill.open('1809890.txt').readlines()
print(f"총 줄 수: {len(bill_lines)}")
print("처음 5줄:")
for line in bill_lines[:5]:
    print(line.strip())
```

---

## 텍스트 시각화 기초

### 시각화의 중요성
텍스트 데이터를 분석한 후 가장 효과적인 시각화 도구는 **워드클라우드**입니다. 워드클라우드는:
- 텍스트의 주요 키워드를 한눈에 파악 가능
- 단어의 빈도수를 크기로 표현
- 다양한 형태와 색상으로 시각적 임팩트 제공

### 시각화 라이브러리 설치
```bash
pip install pytagcloud
pip install pygame
pip install wordcloud
pip install matplotlib
pip install pillow
```

### 워드클라우드 라이브러리 비교

| 라이브러리 | 장점 | 단점 |
|------------|------|------|
| pytagcloud | 다양한 스타일 | 한글 폰트 설정 복잡 |
| wordcloud | 사용 간편, 마스킹 지원 | 상대적으로 단순한 스타일 |

---

## 워드클라우드 생성

### 1. pytagcloud 기본 사용법
```python
# 파일명: exam15_6.py
import pytagcloud
import webbrowser

# 데이터 준비 (단어, 빈도수) 튜플의 리스트
tag_data = [
    ('school', 30), ('rainbow', 10), ('cloud', 23), 
    ('peach', 10), ('pink', 20)
]

# 태그 리스트 생성
taglist = pytagcloud.make_tags(tag_data, maxsize=50)

# 워드클라우드 이미지 생성
pytagcloud.create_tag_image(
    taglist,
    'wordcloud.jpg',        # 저장할 파일명
    size=(300, 300),        # 이미지 크기
    fontname='Nobile',      # 폰트명
    rectangular=True        # 사각형 모양
)

# 브라우저로 이미지 보기
webbrowser.open('wordcloud.jpg')
```

### 2. WordCloud 라이브러리 기본 사용법
```python
# 파일명: exam15_7.py
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# 텍스트 파일 읽기
with open("./data/alice.txt", "r", encoding="utf-8") as file:
    text = file.read()

# 워드클라우드 생성
wordcloud = WordCloud(
    width=800, 
    height=400,
    background_color='white'
).generate(text)

# 시각화
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
```

### 3. 한국어 텍스트 처리
```python
# 파일명: exam15_8.py
from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt

# 텍스트 파일 읽기
with open("./data/korean_text.txt", "r", encoding="utf-8") as file:
    text = file.read()

# 형태소 분석
okt = Okt()
nouns = okt.nouns(text)

# 단어 빈도 계산
word_count = Counter(nouns)

# 상위 100개 단어만 사용
top_100 = word_count.most_common(100)

# 워드클라우드 생성
wordcloud = WordCloud(
    font_path="c:/Windows/Fonts/malgun.ttf",  # 한글 폰트
    width=800,
    height=400,
    background_color='white'
).generate_from_frequencies(dict(top_100))

# 시각화
plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("한국어 텍스트 워드클라우드", fontsize=16)
plt.show()
```

---

## 한글 폰트 설정

### pytagcloud 한글 폰트 설정

#### 1. 한글 폰트 파일 복사
```
C:\Windows\Fonts → C:\ProgramData\Anaconda3\Lib\site-packages\pytagcloud\fonts
```

**권장 폰트:**
- 맑은고딕: `malgun.ttf`
- 나눔고딕: `NanumGothic.ttf`
- 돋움: `dotum.ttf`

#### 2. fonts.json 파일 수정
```json
{
  "name": "HangleFont1",
  "ttf": "malgun.ttf",
  "web": "http://fonts.googleapis.com/css?family=Nobile"
}
```

**주의사항:**
- ProgramData 폴더는 숨김 폴더입니다
- 파일 탐색기 → 보기 → 숨김 파일 표시 활성화 필요

#### 3. 한글 워드클라우드 생성
```python
# 파일명: exam15_9.py
import pytagcloud
import webbrowser

# 한글 데이터
korean_tags = [
    ('학교', 30), ('무지개', 10), ('구름', 23), 
    ('복숭아', 14), ('분홍색', 20)
]

# 태그 리스트 생성
taglist = pytagcloud.make_tags(korean_tags, maxsize=40)

# 한글 폰트로 워드클라우드 생성
pytagcloud.create_tag_image(
    taglist,
    'korean_wordcloud.jpg',
    size=(400, 400),
    fontname='HangleFont1',    # 설정한 한글 폰트
    rectangular=True
)

webbrowser.open('korean_wordcloud.jpg')
```

### WordCloud 한글 폰트 설정
WordCloud 라이브러리는 `font_path` 매개변수로 간단히 한글 폰트를 설정할 수 있습니다.

```python
from wordcloud import WordCloud

wordcloud = WordCloud(
    font_path="c:/Windows/Fonts/malgun.ttf",  # 한글 폰트 경로
    width=800,
    height=400,
    background_color='white'
).generate(text)
```

---

## 고급 워드클라우드

### 1. 불용어 제거
분석에 불필요한 단어들을 제거하여 더 의미 있는 워드클라우드를 생성합니다.

```python
# 파일명: exam15_10.py
from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt

# 텍스트 읽기
with open("./data/korean_text.txt", "r", encoding="utf-8") as file:
    text = file.read()

# 형태소 분석
okt = Okt()
nouns = okt.nouns(text)

# 불용어 정의
stopwords = [
    '다만', '그', '곳', '나', '일', '패', '달리', '의', 
    '것', '등', '및', '를', '이', '가', '에', '은', '는'
]

# 불용어 제거
filtered_nouns = [word for word in nouns if word not in stopwords and len(word) > 1]

# 단어 빈도 계산
word_count = Counter(filtered_nouns)
top_50 = word_count.most_common(50)

# 워드클라우드 생성
wordcloud = WordCloud(
    font_path="c:/Windows/Fonts/malgun.ttf",
    width=800,
    height=400,
    background_color='white',
    max_words=50,
    colormap='viridis'
).generate_from_frequencies(dict(top_50))

plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("불용어 제거 후 워드클라우드", fontsize=16)
plt.show()
```

### 2. 마스크 이미지 활용
특정 이미지 모양에 맞춰 워드클라우드를 생성합니다.

```python
# 파일명: exam15_11.py
from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import random

# 텍스트 처리
with open("./data/korean_text.txt", "r", encoding="utf-8") as file:
    text = file.read()

okt = Okt()
nouns = okt.nouns(text)

# 불용어 제거
stopwords = ['다만', '그', '곳', '나', '일', '패', '달리', '의']
filtered_nouns = [word for word in nouns if word not in stopwords and len(word) > 1]

# 단어 빈도 계산
word_count = Counter(filtered_nouns)
top_100 = dict(word_count.most_common(100))

# 마스크 이미지 로드
mask_image = np.array(Image.open("./image/korea_mask.jpg"))

# 사용자 정의 색상 함수
def custom_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return f"rgb({random.randint(0, 255)},{random.randint(0, 255)},{random.randint(0, 255)})"

# 워드클라우드 생성
wordcloud = WordCloud(
    font_path="c:/Windows/Fonts/malgun.ttf",
    relative_scaling=0.2,
    background_color='white',
    mask=mask_image,
    max_words=100
).generate_from_frequencies(top_100)

# 시각화
plt.figure(figsize=(16, 8))
random.seed(1234)  # 색상 고정
plt.imshow(
    wordcloud.recolor(color_func=custom_color_func), 
    interpolation="bilinear"
)
plt.axis("off")
plt.title("마스크 이미지 워드클라우드", fontsize=20)
plt.show()
```

### 3. 법률 문서 분석
```python
# 파일명: exam15_12.py
from wordcloud import WordCloud
from konlpy.corpus import kolaw
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt

# 헌법 텍스트 읽기
constitution_text = kolaw.open('constitution.txt').read()

# 형태소 분석
okt = Okt()
nouns = okt.nouns(constitution_text)

# 의미 있는 단어 필터링
meaningful_words = [
    word for word in nouns 
    if len(word) > 1 and word not in ['조', '항', '의', '은', '는', '을', '를']
]

# 단어 빈도 계산
word_count = Counter(meaningful_words)
top_50 = dict(word_count.most_common(50))

# 워드클라우드 생성
wordcloud = WordCloud(
    font_path="c:/Windows/Fonts/malgun.ttf",
    width=1000,
    height=600,
    background_color='white',
    max_words=50,
    colormap='Blues'
).generate_from_frequencies(top_50)

# 시각화
plt.figure(figsize=(15, 9))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("대한민국 헌법 워드클라우드", fontsize=20, pad=20)
plt.tight_layout()
plt.show()

# 주요 단어 출력
print("헌법에서 가장 많이 사용된 단어 Top 10:")
for i, (word, count) in enumerate(word_count.most_common(10), 1):
    print(f"{i:2d}. {word}: {count}회")
```

---

## 실습 예제

### 과제: 헌법 문서 워드클라우드
KoNLPy의 kolaw 말뭉치에서 헌법 파일을 읽고, `image/korea_mask.jpg`를 마스크로 사용하여 태극기 모양의 워드클라우드를 생성하세요.

**요구사항:**
1. 불용어 제거
2. 한글 폰트 적용
3. 커스텀 색상 적용
4. 상위 100개 단어만 사용

### 해답
```python
# 파일명: homework15.py
from wordcloud import WordCloud
from konlpy.corpus import kolaw
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import random

# 1. 헌법 텍스트 읽기
constitution_text = kolaw.open('constitution.txt').read()
print("헌법 텍스트 읽기 완료")

# 2. 형태소 분석
okt = Okt()
nouns = okt.nouns(constitution_text)
print(f"추출된 명사 개수: {len(nouns)}")

# 3. 불용어 제거
stopwords = [
    '다만', '그', '곳', '나', '일', '패', '달리', '의', 
    '조', '항', '호', '각', '제', '이', '그', '수', '때'
]
filtered_nouns = [
    word for word in nouns 
    if word not in stopwords and len(word) > 1
]
print(f"불용어 제거 후: {len(filtered_nouns)}개")

# 4. 단어 빈도 계산
word_count = Counter(filtered_nouns)
top_100 = dict(word_count.most_common(100))

# 5. 마스크 이미지 로드
mask_image = np.array(Image.open("./image/korea_mask.jpg"))

# 6. 커스텀 색상 함수
def korean_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    # 태극기 색상 (빨강, 파랑, 검정) 위주
    colors = [
        f"rgb(205, 92, 92)",   # 빨강
        f"rgb(65, 105, 225)",  # 파랑  
        f"rgb(47, 79, 79)",    # 검정
        f"rgb(255, 140, 0)"    # 주황
    ]
    return random.choice(colors)

# 7. 워드클라우드 생성
wordcloud = WordCloud(
    font_path="c:/Windows/Fonts/malgun.ttf",
    relative_scaling=0.2,
    background_color='white',
    mask=mask_image,
    max_words=100,
    width=800,
    height=600
).generate_from_frequencies(top_100)

# 8. 시각화
plt.figure(figsize=(16, 12))
random.seed(1234)  # 재현 가능한 색상

plt.imshow(
    wordcloud.recolor(color_func=korean_color_func), 
    interpolation="bilinear"
)
plt.axis("off")
plt.title("대한민국 헌법 워드클라우드", fontsize=24, pad=30)
plt.tight_layout()
plt.show()

# 9. 결과 분석
print("\n=== 헌법 주요 키워드 Top 20 ===")
for i, (word, count) in enumerate(word_count.most_common(20), 1):
    print(f"{i:2d}. {word}: {count}회")

# 워드클라우드 이미지 저장
wordcloud.to_file("constitution_wordcloud.png")
print("\n워드클라우드가 'constitution_wordcloud.png'로 저장되었습니다.")
```

---

## 문제 풀이

### 문제 1
형태소 분석에 대하여 잘못된 설명은?

① 형태소란 언어에 있어서 "최소 의미 단위"를 말합니다
② 자연어 처리에서 가장 중요합니다
③ 말뭉치들로부터 사전을 구성하여 형태소 분석에 이용합니다
④ 형태소 분석에 어떤 사전을 사용하는지는 중요하지 않습니다

**정답: ④**

**해설**: 분석할 대상에 맞는 적절한 사전을 사용해야 합니다. 법률 관련 텍스트 분석에는 법률 사전, 의학 관련 텍스트 분석에는 의학 관련 사전 등 도메인에 특화된 사전을 사용해야 정확한 분석이 가능합니다.

**난이도**: 5 (아주 쉬움)

---

## 핵심 요약

### KoNLPy를 활용한 한국어 형태소 분석
- **형태소 분석**: 어절이나 문장을 최소 의미 단위인 형태소로 분절하는 과정
- **KoNLPy**: 한글 형태소 분석을 위해 KAIST에서 개발한 파이썬 라이브러리
- **지원 패키지**: Kkma, Hannanum, Okt(Twitter), Komoran, Mecab 등
- **도메인 특화**: 분석 대상에 맞는 적절한 말뭉치와 사전 선택이 중요

### 주요 형태소 분석기 특성
| 분석기 | 속도 | 정확도 | 특징 |
|--------|------|--------|------|
| Kkma | 느림 | 높음 | 세종말뭉치 기반, 문장 분리 지원 |
| Hannanum | 보통 | 높음 | KAIST 말뭉치 기반, 안정적 |
| Okt | 빠름 | 보통 | 신조어 처리 특화, 정규화 기능 |

### 텍스트 시각화
- **워드클라우드**: 단어 빈도를 시각적 크기로 표현하는 인기 있는 차트
- **주요 라이브러리**: pytagcloud, wordcloud
- **데이터 형태**: 단어와 빈도수의 쌍으로 구성된 데이터
- **한글 지원**: 한글 폰트 설정을 통한 한국어 텍스트 시각화

### 고급 기능
- **불용어 처리**: 분석에 불필요한 단어 제거로 의미 있는 결과 도출
- **마스크 이미지**: 특정 이미지 모양에 맞춘 워드클라우드 생성
- **커스텀 색상**: 사용자 정의 색상 함수로 시각적 효과 향상
- **파일 처리**: 다양한 형식의 텍스트 파일 읽기 및 처리

### 실무 응용 분야
- **소셜미디어 분석**: SNS 게시물 감정 분석, 트렌드 파악
- **문서 분석**: 계약서, 보고서 등 업무 문서의 핵심 키워드 추출
- **고객 피드백 분석**: 리뷰, 설문 응답 등의 의견 분석
- **뉴스 분석**: 기사 내용의 주요 이슈 파악

### 주의사항
- Java 환경 설정 필요 (JDK 설치 및 환경변수 설정)
- 한글 폰트 설정 시 경로와 권한 확인
- 도메인별 특성을 고려한 적절한 분석기 선택
- 불용어와 전처리를 통한 분석 품질 향상

형태소 분석과 텍스트 시각화는 현대 데이터 분석에서 매우 중요한 기술로, 비정형 텍스트 데이터에서 의미 있는 인사이트를 도출하는 핵심 도구입니다.
