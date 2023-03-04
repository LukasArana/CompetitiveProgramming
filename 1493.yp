import math

n = int(input())

for i in range(n):
    t, k = map(int, input().split())
    res = []
    for j in range(k +1, t +1):
        res.append(str(j))
    for j in range(1, math.ceil(k/2) + 1):
        if (j <= k/2):
            res.append(str(j))
    print(len(res))
    print(" ".join(res))
