import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())

# 델타 오른쪽 아래
dr = [0,1]
dc = [1,0]

def dfs(r,c):
    global total,sum_num

    if sum_num > total:                                            # 현재 sum이 최소값 보다 커졌으면 return
        return

    if r == n-1 and c == n-1:                                      # 오른쪽 아래에 도착했을때
        total = sum_num                                            # 최소값 갱신
        return

    for k in range(2):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0<= nr < n and 0<= nc < n and visited[nr][nc] != 1:
            visited[nr][nc] = 1                                     # 범위를 만족했을때 방문 처리
            sum_num += matrix[nr][nc]                               # sum 값 갱신
            dfs(nr,nc)                                              # dfs
            visited[nr][nc] = 0                                     # 방문값 초기화
            sum_num -= matrix[nr][nc]                               # 최근 갈림길까지 sum 빼준다.

for tc in range(1, T + 1):
    n = int(input())
    matrix = [ list(map(int,input().split())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]                             # 방문처리할 visited 생성
    total = 987654321                                               # 최대값 설정
    sum_num = matrix[0][0]                                          # sum_num 에 시작점
    dfs(0,0)                                                        # 시작점 시작
    print(f'#{tc} {total}')

