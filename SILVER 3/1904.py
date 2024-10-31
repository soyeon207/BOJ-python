# 자연수 N 을 입력받기
N = int(input())
# dp 배열 초기화
dp = [0 for _ in range(N)]

# N = 1 과 N = 2 일 경우 초기값 입력
dp[0] = 1
if N >= 2:
    dp[1] = 2

# i-1 2진 수열에 1 을 더하거나 
# i-2 2진 수열에 00 을 더하면 
# i 일 때 만들 수 있는 2진 수열의 개수가 나온다.
for i in range(2, N):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[N-1])