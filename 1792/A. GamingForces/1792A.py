# 코드포스 1792A GamingForces
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    h = list(map(int, put().split()))
    cnt = h.count(1)
    h = len(h) - cnt

    print(h + cnt // 2 + 1 if cnt % 2 else h + cnt // 2)