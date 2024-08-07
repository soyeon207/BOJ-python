n = int(input())

# 저울 추를 입력 받는다
scale_weight = list(map(int, input().split()))
scale_weight.sort()

min = max = 0
# 낮은 순으로 정렬했을 때 첫번째 값이 1 이 아니면 최솟값이 1이다
if scale_weight[0] == 1:
    min = max = 1
    # 저울추들을 하나씩 더해가면서 기존 범위와 연결될 수 있는지 확인한다
    # 더해지는 저울추의 범위는 [더해지는 저울추 - max + 1] 임으로 
    # 기존 해당 범위가 기존 저울추 범위와 연결될 수 있는지 확인하면 된다
    for weight in range(1, len(scale_weight)):
        if scale_weight[weight] <= max + 1:
            max += scale_weight[weight] 
        else:
            break

print(max + 1)
