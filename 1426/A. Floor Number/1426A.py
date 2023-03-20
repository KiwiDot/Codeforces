# 코드포스 1426A Floor Number
import sys
from math import ceil
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n, x = map(int, put().split())

    if n <= 2:
        print(1)
    else:
        n -= 2
        print(ceil(n / x) + 1)