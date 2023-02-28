# 코드포스 1399A Remove Smallest
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    N = int(put())
    a = sorted([int(_) for _ in put().split()])
    idx = 0

    for i in range(1, N):
        if a[i] - a[i-1] <= 1:
            idx += 1
        else:
            break

    if len(set(a[idx:])) == 1:
        print("YES")
    else:
        print("NO")