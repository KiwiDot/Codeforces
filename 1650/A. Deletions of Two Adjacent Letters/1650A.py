# 코드포스 1650A Deletions of Two Adjacent Letters
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    s = put().strip()
    c = put().strip()
    n = len(s)

    for i in range(n):
        if s[i] == c and not i % 2 and not (n-i-1) % 2:
            print("YES")
            break
    else:
        print("NO")