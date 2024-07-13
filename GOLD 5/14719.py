h, w = map(int, input().split())
block = [[0] * w for _ in range(h)]
block_input = list(map(int, input().split()))

for idx, i in enumerate(block_input):
    for j in range(1, i+1):
        block[h - j][idx] = 1

count = 0
start = -1
for i in range(h):
    start = - 1
    for j in range(w):
        if block[i][j] == 1:
            if start == -1:
                start = j
            else:
                for k in range(start, j):
                    if block[i][k] == 0:
                        count += 1
                start = j
    
print(count)