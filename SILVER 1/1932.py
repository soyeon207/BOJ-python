n = int(input())

circle = [list(map(int, input().split())) for _ in range(n)]
dp = dp = [[0] * n for _ in range(n)]

dp[0][0] = circle[0][0]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = circle[i][j] + dp[i-1][j]
        elif j == i:
            dp[i][j] = circle[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = circle[i][j] + max(dp[i-1][j-1], dp[i-1][j])


print(max(dp[-1]))