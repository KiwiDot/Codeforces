# 코드포스 116A Tram
import sys
put = sys.stdin.readline

n = int(put())
cnt = [0]

while n:
    n -= 1
    a, b = map(int, put().split())
    cnt.append(cnt[-1] - a + b)

print(max(cnt))