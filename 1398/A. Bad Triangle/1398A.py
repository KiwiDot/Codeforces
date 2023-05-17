# 코드포스 1398A Bad Triangle
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    a = list(map(int, put().split()))
    answer = ""

    ai, aj, ak = a[0], a[1], a[-1]
    if ai + aj > ak:
        print(-1)
    else:
        print(1, 2, n)