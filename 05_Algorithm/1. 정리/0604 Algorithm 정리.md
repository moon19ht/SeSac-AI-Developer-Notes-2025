# 🧮 Algorithm 이론과 개념 정리  

##### 🗓️ 2025.06.04  
##### 📝 Writer : Moon19ht  

---

## 📚 목차  


- [1. 큐](#1-큐)
- [2. 링크드 리스트](#2-링크드-리스트)
- [3. 이중 링크드 리스트](#3-이중-링크드-리스트)

---

## 1. 큐

큐(Queue)는 선입선출(FIFO, First-In-First-Out) 방식의 자료구조입니다. 먼저 들어온 데이터가 먼저 나가게 됩니다. 주로 대기열, 프린터 작업 처리 등 순서가 중요한 곳에서 사용됩니다.

### 주요 연산

- **enqueue**: 큐의 뒤에 데이터를 추가
- **dequeue**: 큐의 앞에서 데이터를 제거 및 반환
- **peek**: 큐의 앞에 있는 데이터를 확인(제거하지 않음)
- **is_empty**: 큐가 비어있는지 확인

### 예시

파이썬에서는 `collections.deque`를 사용하여 큐를 쉽게 구현할 수 있습니다.

```python
from collections import deque

# 큐 생성
queue = deque()

# 데이터 추가 (enqueue)
queue.append('A')
queue.append('B')
queue.append('C')

print("큐 상태:", queue)  # 큐 상태: deque(['A', 'B', 'C'])

# 데이터 제거 (dequeue)
first = queue.popleft()
print("제거된 데이터:", first)  # 제거된 데이터: A
print("큐 상태:", queue)       # 큐 상태: deque(['B', 'C'])

# 큐의 맨 앞 데이터 확인 (peek)
front = queue[0]
print("맨 앞 데이터:", front)  # 맨 앞 데이터: B

# 큐가 비어있는지 확인
print("큐가 비어있는가?", not queue)  # 큐가 비어있는가? False
```

### 활용 예시

- **프린터 대기열**: 인쇄 요청이 들어온 순서대로 처리
- **탐색 알고리즘**: BFS(너비 우선 탐색)에서 사용

---

## 2. 링크드 리스트

링크드 리스트(Linked List)는 각 요소(노드)가 데이터와 다음 노드를 가리키는 포인터(참조)로 구성된 선형 자료구조입니다. 배열과 달리 메모리상에 연속적으로 저장되지 않고, 필요에 따라 동적으로 크기를 조절할 수 있습니다. 삽입과 삭제가 빠르지만, 임의의 위치에 접근하려면 순차적으로 탐색해야 하므로 접근 속도는 느립니다.

### 주요 특징

- **노드(Node)**: 데이터와 다음 노드를 가리키는 포인터(`next`)로 구성
- **동적 메모리 할당**: 크기 제한이 없고, 필요할 때마다 노드를 추가/삭제 가능
- **중간 삽입/삭제 효율적**: 포인터만 변경하면 되므로 O(1) 시간 복잡도(삽입/삭제 위치를 알고 있을 때)
- **임의 접근 비효율적**: 특정 위치에 접근하려면 처음부터 순차 탐색 필요(O(n))
- **메모리 사용**: 각 노드마다 포인터를 추가로 저장하므로 배열보다 메모리 사용량이 많을 수 있음

### 구조도

```
[Head] -> [A|next] -> [B|next] -> [C|next] -> None
```

### 주요 연산

- **append(data)**: 리스트 끝에 데이터 추가
- **insert(pos, data)**: 지정한 위치에 데이터 삽입
- **delete(data)**: 지정한 데이터를 가진 노드 삭제
- **search(data)**: 데이터 탐색
- **print_list()**: 전체 리스트 출력

### 파이썬 구현 예시

파이썬에는 내장 링크드 리스트 자료구조가 없으므로, 클래스를 직접 정의하여 구현합니다.

```python
```python
# 노드 클래스 정의: 데이터와 다음 노드를 가리키는 포인터를 가짐
class Node:
    def __init__(self, data):
        self.data = data      # 노드가 저장할 데이터
        self.next = None      # 다음 노드를 가리키는 포인터

# 단일 링크드 리스트 클래스 정의
class LinkedList:
    def __init__(self):
        self.head = None      # 리스트의 첫 번째 노드를 가리키는 포인터

    # 리스트 끝에 데이터 추가
    def append(self, data):
        new_node = Node(data)
        if not self.head:     # 리스트가 비어있으면 새 노드를 head로 지정
            self.head = new_node
            return
        curr = self.head
        while curr.next:      # 마지막 노드까지 이동
            curr = curr.next
        curr.next = new_node  # 마지막 노드의 next에 새 노드 연결

    # 지정한 위치(pos)에 데이터 삽입
    def insert(self, pos, data):
        new_node = Node(data)
        if pos == 0:          # 맨 앞에 삽입하는 경우
            new_node.next = self.head
            self.head = new_node
            return
        curr = self.head
        for _ in range(pos - 1):  # 삽입 위치 바로 전 노드까지 이동
            if curr is None:
                return            # 위치가 리스트 길이보다 크면 아무 작업도 하지 않음
            curr = curr.next
        new_node.next = curr.next # 새 노드의 next를 현재 노드의 next로 지정
        curr.next = new_node      # 현재 노드의 next를 새 노드로 변경

    # 지정한 데이터를 가진 노드 삭제
    def delete(self, data):
        curr = self.head
        prev = None
        while curr:
            if curr.data == data:     # 삭제할 데이터를 찾으면
                if prev:
                    prev.next = curr.next  # 이전 노드의 next를 현재 노드의 next로 변경
                else:
                    self.head = curr.next  # 삭제할 노드가 head인 경우 head를 다음 노드로 변경
                return
            prev = curr
            curr = curr.next

    # 리스트 전체 출력
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=' -> ')
            curr = curr.next
        print('None')

# 사용 예시
ll = LinkedList()
ll.append('A')         # 리스트: A
ll.append('B')         # 리스트: A -> B
ll.append('C')         # 리스트: A -> B -> C
ll.insert(1, 'D')      # 1번째 위치에 'D' 삽입: A -> D -> B -> C
ll.print_list()        # 출력: A -> D -> B -> C -> None
ll.delete('B')         # 'B' 삭제: A -> D -> C
ll.print_list()        # 출력: A -> D -> C -> None
```


### 활용 예시

- **메모리 관리**: 동적으로 크기가 변하는 데이터 저장
- **실시간 데이터 처리**: 음악 재생 목록, 작업 스케줄러 등
- **스택, 큐 등 다른 자료구조의 기반**: 링크드 리스트로 스택, 큐 구현 가능

---

## 3. 이중 링크드 리스트

이중 링크드 리스트(Doubly Linked List)는 각 노드가 데이터와 함께 두 개의 포인터(참조)를 가지는 자료구조입니다. 하나는 이전 노드를, 다른 하나는 다음 노드를 가리킵니다. 이를 통해 양방향으로 리스트를 탐색할 수 있어, 단일 링크드 리스트보다 삽입과 삭제가 더 유연합니다.

### 주요 특징

- **양방향 연결**: 각 노드는 `prev`(이전 노드)와 `next`(다음 노드)를 참조
- **양방향 탐색**: 앞/뒤로 자유롭게 이동 가능
- **중간 삽입/삭제 용이**: 노드의 포인터만 적절히 변경하면 O(1) 시간에 삽입/삭제 가능(노드 위치를 알고 있을 때)
- **메모리 사용 증가**: 각 노드가 두 개의 포인터를 저장하므로 단일 링크드 리스트보다 메모리 사용량이 많음

### 구조도

```
None <- [A|prev|next] <-> [B|prev|next] <-> [C|prev|next] -> None
```

### 주요 연산

- **append(data)**: 리스트 끝에 데이터 추가
- **insert(pos, data)**: 지정한 위치에 데이터 삽입
- **delete(data)**: 지정한 데이터를 가진 노드 삭제
- **print_forward()**: 앞에서 뒤로 리스트 출력
- **print_backward()**: 뒤에서 앞으로 리스트 출력

### 파이썬 구현 예시

```python
# 노드 클래스 정의: 데이터, 이전 노드(prev), 다음 노드(next) 포인터를 가짐
class Node:
    def __init__(self, data):
        self.data = data      # 노드가 저장할 데이터
        self.prev = None      # 이전 노드를 가리키는 포인터
        self.next = None      # 다음 노드를 가리키는 포인터

# 이중 링크드 리스트 클래스 정의
class DoublyLinkedList:
    def __init__(self):
        self.head = None      # 리스트의 첫 번째 노드를 가리키는 포인터

    # 리스트 끝에 데이터 추가
    def append(self, data):
        new_node = Node(data)
        if not self.head:     # 리스트가 비어있으면 새 노드를 head로 지정
            self.head = new_node
            return
        curr = self.head
        while curr.next:      # 마지막 노드까지 이동
            curr = curr.next
        curr.next = new_node  # 마지막 노드의 next에 새 노드 연결
        new_node.prev = curr  # 새 노드의 prev를 마지막 노드로 지정

    # 지정한 위치(pos)에 데이터 삽입
    def insert(self, pos, data):
        new_node = Node(data)
        if pos == 0:          # 맨 앞에 삽입하는 경우
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return
        curr = self.head
        for _ in range(pos - 1):  # 삽입 위치 바로 전 노드까지 이동
            if curr is None:
                return            # 위치가 리스트 길이보다 크면 아무 작업도 하지 않음
            curr = curr.next
        if curr is None:
            return
        new_node.next = curr.next # 새 노드의 next를 현재 노드의 next로 지정
        new_node.prev = curr      # 새 노드의 prev를 현재 노드로 지정
        if curr.next:
            curr.next.prev = new_node  # 다음 노드의 prev를 새 노드로 변경
        curr.next = new_node      # 현재 노드의 next를 새 노드로 변경

    # 지정한 데이터를 가진 노드 삭제
    def delete(self, data):
        curr = self.head
        while curr:
            if curr.data == data:     # 삭제할 데이터를 찾으면
                if curr.prev:
                    curr.prev.next = curr.next  # 이전 노드의 next를 현재 노드의 next로 변경
                else:
                    self.head = curr.next       # 삭제할 노드가 head인 경우 head를 다음 노드로 변경
                if curr.next:
                    curr.next.prev = curr.prev  # 다음 노드의 prev를 현재 노드의 prev로 변경
                return
            curr = curr.next

    # 앞에서 뒤로 리스트 출력
    def print_forward(self):
        curr = self.head
        while curr:
            print(curr.data, end=' <-> ')
            last = curr
            curr = curr.next
        print('None')

    # 뒤에서 앞으로 리스트 출력
    def print_backward(self):
        curr = self.head
        if not curr:
            print('None')
            return
        while curr.next:   # 마지막 노드까지 이동
            curr = curr.next
        while curr:
            print(curr.data, end=' <-> ')
            curr = curr.prev
        print('None')

# 사용 예시
dll = DoublyLinkedList()
dll.append('A')         # 리스트: A
dll.append('B')         # 리스트: A <-> B
dll.append('C')         # 리스트: A <-> B <-> C
dll.insert(1, 'D')      # 1번째 위치에 'D' 삽입: A <-> D <-> B <-> C
dll.print_forward()     # 출력: A <-> D <-> B <-> C <-> None
dll.delete('B')         # 'B' 삭제: A <-> D <-> C
dll.print_forward()     # 출력: A <-> D <-> C <-> None
dll.print_backward()    # 출력: C <-> D <-> A <-> None
```

### 활용 예시

- **브라우저 방문 기록**: 앞/뒤로 이동
- **텍스트 에디터의 undo/redo 기능**
- **양방향 탐색이 필요한 자료구조**: LRU 캐시 등
