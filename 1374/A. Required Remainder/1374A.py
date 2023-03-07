# 코드포스 1374A Required Remainder
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    x, y, n = map(int, put().split())

    result = n // x * x
    if result + y > n:
        result = result + y - x
    else:
        result += y

    print(result)