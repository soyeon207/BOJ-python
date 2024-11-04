N = int(input())

# 상근 = 0
# 창영 = 1

stones = [0] * N
for i in range(1, N):
    stones[i] = (stones[i-1] + 1) % 2

if stones[-1] == 1:
    print('SK')
else:
    print('CY')
