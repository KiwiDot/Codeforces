# 코드포스 263A Beautiful Matrix
import sys
put = sys.stdin.readline

matrix = [put().split() for i in range(5)]

for i in range(5):
    for j in range(5):
        if matrix[i][j] == '1':
            print(abs(i-2) + abs(j-2))
            break