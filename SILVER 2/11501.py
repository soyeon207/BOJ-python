import sys
input = sys.stdin.readline

T = int(input()) # 테스트케이스
for _ in range(T):
    N = int(input())
    # 주가를 입력받아서 반대로 뒤집어 준다
    stocks = list(map(int, input().split()))[::-1]
    max = stocks.pop(0)
    result = 0

    for i in range(len(stocks)):
        current = stocks[i] 
        # 뒤에서 가장 큰 값이 지금 값보다 크다면
        if max > current:
            # 차이를 계산해서 더해준다
            result += max - current
        else: 
            # 만약 현재 값이 가장 크다면 
            # 가장 큰 값에 현재 값을 더해준다
            max = current

    print(result)