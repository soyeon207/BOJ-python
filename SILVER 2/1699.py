N = int(input())

dp = [0 for _ in range(N + 1)]
squares = []
i = 0

for n in range(1, N+1):
    if n ** 2 <= N:
        dp[n ** 2] = 1
        squares.append(n ** 2)
    
    if n <= 3:
        dp[n] = n
    elif dp[n] == 0:
        m = dp[n-1] + 1
        for square in squares:
            if square > n:
                break
            m = min(m, dp[n-square] + 1)

        dp[n] = m

print(dp[-1])