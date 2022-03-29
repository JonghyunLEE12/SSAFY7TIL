import sys
import pprint

sys.stdin = open('input.txt')


from collections import deque
from itertools import combinations



# 델타 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(starts):
    global remain_empty
    visited = [[0]*n for _ in range(n)]
    queue = deque(starts)
    for i in queue:
        visited[i[0]][i[1]] = 1                                 # 시작점 방문

    while queue:
        node = queue.popleft()
        for i in range(4):
            nr = node[0] + dr[i]
            nc = node[1] + dc[i]
            if 0<= nr < n and 0<= nc < n and not visited[nr][nc] and matrix[nr][nc] != 1:
                visited[nr][nc] = visited[node[0]][node[1]] + 1 # 방문 처리 및 거리 증가
                remain_empty -=1                                # 비어있는 거리 -1
                queue.append((nr,nc))                           # queue.append
    return visited[node[0]][node[1]] -1                         # 필요한 시간 반환




n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]

'''
. 0은 빈 칸, 1은 벽, 2는 바이러스를 놓을 수 있는 칸이다. 2의 개수는 M보다 크거나 같고, 10보다 작거나 같은 자연수이다.
'''

# 바이러스 시작 가능 좌표
virus = []
# 비어있는 공간 파악
count = 0
ans = 987654321
for r in range(len(matrix)):
    for c in range(len(matrix)):
        if matrix[r][c] == 2:
            virus.append([r,c])
            count += 1
        elif matrix[r][c] == 0:
            count += 1

# 바이러스를 놓을 수 있는 공간 조합
for C in combinations(virus,m):
    # 비어있는 공간 - 바이러스 놓을 개 수
    remain_empty = count - m
    tmp = bfs(C)
    if tmp < ans and remain_empty == 0:
        ans = tmp

if ans == 987654321:
    print(-1)
else:
    print(ans)