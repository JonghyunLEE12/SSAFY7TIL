import sys

sys.stdin = open('input.txt')

T = int(input())

def dfs(cnt,now,total):
    global rlt
    if cnt == n:
        total += matrix[now][0]
        if total < rlt:
            rlt = total
            return
    if total > rlt:
        return

    for next in range(1,n):
        if now != next and visited[next] != 1:
            visited[next] = 1
            dfs(cnt+1,next,total + matrix[now][next])
            visited[next] = 0


for tc in range(1, T + 1):
    n = int(input())
    matrix = [ list(map(int,input().split())) for _ in range(n) ]
    rlt = 987654321
    visited = [0]*n
    dfs(1,0,0)

    print(f'#{tc} {rlt}')

