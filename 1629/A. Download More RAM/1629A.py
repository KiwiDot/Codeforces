# 코드포스 1629A Download More RAM
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n, k = map(int, put().split())
    a = list(map(int, put().split()))
    b = list(map(int, put().split()))

    program = sorted([[a[i], b[i]] for i in range(n)], key=lambda x: [x[0], x[1]])

    for i in program:
        a, b = i
        if k >= a:
            k += b
        else:
            break

    print(k)