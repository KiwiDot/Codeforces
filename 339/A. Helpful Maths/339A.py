# 코드포스 339A Helpful Maths
import sys
put = sys.stdin.readline

s = sorted([int(i) for i in put().split('+')])
print('+'.join([str(i) for i in s]))