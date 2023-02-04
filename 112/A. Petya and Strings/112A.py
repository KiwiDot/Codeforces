# 코드포스 112A Petya and Strings
import sys
put = sys.stdin.readline

s1 = put().strip().lower()
s2 = put().strip().lower()

if s1 == s2:
    print(0)

elif s1 > s2:
    print(1)

else:
    print(-1)