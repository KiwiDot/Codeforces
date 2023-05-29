# 코드포스 1759A Yes-Yes?
import sys
put = sys.stdin.readline

t = int(put())
yes = "Yes" * 50

while t:
    t -= 1
    s = put().strip()
    length = len(s)

    for i in range(3):
        if s == yes[i:i+length]:
            print("YES")
            break
    else:
        print("NO")