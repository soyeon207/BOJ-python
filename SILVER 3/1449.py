# 물이 새는 곳 개수 = N
# 테이프의 길이 = L
N, L = map(int, input().split())
leaky_places = list(map(int, input().split()))
leaky_places.sort()

tape_start = leaky_places.pop(0)
tape_end = tape_start + L - 1
result = 1

for place in leaky_places:
    if tape_start <= place and place <= tape_end:
        continue
    else:
        result += 1
        tape_start = place
        tape_end = place + L - 1

print(result)