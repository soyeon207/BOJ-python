n = int(input())

nums = list(map(int, input().split()))
dp = [0 for _ in range(n)]
dp[0] = nums[0]

for i in range(1, n):
    dp[i] = max(dp[i-1], 0) + nums[i]

print(max(dp))