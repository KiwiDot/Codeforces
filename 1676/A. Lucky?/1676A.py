# 코드포스 1676A Lucky?
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    digit = put().strip()
    d1 = sum([int(i) for i in digit[:3]])
    d2 = sum([int(i) for i in digit[3:]])

    if d1 == d2:
        print("YES")
    else:
        print("NO")