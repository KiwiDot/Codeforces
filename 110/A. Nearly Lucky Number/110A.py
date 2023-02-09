# 코드포스 110A Nearly Lucky Number
import sys
put = sys.stdin.readline

n = put().strip()
cnt = len([i for i in n if i == '4' or i == '7'])

if cnt == 4 or cnt == 7:
    print("YES")
else:
    print("NO")