# https://www.acmicpc.net/problem/1541 잃어버린 괄호 
expression = input()
# 최소 값으로 만들기 위해서는 - 기준으로 
# 빼는 값이 최대가 되어야 하기 때문에
# 일단 - 로 split 한다
minus_expression = expression.split('-')
min_result = 0

for idx, minus in enumerate(minus_expression):
    # + 인 값들을 더해주고
    plus_arr = minus.split('+')
    value = 0
    for p in plus_arr:
        value += int(p)

    # 첫번째 값이면 값을 넣어주고
    # 그 외의 경우 값을 뺴준다
    if idx == 0:
        min_result = value
    else :
        min_result -= value

print(min_result)