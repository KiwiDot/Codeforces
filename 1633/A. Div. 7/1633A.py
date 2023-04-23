# 코드포스 1633A Div. 7
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = put().strip()
    check = False

    if int(n) % 7 == 0:
        print(n)

    else:
        for i in range(len(n)):
            for j in range(10):
                if i == j == 0:
                    continue
                d = n[:i] + str(j) + n[i+1:]
                if int(d) % 7 == 0:
                    print(d)
                    check = True
                    break

            if check:
                break