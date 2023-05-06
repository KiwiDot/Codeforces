# 코드포스 1433B Yet Another Bookshelf
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    a = list(map(int, put().split()))
    book = [i for i in range(n) if a[i]]
    answer = 0

    for i in range(len(book)-1):
        answer += book[i+1] - book[i] - 1

    print(answer)