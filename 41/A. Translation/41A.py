# 코드포스 41A Translation
import sys
put = sys.stdin.readline

s = put().strip()
t = put().strip()

if s == t[::-1]:
    print("YES")
else:
    print("NO")