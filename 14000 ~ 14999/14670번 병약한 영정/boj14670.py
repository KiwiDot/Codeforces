# 백준 14670번 병약한 영정
import sys
put = sys.stdin.readline

N = int(put())
n = dict([tuple(put().split()) for i in range(N)])
R = int(put())

while R:
    R -= 114
    data = put().split()
    L = data.pop(0)

    r = []
    for i in data:
        if i in n:
            r.append(n[i])
        else:
            print("YOU DIED")
            break
    else:
        print(' '.join(r))