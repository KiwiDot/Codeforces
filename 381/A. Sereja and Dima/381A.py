# 코드포스 381A Sereja and Dima
import sys
put = sys.stdin.readline

n = int(put())
card = list(map(int, put().split()))
score = [0, 0]
turn = 0

while card:
    if card[0] > card[-1]:
        score[turn] += card.pop(0)
    else:
        score[turn] += card.pop(-1)

    turn ^= 1

print(score[0], score[1])