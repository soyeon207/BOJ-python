# 레벨의 수 N
n = int(input())
scores = [int(input()) for _ in range(n)]
# 입력받은 레벨을 뒤집어 준다
scores = scores[::-1]

# 어려운 레벨이 점수가 더 높아야 하기 때문에 
# 다음 어려운 레벨과 점수 차를 계산하기 위해서 
# 높은 레벨의 점수를 저장해준다
high_score = scores.pop(0)
result = 0

for score in scores:
    # 만약 쉬운 레벨의 점수가 더 높다면
    if score >= high_score:
         # 어려운 레벨 점수에서 -1 을 점수로 측정한다
         # 그리고 현재 점수에서 감소해야하는 수 만큼 저장해준다
        result += score - high_score + 1
        high_score = high_score - 1
    else:
        high_score = score
    
print(result)