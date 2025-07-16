list = []

def comb(nums, idx):
	if idx == 6:
		print(' '.join(list))
		return
	
	for i in range(len(nums)):
		list.append(nums[i])
		comb(nums[i+1:], idx + 1)
		list.pop()

while True:
	case = input()
	if case == '0':
		break
	comb(case.split(' ')[1:], 0)
	print()