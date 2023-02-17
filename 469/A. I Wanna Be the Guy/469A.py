# 코드포스 469A I Wanna Be the Guy
import sys
put = sys.stdin.readline

n = int(put())
p = list(map(int, put().split()))
q = list(map(int, put().split()))

game = {i for i in range(1, n+1)}
p = set(p[1:])
q = set(q[1:])

if p | q == game:
    print("I become the guy.")

else:
    print("Oh, my keyboard!")