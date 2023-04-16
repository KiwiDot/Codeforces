# 코드포스 1791C Prepend and Append
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    text = list(put().strip())

    while text:
        if text[0] == text[-1]:
            break
        text.pop(0)
        text.pop(-1)

    print(len(text))
