T = int(input())

for _ in range(T):
    k = int(input()) # 층
    n = int(input()) # 호
    dp = [0] * n
    for i in range(k):
        for j in range(n):
            if i == 0 or j == 0:
                dp[j] = (j+1)
            else:
                dp[j] += dp[j - 1]
    print(sum(dp))

