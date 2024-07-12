# https://www.acmicpc.net/problem/12904 A 와 B
s = list(map(str, input().strip()))
t = list(map(str, input().strip()))

while len(s) < len(t):
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t = t[::-1]
        
    if len(s) == len(t):
        break

if s == t:
    print(1)
else:
    print(0)