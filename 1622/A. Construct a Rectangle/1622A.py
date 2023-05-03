# 코드포스 1622A Construct a Rectangle
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    l1, l2, l3 = sorted(map(int, put().split()))

    if l1 + l2 == l3 or (l1 % 2 == 0 and l2 == l3) or (l1 == l2 and l3 % 2 == 0):
        print("YES")
    else:
        print("NO")