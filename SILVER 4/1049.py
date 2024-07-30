n, m = map(int, input().split())
packages = [list(map(int, input().split())) for _ in range(m)]

per_price = min(packages, key = lambda x: x[1])[1]
package_price = min(packages, key = lambda x: x[0])[0]

price = 0
# 패키지(6) 구매가 더 싼 경우에만 패키지를 구매한다
if package_price < per_price * 6:
    price += package_price * (n // 6)
    n %= 6        

# 남은 끊어진 기타줄에 대해서는  낱개와 패키지 구매 중 더 싼 방식으로 구매한다
per_total = per_price * n
package_total = package_price * (n // 6  + 1)

print(price + min(per_total, package_total))
