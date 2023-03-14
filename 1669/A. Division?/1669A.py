# 코드포스 1669A Division?
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    rationg = int(put())

    if rationg >= 1900:
        print("Division 1")
    elif rationg >= 1600:
        print("Division 2")
    elif rationg >= 1400:
        print("Division 3")
    else:
        print("Division 4")