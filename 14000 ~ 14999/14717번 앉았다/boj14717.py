# 백준 14717번 앉았다
import sys
put = sys.stdin.readline

A, B = map(int, put().split())
total = 153

if A == B:
    t = 10 - A

else:
    card = [i for i in range(1, 11)] * 2
    card.remove(A)
    card.remove(B)
    ab = (A + B) % 10
    t = 0

    for i in range(17):
        for j in range(i+1, 18):
            if card[i] == card[j]:
                t += 1
            elif (card[i] + card[j]) % 10 >= ab:
                t += 1

answer = (total - t) / total
print("{:.3f}".format(answer))