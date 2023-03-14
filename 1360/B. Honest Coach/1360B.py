# 코드포스 1360B Honest Coach
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    s = sorted(list(map(int, put().split())))

    answer = [s[i+1] - s[i] for i in range(n-1)]
    print(min(answer))