# 백준 1553A Digits Sum
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put()) + 1
    print(n // 10)