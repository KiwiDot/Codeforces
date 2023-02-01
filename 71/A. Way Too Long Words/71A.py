# 코드포스 71A Way Too Long Words
import sys
put = sys.stdin.readline

n = int(put())

while n:
    n -= 1
    word = put().strip()

    if len(word) > 10:
        print(word[0] + str(len(word)-2) + word[-1])
    else:
        print(word)