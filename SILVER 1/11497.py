import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())                    # 통나무 개수
    L = list(map(int, input().split())) # 통나무 높이
    L.sort()

    start = L[0]
    end = L[1]
    result = 0
    
    # 정렬한 상태에서 작은 숫자부터 두개씩 가져와서
    # 왼쪽끝과 오른쪽 끝으로 배치해준다. 
    # 배치했을 때 통나무의 길이의 차가 가장 작도록 계산하도록 배치한다.
    for i in range(2, len(L) - 1, 2):
        s = L[i]
        e = L[i + 1]

        temp_start = e
        temp_end = s

        if start < end:
            temp_start = s
            temp_end = e
        
        result = max(result, max(temp_start - start, temp_end - end))
        start = temp_start
        end = temp_end

    if len(L) % 2 != 0:
        result = max(result, L[-1] - min(start, end))

    print(result)