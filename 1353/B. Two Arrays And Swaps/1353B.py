# 코드포스 1353B Two Arrays And Swaps
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n, k = map(int, put().split())
    a = sorted(list(map(int, put().split())))
    b = sorted(list(map(int, put().split())))

    for i in range(k):
        if a[0] < b[-1]:
            a.pop(0)
            a.append(b.pop(-1))
        else:
            break

    print(sum(a))