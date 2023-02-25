# 코드포스 1352A Sum of Round Numbers
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = put().strip()
    length = len(n)
    answer = []

    for i in range(length):
        if n[i] != '0':
            answer.append(str(int(n[i]) * 10 ** (length-i-1)))

    print(len(answer))
    print(' '.join(answer))