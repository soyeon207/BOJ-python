# https://www.acmicpc.net/problem/1343 폴리오미노
board = input()
collect = ''
idx = 0

while len(board) > idx:
    if board[idx] == '.':
        collect += '.'
        idx += 1
    elif board[idx:idx+4] == 'XXXX':
        collect += 'AAAA'
        idx += 4
    elif board[idx:idx+2] == 'XX':
        collect += 'BB'
        idx += 2
    else:
        collect = '-1'
        break

print(collect)