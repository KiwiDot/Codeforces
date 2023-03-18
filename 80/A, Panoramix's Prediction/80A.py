# 코드포스 80A Panoramix's Prediction
import sys
put = sys.stdin.readline

n, m = map(int, put().split())
prime = [2, 3]

for i in range(4, m+1):
    for j in range(2, int(i**0.5)+1):
        if not i % j:
            break
    else:
        prime.append(i)

if prime[-2] == n and prime[-1] == m:
    print("YES")
else:
    print("NO")