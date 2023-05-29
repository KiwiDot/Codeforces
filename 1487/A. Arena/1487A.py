# 코드포스 1487A Arena
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    a = sorted(list(map(int, put().split())))
    answer = 0

    for i in range(n):
        if a[i] != a[0]:
            answer = n - i
            break

    print(answer)