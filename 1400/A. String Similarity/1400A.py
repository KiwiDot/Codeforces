# 코드포스 1400A String Similarity
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    s = put().strip()
    answer = ''.join([s[i] for i in range(0, 2 * n, 2)])

    print(answer)