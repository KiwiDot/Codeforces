# 코드포스 1397A Juggling Letters
import sys
from collections import Counter
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    cnt = Counter()

    for i in range(n):
        s = put().strip()
        cnt += Counter(s)

    cnt = dict(cnt)
    check = {i % n for i in cnt.values()}

    if check == {0}:
        print("YES")
    else:
        print("NO")