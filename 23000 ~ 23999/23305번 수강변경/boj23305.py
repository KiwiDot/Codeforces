# 백준 23305번 수강변경
import sys
from collections import Counter
put = sys.stdin.readline

N = int(put())
A = dict(Counter(put().split()))
B = dict(Counter(put().split()))
cnt = N

for i in B.keys():
    b = A[i] if i in A else 0
    cnt -= min(B[i], b)

print(cnt)