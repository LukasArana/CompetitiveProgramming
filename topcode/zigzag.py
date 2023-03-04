
l = list(map(int, input().split()))
print(l)
#0 incresing, 1 decresing
dp = [[0, 0]for i in range(len(l) + 1)]
#dp[2][1] =10
dp[0] = [1, 1]
for i in range(1, len(l)):
    for j in reversed(range(0, i)):
        num = l[j]
        print(num)
        print(l[i])
        if (l[i] > num):
            dp[i][0] = max(dp[i][0], dp[j][0] +1)
        if (l[i] < num):
            dp[i][1] = max(dp[i][1], dp[j][1] + 1)
        if (l[i] == num):
            dp[i][0] = max(dp[j][0] +1, dp[j][1] +1, dp[i][0], dp[i][1])
            dp[i][1] = dp[i][0]
    print(dp)
