# 코드포스 1742B Increasing
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    a = set(put().split())

    if len(a) == n:
        print("YES")
    else:
        print("NO")