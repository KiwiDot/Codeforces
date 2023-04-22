# 코드포스 265A Colorful Stones (Simplified Edition)
import sys
put = sys.stdin.readline

s = put().strip()
t = put().strip()
idx = 0

for i in t:
    if s[idx] == i:
        idx += 1

print(idx + 1)