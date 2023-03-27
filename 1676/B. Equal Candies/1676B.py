# 코드포스 1676B Equal Candies
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    a = list(map(int, put().split()))
    candy = min(a)

    print(sum([i - candy for i in a]))