n = int(input())

l =list(map(int, input().split()))

k = 0
zeros = 0
def prod(a):
    res = 1
    for i in a:
        res = res * i
    return res
for idx, i in enumerate(l):
    if (i > 1):
        l[idx] = 1
        k += i -1
    elif(i < -1):
        l[idx] = -1
        k += (i + 1)  * (-1)
    elif(i == 0):
        l[idx] = 1
        zeros +=1
        k += 1

if (prod(l) < 0):
    if (zeros > 0):
        print(k)
    else:
        print(k + 2)
else:

    print(k)

