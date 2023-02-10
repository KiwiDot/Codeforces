# 코드포스 266B Queue at the School
import sys
put = sys.stdin.readline

n, t = map(int, put().split())
s = put().strip()

for i in range(t):
    s = s.replace('BG', 'GB')

print(s)