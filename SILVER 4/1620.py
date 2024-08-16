import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pocketmon_idx = {}
pocketmons_name = {}

for i in range(N):
    pocketmon = input().strip()
    pocketmon_idx[i + 1] = pocketmon
    pocketmons_name[pocketmon] = i + 1

for _ in range(M):
    question = input().strip()
    if question.isdigit():
        print(pocketmon_idx[int(question)])
    else:
        print(pocketmons_name[question])

    