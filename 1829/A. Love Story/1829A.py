# 코드포스 1829A Love Story
import sys
put = sys.stdin.readline

t = int(put())
codeforces = "codeforces"

while t:
    t -= 1
    s = put().strip()
    answer = 0

    for i in range(10):
        if s[i] != codeforces[i]:
            answer += 1

    print(answer)