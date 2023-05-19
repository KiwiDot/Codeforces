# 코드포스 1660B Vlad and Candies
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    a = sorted(list(map(int, put().split())))

    if n == 1:
        if a == [1]:
            print("YES")
        else:
            print("NO")
    elif a[-1] <= a[-2] + 1:
        print("YES")
    else:
        print("NO")