# 코드포스 1631A Min Max Swap
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    a = list(map(int, put().split()))
    b = list(map(int, put().split()))

    if max(a) > max(b):
        a, b = b, a

    for i in range(n):
        a[i], b[i] = sorted([a[i], b[i]])

    print(max(a) * max(b))