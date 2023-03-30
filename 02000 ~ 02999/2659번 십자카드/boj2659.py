# 백준 2659번 십자카드
import sys
from itertools import product
put = sys.stdin.readline

card = [str(i) for i in range(1, 10)]
num = ''.join(put().split())
num = min([int(num[i:] + num[:i]) for i in range(4)])
cnt = 0

for i in product(card, repeat=4):
    num_i = ''.join(i)
    num_i = min([int(num_i[i:] + num_i[:i]) for i in range(4)])

    if int(''.join(i)) == num_i:
        cnt += 1

        if num == num_i:
            print(cnt)
            break