# 코드포스 1702A Round Down the Price
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    m = put().strip()
    print(int(m) - 10 ** (len(m) - 1))