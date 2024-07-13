h, w = map(int, input().split())
block = list(map(int, input().split()))

result = 0
for idx in range(1, w - 1):
    left = max(block[:idx])
    right = max(block[idx + 1:])

    m = min(left, right)
    if m > block[idx]:
        result += m - block[idx]

print(result)    