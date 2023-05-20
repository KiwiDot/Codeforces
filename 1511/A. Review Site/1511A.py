# 코드포스 1511A Review Site
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    r = list(map(int, put().split()))
    vote = {1: 0, 2: 0, 3: 0}

    for i in r:
        vote[i] += 1

    print(vote[1] + vote[3])