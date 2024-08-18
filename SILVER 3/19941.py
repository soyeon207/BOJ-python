N, K = map(int, input().split())
ph = list(input())
count = 0

for i in range(len(ph)):
    # 사람 인경우
    if ph[i] == 'P':
        # K 만큼의 거리 범위를 반복문을 돌면서
        for j in range(max(i-K, 0), min(i+K+1, len(ph))):
            # 햄버거를 먹을 수 있는지 확인한다
            if ph[j] == 'H':
                count += 1
                ph[j] = 'X'
                # 먹은 햄버거 자리는 X 로 다른 사람이 못 먹게 하고
                # 먹었다고 갯수를 세준다
                break

print(count)


    