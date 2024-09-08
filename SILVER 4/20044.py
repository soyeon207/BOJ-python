n = int(input())
numbers = sorted(list(map(int, input().split())))
result = 0

for i in range(n):
    r = numbers[i] + numbers[len(numbers) - i - 1]
    if i == 0 or result > r:
        result = r

print(result)