# 코드포스 1234A Equalize Prices Again
import sys
from math import ceil
put = sys.stdin.readline

q = int(put())

while q:
    q -= 1
    n = int(put())
    a = list(map(int, put().split()))

    print(ceil(sum(a) / n))