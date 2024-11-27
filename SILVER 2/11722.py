A = int(input())
sequence = [int(i) for i in input().split()]
dp = [1 for _ in range(A)]
for i in range(1, A):
     for j in range(i):
            if sequence[j] > sequence[i]:
                dp[i] = max(dp[j] + 1, dp[i])    
print(max(dp))