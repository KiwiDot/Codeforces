# 코드포스 1385B Restore the Permutation by Merger
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    a = put().split()

    arr1, arr2 = [], []
    for i in a:
        if i in arr1:
            arr2.append(i)
        else:
            arr1.append(i)

    print(' '.join(arr1))