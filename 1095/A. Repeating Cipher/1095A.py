# 코드포스 1095A Repeating Cipher
import sys
put = sys.stdin.readline

n = int(put())
s = put().strip()
idx = 0

answer = ""
for i in range(10):
    answer += s[idx]
    idx += i + 1

    if idx >= n:
        break

print(answer)