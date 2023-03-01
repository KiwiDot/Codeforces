# 코드포스 472A Design Tutorial: Learn from Math
import sys
put = sys.stdin.readline

n = int(put())
n1 = n // 2
n2 = n - n1

for i in range(n1):
    for i1 in range(2, int(n1**0.5)+2):
        if not n1 % i1:
            break
    else:
        n1 -= 1
        n2 += 1
        continue

    for i2 in range(2, int(n2**0.5)+2):
        if not n2 % i2:
            break
    else:
        n1 -= 1
        n2 += 1
        continue

    print(n1, n2)
    break