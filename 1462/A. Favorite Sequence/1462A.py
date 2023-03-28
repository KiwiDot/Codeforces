# 코드포스 1462A Favorite Sequence
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    b = put().split()
    a = []

    for i in range(n):
        if i % 2:
            a.append(b.pop(-1))
        else:
            a.append(b.pop(0))

    print(' '.join(a))