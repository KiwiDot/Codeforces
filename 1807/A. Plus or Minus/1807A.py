# 코드포스 1807A Plus or Minus
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    a, b, c = map(int, put().split())

    if a + b == c:
        print('+')
    else:
        print('-')