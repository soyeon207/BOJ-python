import sys
input = sys.stdin.readline

T = int(input())
nums = []
for _ in range(T):
    nums.append(int(input()))

max_num = max(nums)
dp = [0] * (max_num + 1)
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, max_num + 1):
    dp[i] = sum(dp[i-3:i])

for num in nums:
    print(dp[num])