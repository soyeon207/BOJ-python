N = int(input())

dp = [0] * (N+1)
dp[1] = 1
# i-2 에는 [01] 을 i-1 에는 [0] 을 붙여서 이친수를 완성한다.
for i in range(2, N + 1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])