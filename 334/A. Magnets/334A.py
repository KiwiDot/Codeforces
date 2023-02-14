# 코드포스 334A Magnets
import sys
put = sys.stdin.readline

n = int(put()) - 1
magnet = put().strip()
cnt = 1

while n:
    n -= 1
    magnet_i = put().strip()

    if magnet != magnet_i:
        cnt += 1
        magnet = magnet_i

print(cnt)