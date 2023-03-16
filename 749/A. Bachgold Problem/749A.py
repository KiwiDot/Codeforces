# 코드포스 749A Bachgold Problem
import sys
put = sys.stdin.readline

n = int(put())

if n % 2:
    answer = ['2'] * (n // 2 - 1) + ['3']
else:
    answer = ['2'] * (n // 2)
k = len(answer)

print(k)
print(' '.join(answer))