S = input()

words = []
for i in range(len(S)):
    for j in range(len(S) - i):
        words.append(S[j:j+i+1])

words = set(words)
print(len(words))