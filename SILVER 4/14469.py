import sys
input = sys.stdin.readline

N = int(input())
times = [list(map(int, input().split())) for _ in range(N)]
times.sort(key=lambda x: x[0])

end_time = 0
for start, end in times:
    end_time = max(start, end_time) + end

print(end_time)