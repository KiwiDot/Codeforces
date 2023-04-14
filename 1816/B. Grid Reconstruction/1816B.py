# 코드포스 1816B Grid Reconstruction
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())

    answer = []
    for i in range(n // 2):
        answer.extend([str((n - i) * 2), str((i + 1) * 2)])
    print(' '.join(answer))

    answer = []
    for i in range(n // 2):
        answer.extend([str(2 * i + 1), str(n + i * 2 + 1)])
    print(' '.join(answer))