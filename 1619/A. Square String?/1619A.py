# 코드포스 1619A Square String?
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    s = put().strip()

    if s == s[:len(s)//2] * 2:
        print("YES")
    else:
        print("NO")