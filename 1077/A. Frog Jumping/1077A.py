# 코드포스 1077A Frog Jumping
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    a, b, k = map(int, put().split())

    if k % 2:
        print((k // 2) * (a - b) + a)
    else:
        print((k // 2) * (a - b))