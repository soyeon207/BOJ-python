def number_add_func(arr):
    # 파라미터로 넘겨받은 배열에 대해서 최대한의 합을 구하는 함수
    result = 0
    # 넘겨받은 배열은 이미 정렬된 배열임으로 
    # 앞에서 2개씩 더하거나 곱해주면 된다
    if len(arr) % 2 != 0:
        result = arr.pop()

    for i in range(0, len(arr), 2):
        result += max(arr[i] * arr[i+1], arr[i] + arr[i+1])
    
    return result

import sys 
input = sys.stdin.readline

n = int(input())
sequence = [int(input()) for _ in range(n)]
sequence.sort()

# 입력받은 수열을 [음수 + 0] 과 [양수] 로 나눈다
minus_arr = [s for s in sequence if s <= 0]
plus_arr = [s for s in sequence if s > 0]
    
result = 0
result += number_add_func(minus_arr)
result += number_add_func(plus_arr[::-1])

print(result)

