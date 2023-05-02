# 코드포스 1619B Squares and Cubes
import sys
from math import ceil
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    n2 = {i ** 2 for i in range(1, ceil(n ** (1/2))+1) if i ** 2 <= n}
    n3 = {i ** 3 for i in range(1, ceil(n ** (1/3))+1) if i ** 3 <= n}

    print(len(n2 | n3))