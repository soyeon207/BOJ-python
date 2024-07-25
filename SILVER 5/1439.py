s = input()
last = s[0]
h = {'0': 0, '1': 0}

for i in s:
    if last != i:
        h[last] += 1
        last = i
h[last] += 1

if h['0'] < h['1']:
    print(h['0'])
else:
    print(h['1'])
