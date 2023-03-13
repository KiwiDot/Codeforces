# 코드포스 9A Die Roll
import sys
from math import gcd
put = sys.stdin.readline

Y, W = map(int, put().split())
d = 6 - max(Y, W) + 1

g = gcd(d, 6)
print("{}/{}".format(d//g, 6//g))