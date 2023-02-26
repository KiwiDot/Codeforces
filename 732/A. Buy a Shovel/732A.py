# 코드포스 732A Buy a Shovel
import sys
put = sys.stdin.readline

k, r = map(int, put().split())
for i in range(1, 11):
    if k * i % 10 in {r, 0}:
        print(i)
        break