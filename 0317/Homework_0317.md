# Homework_0317

### # 1231_사칙연산

```python
import sys

sys.stdin = open('input.txt')

T = 10


for tc in range(1, T + 1):
    N = int(input())
    tree = [0]*(N+1)
    matrix = [[0]*3 for _ in range(N+1)]

    for i in range(1,N+1):
        values = list(map(str,input().split()))
        tree[i] = values[1]

        if values[1] == '+' or values[1]=='-' or values[1]=='*' or values[1]=='/':
            matrix[i][1], matrix[i][2] = int(values[2]), int(values[3])
            matrix[int(values[2])][0], matrix[int(values[3])][0] = i, i

    for j in range(N,0,-1):
        if tree[j] == '-':
            tree[j] = int(tree[matrix[j][1]]) - int(tree[matrix[j][2]])
        elif tree[j] == '+':
            tree[j] = int(tree[matrix[j][1]]) + int(tree[matrix[j][2]])
        elif tree[j] == '/':
            tree[j] = int(tree[matrix[j][1]]) // int(tree[matrix[j][2]])
        elif tree[j] == '*':
            tree[j] = int(tree[matrix[j][1]]) * int(tree[matrix[j][2]])

    print(f'#{tc} {tree[1]}')
```

