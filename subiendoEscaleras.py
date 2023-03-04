

l = list(map(int, input().split()))
while (l != [0]):
    n= l[0]
    m = l[1]
    l = l[2:]
    dp = [0 for i in range(n +1)]
    dp[0] = 1
    for i in range(n +1):
        for j in reversed(l):
            if (i - j >= 0):
                dp[i] += dp[i - j]
    print(dp[-1])
    l = list(map(int, input().split()))

