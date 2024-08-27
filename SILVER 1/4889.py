idx = 1
while(True):
    left = 0 # 사용가능한 } 의 개수
    right = 0 # 사용가능한 { 의 개수
    data = str(input())
    # - 가 하나라도 있으면 프로그램 종료
    if '-' in data:
        break

    for d in data:
        if d == '}' and right > 0:
            # 한쌍이 될 수 있는 경우 사용가능한 { 개수에서 하나 빼주고
            right -= 1
        elif d == '}':
            # 한쌍이 될 수 없는 경우 사용 가능한 } 개수를 더해준다.
            left  += 1
        elif d == '{':
            right += 1

    result = (left + 1) // 2 + (right + 1) // 2
    print(f"{idx}. {result}")
    idx += 1