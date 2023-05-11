# 코드포스 1741A Compare T-Shirt Sizes
import sys
put = sys.stdin.readline
size = {"S": 0, "M": 1, "L": 2}
value = {"S": -1, "M": 0, "L": 1}

t = int(put())

while t:
    t -= 1
    a, b = put().split()

    if a == b:
        print("=")

    elif size[a[-1]] == size[b[-1]]:
        if len(a) * value[a[-1]] > len(b) * value[b[-1]]:
            print(">")
        else:
            print("<")

    else:
        if size[a[-1]] > size[b[-1]]:
            print(">")
        else:
            print("<")