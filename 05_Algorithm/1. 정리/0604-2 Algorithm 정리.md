# 🧮 Algorithm 이론과 개념 정리  

##### 🗓️ 2025.06.04  
##### 📝 Writer : Moon19ht  

---

## 📚 목차

- [🧮 Algorithm 이론과 개념 정리](#-algorithm-이론과-개념-정리)
        - [🗓️ 2025.06.04](#️-20250604)
        - [📝 Writer : Moon19ht](#-writer--moon19ht)
  - [📚 목차](#-목차)
  - [1. 선택(Select) 정렬](#1-선택select-정렬)
  - [2. 퀵(Quick) 정렬](#2-퀵quick-정렬)
  - [3. 버블(Bubble) 정렬](#3-버블bubble-정렬)

---

## 1. 선택(Select) 정렬

선택 정렬은 가장 작은(또는 큰) 값을 찾아서 맨 앞(또는 맨 뒤)과 교환하는 과정을 반복하는 정렬 알고리즘입니다. 시간 복잡도는 O(n²)입니다.

```python
def selection_sort(arr):
    # 배열의 길이만큼 반복
    for i in range(len(arr)):
        min_idx = i  # 현재 위치를 최소값 인덱스로 가정
        # i 이후의 요소 중 최소값 탐색
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j  # 더 작은 값이 있으면 인덱스 갱신
        # 최소값을 현재 위치와 교환
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 예시
data = [64, 25, 12, 22, 11]
print(selection_sort(data))  # [11, 12, 22, 25, 64]
```
- **설명**: 바깥 반복문은 정렬되지 않은 부분의 첫 번째 인덱스를 가리킵니다. 내부 반복문은 그 이후의 값 중 최소값을 찾아 현재 위치와 교환합니다.

---

## 2. 퀵(Quick) 정렬

퀵 정렬은 분할 정복(Divide and Conquer) 방식의 정렬 알고리즘입니다. 기준점(pivot)을 정해 작은 값과 큰 값으로 분할하여 재귀적으로 정렬합니다. 평균 시간 복잡도는 O(n log n)입니다.

```python
def quick_sort(arr):
    # 배열의 길이가 1 이하이면 이미 정렬된 상태
    if len(arr) <= 1:
        return arr
    pivot = arr[0]  # 첫 번째 요소를 피벗으로 선택
    left = [x for x in arr[1:] if x < pivot]   # 피벗보다 작은 값
    right = [x for x in arr[1:] if x >= pivot] # 피벗보다 크거나 같은 값
    # 재귀적으로 정렬 후 합치기
    return quick_sort(left) + [pivot] + quick_sort(right)

# 예시
data = [64, 25, 12, 22, 11]
print(quick_sort(data))  # [11, 12, 22, 25, 64]
```
- **설명**: 피벗을 기준으로 작은 값과 큰 값으로 나누고, 각각을 재귀적으로 정렬한 뒤 합칩니다.

---

## 3. 버블(Bubble) 정렬

버블 정렬은 인접한 두 값을 비교하여 큰 값을 뒤로 보내는 방식으로 정렬합니다. 시간 복잡도는 O(n²)입니다.

```python
def bubble_sort(arr):
    n = len(arr)
    # 배열 전체를 반복
    for i in range(n):
        # 마지막 i개는 이미 정렬되어 있으므로 제외
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # 인접한 두 값이 순서가 잘못되었으면 교환
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 예시
data = [64, 25, 12, 22, 11]
print(bubble_sort(data))  # [11, 12, 22, 25, 64]
```
- **설명**: 각 반복마다 가장 큰 값이 뒤로 이동합니다. 내부 반복문에서 인접한 두 값을 비교하여 필요하면 교환합니다.



