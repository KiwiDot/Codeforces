# 코드포스 1547B Alphabetical Strings
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    s = list(put().strip())

    if 'a' in s:
        idx = s.index('a')
        s.pop(idx)
        alphabet = 98

        while s:
            if chr(alphabet) not in s:
                print("NO")
                break
            if idx < len(s) and s[idx] == chr(alphabet):
                s.pop(idx)
            elif idx - 1 > -1 and s[idx-1] == chr(alphabet):
                s.pop(idx-1)
                idx -= 1
            alphabet += 1
        else:
            print("YES")

    else:
        print("NO")