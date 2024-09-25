K = int(input())

a = [1, 0] 
b = [0, 1]

a += [0] * (K - 1)
b += [0] * (K - 1)

for i in range(2, K+1):
    a[i] = a[i-1] + a[i-2]
    b[i] = b[i-1] + b[i-2]

print(a[-1], b[-1])