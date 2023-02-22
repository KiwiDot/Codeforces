# 코드포스 141A Amusing Joke
import sys
put = sys.stdin.readline

guest = put().strip()
host = put().strip()
dummy = sorted(list(put().strip()))

if sorted(list(guest + host)) == dummy:
    print("YES")
else:
    print("NO")