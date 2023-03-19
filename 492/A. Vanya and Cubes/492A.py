# 코드포스 492A Vanya and Cubes
import sys
put = sys.stdin.readline

n = int(put())
cube = 0

for i in range(1, n+1):
    cube += i * (i + 1) // 2
    if cube > n:
        print(i - 1)
        break
else:
    print(n)

