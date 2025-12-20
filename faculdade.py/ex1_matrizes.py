toques = []
maior = 0

for i in range(8):
    toques.append([0]*4)

for i in range(20):
    L, C = map(int, input().split())
    toques[L][C] += 1

for l in range(8):
    for c in range(4):
        if toques[l][c] > maior:
            maior = toques[l][c]

for l in range(8):
    for c in range(4):
        if toques[l][c] == maior:
            print(l, c)

