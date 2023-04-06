# 코드포스 1791B Following Directions
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    move = put().strip()
    x = y = 0

    answer = set()
    for i in move:
        if i == 'L':
            x -= 1
        elif i == 'R':
            x += 1
        elif i == 'U':
            y += 1
        else:
            y -= 1
        answer.add((x, y))

    if (1, 1) in answer:
        print("YES")
    else:
        print("NO")