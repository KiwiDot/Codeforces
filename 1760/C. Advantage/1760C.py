# 코드포스 1760C Advantage
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    s = list(map(int, put().split()))
    sorted_s = sorted(s)

    answer = []
    for i in s:
        if i == sorted_s[-1]:
            answer.append(str(i - sorted_s[-2]))
        else:
            answer.append(str(i - sorted_s[-1]))

    print(' '.join(answer))