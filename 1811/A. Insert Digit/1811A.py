# 코드포스 1811A Insert Digit
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n, d = map(int, put().split())
    digit = put().strip()

    for i in range(n):
        if d > int(digit[i]):
            print(digit[:i] + str(d) + digit[i:])
            break
    else:
        print(digit + str(d))