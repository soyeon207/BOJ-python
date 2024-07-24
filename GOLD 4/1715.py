from queue import PriorityQueue
n = int(input())

cards = PriorityQueue()
[cards.put(int(input())) for _ in range(n)]

result = 0
for _ in range(n-1):
    sum = cards.get() + cards.get()
    cards.put(sum)
    result += sum

print(result)
