# 코드포스 510A Fox And Snake
import sys
put = sys.stdin.readline

n, m = map(int, put().split())
print('#' * m)

for i in range(n//2):
    if i % 2:
        print('#' + '.' * (m - 1))
    else:
        print('.' * (m - 1) + '#')
    print('#' * m)