# 코드포스 1702B Polycarp Writes a String from Memory
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    s = put().strip()
    memory = set()
    answer = 1

    for i in s:
        if i in memory:
            continue
        if len(memory) == 3:
            answer += 1
            memory = {i}
        else:
            memory.add(i)
    print(answer)