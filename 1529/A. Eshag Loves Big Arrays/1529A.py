# 코드포스 1529A Eshag Loves Big Arrays
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    a = list(map(int, put().split()))
    cnt = a.count(min(a))

    print(n - cnt)