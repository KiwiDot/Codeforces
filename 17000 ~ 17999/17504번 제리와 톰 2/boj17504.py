# 백준 17504번 제리와 톰 2
import sys
import math
put = sys.stdin.readline

N = int(put())
a = list(map(int, put().split()))[::-1]
p, q = 1, a[0]

for i in a[1:]:
    p = p + i * q
    p, q = q, p

p = q - p
gcd = math.gcd(p, q)
print(p//gcd, q//gcd)