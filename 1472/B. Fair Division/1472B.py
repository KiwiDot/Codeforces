# 코드포스 1472B Fair Division
import sys
from collections import Counter
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    a = {**{'1': 0, '2': 0}, **dict(Counter(put().split()))}
    c1, c2 = a['1'], a['2']

    if not c1 % 2 and (not c2 % 2 or c1 > 1):
        print("YES")
    else:
        print("NO")