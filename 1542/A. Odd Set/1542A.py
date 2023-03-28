# 코드포스 1542A Odd Set
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    a = list(map(int, put().split()))

    cnt = sum([1 for i in a if i % 2])
    if cnt == n:
        print("Yes")
    else:
        print("No")