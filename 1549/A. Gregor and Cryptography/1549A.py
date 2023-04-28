# 코드포스 1549A Gregor and Cryptography
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    P = int(put())

    a = 2
    b = P // 2 if P > 5 else 4
    print(a, b)