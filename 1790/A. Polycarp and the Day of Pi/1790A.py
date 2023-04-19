# 코드포스 1790A Polycarp and the Day of Pi
import sys
put = sys.stdin.readline
pi = "314159265358979323846264338327"

t = int(put())

while t:
    t -= 1
    n = put().strip()
    cnt = 0

    for i in range(len(n)):
        if n[i] != pi[i]:
            break
        cnt += 1

    print(cnt)