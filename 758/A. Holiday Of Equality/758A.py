# 코드포스 758A Holiday Of Equality
import sys
put = sys.stdin.readline

n = int(put())
a = list(map(int, put().split()))
maximum = max(a)

print(sum([maximum - i for i in a]))