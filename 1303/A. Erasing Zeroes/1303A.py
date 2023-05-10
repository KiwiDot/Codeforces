# 코드포스 1303A Erasing Zeroes
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    s = put().strip().strip('0')
    print(s.count('0'))
