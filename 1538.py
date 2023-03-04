
n =int(input())
for i in range(n):
    m = int(input())

    l = list(map(int, input().split()))
    num = len(l)
    sum = 0
    for j in l:
        sum += j

    if (sum % num ==0):
        med = int(sum / num)
        res = 0
        for n in l:
            if (n > med):
                res += 1
        print(res)
    else:
        print(-1)



