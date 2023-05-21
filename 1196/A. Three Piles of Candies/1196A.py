# 코드포스 1196A Three Piles of Candies
import sys
put = sys.stdin.readline

q = int(put())

while q:
    q -= 1
    a, b, c = sorted(list(map(int, put().split())))

    c -= b - a
    print(b + c // 2)