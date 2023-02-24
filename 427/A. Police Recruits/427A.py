# 코드포스 427A Police Recruits
import sys
put = sys.stdin.readline

n = int(put())
num = list(map(int, put().split()))
police = cnt = 0

for i in num:
    if i > 0:
        police += i
    elif police:
        police -= 1
    else:
        cnt += 1

print(cnt)