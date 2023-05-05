# 코드포스 1519B The Cake Is a Lie
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n, m, k = map(int, put().split())
    dx, dy = n - 1, m - 1

    answer = 1 * (n - 1) + n * (m - 1)
    if answer == k:
        print("YES")
    else:
        print("NO")