# 코드포스 1478A Nezzar and Colorful Balls
import sys
from collections import Counter
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    a = list(map(int, put().split()))

    cnt = dict(Counter(a))
    print(max(cnt.values()))