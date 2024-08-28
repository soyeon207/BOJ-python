N, M = map(int, input().split())
result = 0;
box = 0;

if N > 0:
    books = list(map(int, input().split()))
    for book in books:
        if box + book > M:
            result += 1
            box = 0
        box += book

    if box != 0:
        result += 1

print(result)

