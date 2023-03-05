# 코드포스 1560A Dislike of Threes
import sys
put = sys.stdin.readline

t = int(put())
num = [0, 1]

while t:
    t -= 1
    k = int(put())

    for i in range(len(num), k+1):
        n = num[-1] + 1

        while not n % 3 or n % 10 == 3:
            n += 1

        num.append(n)

    print(num[k])