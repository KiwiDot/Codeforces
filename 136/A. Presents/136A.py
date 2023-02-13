# 코드포스 136A Presents
import sys
put = sys.stdin.readline

n = int(put())
p = list(map(int, put().split()))
present = dict([(p[i], i+1) for i in range(n)])

answer = ' '.join([str(present[i+1]) for i in range(n)])
print(answer)