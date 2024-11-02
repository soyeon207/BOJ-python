T = int(input())

nums = [int(input()) for _ in range(T)]
max_num = max(nums)

dp = [1, 1, 1, 2, 2]
dp = dp + [0] * max(0, max_num - 5)

# P(N) 은 dp[i-1] + dp[i-5] 를 더한 값이다
for i in range(5, max_num):
    dp[i] = dp[i-1] + dp[i-5]

for num in nums:
    print(dp[num-1])
