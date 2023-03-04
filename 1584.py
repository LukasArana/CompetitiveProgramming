
n = int(input())

for i in range(n):
    m = int(input())
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    l1.sort()
    l2.sort()
    ans = True
    for j in range(len(l1)):
        if (abs(l1[j] -l2[j]) >1 or l1[j] > l2[j]  ):
            ans = False
            break
    if ans:
        print("YES")
    else:
        print("NO")
