import sys
input = sys.stdin.readline

def check_invalid(board_value, check):
    return (board_value == 'W' and check == True) or (board_value == 'B' and check == False)

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

result = 8 * 8
for n in range(0, N-7):
    for m in range(0, M-7):
        temp_board = [[board[n+q][m+p] for p in range(8)] for q in range(8)]

        for start in [True, False]:
            check = start
            count = 0   
            for a in range(8):
                check = not check
                for b in range(8):
                    if check_invalid(temp_board[a][b], check): 
                        count += 1
                    check = not check    
                    
            if result > count:
                result = count

print(result)