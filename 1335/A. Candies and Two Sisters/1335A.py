# 코드포스 1335A Candies and Two Sisters
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    if n < 3:
        print(0)
        continue

    print(n - n // 2 - 1)