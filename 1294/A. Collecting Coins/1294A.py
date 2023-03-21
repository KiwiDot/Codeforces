# 코드포스 1294A Collecting Coins
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    a, b, c, n = map(int, put().split())
    coin = max(a, b, c)

    A = coin - a
    B = coin - b
    C = coin - c
    n -= A + B + C

    if n >= 0 and not n % 3:
        print("YES")
    else:
        print("NO")