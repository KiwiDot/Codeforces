# 코드포스 711A Bus to Udayland
import sys
put = sys.stdin.readline

n = int(put())
seat = [put().strip() for i in range(n)]

for i in range(n):
    if "OO" in seat[i]:
        print("YES")
        seat[i] = seat[i].replace("OO", "++", 1)
        for j in seat:
            print(j)
        break

else:
    print("NO")