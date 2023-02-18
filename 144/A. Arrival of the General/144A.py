# 코드포스 144A Arrival of the General
import sys
put = sys.stdin.readline

n = int(put())
a = list(map(int, put().split()))
min_a = a[::-1].index(min(a))
max_a = a.index(max(a))

if (n - min_a) <= max_a:
    print(min_a + max_a - 1)
else:
    print(min_a + max_a)