# 백준 1296A Array with Odd Sum
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    a = {int(i) % 2 for i in put().split()}

    if n % 2 and 1 in a:
        print("YES")

    elif not n % 2 and a == {0, 1}:
        print("YES")

    else:
        print("NO")