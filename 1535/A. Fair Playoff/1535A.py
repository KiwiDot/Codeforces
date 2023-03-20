# 코드포스 1535A Fair Playoff
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    s1, s2, s3, s4 = map(int, put().split())

    s12 = max(s1, s2)
    s34 = max(s3, s4)

    if {s12, s34} == set(sorted([s1, s2, s3, s4])[2:]):
        print("YES")
    else:
        print("NO")