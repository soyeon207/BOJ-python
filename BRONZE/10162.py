t = int(input())

timers = [300, 60, 10]
result = []
for timer in timers:
    result.append(str(t // timer))
    if t // timer > 0:
        t %= timer

if t > 0:
    print(-1)
else:
    print(" ".join(result))