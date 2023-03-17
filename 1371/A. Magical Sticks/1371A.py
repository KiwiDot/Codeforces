# 코드포스 1371A Magical Sticks
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())

    print((n - 1) // 2 + 1)