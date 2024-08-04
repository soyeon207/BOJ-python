idx = 0

while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    idx += 1

    camping_available = L * (V // P)
    print('Case %d: %d' % (idx, camping_available + min(L, V % P)))
    