import sys

sys.stdin = open('input.txt')

T = int(input())

# run 또는 triplet 검사
def is_run_or_triplet(card):
    for i in range(len(card)):
        for j in range(i+1,len(card)):
            for k in range(j+1,len(card)):
                # 3개의 카드가 모두 같으면 run
                if card[i] == card[j] == card[k]:
                    return True
                # triplet 검사를 위해 정렬해준다.
                check_triplet = sorted([card[i],card[j],card[k]])
                # 3개의 카드가 순서를 이루면 triplet
                if check_triplet[0] + 2 == check_triplet[2] and check_triplet[1]+1 == check_triplet[2]:
                    return True
    # run 과 triplet을 만족 못하면 False
    return False

for tc in range(1, T + 1):
    numbers = list(map(int,input().split()))
    player1 = []
    player2 = []
    win = 0
    for i in range(len(numbers)):
        if i % 2:
            player2.append(numbers[i])
            if len(player2) >=3 and is_run_or_triplet(player2):
                win = 2
                break
        else:
            player1.append(numbers[i])
            if len(player1) >=3 and is_run_or_triplet(player1):
                win = 1
                break

    print(f'#{tc} {win}')

