str = input()

# 순서대로 만들 수 있어야 하기 때문에 
# pop 을 사용해서 순서대로 비교할 수 있도록 한다
UCPC = ['U', 'C', 'P', 'C']
alphabet = UCPC.pop(0)

# 입력받은 문자열을 반복하면서 UCPC 를 만들 수 있을지를 판단한다
for s in str:
    # 만일 알파벳이 동일하고
    if s == alphabet:
        # 모든 UCPC 문자가 있는 경우에는 
        # love 를 출력하고 프로그램을 종료한다
        if len(UCPC) == 0:
            print('I love UCPC')
            exit()
        # 다음 알파벳을 확인하기 위해서 맨 앞 글자를 pop 해준다
        alphabet = UCPC.pop(0)
    
# 반복문을 모두 돌고도 프로그램이 종료되지 않은 경우 
# UCPC 를 만들 수 없는 경우다
print('I hate UCPC')
