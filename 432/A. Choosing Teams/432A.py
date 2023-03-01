# 코드포스 432A Choosing Teams
import sys
put = sys.stdin.readline

n, k = map(int, put().split())
y = [1 for i in list(map(int, put().split())) if i + k <= 5]

print(len(y) // 3)