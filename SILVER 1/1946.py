import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    scores = [list(map(int, input().split(' '))) for _ in range(n)]
    scores.sort()

    top = scores[0]
    result = 1
    for i in range(1, len(scores)):
        if scores[i][1] < top[1]:
            top = scores[i]
            result += 1
    
    print(result)