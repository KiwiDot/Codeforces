# 코드포스 1462B Last Year's Substring
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    s = list(put().strip())
    check = ['2', '0', '2', '0']

    for i in range(4):
        if s[i] == check[0]:
            check.pop(0)
        else:
            break

    if not check or s[-len(check):] == check:
        print("YES")
    else:
        print("NO")