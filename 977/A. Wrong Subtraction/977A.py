# 코드포스 977A Wrong Subtraction
import sys
put = sys.stdin.readline

n, k = map(int, put().split())

while k:
    k -= 1

    if not n % 10:
        n //= 10
    else:
        n -= 1

print(n)