

n = int(input())
for i in range(n):
    a = list(map(int, input()))
    if (sum(a[0:3]) == sum(a[len(a) -3:])):
        print("YES")
    else:
        print("NO") 

