# 코드포스 731A Night at the Museum
import sys
put = sys.stdin.readline

alphabet = dict([(chr(i+97), i) for i in range(26)])
s = put().strip()
cnt = 0
idx = 0

for i in s:
    move = abs(alphabet[i] - idx)
    cnt += min(move, 26 - move)
    idx = alphabet[i]

print(cnt)