# 코드포스 1472A Cards for Friends
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    w, h, n = map(int, put().split())

    cnt_w = 0
    while not w % 2:
        w //= 2
        cnt_w += 1

    cnt_h = 0
    while not h % 2:
        h //= 2
        cnt_h += 1

    if n <= 2 ** cnt_w * 2 ** cnt_h:
        print("YES")
    else:
        print("NO")