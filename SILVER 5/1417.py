import heapq

n = int(input())
my = int(input())

votes = []
count = 0

for _ in range(n - 1):
    heapq.heappush(votes, -int(input()))

if len(votes) > 0:
    while True:
        a = heapq.heappop(votes)
        if abs(a) >= my:
            heapq.heappush(votes, a + 1)
            my += 1
            count += 1
        else:
            break

print(count)