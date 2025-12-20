# Vamos criar uma matriz 8x4 para contar quantos toques existem em cada posição.
# L = 0..7  (8 linhas)
# C = 0..3  (4 colunas)

toques = [[0 for c in range(4)] for l in range(8)]

# Ler 20 toques
for _ in range(20):
    L, C = map(int, input().split())
    toques[L][C] += 1


# Agora vamos descobrir o maior número de toques em uma região
maior = 0
for l in range(8):
    for c in range(4):
        if toques[l][c] > maior:
            maior = toques[l][c]

# Agora imprimimos TODAS as regiões empatadas com esse maior valor
for l in range(8):
    for c in range(4):
        if toques[l][c] == maior:
            print(l, c)
