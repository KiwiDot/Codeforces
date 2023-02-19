# 코드포스 148A Insomnia cure
import sys
put = sys.stdin.readline

k = int(put())
l = int(put())
m = int(put())
n = int(put())
d = int(put())
cnt = 0

for i in range(1, d+1):
    if i % k and i % l and i % m and i % n:
        cnt += 1

print(d - cnt)