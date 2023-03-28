# 코드포스 1703B ICPC Balloons
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    s = put().strip()
    cnt = 0

    solved = set()
    for i in s:
        if i not in solved:
            solved.add(i)
            cnt += 1
        cnt += 1

    print(cnt)