import sys
input = sys.stdin.readline

N = int(input())
expected_rank = [int(input()) for _ in range(N)]
expected_rank.sort()

result = 0 # 불만도의 합
# 작은 불만도부터 정렬했기 때문에 
# |rank - 현재 불만도| 가 최선의 등수이다
for i in range(1, len(expected_rank) + 1):
    result += abs(expected_rank[i - 1] - i)

print(result)