# https://www.acmicpc.net/problem/1931 회의실 배정
n = int(input())
meeting_time = [list(map(int, input().split())) for _ in range(n)]
meeting_time.sort(key = lambda x: (x[1], x[0]))

cnt = 1
current = meeting_time[0]

for start, end in meeting_time[1:]:
    if start < current[1]:
        continue
    cnt += 1
    current = [start, end]

print(cnt)