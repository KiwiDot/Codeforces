# 코드포스 1660A Vasya and Coins
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    a, b = map(int, put().split())

    if not a:
        print(1)

    elif not b:
        print(a + 1)

    else:
        print(a + b * 2 + 1)