# 코드포스 1691A Beat The Odds
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    a = list(map(int, put().split()))
    r = [0, 0]

    for i in a:
        r[i % 2] += 1

    print(min(r))