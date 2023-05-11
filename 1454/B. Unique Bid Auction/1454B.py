# 코드포스 1454B Unique Bid Auction
import sys
from collections import Counter
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    a = list(map(int, put().split()))
    a_dict = dict(Counter(a))

    unique = [i for i in set(a) if a_dict[i] == 1]
    if unique:
        answer = min(unique)
        print(a.index(answer) + 1)
    else:
        print(-1)