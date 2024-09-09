for _ in range(int(input())):
    N = int(input())
    initial = input()
    goal = input()

    result = 0
    b_count = 0
    w_count = 0
    for i in range(len(initial)):
        if initial[i] != goal[i]:
            if initial[i] == 'W' and b_count > 0:
                b_count -= 1
            elif initial[i] == 'B' and w_count > 0:
                w_count -= 1
            elif initial[i] == 'W':
                w_count += 1
                result += 1
            elif initial[i] == 'B':
                b_count += 1
                result += 1

    print(result)
