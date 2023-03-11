# 코드포스 431A Black Square
import sys
put = sys.stdin.readline

a = list(map(int, put().split()))
s = put().strip()
answer = 0

for i in s:
    answer += a[int(i) - 1]

print(answer)