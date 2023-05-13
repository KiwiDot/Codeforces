# 코드포스 1519A Red and Blue Beans
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    r, b, d = map(int, put().split())

    if max(r, b) <= min(r, b) * (d + 1):
        print("YES")
    else:
        print("NO")