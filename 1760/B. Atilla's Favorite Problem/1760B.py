# 코드포스 1760B Atilla's Favorite Problem
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    s = set(put().strip())

    print(max([ord(i) - 96 for i in s]))