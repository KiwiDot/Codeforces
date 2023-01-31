# 코드포스 1792B Stand-up Comedian
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    a = [0] + list(map(int, put().split()))
    if a[1]:
        a1 = a[1]
        a2 = min(a[1] + a[3], a[2])
        a3 = min(a[1] + a[2], a[3])

        a[2] -= a2
        a[3] -= a3

        if a[2] or a[3]:
            print(a1 + a2 + a3 + 1)

        else:
            Alice = a1 + a2 - a3
            Bob = a1 - a2 + a3
            a4 = min(Alice + 1, Bob + 1, a[4])
            print(a1 + a2 + a3 + a4)

    else:
        print(1)

