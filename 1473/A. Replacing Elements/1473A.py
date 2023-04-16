# 코드포스 1473A Replacing Elements
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n, d = map(int, put().split())
    a = sorted(list(map(int, put().split())))

    check1 = sum([1 for i in a if i <= d])
    check2 = a[0] + a[1]

    if check1 == n:
        print("YES")
    elif check2 <= d:
        print("YES")
    else:
        print("NO")