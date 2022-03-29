import sys
import pprint
sys.stdin = open('input.txt')

from itertools import combinations
from collections import deque

# 델타 상 하 좌 우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(start):
    global empty
    visited = [[0]*n for _ in range(n)]
    queue = deque(start)
    for i in queue:
        visited[i[0]][i[1]] = 1

    while queue:
        node = queue.popleft()
        for i in range(4):
            nr = node[0] + dr[i]
            nc = node[1] + dc[i]
            if 0<= nr < n and 0<= nc < n and not visited[nr][nc] and matrix[nr][nc] != 1:
                visited[nr][nc] = visited[node[0]][node[1]] + 1
                empty -= 1
                queue.append((nr,nc))
    return visited[node[0]][node[1]] -1


n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]

count = 0
virus = []
for r in range(n):
    for c in range(n):
        if matrix[r][c] == 2:
            virus.append((r,c))
            count += 1
        if matrix[r][c] == 0:
            count += 1

ans = 1e10
for C in combinations(virus[0:m],m):
    empty = count - m
    tmp = bfs(C)

    if tmp < ans and not empty:
        ans = tmp

if ans == 1e10:
    print(-1)
else:
    print(ans)

