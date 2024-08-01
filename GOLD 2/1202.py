import sys
import heapq
input = sys.stdin.readline

# 보석 개수 = n, 가방 개수 = k 
n, k = map(int, input().split())
jewels = []

for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(jewels, (m, v))

bags = [int(input()) for _ in range(k)]
bags.sort()

temp = []
result = 0
# 가장 작은 가방부터 채워준다
for bag in bags:
    # 가방에 들어갈 수 있는 보석들을 temp 배열에 저장해준다
    while len(jewels) > 0 and jewels[0][0] <= bag:
        j = heapq.heappop(jewels)
        heapq.heappush(temp, (-j[1], j[0]))

    # 가방에 들어갈 수 있는 보석들 중 
    # 가장 값어치가 큰 보석을 가방에 넣어준다
    if len(temp) > 0:
        k = heapq.heappop(temp)
        result += -k[0]
    
    # 만일 보석도 없고, 가방에 들어갈 수 있는 보석도 없으면
    # 프로그램을 끝낸다
    if len(temp) == 0 and len(jewels) == 0:
        break
    
print(result)