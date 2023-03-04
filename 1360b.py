



n = int(input())

for i in range(n):
    m = int(input())
    a = list(map(int, input().split()))
    a.sort()
    diff = []
    for idx in range(len(a) -1):
       diff.append(a[idx+1] - a[idx])
    print(min(diff))
