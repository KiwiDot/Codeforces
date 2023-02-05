# 코드포스 236A Boy or Girl
import sys
put = sys.stdin.readline

name = set(put().strip())

if len(name) % 2:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")