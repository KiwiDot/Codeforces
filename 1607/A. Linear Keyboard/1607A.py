# 코드포스 1607A Linear Keyboard
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    data = put().strip()
    keyboard = dict([(data[i], i) for i in range(len(data))])
    s = [keyboard[i] for i in put().strip()]
    answer = 0

    for i in range(1, len(s)):
        answer += abs(s[i] - s[i-1])

    print(answer)