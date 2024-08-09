N, K = map(int, input().split())
number = list(input())
result = [number.pop(0)]

for num in number:
    # 지워야 하는 숫자를 모두 지우지 않았고
    if K != 0:
        # stack 의 가장 마지막 값보다 현재의 값이 큰 경우 pop() 해준다
        # 최대한 큰 값이 앞에 위치해야 가장 큰 수를 만들 수 있기 때문
        while len(result) > 0 and result[-1] < num and K > 0:
            result.pop()
            K -= 1 
            
    result.append(num)

if K > 0:
    result = result[:len(result) - K]

print(''.join(result))
