# 코드포스 705A Hulk
import sys
put = sys.stdin.readline

n = int(put())
answer = []

for i in range(n):
    if i % 2:
        answer += ["I", "love"]
    else:
        answer += ["I", "hate"]

    if i == n - 1:
        answer += ["it"]
    else:
        answer += ["that"]

print(' '.join(answer))