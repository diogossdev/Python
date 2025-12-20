total = 0
sapos = 0
coelhos = 0
ratos = 0

testes = int(input('Digite quantas vezes o lab foi usado: '))

for i in range(1, testes + 1):
    quantia = int(input('Quantas cobaias foram usadas? '))
    nome = input('Qual era o tipo de cobaia? ')
    total += quantia

    if nome == 'S':
        sapos += quantia
    elif nome == 'R':
        ratos += quantia
    elif nome == 'C':
        coelhos += quantia
        
print(f'Total: {total}')
print(f'Total de coelhos: {coelhos}')
print(f'Total de sapos: {ratos}')
print(f'Total de ratos: {sapos}')
print(f'Percentual de coelhos: {coelhos*100/total:.2f}')
print(f'Percentual de ratos: {ratos*100/total:.2f}')
print(f'Percentual de sapos: {sapos*100/total:.2f}')
