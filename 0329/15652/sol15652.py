import sys

sys.stdin = open('input.txt')

n,m = map(int,input().split())

stack = []

def dfs(start):
    if len(stack) == m:
        print(*stack)
        return
    for next in range(start,n+1):
        stack.append(next)
        dfs(next)
        stack.pop()
dfs(1)

