N, K = map(int, input().split())

default = N // K
result = 0
for i in range(1, K + 1):
    result += i

if N < result:
    print(-1)
else:
    if (N - result) % K == 0:
        print(K - 1)
    else:
        print(K)