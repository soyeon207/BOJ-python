n = int(input())

won5 = n // 5 # 5원 개수 계산
n %= 5

# 5를 더했을 때 2로 나누어 지는 경우도 있으므로
# 그 경우에는 5원 개수에서 하나를 빼고 다시 금액에 더해준다
if won5 >= 1 and n % 2 != 0:
    n += 5
    won5 -= 1

if n % 2 != 0:
    print(-1)
else:
    print(won5 + n // 2)