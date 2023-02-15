# 코드포스 200B Drinks
import sys
put = sys.stdin.readline

n = int(put())
p = list(map(int, put().split()))

print(sum(p) / n)