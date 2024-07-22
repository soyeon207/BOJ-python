name = input()
alphabet = {}
for n in name:
    if (n in alphabet) == False:
        alphabet[n] = 0
    alphabet[n] = alphabet[n] + 1

mid = ''
for key, value in alphabet.items():
    if value % 2 != 0:
        if mid != '':
            print("I'm Sorry Hansoo")
            exit()
        mid = key

result = ''
for key, value in sorted(alphabet.items()):
    result += key * (value // 2)

print(result + mid + result[::-1])