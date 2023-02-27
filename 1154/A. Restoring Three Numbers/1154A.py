# 코드포스 1154A Restoring Three Numbers
import sys
put = sys.stdin.readline

x1, x2, x3, x4 = sorted([int(_) for _ in put().split()])
a = x1 + x2 - x4
b = x1 - a
c = x3 - b

print(a, b, c)