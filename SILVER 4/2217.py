n = int(input())
ropes = [int(input()) for _ in range(n)]

ropes = sorted(ropes)
count = len(ropes) + 1

result = []
for rope in ropes:
    count -= 1
    result.append(rope * count)

print(max(result))