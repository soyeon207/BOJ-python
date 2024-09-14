import sys 
input = sys.stdin.readline

N = int(input())

locations = [list(map(int, input().split())) for _ in range(N)]

locations.sort(key=(lambda x: x[1]))
locations.sort(key=(lambda x: x[0]))

for location in locations:
    print(location[0], location[1])

