# 코드포스 686A Free Ice Cream
import sys
put = sys.stdin.readline

n, x = map(int, put().split())
cnt = 0

while n:
    n -= 1
    data = put().split()
    d = int(data.pop(-1))

    if data[0] == '+':
        x += d
    else:
        if x >= d:
            x -= d
        else:
            cnt += 1

print(x, cnt)