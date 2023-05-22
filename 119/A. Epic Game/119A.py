# 코드포스 119A Epic Game
import sys
from math import gcd
put = sys.stdin.readline

a, b, n = map(int, put().split())

for i in range(n+1):
    if i % 2:
        gcd_i = gcd(b, n)
    else:
        gcd_i = gcd(a, n)

    if n:
        n -= gcd_i
    else:
        print((i % 2) ^ 1)
        break

