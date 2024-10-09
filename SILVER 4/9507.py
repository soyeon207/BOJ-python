t = int(input())
nums = list(int(input()) for _ in range(t))

m = max(nums)
dp = [0 for _ in range(m+1)]
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, m+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4]

for num in nums:
    print(dp[num])