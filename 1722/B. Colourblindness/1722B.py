# 코드포스 1722B Colourblindness
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    color1 = put().strip().replace('B', 'G')
    color2 = put().strip().replace('B', 'G')

    if color1 == color2:
        print("YES")
    else:
        print("NO")