import sys
input = sys.stdin.readline

N = int(input())
alphabet = [input().strip() for _ in range(N)]

alphabet = list(set(alphabet))
alphabet.sort()
alphabet.sort(key=len)

print("\n".join(alphabet))