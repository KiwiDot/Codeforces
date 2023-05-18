# 코드포스 599A Patrick and Shopping
import sys
put = sys.stdin.readline

d1, d2, d3 = map(int, put().split())

case1 = d1 * 2 + d2 * 2
case2 = d1 + d2 + d3
case3 = min(d1, d2) * 2 + d3 * 2

print(min(case1, case2, case3))