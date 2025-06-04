# 🧮 Algorithm 이론과 개념 정리  

##### 🗓️ 2025.06.04  
##### 📝 Writer : Moon19ht  

---

## 📚 목차  


- [1. 큐](#1-큐)

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
