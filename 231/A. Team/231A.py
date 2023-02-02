# 코드포스 231A Team
import sys
put = sys.stdin.readline

n = int(put())
cnt = 0

while n:
    n -= 1
    if sum(map(int, put().split())) > 1:
        cnt += 1

print(cnt)