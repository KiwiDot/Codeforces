# 코드포스 750A New Year and Hurry
import sys
put = sys.stdin.readline

n, k = map(int, put().split())
limit = 240

for i in range(1, n+1):
    if i * 5 + k > limit:
        print(i - 1)
        break
    k += i * 5

else:
    print(n)