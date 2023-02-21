# 코드포스 996A Hit the Lottery
import sys
put = sys.stdin.readline

n = int(put())
money = [100, 20, 10, 5, 1]
cnt = 0

for i in money:
    cnt += n // i
    n %= i

print(cnt)