N = int(input())
candies = [list(input()) for _ in range(N)]
result = 0

def check(i, j):
    result = 0
    cnt = 1
    for k in range(1, N):
        if candies[k-1][j] == candies[k][j]:
            cnt +=1
        else:
            result = max(result, cnt)
            cnt = 1
        result = max(result, cnt)

    cnt = 1
    for k in range(1, N):
        if candies[i][k-1] == candies[i][k]:
            cnt +=1
        else:
            result = max(result, cnt)
            cnt = 1
        result = max(result, cnt)
    return result

def change_location(x1, y1, x2, y2):
    temp = candies[x1][y1]
    candies[x1][y1] = candies[x2][y2]
    candies[x2][y2] = temp

for i in range(N):
    for j in range(N):
        result = max(result, check(i, j))
        current = candies[i][j]
        if j+1 != N and current != candies[i][j+1]:
            change_location(i, j, i, j+1)
            result = max(result, check(i, j))
            result = max(result, check(i, j+1))
            change_location(i, j, i, j+1)

        if i+1 != N and current != candies[i+1][j]:
            change_location(i, j, i+1, j)
            result = max(result, check(i, j))
            result = max(result, check(i+1, j))
            change_location(i, j, i+1, j)
            
print(result)