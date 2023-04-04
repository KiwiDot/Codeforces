# 코드포스 1369A FashionabLee
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())

    print("NO" if n % 4 else "YES")
