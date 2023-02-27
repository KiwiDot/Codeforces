# 코드포스 1409A Yet Another Two Integers Problem
import sys
from math import ceil
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    a, b = map(int, put().split())
    print(ceil(abs(a-b) / 10))