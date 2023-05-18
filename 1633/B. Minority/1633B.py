# 코드포스 1633B Minority
import sys
from collections import Counter
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    s = put().strip()
    cnt = Counter({'0': 0, '1': 0}) + Counter(s)

    if cnt['0'] == cnt['1']:
        print(cnt['0'] - 1)
    else:
        print(min(cnt['0'], cnt['1']))