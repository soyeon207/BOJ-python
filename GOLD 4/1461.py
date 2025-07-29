N, M = map(int, input().split())
locs = list(map(int, input().split()))

locs.sort()
result = abs(locs[0]) * -1 
if abs(locs[0]) < abs(locs[-1]):
	result = locs[-1] * -1

minus = []
plus = []
for loc in locs:
	if loc < 0:
		minus.append(loc)
	else:
		plus.append(loc)
plus.sort(reverse=True)

for i in range(0, len(minus), M):
	result += abs(minus[i]) * 2

for i in range(0, len(plus), M):
	result += plus[i] * 2

print(result)