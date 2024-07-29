import sys
import heapq # 시간 초과가 계속 나기 때문에 heap 을 사용해줘야 한다
input = sys.stdin.readline

n = int(input())
times = [list(map(int, input().split())) for _ in range(n) ]
times.sort()

end_times = [] # 끝나는 시간들을 저장하는 배열
end_times.append(times.pop(0)[1])
for time in times:
    end_time = heapq.heappop(end_times)
    # 힙에서 뽑은 시작 시간보다 끝나는 시간이 큰 경우에는 
    # 연결될 시간이 없다는 것을 의미하기 때문에 해당 시간을 더해준다
    if end_time > time[0]:
        heapq.heappush(end_times, end_time)
    heapq.heappush(end_times, time[1])

print(len(end_times))