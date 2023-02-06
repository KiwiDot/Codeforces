# 코드포스 266A Stones on the Table
import sys
put = sys.stdin.readline

n = int(put())
s = put().strip()
cnt = 0

for i in range(1, n):
    if s[i-1] == s[i]:
        cnt += 1

print(cnt)