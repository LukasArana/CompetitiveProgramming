import math

m, d, n = list(map(int, input().split()))
while (m != 0 or d != 0 or n != 0):
    if (max(m, d) % min(m, d) ==0):
        res = max(m,d)
    else:
        res = m * d


    print( math.floor(n / res))

    m, d, n = list(map(int, input().split()))
