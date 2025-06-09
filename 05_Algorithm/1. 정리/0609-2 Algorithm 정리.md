# 🧮 Algorithm 이론과 개념 정리  

##### 🗓️ 2025.06.09
##### 📝 Writer : Moon19ht  

---

## 📚 목차

- [1. 배열로 이진트리 표현하기](#1-배열로-이진트리-표현하기)
- [2. 재귀 순회 함수 만들기](#2-재귀-순회-함수만들기)
- [3. 스택으로 순회함수 만들기](#3-스택으로-순회함수만들기)
- [4. 연결 리스트로 이진트리 표현하기](#4-연결-리스트로-이진트리-표현하기)

---

# 1. 배열로 이진트리 표현하기

![이진트리 배열](https://wikidocs.net/images/page/193817/fig-044.png)


| 인덱스 | 0 | 1 | 2 | 3 | 4 | 5 | 6    | 7 |
|--------|---|---|---|---|---|---|------|---|
|   값   | A | B | C | D | E | F | None | G |

## 배열에서 노드의 인덱스 계산

배열을 사용해 이진트리를 나타낼 때, 각 노드의 인덱스에 따른 부모 노드와 자식 노드의 인덱스를 다음 규칙으로 계산할 수 있다.

- 부모 노드가 인덱스 `n`일 때:
    - 왼쪽 자식 노드의 인덱스: `2 × n + 1`
    - 오른쪽 자식 노드의 인덱스: `2 × n + 2`
- 자식 노드가 인덱스 `n`일 때:
    - 부모 노드의 인덱스: `(n - 1) // 2`

## 예시

- A(루트)의 인덱스는 0:
  - 왼쪽 자식 B의 인덱스: `2 × 0 + 1 = 1`
  - 오른쪽 자식 C의 인덱스: `2 × 0 + 2 = 2`
- B의 인덱스는 1:
  - 왼쪽 자식 D의 인덱스: `2 × 1 + 1 = 3`
  - 오른쪽 자식 E의 인덱스: `2 × 1 + 2 = 4`
- C의 인덱스는 2:
  - 왼쪽 자식 F의 인덱스: `2 × 2 + 1 = 5`
- D의 인덱스는 3:
  - 왼쪽 자식 G의 인덱스: `2 × 3 + 1 = 7`

인덱스 0은 비워두고, 인덱스 1부터 자료를 넣어 트리를 구성하기도 한다. 그렇게 하면 왼쪽 자식 노드의 인덱스는 `(2 × n)`, 오른쪽 자식 노드의 인덱스는 `( 2 × n + 1)` 이다. 그럼 부모 노드의 인덱스는 자식 노드의 인덱스를 2로 나눈 몫만 취하면 된다.

## 자식 노드와 부모 노드를 찾기
### 자식 노드 찾기

- 배열을 순회한다.
  - 값이 None이 아니면
    - 값을 출력한다.
    - 왼쪽 자식 노드와 오른쪽 자식 노드의 인덱스를 계산한다.
    - 각 인덱스가 배열의 길이보다 작고, 해당 배열의 값이 None이 아니면 출력한다.

```python
tree = ["A", "B", "C", "D", "E", "F", None, "G"]

n = len(tree)
for i in range(n):
    if tree[i] is not None:  # 현재 노드가 None이 아닐 때
        print(f"Parent: {tree[i]}", end=", ")
        left = 2 * i + 1  # 왼쪽 자식 노드
        right = 2 * i + 2  # 오른쪽 자식 노드

        if left < n and tree[left] is not None:  # 왼쪽 자식이 배열 범위 안에 있을 때
            print(f"Left: {tree[left]}", end=", ")
        if right < n and tree[right] is not None:  # 오른쪽 자식이 배열 범위 안에 있을 때
            print(f"Right: {tree[right]}", end=" ")
        print()
```

실행 결과

```
Parent: A, Left: B, Right: C 
Parent: B, Left: D, Right: E 
Parent: C, Left: F, 
Parent: D, Left: G, 
Parent: E, 
Parent: F, 
Parent: G, 
```

### 부모 노드 찾기
```python
# 위의 코드에 이어서 작성

# 부모 노드 찾기
for i in range(1, n):  # 루트 노드 제외하고 순회
    if tree[i] is not None:
        print(f"Parent of {tree[i]} -> {tree[(i-1)//2]}")
```

실행 결과
```
Parent of B -> A
Parent of C -> A
Parent of D -> B
Parent of E -> B
Parent of F -> C
Parent of G -> D
```

---

# 2. 재귀 순회 함수 만들기

