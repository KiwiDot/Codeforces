# 코드포스 271A Beautiful Year
import sys
put = sys.stdin.readline

y = int(put())

while True:
    y += 1
    if len(set(str(y))) == 4:
        print(y)
        break