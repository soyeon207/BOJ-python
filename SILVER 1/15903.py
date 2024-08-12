import heapq

n, m = map(int, input().split())

cards = []
for input in input().split():
    heapq.heappush(cards, int(input))

for i in range(m):
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)

    heapq.heappush(cards, card1 + card2)
    heapq.heappush(cards, card1 + card2)

print(sum(cards))