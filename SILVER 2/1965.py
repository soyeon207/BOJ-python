n = int(input())
boxes = [int(box) for box in input().split()]
dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if boxes[j] < boxes[i]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))