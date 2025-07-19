from itertools import combinations

N, S = list(map(int, input().split()))
nums = list(map(int, input().split()))

count = 0
for i in range(N):
		for p in combinations(nums, i + 1):
				count += (sum(p) == S)

print(count)