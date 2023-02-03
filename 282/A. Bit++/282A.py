# 코드포스 282A Bit++
import sys
put = sys.stdin.readline

n = int(put())
x = 0

while n:
    n -= 1
    statement = put().strip()

    if '+' in statement:
        x += 1
    else:
        x -= 1

print(x)