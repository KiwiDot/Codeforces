# 코드포스 935A Fafa and his Company
import sys
put = sys.stdin.readline

n = int(put())
cnt = 0

for i in range(1, n//2 + 1):
    if not (n - i) % i:
        cnt += 1

print(cnt)