# 코드포스 1385A Three Pairwise Maximums
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    x, y, z = sorted(list(map(int, put().split())))

    if y != z:
        print("NO")

    else:
        print("YES")
        print(x, x, z)