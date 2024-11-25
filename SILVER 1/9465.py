import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    scores = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0 for _ in range(n)] for _ in range(2)] 

    dp[0][0] = scores[0][0]
    dp[1][0] = scores[1][0]

    for i in range(1, n):
        dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + scores[0][i]
        dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + scores[1][i]

    print(max(dp[0][-1], dp[1][-1]))