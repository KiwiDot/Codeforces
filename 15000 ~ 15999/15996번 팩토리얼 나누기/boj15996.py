# 백준 15996번 팩토리얼 나누기
import sys
put = sys.stdin.readline

N, A = map(int, put().split())
cnt = 0
n = N

while N // A:
    cnt += 1
    N //= A

k = 0
for i in range(1, cnt+1):
    k += n // A ** i

print(k)