# 🧮 Algorithm 이론과 개념 정리  

##### 🗓️ 2025.06.09
##### 📝 Writer : Moon19ht  

---

## 📚 목차

- [1. 트리(Tree)](#4-트리tree)
- [2. 이진 탐색 트리](#5-이진-탐색-트리binary-search-tree-bst)
- [3. 이진 탐색 트리의 순회](#6-이진-탐색-트리의-순회)
- [4. 트리를 이용한 전위, 중위, 후위 계산 방법](#4-트리를-이용한-전위-중위-후위-계산-방법)

---
## 1. 트리(Tree)

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
## 2. 이진 탐색 트리(Binary Search Tree, BST)

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

## 3. 이진 탐색 트리의 순회

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

## 4. 트리를 이용한 전위, 중위, 후위 계산 방법

트리 구조(특히 이진 트리)를 이용하면 전위, 중위, 후위 순회 방식으로 수식의 값을 계산할 수 있습니다. 각 순회 방식은 수식의 표기법(전위: Prefix, 중위: Infix, 후위: Postfix)과 밀접하게 연관되어 있습니다.

### 1. 이진 트리에서의 수식 표현

예를 들어, 수식 `3 + (4 * 5)`를 이진 트리로 표현하면 다음과 같습니다.

```
    +
   / \
  3   *
     / \
    4   5
```

- **전위(Prefix)**: 연산자를 먼저 방문 → `+ 3 * 4 5`
- **중위(Infix)**: 연산자를 가운데 방문 → `3 + 4 * 5`
- **후위(Postfix)**: 연산자를 마지막에 방문 → `3 4 5 * +`

### 2. 순회별 계산 방법

#### 전위 순회(Prefix) 계산

1. 노드가 연산자면, 왼쪽과 오른쪽 자식의 값을 재귀적으로 계산한 뒤 연산을 수행합니다.
2. 노드가 숫자면, 그 값을 반환합니다.

```python
def eval_prefix(node):
    if node is None:
        return 0
    if node.data in '+-*/':
        left = eval_prefix(node.left)
        right = eval_prefix(node.right)
        if node.data == '+': return left + right
        if node.data == '-': return left - right
        if node.data == '*': return left * right
        if node.data == '/': return left / right
    else:
        return int(node.data)
```

#### 중위 순회(Infix) 계산

- 실제 계산은 연산자 우선순위에 따라 괄호를 고려해야 하므로, 트리 구조를 이용하면 중위 순회로는 수식의 계산이 직접적으로 이루어지지 않습니다.
- 중위 순회는 주로 수식을 사람이 읽기 좋은 형태(중위 표기법)로 변환할 때 사용하며, 계산은 후위 또는 전위 순회를 통해 수행하는 것이 일반적입니다.

#### 후위 순회(Postfix) 계산

1. 왼쪽, 오른쪽 자식을 먼저 계산한 뒤, 현재 노드가 연산자면 두 값을 연산합니다.
2. 노드가 숫자면, 그 값을 반환합니다.

```python
def eval_postfix(node):
    if node is None:
        return 0
    if node.data in '+-*/':
        left = eval_postfix(node.left)
        right = eval_postfix(node.right)
        if node.data == '+': return left + right
        if node.data == '-': return left - right
        if node.data == '*': return left * right
        if node.data == '/': return left / right
    else:
        return int(node.data)
```

### 3. 예시

위 트리 구조에서 후위 순회로 계산하면 다음과 같습니다.

- 왼쪽 자식(3): 3
- 오른쪽 자식(`*`): 4 * 5 = 20
- 루트(`+`): 3 + 20 = 23

### 4. 요약

- **전위/후위 순회**를 이용하면 트리 구조에서 수식의 값을 쉽게 계산할 수 있습니다.
- 각 노드를 방문할 때 연산자라면 자식 노드의 값을 계산하여 연산을 수행합니다.
- 트리 구조는 복잡한 수식의 계산, 컴파일러의 파싱, 계산기 구현 등에 널리 활용됩니다.

---

