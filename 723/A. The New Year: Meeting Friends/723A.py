# 코드포스 723A The New Year: Meeting Friends
import sys
put = sys.stdin.readline

x1, x2, x3 = map(int, put().split())
x = sorted([x1, x2, x3])[1]

print(abs(x1 - x) + abs(x2 - x) + abs(x3 - x))