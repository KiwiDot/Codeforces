# 코드포스 1714B Remove Prefix
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    a = list(map(int, put().split()))[::-1]
    check = set()

    for i in a:
        if i in check:
            break
        check.add(i)

    print(n - len(check))