# 코드포스 1690A Print a Pedestal (Codeforces logo?)
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put()) - 6

    n2 = 2 + n // 3
    n3 = 3 + n // 3
    n1 = 1 + n // 3

    if n % 3 == 2:
        n2 += 1
        n3 += 1
    else:
        n3 += n % 3

    print(n2, n3, n1)