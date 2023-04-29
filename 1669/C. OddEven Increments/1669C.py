# 코드포스 1669C Odd/Even Increments
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    a = list(map(int, put().split()))

    odd = {a[i] % 2 for i in range(0, n, 2)}
    even = {a[i] % 2 for i in range(1, n, 2)}

    if len(odd) == len(even) == 1:
        print("YES")
    else:
        print("NO")