# 코드포스 1220A Cards
import sys
put = sys.stdin.readline

n = int(put())
string = put().strip()
cnt = {'z': 0, 'e': 0, 'r': 0, 'o': 0, 'n': 0}

for i in string:
    cnt[i] += 1

answer = []
one = min(cnt['o'], cnt['n'], cnt['e'])
answer += ['1'] * one
for i in ['o', 'n', 'e']:
    cnt[i] -= one

zero = min(cnt['z'], cnt['e'], cnt['r'], cnt['o'])
answer += ['0'] * zero

print(' '.join(answer))