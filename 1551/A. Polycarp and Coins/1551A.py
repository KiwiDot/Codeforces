# 코드포스 1551A Polycarp and Coins
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    c1 = n // 3
    c2 = n // 3 + 1 if n % 3 else n // 3

    if n % 3 < 2:
        c1, c2 = c2, c1

    print(c1, c2)