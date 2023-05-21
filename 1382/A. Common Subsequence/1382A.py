# 코드포스 1382A Common Subsequence
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n, m = map(int, put().split())
    a = put().split()
    b = put().split()

    if set(a) & set(b):
        print("YES")
        print(1, list(set(a) & set(b))[0])

    else:
        print("NO")