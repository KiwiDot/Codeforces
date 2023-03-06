# 코드포스 703A Mishka and Game
import sys
put = sys.stdin.readline

n = int(put())
m = c = 0

while n:
    n -= 1
    mi, ci = map(int, put().split())

    if mi > ci:
        m += 1
    elif mi < ci:
        c += 1

if m > c:
    print("Mishka")
elif m < c:
    print("Chris")
else:
    print("Friendship is magic!^^")