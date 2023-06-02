# 코드포스 1701A Grass Field
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    a = [list(map(int, put().split())) for i in range(2)]

    if a == [[0, 0], [0, 0]]:
        print(0)
    elif a == [[1, 1], [1, 1]]:
        print(2)
    else:
        print(1)