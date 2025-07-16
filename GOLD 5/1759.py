lst = []

def cntVowel(word):
	cnt = 0
	for w in word:
		if ('a' in w) or ('e' in w) or ('i' in w) or ('o' in w) or ('u' in w):
			cnt +=1
	return cnt

def comb(idx, cnt):
	global words, L, C
	if cnt == L:
		password = ''.join(lst)
		vowelCnt = cntVowel(password)
		consonantCnt = L - vowelCnt
		if vowelCnt >= 1 and consonantCnt >= 2:
			print(password)
		return

	for i in range(idx, C):
		lst.append(words[i])
		comb(i+1, cnt+1)
		lst.pop()


L, C = list(map(int, input().split()))
words = sorted(list(map(str, input().split())))
comb(0, 0)