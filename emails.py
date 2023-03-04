
def bukatuta(arr):
    for i in arr:
        if (len(i) +1 < len(arr)):
            return False

    return True

n, m = list(map(int, input().split()))
adj = [[j +1] for j in range(n)]
for i in m:
    lag1, lag2 = list(map(int, input().split()))
    adj[lag1] = lag2
    adj[lag2] = lag1

idx = 0
ans = True
bukatu = False
while(not bukatuta(l)):
    idx += 1
    for i in l:
        for j in i:
            adj[j].append(i)
            
#Egun batean norbaiti ez bazaio bidaltzen, -1
if (ans):
    for i in range(n):
        if (len(adj[i]) < n):
            ans = False
            break

if ans:
    print(idx)
else:
    print(-1)
