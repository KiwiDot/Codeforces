# 백준 1367B Even Array
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    a = list(map(int, put().split()))
    cnt = 0

    for i in range(n):
        if a[i] % 2 == i % 2:
            continue

        for j in range(i+1, n):
            if a[i] % 2 == j % 2 and a[j] % 2 == i % 2:
                a[i], a[j] = a[j], a[i]
                cnt += 1
                break
        else:
            cnt = -1
            break

    print(cnt)