import sys
input = sys.stdin.readline

N, M = input().split()
N = int(N)
M = int(M)

nums = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]
dp[0][0] = nums[0][0]

for i in range(N):
    for j in range(M):
        if i == 0:
            if j ==0:
                pass
            dp[i][j] = dp[i][j-1] + nums[i][j]
        elif j == 0:
            if i == 0:
                pass
            dp[i][j] = dp[i-1][j] + nums[i][j]
        else:
            dp[i][j] = max(max(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1]) + nums[i][j]

print(dp[N-1][M-1])
            
