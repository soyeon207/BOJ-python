N = int(input())
antennas = list(map(int, input().split()))
antennas.sort()

# 중앙 값을 구해준다
if len(antennas) % 2 == 0:
    print(antennas[len(antennas)//2-1])
else:
    print(antennas[len(antennas)//2])