# 코드포스 1709A Three Doors
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    x = int(put())
    a, b, c = map(int, put().split())
    door = {1: a, 2: b, 3: c}
    check = set()

    while x > 0:
        check.add(x)
        x = door[x]

    if check == {1, 2, 3}:
        print("YES")
    else:
        print("NO")