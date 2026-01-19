lista = []

while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não irei adicionar.')
    resposta = input('Deseja continuar? [S/N] ')
    if resposta in 'Nn':
        break

valor_ordenado = sorted(lista)
print(f'Sua lista na ordem é {valor_ordenado}')
