paid = int(input())
change = 1000 - paid
change_yen = [500, 100, 50, 10, 5, 1]
count = 0

for yen in change_yen:
	count += change // yen
	change %= yen

print(count)