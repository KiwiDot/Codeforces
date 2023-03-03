# 코드포스 1512A Spy Detected!
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    a = list(map(int, put().split()))

    num = sorted(a)[1]
    for i in range(n):
        if a[i] != num:
            print(i+1)
            break