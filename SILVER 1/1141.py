N = int(input())
alphabet = [input() for _ in range(N)]

alphabet.sort()
result = 1
for i in range(len(alphabet) - 1):
    if alphabet[i + 1].startswith(alphabet[i]) == False:
        result += 1

print(result)
    