A, B = map(int, input().split())
N = int(input())
frequencies = [int(input()) for _ in range(N)]

m = abs(A - B)
for frequency in frequencies:
    m = min(m, abs(frequency - B) + 1)

print(m)