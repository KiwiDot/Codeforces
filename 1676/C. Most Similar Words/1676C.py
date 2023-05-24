# 코드포스 1676C Most Similar Words
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n, m = map(int, put().split())
    s = [put().strip() for i in range(n)]
    answer = set()

    for i in range(n-1):
        for j in range(i+1, n):
            cnt = 0
            for k in range(m):
                cnt += abs(ord(s[i][k]) - ord(s[j][k]))

            answer.add(cnt)

    print(min(answer))