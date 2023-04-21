# 코드포스 540A Combination Lock
import sys
put = sys.stdin.readline

n = int(put())
pw1 = put().strip()
pw2 = put().strip()
answer = 0

for i in range(n):
    a, b = sorted([int(pw1[i]), int(pw2[i])])
    answer += min(b - a, a - b + 10)

print(answer)