N = int(input())
drinks = list(map(int, input().split()))
drinks.sort(reverse=True)

result = drinks.pop(0)
for drink in drinks:
    result += drink / 2

print(result)

