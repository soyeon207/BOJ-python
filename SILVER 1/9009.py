T = int(input())
nums = [int(input()) for _ in range(T)]

max_num = max(nums)
fibo = [0, 1]
idx = len(fibo)
while fibo[-1] < max_num:
    fibo.append(fibo[idx-1] + fibo[idx-2])
    idx += 1
fibo.sort(reverse=True)

for num in nums:
    temp = []
    for f in fibo:
        if num >= f and f != 0:
            temp.append(str(f))
            num -= f
    print(" ".join(temp[::-1]))




