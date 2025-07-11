from collections import deque
import sys

N = int(sys.stdin.readline())
q = deque()

def isNotEmpty():
    if not q:
        print(-1)
    return q

for _ in range(N):
    command = sys.stdin.readline().strip()
    if command == 'pop' and isNotEmpty():
        print(q.popleft())
    elif command == 'size':
        print(len(q))
    elif command == 'empty':
        print(int(not q))
    elif command == 'front'and isNotEmpty():
        print(q[0])
    elif command == 'back'and isNotEmpty():
        print(q[-1])
    elif command.startswith('push'):
        commands = command.split(' ')
        q.append(commands[1])
