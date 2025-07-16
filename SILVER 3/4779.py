def cantor(size):
	if size == 1:
		return '-'

	div = size // 3
	blank = ' ' * div
	return cantor(div) + blank + cantor(div)


while True:
	try: 
		print(cantor(3 ** int(input())))
	except:
		break