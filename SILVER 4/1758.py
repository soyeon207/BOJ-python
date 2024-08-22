import sys
input = sys.stdin.readline

N = int(input())
tips = [int(input()) for _ in range(N)]
tips.sort(reverse=True)
result = 0

# 팁들을 내림차순으로 정렬해주고, 
# 기다린만큼 마이너스를 해서 값을 더해준다.
# 만약, 0 미만인 경우 0 을 더해주도록 한다.
for i in range(len(tips)):
    result += max(tips[i] - i, 0)

print(result)