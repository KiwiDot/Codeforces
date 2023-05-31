# 코드포스 1833A Musical Puzzle
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    s = put().strip()
    answer = {s[i:i+2] for i in range(n-1)}

    print(len(answer))