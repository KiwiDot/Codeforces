# 코드포스 486A Calculating Function
import sys
put = sys.stdin.readline

n = int(put())

if n % 2:
    print(n // 2 - n)
else:
    print(n // 2)