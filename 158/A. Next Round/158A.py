# 코드포스 158A Next Round
import sys
put = sys.stdin.readline

n, k = map(int, put().split())
a = sorted(map(int, put().split()), reverse=True)
cnt = 0
score = a[k-1]

for i in a:
    if i < score:
        break
    if i > 0:
        cnt += 1

print(cnt)