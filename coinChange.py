

k, n = map(int, input().split())

l = map(int, input().split())

dp = [1] + [0] * k
for coin in l:
    print(coin)
    for i in range(coin, k+1):
        print(i)
        dp[i] += dp[i - coin]
print(dp)



