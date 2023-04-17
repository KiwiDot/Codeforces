# 코드포스 1372A Omkar and Completion
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    answer = [str(n) for i in range(n)]
    print(' '.join(answer))