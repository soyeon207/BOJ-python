str1 = str(input())
str2 = str(input())


m = [[0 for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]

for i in range(len(str1)):
    s1 = str1[i]
    for j in range(len(str2)):
        s2 = str2[j]

        if s1 == s2:    
            m[i + 1][j + 1] = m[i][j] + 1
        else:
            m[i + 1][j + 1] = max(m[i][j+1], m[i+1][j])        



print(max(max(m)))