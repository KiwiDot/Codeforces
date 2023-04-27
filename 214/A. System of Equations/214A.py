# 코드포스 214A System of Equations
import sys
put = sys.stdin.readline

n, m = map(int, put().split())
answer = 0

for a in range(m+1):
    b = n - a ** 2
    if b >= 0 and a + b ** 2 == m:
        answer += 1

print(answer)