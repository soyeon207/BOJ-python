import sys
input = sys.stdin.readline

N, M = map(int, input().split())
p = [int(input()) for _ in range(M)]
p.sort(reverse=True)

price = 0 # 경래가 책정한 가격
total = 0 # 가격으로 올릴 수 있는 수익
for i in range(len(p)):
    # 얻을 수 있는 수익을 구한 후
    # 수익이 최대인지 확인한다.
    temp = p[i] * min(i + 1, N)
    if total <= temp:
        total = temp
        price = p[i]

print(price, total)