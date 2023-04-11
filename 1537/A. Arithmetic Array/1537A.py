# 코드포스 1537A Arithmetic Array
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    a = list(map(int, put().split()))

    if sum(a) == n:
        print(0)

    elif sum(a) < n:
        print(1)

    else:
        print(sum(a) - n)