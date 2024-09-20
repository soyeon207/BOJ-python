N = int(input())

dp = [0] * 1001
dp[1] = 0
dp[2] = 1
dp[3] = 0

for i in range(4, N + 1):
    dp[i] = (dp[i - 3] + 1) % 2

if dp[N] == 0:
    print('SK')
else:
    print('CY')


