t = int(input())
changes = [int(input()) for _ in range(t)]
moneys = [25, 10, 5, 1]

for change in changes:
    result = []
    for money in moneys:
        result.append(str(change // money))
        if change // money > 0:
            change %= money
    print(" ".join(result))