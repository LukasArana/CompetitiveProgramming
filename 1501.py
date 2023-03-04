



n = int(input())

for i in range(n):
    m = int(input())
    l = list(map(int, input().split()))
    res = [0 for j in range(m + 1)]
    for j in range(m):
        a= j-l[j] +1
        if (a < 0):
           a = 0
        res[a: j+1] =[1 for k in range(a, j+1)]
    print(" ".join(map(str, res[0:len(res)-1])))

