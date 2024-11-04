import sys 
input = sys.stdin.readline

N = int(input())
tp = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N)]

for i in range(N):
    t = tp[i][0]
    p = tp[i][1]
    idx = i + t - 1 

    if idx < N:
        m = dp[:i]
        an = p
        if len(m) > 0:
            an += max(m)
        dp[idx] = max(an, dp[idx])

print(max(dp))



    