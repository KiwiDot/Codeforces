# 코드포스 1547A Shortest Path with Obstacle
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    blank = put()
    xA, yA = map(int, put().split())
    xB, yB = map(int, put().split())
    xF, yF = map(int, put().split())

    if xA == xB == xF and min(yA, yB) < yF < max(yA, yB):
        print(abs(xA - xB) + abs(yA - yB) + 2)

    elif yA == yB == yF and min(xA, xB) < xF < max(xA, xB):
        print(abs(xA - xB) + abs(yA - yB) + 2)

    else:
        print(abs(xA - xB) + abs(yA - yB))