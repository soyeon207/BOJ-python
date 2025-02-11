import sys
input = sys.stdin.readline

N = int(input())
numbers = dict.fromkeys(map(int, input().split()), True)

M = int(input())
munmbers = list(map(int, input().split()))

for mumber in munmbers:
    print(int(mumber in numbers))