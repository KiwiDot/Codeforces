# 코드포스 1311A Add Odd or Subtract Even
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    a, b = map(int, put().split())

    if a > b:
        print(2 if (b - a) % 2 else 1)

    elif a < b:
        print(1 if (b - a) % 2 else 2)

    else:
        print(0)