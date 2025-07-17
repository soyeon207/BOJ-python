N = int(input())

players = [list(map(int, input().split())) for _ in range(N)]
ranking = sorted(players, key=lambda x: (x[1] * x[2] * x[3], 
										x[1] + x[2]+x[3], 
										x[0]))

print(ranking[0][0], ranking[1][0], ranking[2][0])