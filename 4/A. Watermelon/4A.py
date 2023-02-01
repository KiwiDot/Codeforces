# 코드포스 4A Watermelon
import sys
put = sys.stdin.readline

w = int(put())

print("YES" if not w % 2 and w > 2 else "NO")