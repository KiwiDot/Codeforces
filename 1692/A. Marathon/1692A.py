# 코드포스 1692A Marathon
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    a, b, c, d = map(int, put().split())
    cnt = 0

    for i in [b, c, d]:
        if i > a:
            cnt += 1

    print(cnt)