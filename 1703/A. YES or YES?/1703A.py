# 코드포스 1703A YES or YES?
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    s = put().strip().upper()
    if s == "YES":
        print(s)
    else:
        print("NO")