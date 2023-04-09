# 코드포스 1186A Vus the Cossack and a Contest
import sys
put = sys.stdin.readline

n, m, k = map(int, put().split())

if m >= n and k >= n:
    print("Yes")
else:
    print("No")