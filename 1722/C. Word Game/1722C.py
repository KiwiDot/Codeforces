# 코드포스 1722C Word Game
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    p1, p2, p3 = [set(put().split()) for i in range(3)]

    p123 = p1 & p2 & p3
    p12 = p1 & p2 - p123
    p23 = p2 & p3 - p123
    p31 = p3 & p1 - p123

    s1 = s2 = s3 = n * 3 - len(p123) * 3
    s1 -= (len(p12) + len(p31)) * 2
    s2 -= (len(p23) + len(p12)) * 2
    s3 -= (len(p31) + len(p23)) * 2

    print(s1, s2, s3)
