# 코드포스 1353A Most Unstable Array
import sys
from math import ceil
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n, m = map(int, put().split())

    if n == 1:
        print(0)
        continue

    n = ceil(n / 2)
    if n > 1:
        print(m * 2)
    else:
        print(m)