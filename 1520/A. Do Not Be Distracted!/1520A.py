# 코드포스 1520A Do Not Be Distracted!
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    text = put().strip()
    check = {text[0]}

    for i in range(1, n):
        if text[i] == text[i-1]:
            continue

        elif text[i] in check:
            print("NO")
            break

        check.add(text[i])

    else:
        print("YES")
