T = int(input())

memo = [0 for _ in range(31)]
# 팩토리얼을 구하는 함수
# 메모제이션을 사용해서 결과를 저장해둔다
def fact(n):
    if n == 0:
        return 1
    if memo[n] != 0:
        return memo[n]
    memo[n] = n * fact(n - 1)
    return memo[n]

# 조합 공식을 사용해서 풀어준다.
for _ in range(T):
    N, M = map(int, input().split())
    print(fact(M) // (fact(M - N) * fact(N)))