n = int(input())
dp = [0 for _ in range(max(n, 3))]

dp[0] = 1
dp[1] = 3
dp[2] = 5

for i in range(3, n):
    dp[i] = dp[i-1] + dp[i-2] * 2

print(dp[n-1] % 10007)
