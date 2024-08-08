n, m = map(int, input().split())

a = [list(input()) for _ in range(n)]
b = [list(input()) for _ in range(n)]
reverse = {'000': '111', '001':'110', '010':'101', '011': '100','100':'011', '101':'010', '111':'000', '110':'001'}

def reverse_list(i, j):
    # 행렬의 원소를 뒤집는 메소드
    change = reverse[''.join(a[i][j:j+3])]
    a[i][j:j+3] = list(change)

count = 0
for i in range(m-2):
    for j in range(n-2):
        # (3 x 3) 의 행렬을 확인해야하기 때문에 가로 - 2, 세로 - 2 의 모든 원소를
        # 반복하면서 행렬의 [0][0] 에 있는 값을 비교한다 
        # 첫번째 줄이 아니라 [0][0] 을 비교하는 이유는 [0][0] 이외의 부분은
        # 다음 시도에서 뒤집힐 수 있지만, [0][0] 은 현재에서만 뒤집을 수 있기 때문
        if a[j][i] != b[j][i]:
            reverse_list(j, i)
            reverse_list(j+1, i)
            reverse_list(j+2, i)
            count += 1

if a != b:
    print(-1)
else:
    print(count)