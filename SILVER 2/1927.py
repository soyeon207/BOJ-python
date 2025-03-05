from queue import PriorityQueue
import sys

input = sys.stdin.readline
queue = PriorityQueue()
N = int(input())

for i in range(N):
    x = int(input())
    
    if x == 0:
        if queue.empty():
            print(0)
        else:
            print(queue.get(0))
    else:
        queue.put(x)