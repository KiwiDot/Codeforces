# 코드포스 1348A Phoenix and Balance
import sys
put = sys.stdin.readline

t = int(put())
coin = [2 ** i for i in range(1, 31)]

while t:
    t -= 1
    n = int(put())

    if n == 2:
        print(2)

    else:
        a = sum(coin[n//2-1:n-1])
        b = sum(coin[:n]) - a

        print(abs(a - b))
