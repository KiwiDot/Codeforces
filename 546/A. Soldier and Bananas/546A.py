# 코드포스 546A Soldier and Bananas
import sys
put = sys.stdin.readline

k, n, w = map(int, put().split())
money = w * (w+1) * k // 2

print(money - n if money > n else 0)
