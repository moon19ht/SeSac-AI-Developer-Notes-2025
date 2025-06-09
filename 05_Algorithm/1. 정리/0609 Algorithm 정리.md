# 🧮 Algorithm 이론과 개념 정리  

##### 🗓️ 2025.06.09
##### 📝 Writer : Moon19ht  

---

## 📚 목차




---

## 1. 트리를 이용한 전위, 중위, 후위 계산 방법

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

