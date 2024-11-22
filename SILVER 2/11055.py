import sys
input = sys.stdin.readline

A = int(input())
sequence = [int(i) for i in input().split()]
dp = sequence.copy()

for i in range(1, A):
    for j in range(i):
            if sequence[j] < sequence[i]:
               dp[i] = max(dp[j] + sequence[i], dp[i]) 
  
print(max(dp)) 