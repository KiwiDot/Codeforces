# 코드포스 1283A Minutes Before the New Year
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    h, m = map(int, put().split())

    print(1440 - h * 60 - m)