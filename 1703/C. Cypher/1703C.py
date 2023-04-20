# 코드포스 1703C Cypher
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    a = list(map(int, put().split()))
    answer = []

    for i in range(n):
        b, move = put().split()
        cnt = 0
        for m in move:
            cnt += 1 if m == 'D' else -1

        ai = a[i] + cnt
        if ai < 0:
            ai += 10
        if ai > 9:
            ai -= 10

        answer.append(str(ai))

    print(' '.join(answer))