# 코드포스 1729B Decode String
import sys
put = sys.stdin.readline

q = int(put())

while q:
    q -= 1
    n = int(put())
    t = put().strip() + "---"

    answer = ""
    idx = 0

    while idx < n:
        if t[idx+2] == '0' and t[idx+3] != '0':
            answer += chr(int(t[idx] + t[idx+1]) + 96)
            idx += 2
        else:
            answer += chr(int(t[idx]) + 96)
        idx += 1

    print(answer)