# 코드포스 1669B Triple
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    a = list(map(int, put().split()))
    cnt = {}

    for i in a:
        if i in cnt:
            cnt[i] += 1
            if cnt[i] == 3:
                print(i)
                break
        else:
            cnt[i] = 1

    else:
        print(-1)