import math

for i in range(int(input())):
    l = list(map(int, input().split()))
    c = l[0]
    n = l[1]
    k = math.floor( n /2)
    if (c % n ==0):
        suma = c
    else:
        suma = math.floor(c / n) * n
        if ((c % n ) < k):
            suma = c
        else:
            suma = suma + k
    print(suma)


