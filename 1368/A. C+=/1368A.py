# 코드포스 1368A C+=
import sys
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    a, b, n = map(int, put().split())
    cnt = 0

    while a <= n and b <= n:
        cnt += 1
        if a < b:
            a += b
        else:
            b += a

    print(cnt)