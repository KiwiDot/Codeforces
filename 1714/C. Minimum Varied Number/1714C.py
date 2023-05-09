# 코드포스 1714C Minimum Varied Number
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    s = int(put())
    answer = []

    for i in range(9, 0, -1):
        if s == i:
            answer.append(str(i))
            break

        elif s > i:
            answer.append(str(i))
            s -= i

    print(''.join(answer[::-1]))
