# 백준 1480A Yet Another String Game
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    s = list(put().strip())

    for i in range(len(s)):
        if i % 2:
            s[i] = 'y' if s[i] == 'z' else 'z'
        else:
            s[i] = 'b' if s[i] == 'a' else 'a'

    print(''.join(s))