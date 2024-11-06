num = int(input())
scores = [int(input()) for _ in range(num)]

dp = [0] * num
dp[0] = scores[0]

if num > 1:
    dp[1] = scores[0] + scores[1] 
if num > 2:
    dp[2] = max(scores[0] + scores[2], scores[1] + scores[2])

for i in range(3, num):
    dp[i] = max(dp[i - 3] + scores[i - 1] + scores[i], dp[i - 2] + scores[i])

print(dp[-1])
