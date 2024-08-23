N = int(input())
trees = list(map(int, input().split()))
trees.sort(reverse=True)

# 나무를 모두 다 심고나서 몇일이 남는지를 계산해주고
for i in range(N):
    trees[i] -= (N - i - 1)

# 모두 심고나서 가장 자라는데 오래 걸리는 시간 + 나무 심는데 걸린 시간 + 다음날(1)
# 을 더해서 정답을 구해준다
print(max(trees) + N + 1)