# 코드포스 59A Word
import sys
put = sys.stdin.readline

s = put().strip()
cnt = len([i for i in s if i.isupper()])

if cnt > len(s) / 2:
    print(s.upper())
else:
    print(s.lower())