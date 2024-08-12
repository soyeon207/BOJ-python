N = int(input())
K = int(input())

sensors = list(map(int, input().split()))
sensors.sort()

# 각 센서들 사이의 차이를 구해서 리스트로 만들어준다
differences = [0]
for i in range(1, len(sensors)):
    differences.append(sensors[i] - sensors[i-1])
differences.sort(reverse=True)

# 센서들 간의 사이 중 가장 먼 차이를 K -1 만큼 빼고 더해준다 
# 집중국을 세우게 되면 집중국 간에 K -1 만큼의 공간이 생기는데 
# 가장 최소로 만들어야 하니깐 가장 먼 곳을 빼주고 다 더해주는것
result = 0
for j in range(K - 1, len(differences)):
    result += differences[j]

print(result)