# 백준 1541A Pretty Permutations
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    answer = []

    if n % 2:
        answer += ['3', '1', '2']
        for i in range(4, n+1, 2):
            answer += [str(i+1), str(i)]

    else:
        for i in range(1, n+1, 2):
            answer += [str(i+1), str(i)]

    print(' '.join(answer))