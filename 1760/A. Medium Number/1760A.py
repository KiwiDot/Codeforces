# 코드포스 1760A Medium Number
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    a, b, c = sorted([int(i) for i in put().split()])

    print(b)