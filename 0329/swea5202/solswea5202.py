import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    n = int(input())
    paper = [list(map(int,input().split())) for _ in range(n)]  # 신청서 정보 받음
    sorted_paper = sorted(paper, key=lambda x: x[1])            # 종료시간별로 순서정렬

    cnt = 0                                                     # 최대 몇대의 화물차가 이용 가능한가?
    now = 0
    for i in range(n):
        start = sorted_paper[i][0]                              # 시작시간
        end = sorted_paper[i][1]                                # 종료시간
        if now <= start:                                        # 만약 시작시간이 크거나(24시간) 같을 때
            cnt +=1                                             # 작업 횟수 +1
            now = end                                           # now 를 종료시간으로 갱신

    print(f'#{tc} {cnt}')

