# 🐍 파이썬(Python) 기초 개념 설명서

##### 🗓️ 2025.04.30
##### 📝 Writer : Moon19ht

---

## 📚 목차

- [📌 1. `zip()` 함수](#-1-zip-함수)
- [📌 2. `dict()` 함수](#-2-dict-함수)
- [📌 3. 순차 검색 (선형 검색, Sequential Search)](#-3-순차-검색-선형-검색-sequential-search)
- [📌 4. 색인 순차 검색 (Indexed Sequential Search)](#-4-색인-순차-검색-indexed-sequential-search)
- [📌 5. 이분 검색 (Binary Search)](#-5-이분-검색-binary-search)
- [📌 6. 해시 검색 (Hash Search)](#-6-해시-검색-hash-search)
- [📌 7. 정렬 (Sorting)](#-7-정렬-sorting)
- [✅ 선택 정렬 (Selection Sort)](#-선택-정렬-selection-sort)
- [🔚 마무리](#-마무리)

---

## 📌 1. `zip()` 함수

여러 개의 **반복 가능한 객체(iterable)**를 병렬적으로 묶어주는 함수

### 📌 문법
```python
zip(반복가능한 객체1, 객체2, ...)
```

### 📌 예시
```python
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]

combined = list(zip(names, scores))
print(combined)
# 출력: [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
```

> ❗ 길이가 다른 경우 짧은 쪽에 맞춰서 짝을 지음

---

## 📌 2. `dict()` 함수

사전(dictionary) 객체를 생성하는 함수로, 키-값 쌍의 집합을 표현

### ✅ 문법
```python
dict(키1=값1, 키2=값2, ...)
dict([(키1, 값1), (키2, 값2)])
```

### ✅ 예시
```python
d1 = dict(name='Alice', age=25)
d2 = dict([('name', 'Bob'), ('age', 30)])

print(d1)  # {'name': 'Alice', 'age': 25}
print(d2)  # {'name': 'Bob', 'age': 30}
```

> ✅ 일반적으로 `zip()`과 함께 사용하여 딕셔너리를 쉽게 생성할 수 있음:
```python
keys = ['name', 'age']
values = ['Charlie', 28]
d = dict(zip(keys, values))
```

---

## 📌 3. 순차 검색 (선형 검색, Sequential Search)

- 데이터를 **처음부터 끝까지 하나씩** 비교하여 찾는 방식
- 정렬이 필요 없고 구현이 간단하지만, 데이터가 많아질수록 비효율적
- 최악의 경우 **O(n)** 시간 복잡도

### 예시
```python
def sequential_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1
```

### 시간 복잡도
- `3n + 100 → O(n)`
- `n² + 3n + 30 → O(n²)`  
※ 점근적 분석에서 상수와 하위 차항은 제거

---

## 📌 4. 색인 순차 검색 (Indexed Sequential Search)

- 데이터를 정렬한 후, 인덱스를 기반으로 검색
- 색인된 위치에서 검색 범위를 줄여 순차 검색을 수행
- **데이터 정렬**이 전제조건  
※ 자주 변경되는 데이터에 부적합

---

## 📌 5. 이분 검색 (Binary Search)

- **정렬된 데이터**를 전제로 하며, 중간값과 비교하여 탐색 구간을 절반으로 줄임
- 검색 과정:
  1. 중간값과 타겟 비교
  2. 왼쪽 또는 오른쪽 절반으로 범위 축소
  3. 반복
- 시간 복잡도: **O(log n)**

### 예시
```python
def binary_search(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

---

## 📌 6. 해시 검색 (Hash Search)

- **해시 함수**를 사용해 데이터를 고유 인덱스에 매핑
- 평균 시간 복잡도: **O(1)**
- 속도가 빠르지만, 메모리를 많이 소모하고 **충돌(Collision)** 문제 있음

### 파이썬에서는?
- `dict`, `set` 타입이 해시 기반 자료구조
- 내부적으로 **HashTable**로 구현

---

## 📌 7. 정렬 (Sorting)

- 데이터를 정해진 순서로 나열 (오름차순 / 내림차순)
- DB 사용 시 SQL 쿼리로 처리 가능하지만, 직접 구현하는 경우도 존재

### 주요 정렬 알고리즘
- **선택 정렬 (Selection Sort)**
- **버블 정렬 (Bubble Sort)**
- **퀵 정렬 (Quick Sort)** - 매우 빠름, 실무에서 자주 사용됨

---

## ✅ 선택 정렬 (Selection Sort)

- **리스트에서 가장 작은(또는 큰) 값을 찾아 제일 앞에 배치**
- N개의 원소에 대해 N-1회 반복
- 각 반복마다 **최솟값의 위치를 찾아 교환**

### 예시: 오름차순 정렬
#### 초기 리스트
```
[5, 1, 2, 4, 3]
```

#### 1회전
- 0번 위치에 가장 작은 값(1)을 이동  
```
[1, 5, 2, 4, 3]
```

#### 2회전
- 1번 위치에 그 다음 작은 값(2)을 이동  
```
[1, 2, 5, 4, 3]
```

#### 3회전
- 2번 위치에 3을 이동  
```
[1, 2, 3, 5, 4]
```

#### 4회전
- 3번 위치에 4를 이동  
```
[1, 2, 3, 4, 5]
```

### 코드 예시
```python
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
```

---

## 🔚 마무리

| 알고리즘      | 정렬 필요 | 시간 복잡도 | 특징                                |
|---------------|------------|--------------|-------------------------------------|
| 순차 검색     | ❌         | O(n)         | 간단, 작은 데이터에 적합             |
| 색인 순차 검색 | ✅         | O(n)         | 정렬 + 인덱스 기반 범위 줄임          |
| 이분 검색     | ✅         | O(log n)     | 빠름, 정렬 필수                        |
| 해시 검색     | ❌         | O(1)         | 매우 빠름, 충돌 처리 필요              |
| 선택 정렬     | ❌         | O(n²)        | 구현 쉬움, 느림                        |
