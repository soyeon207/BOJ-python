n = input()
sum = sum(int(k) for k in n)

# 30 의 배수가 아닌 경우 걸러내기
if "0" not in n or sum % 3 != 0:
    print(-1)
else:
    # 30의 배수라면 정렬해서 가장 큰 값을 출력해주면 된다
    n = sorted(n, reverse=True)
    print(''.join(n))