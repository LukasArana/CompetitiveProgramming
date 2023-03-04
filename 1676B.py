
for i in range(int(input())):
    _ = int(input())
    l = list(map(int, input().split()))
    l.sort()
    m = l[0]
    diff = 0
    for i in l:
        diff += i - m
    print(diff)
