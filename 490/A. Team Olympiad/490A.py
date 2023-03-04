# 코드포스 490A Team Olympiad
import sys
put = sys.stdin.readline

n = int(put())
t = put().split()
team = {'1': [], '2': [], '3': []}

for i in range(n):
    team[t[i]].append(str(i+1))

answer = []
while team['1'] and team['2'] and team['3']:
    t1 = team['1'].pop(0)
    t2 = team['2'].pop(0)
    t3 = team['3'].pop(0)

    answer.append(' '.join([t1, t2, t3]))

if answer:
    print(len(answer))
    for i in answer:
        print(i)
else:
    print(0)