L, R = map(str, input().split())
count = 0

if L == R:
    # 1. L 과 R 이 같은 경우 
    # 포함되어 있는 8 의 개수를 출력
    count = str(L).count('8')
elif len(L) == len(R):
    # 2. L 과 R 의 길이가 같은 경우 
    # 맨 앞자리부터 같은 값을 가지고 있는지 확인하고, 
    # 같은 값인 경우 8의 개수를 세어준다.
    for i in range(len(L)):
        if L[i] == '8' and R[i] == '8':
            count += 1
        elif L[i] != R[i]:
            break
# 3. 그 외의 경우 => 0

print(count)

    