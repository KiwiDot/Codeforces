# 코드포스 1520B Ordinary Numbers
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = put().strip()
    cnt = 9 * (len(n) - 1) if len(n) > 1 else 0

    for i in range(1, 10):
        if int(n) >= int(str(i) * len(n)):
            cnt += 1

    print(cnt)