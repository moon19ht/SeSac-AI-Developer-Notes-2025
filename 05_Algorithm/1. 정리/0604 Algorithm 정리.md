# 🧮 Algorithm 이론과 개념 정리  

##### 🗓️ 2025.06.04  
##### 📝 Writer : Moon19ht  

---

## 📚 목차  

- [1. 연결 리스트](#1-연결-리스트)
- [2. 스택](#2-스택)

---

## 1. 연결 리스트(Linked List)

연결 리스트는 데이터를 저장하는 노드들이 일렬로 연결된 선형 자료 구조입니다. 각 노드는 데이터와 다음 노드에 대한 참조(포인터)를 가지고 있습니다. 배열과 달리 연결 리스트는 크기가 동적으로 변할 수 있고, 데이터의 삽입/삭제가 효율적입니다.

### 1.1. 연결 리스트의 구조

- **노드(Node)**: 데이터와 다음 노드를 가리키는 포인터(참조)로 구성됩니다.
- **헤드(Head)**: 연결 리스트의 첫 번째 노드를 가리키는 포인터입니다.
- **테일(Tail)**: 마지막 노드는 다음 노드에 대한 포인터가 `None`입니다.

### 1.2. 연결 리스트의 종류

- **단일 연결 리스트(Singly Linked List)**: 한 방향(다음 노드)으로만 연결됨.
- **이중 연결 리스트(Doubly Linked List)**: 이전 노드와 다음 노드 모두를 참조.
- **원형 연결 리스트(Circular Linked List)**: 마지막 노드가 첫 번째 노드를 가리킴.

### 1.3. 파이썬으로 구현하는 단일 연결 리스트

```python
# 노드 클래스 정의
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 연결 리스트 클래스 정의
class LinkedList:
    def __init__(self):
        self.head = None

    # 리스트 끝에 데이터 추가
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # 리스트 출력
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# 사용 예시
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()  # 1 -> 2 -> 3 -> None
```

### 1.4. 연결 리스트의 주요 연산

- **삽입(append, insert)**: 원하는 위치에 노드 추가
- **삭제(remove)**: 특정 값을 가진 노드 삭제
- **탐색(search)**: 특정 값을 가진 노드 찾기
- **출력(display)**: 리스트의 모든 노드 출력

### 1.5. 연결 리스트의 장단점

- **장점**
  - 크기가 동적으로 변함
  - 중간에 데이터 삽입/삭제가 빠름(포인터만 변경)
- **단점**
  - 임의 접근이 느림(순차 탐색 필요)
  - 추가적인 포인터 공간 필요

---

## 2. 스택(Stack)

스택은 데이터를 일시적으로 저장할 때 사용하는 선형 자료 구조로, **후입선출(Last-In, First-Out, LIFO)**의 특징을 가진다. 즉, 가장 나중에 삽입된 데이터가 가장 먼저 삭제된다. 스택은 한 쪽 끝에서만 데이터를 추가(push)하거나 삭제(pop)할 수 있다.

### 2.1. 스택의 주요 연산

- **push(item)** : 스택의 맨 위에 데이터를 추가한다.
- **pop()** : 스택의 맨 위에 있는 데이터를 삭제하고 반환한다.
- **peek()** : 스택의 맨 위에 있는 데이터를 삭제하지 않고 반환한다.
- **is_empty()** : 스택이 비어 있는지 확인한다.

### 2.2. 스택의 활용 예시

- 함수 호출(재귀 호출) 시 호출 정보를 저장
- 웹 브라우저의 뒤로 가기 기능
- 괄호의 짝 검사
- 깊이 우선 탐색(DFS) 등

### 2.3. 파이썬으로 구현하는 스택

파이썬에서는 리스트(list)를 이용해 간단하게 스택을 구현할 수 있다.

```python
# 리스트를 이용한 스택 구현
stack = []

# 데이터 추가 (push)
stack.append(1)
stack.append(2)
stack.append(3)
print("스택 상태:", stack)  # [1, 2, 3]

# 데이터 삭제 (pop)
top = stack.pop()
print("pop된 값:", top)    # 3
print("스택 상태:", stack)  # [1, 2]
```

#### 스택 클래스 직접 구현하기

```python
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("스택이 비어 있습니다.")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("스택이 비어 있습니다.")
        return self.items[-1]

    def size(self):
        return len(self.items)

# 사용 예시
s = Stack()
s.push(10)
s.push(20)
print(s.pop())   # 20
print(s.peek())  # 10
print(s.size())  # 1
```

### 2.4. 스택의 장단점

- **장점**
  - 구현이 간단하다.
  - 데이터의 추가/삭제가 빠르다(시간복잡도 O(1)).
- **단점**
  - 중간에 있는 데이터에 접근이 불가능하다(맨 위에서만 접근 가능).

---


