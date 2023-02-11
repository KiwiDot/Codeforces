# 코드포스 677A Vanya and Fence
import sys
put = sys.stdin.readline

n, h = map(int, put().split())
height = list(map(int, put().split()))
cnt = n

for i in height:
    if i > h:
        cnt += 1

print(cnt)