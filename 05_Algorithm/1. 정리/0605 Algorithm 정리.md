# 🧮 Algorithm 이론과 개념 정리  

##### 🗓️ 2025.06.05  
##### 📝 Writer : Moon19ht  

---

## 📚 목차

  - [1. 선택(Select) 정렬](#1-선택select-정렬)
  - [2. 퀵(Quick) 정렬](#2-퀵quick-정렬)
  - [3. 버블(Bubble) 정렬](#3-버블bubble-정렬)
  - [4. 트리(Tree)](#4-트리tree)
  - [5. 이진 탐색 트리](#5-이진-탐색-트리binary-search-tree-bst)
  - [6. 이진 탐색 트리의 순회](#6-이진-탐색-트리의-순회)

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

---
## 4. 트리(Tree)

트리는 계층적(hierarchical) 구조를 가지는 비선형 자료구조로, 노드(node)와 간선(edge)로 구성됩니다. 트리의 최상위 노드를 루트(root)라고 하며, 각 노드는 0개 이상의 자식(child) 노드를 가질 수 있습니다. 트리는 파일 시스템, 데이터베이스 인덱스, 탐색 알고리즘 등 다양한 분야에서 사용됩니다.

### 트리의 기본 용어

- **루트 노드(Root Node)**: 트리의 최상위 노드
- **부모 노드(Parent Node)**: 어떤 노드의 바로 위 단계 노드
- **자식 노드(Child Node)**: 부모 노드로부터 연결된 하위 노드
- **리프 노드(Leaf Node)**: 자식이 없는 노드
- **서브트리(Subtree)**: 트리의 일부로, 하나의 노드와 그 자손들로 구성

### 트리 구조 예시

아래는 이진 트리(Binary Tree)의 예시입니다.

```
    1
       / \
      2   3
     / \   \
    4   5   6
```

### 트리의 Python 구현 예시

```python
class Node:
    def __init__(self, data):
    self.data = data
    self.left = None  # 왼쪽 자식
    self.right = None # 오른쪽 자식

# 트리 생성
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

# 전위 순회(Preorder Traversal) 예시
def preorder(node):
    if node:
    print(node.data, end=' ')
    preorder(node.left)
    preorder(node.right)

preorder(root)  # 출력: 1 2 4 5 3 6
```

### 트리 구조 이미지

![이진 트리 예시](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Binary_tree.svg/320px-Binary_tree.svg.png)

---
## 5. 이진 탐색 트리(Binary Search Tree, BST)

이진 탐색 트리(BST)는 이진 트리의 한 종류로, 각 노드가 다음과 같은 성질을 만족합니다.

- **왼쪽 서브트리**에는 해당 노드보다 **작은 값**의 노드만 존재합니다.
- **오른쪽 서브트리**에는 해당 노드보다 **큰 값**의 노드만 존재합니다.
- 모든 서브트리도 이진 탐색 트리입니다.

이러한 구조 덕분에 탐색, 삽입, 삭제 연산을 평균적으로 O(log n) 시간에 수행할 수 있습니다.

### 이진 탐색 트리의 구조 예시

```
    8
     / \
    3   10
   / \    \
  1   6    14
     / \   /
    4   7 13
```

### 이진 탐색 트리의 Python 구현 예시

```python
class Node:
    def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None

# 노드 삽입 함수
def insert(node, data):
    if node is None:
      return Node(data)
    if data < node.data:
      node.left = insert(node.left, data)
    else:
      node.right = insert(node.right, data)
    return node

# 이진 탐색 트리 생성
root = None
for value in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
    root = insert(root, value)

# 중위 순회(Inorder Traversal): 오름차순 출력
def inorder(node):
    if node:
      inorder(node.left)
      print(node.data, end=' ')
      inorder(node.right)

inorder(root)  # 출력: 1 3 4 6 7 8 10 13 14
```

- **설명**: `insert` 함수는 재귀적으로 트리를 탐색하여 올바른 위치에 새 노드를 삽입합니다. 중위 순회는 BST의 값을 오름차순으로 출력합니다.

### 이진 탐색 트리 구조 이미지

![이진 탐색 트리 예시](https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Binary_search_tree.svg/320px-Binary_search_tree.svg.png)

---

## 6. 이진 탐색 트리의 순회

이진 탐색 트리(BST)의 순회(Traversal)는 트리의 모든 노드를 체계적으로 방문하는 방법입니다. 순회 방식에 따라 트리의 구조를 이해하거나, 데이터를 정렬하거나, 삭제 등 다양한 작업에 활용됩니다. 대표적인 순회 방식은 **전위(Preorder)**, **중위(Inorder)**, **후위(Postorder)** 순회가 있습니다.

### 이진 탐색 트리 순회의 종류와 특징

#### 1. 전위 순회 (Preorder Traversal)

- **방문 순서**: (1) 루트 → (2) 왼쪽 서브트리 → (3) 오른쪽 서브트리
- **특징**: 루트 노드를 가장 먼저 방문하므로 트리의 구조를 저장하거나 복사할 때 유용합니다.
- **실행 흐름**:
    1. 현재 노드 방문
    2. 왼쪽 자식 재귀적으로 방문
    3. 오른쪽 자식 재귀적으로 방문

```python
def preorder(node):
        if node:
                print(node.data, end=' ')
                preorder(node.left)
                preorder(node.right)

# 예시 실행
preorder(root)  # 출력: 8 3 1 6 4 7 10 14 13
```

#### 2. 중위 순회 (Inorder Traversal)

- **방문 순서**: (1) 왼쪽 서브트리 → (2) 루트 → (3) 오른쪽 서브트리
- **특징**: 이진 탐색 트리에서 중위 순회를 하면 노드의 값이 **오름차순**으로 출력됩니다.
- **실행 흐름**:
    1. 왼쪽 자식 재귀적으로 방문
    2. 현재 노드 방문
    3. 오른쪽 자식 재귀적으로 방문

```python
def inorder(node):
        if node:
                inorder(node.left)
                print(node.data, end=' ')
                inorder(node.right)

# 예시 실행
inorder(root)  # 출력: 1 3 4 6 7 8 10 13 14
```

#### 3. 후위 순회 (Postorder Traversal)

- **방문 순서**: (1) 왼쪽 서브트리 → (2) 오른쪽 서브트리 → (3) 루트
- **특징**: 하위 노드를 모두 처리한 후 루트 노드를 방문하므로, 트리의 노드를 삭제하거나 하위 작업을 먼저 수행해야 할 때 사용합니다.
- **실행 흐름**:
    1. 왼쪽 자식 재귀적으로 방문
    2. 오른쪽 자식 재귀적으로 방문
    3. 현재 노드 방문

```python
def postorder(node):
        if node:
                postorder(node.left)
                postorder(node.right)
                print(node.data, end=' ')

# 예시 실행
postorder(root)  # 출력: 1 4 7 6 3 13 14 10 8
```

---

### 순회 방식별 노드 방문 순서 비교

아래 BST 구조에서 각 순회 방식의 방문 순서는 다음과 같습니다.

```
        8
     / \
    3   10
 / \    \
1   6    14
     / \   /
    4   7 13
```

| 순회 방식        | 방문 순서                  | 설명                                      |
|------------------|---------------------------|-------------------------------------------|
| 전위(Preorder)   | 8 3 1 6 4 7 10 14 13      | 루트 → 왼쪽 → 오른쪽                      |
| 중위(Inorder)    | 1 3 4 6 7 8 10 13 14      | 왼쪽 → 루트 → 오른쪽 (오름차순 정렬)      |
| 후위(Postorder)  | 1 4 7 6 3 13 14 10 8      | 왼쪽 → 오른쪽 → 루트                      |

---

### 순회 방식의 시각적 이해

아래 그림은 이진 탐색 트리의 구조와 각 순회 방식의 방문 순서를 시각적으로 보여줍니다.

![이진 탐색 트리 예시](https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Binary_search_tree.svg/320px-Binary_search_tree.svg.png)

- **전위 순회**: 루트에서 시작해 왼쪽, 오른쪽 순으로 깊이 우선 탐색
- **중위 순회**: 가장 왼쪽 노드부터 오른쪽 노드까지 차례로 방문 (정렬 결과)
- **후위 순회**: 모든 자식 노드를 방문한 후 부모 노드를 방문

---

### 순회 방식의 활용 예시

- **전위 순회**: 트리 복사, 트리 구조 직렬화/역직렬화
- **중위 순회**: BST의 값 정렬, 범위 쿼리
- **후위 순회**: 트리 삭제, 하위 노드부터 처리하는 작업(예: 디렉터리 삭제)

---

#### 참고: 순회 방식의 비재귀(스택) 구현

재귀 대신 스택을 이용해 순회를 구현할 수도 있습니다. 예를 들어, 중위 순회의 비재귀 구현은 다음과 같습니다.

```python
def inorder_iterative(node):
        stack = []
        current = node
        while stack or current:
                while current:
                        stack.append(current)
                        current = current.left
                current = stack.pop()
                print(current.data, end=' ')
                current = current.right

# 예시 실행
inorder_iterative(root)  # 출력: 1 3 4 6 7 8 10 13 14
```

---
