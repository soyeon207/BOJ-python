n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

result = 0
for _ in range(n):
    result += a.pop() * b.pop()

print(result)
