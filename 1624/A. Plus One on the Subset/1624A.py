# 코드포스 1624A Plus One on the Subset
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    a = list(map(int, put().split()))

    print(max(a) - min(a))