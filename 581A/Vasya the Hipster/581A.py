# 코드포스 581A Vasya the Hipster
import sys
put = sys.stdin.readline

a, b = map(int, put().split())
ans1 = min(a, b)
a -= ans1
b -= ans1
ans2 = max(a//2, b//2)

print(ans1, ans2)