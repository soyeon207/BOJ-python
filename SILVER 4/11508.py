import sys
input = sys.stdin.readline

n = int(input())
# 유제품 가격을 입력받고, 높은 가격 순으로 정렬해준다
dairy_proudcts = list(int(input()) for _ in range(n))
dairy_proudcts.sort(reverse=True)

# 일단 유제품 가격의 총 금액을 구한다음
result = sum(dairy_proudcts)
# 3, 6, 9 ... 이렇게 3단위로 건너뛰기하면서 
# 총 가격에서 마이너스 시켜준다
# 3번째 상품들은 2 + 1 행사 상품이기 때문에 무료 !!
for i in range(len(dairy_proudcts)// 3):
    result -= dairy_proudcts[(i + 1) * 3 -1]
    
print(result)