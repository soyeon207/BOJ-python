n, k = map(int, input().split())

dp = [1] * n
for i in range(n):
    dp[i] = [1] * (i + 1)
    if i > 1:
        for j in range(1, i):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

print(dp[n-1][k-1])
