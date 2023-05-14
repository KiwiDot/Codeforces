# 코드포스 1550A Find The Array
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    s = int(put()) - 1
    answer = a = 1

    while s > 0:
        a += 2
        s -= a
        answer += 1

    print(answer)