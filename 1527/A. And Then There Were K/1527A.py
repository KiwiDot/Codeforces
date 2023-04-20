# 코드포스 1527A And Then There Were K
import sys
from math import log2
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    N = int(put())

    print(2 ** int(log2(N)) - 1)