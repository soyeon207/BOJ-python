S = input()
total = ''
temp = ''
start = False

for s in S:
    if s == '<':
        total += temp[::-1]
        temp = ''
        start = True
    elif s == '>':
        total += temp + '>'
        temp = ''
        start = False
        continue
    elif s == ' ' and start == False:
        total += temp[::-1] + ' '
        temp = ''
        continue
    temp += s

total += temp[::-1]
print(total)

