import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    n,m = map(int,input().split())
    weight = list(map(int,input().split()))
    truck = list(map(int,input().split()))

    weight = sorted(weight,reverse=True)        # 무거운 순으로 정렬
    truck = sorted(truck,reverse=True)          # 트럭 적재용량 많은 순으로 정렬

    rlt = [0]*m                                 # 결과리스트를 트럭의 수 만큼
    for i in range(n):
        for j in range(m):
            if weight[i] <= truck[j]:           # 트럭에 적재가 가능할때
                if not rlt[j]:                  # rlt[j] 가 비어있으면
                    rlt[j] = weight[i]          # 적재
                    break                       # 다음을 보자
    print(f'#{tc} {sum(rlt)}')

