# 코드포스 151A Soft Drinking
import sys
put = sys.stdin.readline

n, k, l, c, d, p, nl, np = map(int, put().split())

drinks = l * k // nl
lime = c * d
salt = p // np

print(min(drinks, lime, salt) // n)