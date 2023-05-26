# 코드포스 1721A Image
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    color = set()

    for i in range(2):
        color |= set(put().strip())

    print(len(color) - 1)