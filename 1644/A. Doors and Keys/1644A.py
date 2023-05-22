# 코드포스 1644A Doors and Keys
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    key = {'r': False, 'g': False, 'b': False}
    string = put().strip()

    for i in string:
        if i.isupper():
            if not key[i.lower()]:
                print("NO")
                break
        else:
            key[i] = True

    else:
        print("YES")
