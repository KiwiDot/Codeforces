# 코드포스 268A Games
import sys
put = sys.stdin.readline

n = int(put())
h = []
a = dict([(i, 0) for i in range(1, 101)])
cnt = 0

while n:
    n -= 1
    hi, ai = map(int, put().split())
    h.append(hi)
    a[ai] += 1

for i in h:
    cnt += a[i]
print(cnt)