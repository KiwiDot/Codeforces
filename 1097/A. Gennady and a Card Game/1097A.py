# 코드포스 1097A Gennady and a Card Game
import sys
put = sys.stdin.readline

table = put().strip()
hand = put().split()

for i in range(5):
    if hand[i][0] == table[0] or hand[i][1] == table[1]:
        print("YES")
        break

else:
    print("NO")