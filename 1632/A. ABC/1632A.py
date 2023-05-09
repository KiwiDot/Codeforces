# 코드포스 1632A ABC
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    s = put().strip()
    check = False

    for i in range(2, n+1):
        for j in range(n-i+1):
            if s[j:j+i] == s[j:j+i][::-1]:
                check = True
                print("NO")
                break

        if check:
            break

    else:
        print("YES")