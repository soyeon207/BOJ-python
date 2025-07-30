import sys
input = sys.stdin.readline

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
	for j in range(3):
		if j == 0:
			costs[i][j] += min(costs[i-1][1], costs[i-1][2])
		elif j == 1:
			costs[i][j] += min(costs[i-1][0], costs[i-1][2])
		else: 
			costs[i][j] += min(costs[i-1][0], costs[i-1][1])

print(min(costs[-1]))