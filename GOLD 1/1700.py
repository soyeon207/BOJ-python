N, K = map(int, input().split())
electrical_appliances = list(map(int, input().split()))

# 각 전기 용품 별 우선순위를 저장해준다. 
# 우선순위는 앞과 가까울 수록 높고, 배열로 모든 우선순위를 저장해준다.
priority_hash = {}
for i in range(len(electrical_appliances)):
    priority_hash.setdefault(electrical_appliances[i], []).append(K - i)

result = 0
priority = K
multi_tap = []
for appliance in electrical_appliances:
    # 이미 멀티탭에 꽂혀있는 경우에는 패스하고
    # 멀티템에 꽂혀있지 않은 경우 플러그를 빼거나 꽂아야 한다.
    if appliance not in multi_tap:
        if len(multi_tap) < N:
            # 멀티탭이 가득차지 않은 경우 그냥 플러그를 꽂아준다. 
            multi_tap.append(appliance)
        else:
            # 멀티탭이 가득찬 경우 
            # 앞으로 사용하지 않는 전기용품이거나
            # 현재 위치에서 가장 멀리 떨어여 있는 전기용품의 플러그를 제거한다.
            min = 0
            for m in multi_tap:
                if len(priority_hash[m]) <= 0:
                    min = m
                    break
                elif min == 0:
                    min = m
                elif priority_hash[min][0] > priority_hash[m][0]:
                    min = m
            # 로직에 의해서 구해진 플로그를 제거하고
            # 현재 가전용품의 플러그를 껴준다.
            multi_tap.remove(min)
            multi_tap.append(appliance)
            result += 1

    # 우선순위에서 현재 위치는 제거한다.
    priority_hash[appliance].remove(priority)
    priority -= 1
    
print(result)

