# 코드포스 1675A Food for Animals
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    a, b, c, x, y = map(int, put().split())

    x -= min(x, a)
    y -= min(y, b)

    cx = min(x, c)
    x -= cx
    c -= cx

    cy = min(y, c)
    y -= cy
    c -= cy

    if x == y == 0:
        print("YES")
    else:
        print("NO")