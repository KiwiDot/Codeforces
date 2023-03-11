# 코드포스 1742A Sum
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    a, b, c = sorted([int(_) for _ in put().split()])

    if a + b == c:
        print("YES")
    else:
        print("NO")