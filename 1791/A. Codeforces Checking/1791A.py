# 코드포스 1791A Codeforces Checking
import sys
put = sys.stdin.readline

codeforces = set("codeforces")
t = int(put())

while t:
    t -= 1
    c = put().strip()

    if c in codeforces:
        print("YES")
    else:
        print("NO")