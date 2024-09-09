N, M = map(int, input().split())
dna = [input() for _ in range(N)]
result = 0
result_dna = ''

for i in range(M):
    alphabet = {}
    for j in range(N):
        if dna[j][i] not in alphabet:
            alphabet[dna[j][i]] = 0
        alphabet[dna[j][i]] += 1

    # 첫번째 정렬 조건 = 알파벳의 개수 높은 순
    # 두번째 정렬 조건 = 알파벳의 순서 낮은 순
    alphabet_sort = sorted(alphabet.items(), key=lambda x :(x[1], -ord(x[0])), reverse=True)

    for k in range(len(alphabet_sort)):
        # 가장 첫번째로 정렬된 알파벳의 경우에는 
        # Hamming Distance 가 적은 것이기 때문에 정답 DNA 에 더해주고
        if k == 0:
            result_dna += alphabet_sort[k][0]
        else:
            # 그 외의 알파벳들은
            # Hamming Distance 값에 더해준다
            result += alphabet_sort[k][1]

print(result_dna)
print(result)


