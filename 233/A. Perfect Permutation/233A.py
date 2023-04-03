# 코드포스 233A Perfect Permutation
import sys
put = sys.stdin.readline

n = int(put())

if n % 2:
    print(-1)

else:
    answer = []
    for i in range(0, n, 2):
        answer.extend([str(i+2), str(i+1)])

    print(' '.join(answer))