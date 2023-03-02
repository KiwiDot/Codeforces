# 코드포스 1343B Balanced Array
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())

    if n % 4:
        print("NO")
    else:
        print("YES")
        num1 = [i for i in range(2, n+1, 2)]
        num2 = [i for i in range(1, n-1, 2)]
        num = num1 + num2 + [sum(num1) - sum(num2)]

        print(' '.join([str(i) for i in num]))