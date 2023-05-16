# 코드포스 1557A Ezzat and Two Subsequences
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    a = list(map(int, put().split()))

    fa = max(a)
    fb = (sum(a) - max(a)) / (n - 1)

    print(fa + fb)