# 코드포스 1562A The Miracle and the Sleeper
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    l, r = map(int, put().split())

    a = r
    b = max(r // 2 + 1, l)

    print(a % b)