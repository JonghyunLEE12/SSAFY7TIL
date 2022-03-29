import sys

sys.stdin = open('input.txt')

n,m = map(int,input().split())
numbers = list(map(int,input().split()))
numbers.sort()
stack = []
visited = [0]*n

def dfs(start):
    if len(stack) == m:
        print(*stack)
    for next in range(start,n):
        if not visited[next]:
            stack.append(numbers[next])
            visited[next] = 1
            dfs(start+1)
            stack.pop()
            visited[next] = 0

dfs(0)
