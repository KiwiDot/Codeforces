# 코드포스 791A Bear and Big Brother
import sys
put = sys.stdin.readline

a, b = map(int, put().split())
cnt = 0

while a <= b:
    cnt += 1
    a *= 3
    b *= 2

print(cnt)