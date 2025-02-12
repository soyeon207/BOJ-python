N = int(input())
houses = list(map(int, input().split()))
times = list(map(int, input().split()))

total_time = times[N-1] if houses[N-1] < times[N-1] else houses[N-1]
previous_house = houses[N-1]

for i in range(N-2, -1, -1):
    total_time += (previous_house - houses[i])
    if houses[i] < times[i] and times[i] > total_time:
        total_time = times[i]
    previous_house = houses[i]
    
total_time += previous_house
print(total_time)
