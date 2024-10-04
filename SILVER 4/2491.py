import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
dp = [1 for _ in range(N)]
dp2 = [1 for _ in range(N)]

for i in range(1, len(nums)):
    num = nums[i]
    
    if nums[i-1] <= num:
        dp[i] = dp[i-1] + 1
    
    if nums[i-1] >= num:
        dp2[i] = dp2[i-1] + 1

print(max(max(dp), max(dp2)))
