# 코드포스 520A Pangram
import sys
put = sys.stdin.readline

n = int(put())
text = put().strip().lower()

if len(set(text)) == 26:
    print("YES")
else:
    print("NO")