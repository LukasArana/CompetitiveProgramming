import sys


n = int(input())
dp = [sys.maxsize] *(n + 1)
dp[0] = 0
nums = list(map(int, (input().split())))
cost = list(map(int, input().split()))
j = int(input())
for i in range(1, n +1):
    idx = i
    print(idx)
    while(idx <= i  and nums[i] - nums[i - idx] < j and idx <= i):
        print(idx)
        dp[i] = min(dp[i], dp[i -j] + cost[i])
        idx += 1
print(dp)
