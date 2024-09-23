import sys
input = sys.stdin.readline

fibo = {}
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if n in fibo:
            return fibo[n]
        one = fibo.setdefault(n-1, fibonacci(n - 1))
        two = fibo.setdefault(n-2, fibonacci(n-2))
        fibo[n] = one + two
        return fibo[n]

T = int(input())
nums = [int(input()) for _ in range(T)]
m = max(nums)
fibonacci(m + 1)

for num in nums:
    if num == 0:
        print(1, 0)
    else:
        print(fibo[num-1], fibo[num])
