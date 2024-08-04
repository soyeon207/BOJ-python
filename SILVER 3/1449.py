# 물이 새는 곳 개수 = N
# 테이프의 길이 = L
N, L = map(int, input().split())
leaky_places = list(map(int, input().split()))
leaky_places.sort()

# 한 개의 테이프가 붙을 수 있는 거리를 저장
tape_start = leaky_places.pop(0)
tape_end = tape_start + L - 1
result = 1

for place in leaky_places:
    if tape_start <= place and place <= tape_end:
        # 만약 테이프 안에 위치한 구멍이면 테이프를 붙여주고
        continue
    else:
        # 그렇지 않은 경우에는 테이프 하나를 더 사용해야 하기 때문에 
        # 테이프 개수를 + 1 해주고, 거리를 저장해준다
        result += 1
        tape_start = place
        tape_end = place + L - 1

print(result)