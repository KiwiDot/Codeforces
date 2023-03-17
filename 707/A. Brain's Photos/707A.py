# 코드포스 707A Brain's Photos
import sys
put = sys.stdin.readline

n, m = map(int, put().split())
color = set()

while n:
    n -= 1
    color.update(put().split())

if {'C', 'Y', 'M'} & color:
    print("#Color")
else:
    print("#Black&White")