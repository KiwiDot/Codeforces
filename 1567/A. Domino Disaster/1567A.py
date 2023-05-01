# 코드포스 1567A Domino Disaster
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    s = put().strip()
    change = {'L': 'L', 'R': 'R', 'U': 'D', 'D': 'U'}

    answer = ''.join([change[i] for i in s])
    print(answer)