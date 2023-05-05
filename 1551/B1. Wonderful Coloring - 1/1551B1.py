# 코드포스 1551B1 Wonderful Coloring - 1
import sys
from collections import Counter
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    s = put().strip()
    k = 0

    cnt = dict(Counter(s))
    check = set()

    for i in cnt.keys():
        if cnt[i] > 1:
            k += 1
        else:
            check.add(i)

    k += len(check) // 2
    print(k)