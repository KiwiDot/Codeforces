# 코드포스 734A Anton and Danik
import sys
put = sys.stdin.readline

n = int(put())
s = put().strip()
a = s.count('A')
d = n - a

if a > d:
    print("Anton")

elif a < d:
    print("Danik")

else:
    print("Friendship")