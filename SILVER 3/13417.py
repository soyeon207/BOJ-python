import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    cards = list(map(str, input().split()))
    result = cards.pop(0)

    for card in cards:
        # 가장 앞 카드가 현재 카드보다 작은 경우 뒤에 더해주고
        # 현재 카드보다 큰 경우에는 앞에 더해준다.
        if result[0] < card:
            result += card
        else:
            result = card + result
        
    print(result)

