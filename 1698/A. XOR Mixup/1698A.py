# 코드포스 1698A XOR Mixup
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    a = list(map(int, put().split()))
    check = a[0]

    for i in range(1, n):
        check ^= a[i]

    for i in a:
        if check ^ i == i:
            print(i)
            break
