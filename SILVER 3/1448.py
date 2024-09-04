import sys
input = sys.stdin.readline

N = int(input())
straws = [int(input()) for _ in range(N)]
# 최댓값을 구해야하기 때문에 
# 가장 큰 값순으로 정렬
straws.sort(reverse=True)

# 앞에서 부터 3개씩 비교하므로 -2 를 빼서 반복문을 돌려준다.
for i in range(N - 2):
    # 각 길이가 삼각형의 조건에 맞는지 확인해주고 
    if (straws[i+1] + straws[i+2] > straws[i]) or (straws[i+1] == straws[i+2] == straws[i]) :
        # 삼각형의 조건에 맞으면 총 합을 출력한다.
        print(sum(straws[i:i+3]))
        exit()

print(-1)
