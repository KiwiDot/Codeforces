# 코드포스 1389A LCM Problem
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    l, r = map(int, put().split())
    answer = ""

    if l * 2 <= r:
        print(l, l*2)
    else:
        print(-1, -1)