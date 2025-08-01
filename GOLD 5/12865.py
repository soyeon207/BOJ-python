import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(N+1)] for _ in range(K+1)]
for i in range(1, K+1):
    for j in range(1, N+1):
        w, v = items[j-1]
        if i < w:
            dp[i][j] = dp[i][j-1]
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-w][j-1] + v)

print(dp[-1][-1])