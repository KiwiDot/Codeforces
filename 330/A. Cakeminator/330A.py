# 코드포스 330A Cakeminator
import sys
put = sys.stdin.readline

r, c = map(int, put().split())
cake = [put().strip() for i in range(r)]
sr, sc = set(), set()

for i in range(r):
    for j in range(c):
        if cake[i][j] == 'S':
            sr.add(i)
            sc.add(j)

print(r * c - len(sr) * len(sc))