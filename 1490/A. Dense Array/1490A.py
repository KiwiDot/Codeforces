# 코드포스 1490A Dense Array
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    a = list(map(int, put().split()))
    answer = 0

    for i in range(n-1):
        min_, max_ = sorted([a[i], a[i+1]])

        while max_ > min_ * 2:
            min_ *= 2
            answer += 1

    print(answer)