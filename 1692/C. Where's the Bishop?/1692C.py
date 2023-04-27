# 코드포스 1692C Where's the Bishop?
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    blank = put()
    chess = [put().strip() for i in range(8)]
    check = False

    for r in range(1, 7):
        for c in range(1, 7):
            if chess[r][c] == chess[r-1][c-1] == chess[r-1][c+1] == '#':
                print(r+1, c+1)
                check = True
                break

        if check:
            break