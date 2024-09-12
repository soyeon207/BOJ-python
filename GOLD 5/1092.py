import sys 
input = sys.stdin.readline

N = int(input())
cranes_weight = list(map(int, input().split()))

M = int(input())
box_weight = list(map(int, input().split()))

cranes_weight.sort(reverse=True)
box_weight.sort(reverse=True)

if max(cranes_weight) < max(box_weight):
    print(-1)
    exit(0)

result = 0
while len(box_weight) != 0 and len(box_weight) != 0:
    count = 0
    temp_box = []
    i = 0
    for box in box_weight:
        if i >= N:
            temp_box.append(box)
        else:
            crane = cranes_weight[i]
            if box > crane:
                temp_box.append(box)
            else:
                i += 1
                count += 1
    
    box_weight = temp_box
    if count > 0:
        result += 1
        
print(result)

