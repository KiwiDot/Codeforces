# 코드포스 32B Borze
import sys
put = sys.stdin.readline

num = put().strip()
decode = {".": '0', "-.": '1', "--": '2'}
answer = ""
n = ""

for i in num:
    n += i
    if n in decode:
        answer += decode[n]
        n = ""

print(answer)