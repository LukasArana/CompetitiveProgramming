def differencia(a, b):
    diff = 0
    for i in range(len(a)):
        diff += abs(ord(a[i]) - ord(b[i]))
    return diff
n = int(input())
l = []
w = []
for _ in range(n):
    lag = list(map(int, input().split()))
    l = []
    w=  []
    for i in range(lag[0]):
        w.append(input())
    for i in range(lag[0]):
        for j in range(i+1, lag[0]):
            l.append(differencia(w[i], w[j]))
        l.sort()
    print(min(l))

