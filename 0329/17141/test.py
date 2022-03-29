import sys
import pprint

sys.stdin = open('input.txt')
'''
첫째 줄에 연구소의 크기 N(5 ≤ N ≤ 50), 놓을 수 있는 바이러스의 개수 M(1 ≤ M ≤ 10)이 주어진다.
0은 빈 칸, 1은 벽, 2는 바이러스를 놓을 수 있는 칸이다. 
'''
from itertools import combinations
from collections import deque

# 델타
dr =[-1,1,0,0]
dc =[0,0,-1,1]

def bfs(starts):
    global empty
    # 방문 좌표
    visited = [[0]*n for _ in range(n)]
    queue = deque(starts)

    # 시작점 방문 처리
    for i in queue:
        visited[i[0]][i[1]] = 1

    while queue:
        nodes = queue.popleft()
        for i in range(4):
            nr = nodes[0] + dr[i]
            nc = nodes[1] + dc[i]
            # 범위 안에 있고, 방문을 하지 않았으며, 벽이 아닌 경우에
            if 0<= nr < n and 0<= nc < n and not visited[nr][nc] and matrix[nr][nc] != 1:
                # 방문 처리 및 거리(시간) + 1
                visited[nr][nc] += visited[nodes[0]][nodes[1]] + 1
                # 비어있는 공간 -1
                empty -= 1
                queue.append((nr,nc))
    return visited[nodes[0]][nodes[1]] - 1                      # 마지막 방문처리한애가 가장 오래간애라서

n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]


virus = []                                                      # 바이러스 좌표를 담아둘 리스트
count = 0                                                       # 벽이 아닌 빈 공간
for r in range(len(matrix)):
    for c in range(len(matrix)):
        if matrix[r][c] == 2:                                   # 바이러스 좌표 append
            virus.append([r,c])
            count += 1                                          # 공간 +1
        elif matrix[r][c] == 0:
            count += 1

ans = 1e10
for C in combinations(virus,m):                                 # 바이러스 놓을 좌표들의 조합
    empty = count - m                                           # 공간 - m(바이러스 놓을 개수)
    tmp = bfs(C)                                                # tmp => 걸리는 시간
    if tmp < ans and empty == 0:                                # 만약 최소값이고, 비어있는 공간이 없다면
        ans = tmp                                               # 정답 갱신

if ans == 1e10:
    print(-1)
else:
    print(ans)

