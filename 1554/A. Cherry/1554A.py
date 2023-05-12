# 코드포스 1554A Cherry
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    a = list(map(int, put().split()))
    answer = 0

    for i in range(n-1):
        answer = max(answer, a[i] * a[i+1])

    print(answer)