# 코드포스 255A Greg's Workout
import sys
put = sys.stdin.readline

n = int(put())
a = list(map(int, put().split()))
cnt = {"chest": 0, "biceps": 0, "back": 0}
exercise = list(cnt.keys())

for i in range(n):
    cnt[exercise[i % 3]] += a[i]

print(max(cnt, key=cnt.get))