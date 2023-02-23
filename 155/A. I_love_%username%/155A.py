# 코드포스 155A I_love_%username%
import sys
put = sys.stdin.readline

n = int(put())
point = list(map(int, put().split()))
minimum = point[0]
maximum = point[0]
cnt = 0

for i in point[1:]:
    if minimum > i:
        minimum = i
        cnt += 1

    if maximum < i:
        maximum = i
        cnt += 1

print(cnt)