# 코드포스 1399B Gifts Fixing
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    a = list(map(int, put().split()))
    b = list(map(int, put().split()))
    min_a, min_b = min(a), min(b)
    cnt = 0

    for i in range(n):
        cnt += max(a[i] - min_a, b[i] - min_b)

    print(cnt)