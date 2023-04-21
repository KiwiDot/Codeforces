# 코드포스 1807B Grab the Candies
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    a = list(map(int, put().split()))
    odd = sum([i for i in a if i % 2])
    even = sum(a) - odd

    if even > odd:
        print("YES")
    else:
        print("NO")