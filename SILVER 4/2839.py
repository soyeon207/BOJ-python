n = int(input())

a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))

a_arr.sort()
b_arr.sort(reverse=True)
result = 0

for i in range(n):
    result += a_arr[i] * b_arr[i]

print(result)