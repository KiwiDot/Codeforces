# 코드포스 1829B Blank Space
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    a = list(map(int, put().split()))
    answer = cnt = 0

    for i in a:
        if i:
            answer = max(answer, cnt)
            cnt = 0
        else:
            cnt += 1
    answer = max(answer, cnt)

    print(answer)