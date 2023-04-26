# 코드포스 1692B All Distinct
import sys
from collections import Counter
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    a = list(map(int, put().split()))
    count = dict(Counter(a))
    cnt = sum([i - 1 for i in count.values()])
    if cnt % 2:
        cnt += 1

    print(n - cnt)