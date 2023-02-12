# 코드포스 1030A In Search of an Easy Problem
import sys
put = sys.stdin.readline

n = int(put())
opinions = set(map(int, put().split()))

if opinions == {0}:
    print("EASY")
else:
    print("HARD")