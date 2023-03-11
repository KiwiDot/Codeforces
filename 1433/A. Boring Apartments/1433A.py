# 코드포스 1433A Boring Apartments
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    x = put().strip()
    cnt = 0

    for i in range(1, int(x[0])):
        for j in range(5):
            cnt += j

    for i in range(len(x) + 1):
        cnt += i

    print(cnt)