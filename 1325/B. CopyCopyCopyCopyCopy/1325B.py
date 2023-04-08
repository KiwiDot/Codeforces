# 코드포스 1325B CopyCopyCopyCopyCopy
import sys
put = sys.stdin.readline

t = int(put())

while t:
     t -= 1
     n = int(put())
     a = len(set(put().split()))

     print(a)