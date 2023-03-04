last =-1
res = True
l = list(map(int, input().split()))
for i in range(l[0]):
    num = input()
    for j in range(l[1]):
        lag = str(num)[j]
        if (j ==0):
            t = lag
            if (lag == last):
                print("NO")
                res  = False
                break
            last = lag
        else:
            if (lag != t):
                print("NO")
                res = False
                break
    if (not res):
        break
if (res):
    print("YES")

