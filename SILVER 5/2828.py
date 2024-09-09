import sys
input = sys.stdin.readline

N, M = map(int, input().split())
j = int(input())

# 바구니의 최소, 최대 위치를 저장해둔다
# 가장 처음이기에 최소는 1, 최대는 바구니의 총 길이
min_basket = 1
max_basket = M
result = 0

# 사과의 개수만큼 반복문을 돌면서 바구니의 위치를 이동 시켜준다
for _ in range(j):
    apple = int(input())

    if max_basket < apple:
        # 입력 받은 위치 < 현재 위치 바구니 최대
        # 최대 바구니 위치 = 입력받은 위치 
        # 최소 바구니 위치 = 입력받은 위치 - 바구니 총길이 + 1
        result += apple - max_basket
        min_basket = apple - M + 1
        max_basket = apple
    elif min_basket > apple:
        # 현재 위치 바구니 최소 > 입력 받은 위치
        # 최대 바구니 위치 = 입력 받은 위치 - 바구니 총길이 - 1
        # 최소 바구니 위치 = 입력 받은 위치
        result += min_basket - apple
        min_basket = apple
        max_basket = apple + M - 1

print(result)


