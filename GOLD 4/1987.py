import sys
input = sys.stdin.readline

R, C = map(int, input().split())
alphabets = [list(input()) for _ in range(R)]

directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
visited = set([alphabets[0][0]])
result = 0

def dfs(i, j):
    global result
    result = max(result, len(visited))
    for dy, dx in directions:
        ny, nx = i + dy, j + dx
        if 0 <= ny < R and 0 <= nx < C:
            next_al = alphabets[ny][nx]
            if next_al not in visited:
                visited.add(next_al)
                dfs(ny, nx)
                visited.remove(next_al)

dfs(0, 0)
print(result)