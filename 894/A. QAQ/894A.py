# 코드포스 894A QAQ
import sys
from itertools import combinations
put = sys.stdin.readline

string = put().strip()
QA = {'Q': [], 'A': []}

for i in range(len(string)):
    if string[i] == 'Q' or string[i] == 'A':
        QA[string[i]].append(i)

answer = 0
for i in combinations(QA['Q'], 2):
    i1, i3 = i
    for i2 in QA['A']:
        if i1 < i2 < i3:
            answer += 1

print(answer)