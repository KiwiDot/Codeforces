# 코드포스 1506A Strange Table
import sys
from math import ceil
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n, m, x = map(int, put().split())

    idx = x % n - 1 if x % n else n - 1
    jdx = ceil(x / n)

    print(idx * m + jdx)