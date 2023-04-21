# 백준 22858번 원상 복구 (small)
import sys
put = sys.stdin.readline

N, K = map(int, put().split())
S = put().split()
D = list(map(int, put().split()))

while K:
    K -= 1
    P = [''] * N

    for i in range(N):
        P[D[i] - 1] = S[i]

    S = P

print(' '.join(S))