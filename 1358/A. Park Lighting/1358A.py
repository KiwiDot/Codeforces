# 코드포스 1358A Park Lighting
import sys
from math import ceil
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n, m = map(int, put().split())

    print(ceil(n * m / 2))

