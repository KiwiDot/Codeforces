# 코드포스 1360A Minimal Square
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    a, b = sorted(list(map(int, put().split())))

    if a * 2 < b:
        print(b ** 2)
    else:
        print(a ** 2 * 4)