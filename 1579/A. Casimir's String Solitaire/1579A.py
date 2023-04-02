# 코드포스 1579A Casimir's String Solitaire
import sys
from collections import Counter
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    s = dict(Counter(put().strip() + "ABBC"))

    a = s['A']
    b = s['B']
    c = s['C']

    if a + c == b:
        print("YES")
    else:
        print("NO")