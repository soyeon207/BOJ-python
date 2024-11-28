K = int(input())

nums = [int(input()) for _ in range(K)]
result = []

for num in nums:
    if num == 0:
        result.pop()
    else:
        result.append(num)

print(sum(result))