# 코드포스 228A Is your horseshoe on the other hoof?
import sys
put = sys.stdin.readline

x = set(map(int, put().split()))
print(4 - len(x))