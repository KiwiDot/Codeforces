# 코드포스 1716A 2-3 Moves
import sys
from math import ceil
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    if n == 1:
        print(2)

    else:
        print(ceil(n / 3))