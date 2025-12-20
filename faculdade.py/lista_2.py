numeros = []
while True:
    num = int(input('Digite um valor: '))
    if num == 0:
        break
    else:
        numeros.append(num)

lista_somada = sum(numeros)
lista_ordenada = sorted(numeros)
sem_repeticao = sorted(set(numeros))
    
print(f'A quantidade de valores digitados foi {len(numeros)}')
print(f'Os números digitados em ordem: {lista_ordenada}')
print(f'A soma de todos os valores digitados é {lista_somada}')
print(f'A lista sem repetições de valores é {sem_repeticao}')
print('Fim do programa')
