# 코드포스 1722A Spell Check
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    s = put().strip()

    if n == 5 and set(s) == {'T', 'i', 'm', 'u', 'r'}:
        print("YES")
    else:
        print("NO")