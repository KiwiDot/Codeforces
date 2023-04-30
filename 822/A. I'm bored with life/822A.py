# 코드포스 822A I'm bored with life
import sys
from math import factorial
put = sys.stdin.readline

A, B = map(int, put().split())
gcd = factorial(min(A, B))

print(gcd)