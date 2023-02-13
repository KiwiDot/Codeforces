# 코드포스 467A George and Accommodation
import sys
put = sys.stdin.readline

n = int(put())
cnt = 0

while n:
    n -= 1
    p, q = map(int, put().split())

    if q - p >= 2:
        cnt += 1

print(cnt)