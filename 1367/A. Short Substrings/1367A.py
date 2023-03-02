# 코드포스 1367A Short Substrings
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    b = put().strip()
    answer = "-"

    for i in range(0, len(b), 2):
        if answer[-1] == b[i]:
            answer += b[i+1]
        else:
            answer += b[i:i+2]

    print(answer[1:])