import sys
input = sys.stdin.readline

N = int(input())
locations = []

for i in range(N):
    locations.append(list(map(int, input().split())))

locations.sort(key=lambda x: (x[-1], x[0]))

for location in locations:
    print(location[0], location[1])