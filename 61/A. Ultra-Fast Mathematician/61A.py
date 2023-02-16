# 코드포스 61A Ultra-Fast Mathematician
import sys
put = sys.stdin.readline

n1 = put().strip()
n2 = put().strip()

print(bin(int(n1, 2) ^ int(n2, 2))[2:].zfill(len(n1)))