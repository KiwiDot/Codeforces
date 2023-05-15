# 코드포스 1285A Mezo Playing Zoma
import sys
put = sys.stdin.readline

n = int(put())
s = put().strip()
cnt = {'L': 0, 'R': 0}

for i in s:
    cnt[i] += 1

print(cnt['L'] + cnt['R'] + 1)
