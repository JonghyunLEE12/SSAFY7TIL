import sys

sys.stdin = open('input.txt')

def dfs(x,y,size):
    if size == 1:
        return lst[x][y]
    count = 0
    for i in range(x,x+size):
        for j in range(y,y+size):
            count += int(lst[x][y])
    if count == 0 or count == size **2:
        if count == 0:
            return '0'
        else:
            return '1'
    halfsize = size//2
    return(
        '('
        + dfs(x,y,halfsize)
        + dfs(x,y+halfsize,halfsize)
        + dfs(x+halfsize,y,halfsize)
        + dfs(x+halfsize,y+halfsize,halfsize)
        + ')'
    )


n = int(input())
lst = [list(input()) for _ in range(n)]
print(dfs(0,0,n))