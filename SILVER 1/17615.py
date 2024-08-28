N = int(input())
ball = input()

# 총 B 와 R 의 개수를 세준다.
blue = ball.count('B')
red = ball.count('R')

# 맨 앞의 인접한 볼의 개수를 세서
# 총 개수에서 빼주고 어떤 값이 더 작은지 저장해준다.
first = ball[0]
red_minus = ball.find('B') if first == 'R' else 0
blue_minus = ball.find('R') if first == 'B' else 0
first_result = min(blue - blue_minus, red - red_minus)

# 맨 뒤의 인접한 볼의 개수를 세서
# 총 개수에서 빼주고 어떤 값이 더 작은지 저장해준다.
last = ball[-1]
red_minus = len(ball) - ball.rfind('B') - 1 if last == 'R' else 0
blue_minus = len(ball) - ball.rfind('R') - 1 if last == 'B' else 0
last_result = min(blue - blue_minus, red - red_minus)

# 맨 앞의 결과값과 맨 뒤의 결과값 중 더 적은 값을 출력한다.
print(min(first_result, last_result))