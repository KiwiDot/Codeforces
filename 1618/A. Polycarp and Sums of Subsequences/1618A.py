# 코드포스 1618A Polycarp and Sums of Subsequences
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    b = sorted(list(map(int, put().split())))
    a1, a2 = b[0], b[1]
    a3 = b[-1] - a1 - a2

    print(a1, a2, a3)