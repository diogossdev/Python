tabela = []
for i in range(4):
    tabela.append([0]*6)

bombas = int(input('Digite a quantidade de bombas na partida: '))

for i in range(bombas):
    l, c = map(int, input('Digite a linha e coluna da bomba: ').split())
    tabela[l][c] = 10

for i in range(4):
    for j in range(6):
        if tabela[i][j] >= 10:
            if j == 0: 
                tabela[l][c+1] += 1
            elif j == 5:
                tabela[l][c-1] += 1
            else:
                tabela[l][c+1] += 1
                tabela[l][c-1] += 1

for i in tabela:
    print(i)
