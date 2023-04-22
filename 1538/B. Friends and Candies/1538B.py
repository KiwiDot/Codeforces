# 코드포스 1538B Friends and Candies
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    a = list(map(int, put().split()))
    avg = sum(a) / n

    if avg.is_integer():
        print(sum([1 for i in a if i > avg]))
    else:
        print(-1)