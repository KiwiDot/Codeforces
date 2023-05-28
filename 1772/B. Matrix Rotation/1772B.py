# 코드포스 1772B Matrix Rotation
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    a, b = map(int, put().split())
    d, c = map(int, put().split())

    for i in range(4):
        if a < d < c and a < b < c:
            print("YES")
            break
        a, b, c, d = d, a, b, c

    else:
        print("NO")