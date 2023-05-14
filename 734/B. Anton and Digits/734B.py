# 코드포스 734B Anton and Digits
import sys
put = sys.stdin.readline

k2, k3, k5, k6 = map(int, put().split())
answer = 0

# 256
k256 = min(k2, k5, k6)
answer += k256 * 256
k2 -= k256

# 32
k32 = min(k2, k3)
answer += k32 * 32

print(answer)