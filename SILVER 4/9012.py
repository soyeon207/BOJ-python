T = int(input())

for _ in range(T):
    words = input()
    left = 0
    right = 0
    for word in words:
        if word == '(':
            left += 1
        else:
            if left > 0:
                left -= 1
            else:
                right += 1

    if left > 0 or right > 0:
        print('NO')
    else:
        print('YES')
