# 코드포스 702A Maximum Increase
import sys
put = sys.stdin.readline

n = int(put())
a = list(map(int, put().split()))
cnt = 0
length = 1
ai = a[0]

for i in a[1:]:
    if i > ai:
        length += 1
        ai = i

    else:
        cnt = max(cnt, length)
        length = 1
        ai = i
cnt = max(cnt, length)

print(cnt)