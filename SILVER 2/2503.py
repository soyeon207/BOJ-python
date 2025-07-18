from itertools import permutations

N = int(input())
answers = [input().split() for _ in range(N)]

def check(num):
	global answers
	for answer in answers:
		ball = 0
		strike = 0
		for i in range(3):
			if str(num[i]) == answer[0][i]:
				strike += 1
			elif str(num[i]) in answer[0]:
				ball += 1

		if strike != int(answer[1]) or ball != int(answer[2]):
			return False
	return True


nums = list(permutations(range(1, 10), 3))
correct = 0
for num in nums:
	correct += check(num)

print(correct)
