# 코드포스 1626A Equidistant Letters
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    s = put().strip()
    print(''.join(sorted(list(s))))