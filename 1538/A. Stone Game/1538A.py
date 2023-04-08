# 코드포스 1538A Stone Game
import sys

put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    a = list(map(int, put().split()))

    minimum = min(a)
    maximum = max(a)

    answer = [[]]
    for i in a:
        if i == minimum or i == maximum:
            answer.append([])
        else:
            answer[-1].append(i)

    print(n - max([len(i) for i in answer]))
