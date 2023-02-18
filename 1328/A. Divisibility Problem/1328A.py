# 코드포스 1328A Divisibility Problem
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    a, b = map(int, put().split())
    r = a // b + 1 if a % b else a // b

    print(b * r - a)