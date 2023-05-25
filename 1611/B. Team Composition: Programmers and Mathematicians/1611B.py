# 코드포스 1611B Team Composition: Programmers and Mathematicians
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    a, b = sorted([int(i) for i in put().split()])

    if a * 3 < b:
        print(a)

    else:
        a2b2, a1b3 = a // 2, 0
        a -= a2b2 * 2
        b -= a2b2 * 2

        if a and b > 2:
            a -= 1
            b -= 3
            a1b3 += 1

        change = min(a2b2, b // 4)
        print(a2b2 + a1b3 + change)



