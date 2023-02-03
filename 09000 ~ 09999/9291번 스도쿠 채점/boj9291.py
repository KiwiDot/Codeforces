# 백준 9291번 스도쿠 채점
import sys
put = sys.stdin.readline

t = int(put())

for _ in range(1, t+1):
    garo = ['' for i in range(9)]
    sero = [set() for i in range(9)]
    square = [[set() for j in range(3)] for i in range(3)]

    for i in range(9):
        data = put().split()
        garo[i] = set(data)

        for j in range(9):
            sero[j].add(data[j])

        for j in range(3):
            square[i//3][j].update(data[j*3:j*3+3])

    length = set()
    for i in range(9):
        length.update([len(garo[i]), len(sero[i])])

    for i in range(3):
        for j in range(3):
            length.add(len(square[i][j]))

    if length == {9}:
        answer = "CORRECT"
    else:
        answer = "INCORRECT"

    print("Case {}: {}".format(_, answer))
    if _ < t:
        blank = put()