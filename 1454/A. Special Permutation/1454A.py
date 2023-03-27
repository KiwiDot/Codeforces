# 코드포스 1454A Special Permutation
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    answer = [str(i+1) for i in range(n)]

    print(' '.join(answer[1:] + [answer[0]]))