# 백준 1729A Two Elevators
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    a, b, c = map(int, put().split())

    e1 = abs(a - 1)
    e2 = abs(c - b) + abs(c - 1)

    if e1 < e2:
        print(1)
    elif e1 > e2:
        print(2)
    else:
        print(3)