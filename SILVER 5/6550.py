while True:
    try:
        s, t = map(str, input().split())
        idx = 0
        result = 'Yes'

        # 입력받은 t 문자열을 돌면서 
        # s 부분 문자가 동일한 값인지를 확인한다.
        for t2 in t:
            if idx == len(s):
                break

            if s[idx] == t2:
                idx += 1

        # s 문자가 모두 t 에 속해 있는 경우 Yes
        # s 문자가 t 에 속해 있지 않은 경우 No
        if idx != len(s):
            result = 'No'
    
        print(result)
    except:
        break

