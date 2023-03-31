# 코드포스 509A Maximum in Table
import sys
put = sys.stdin.readline

n = int(put())
table = [1] * n

for i in range(1, n):
    t = [sum(table[:j+1]) for j in range(n)]
    table = t

print(table[-1])