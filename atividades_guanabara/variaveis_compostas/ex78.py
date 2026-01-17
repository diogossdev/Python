numeros = []
maior = 0
menor = 0

for i in range(0, 5):
    num = int(input(f'Digite o número da posição {i}: '))
    numeros.append(num)
    if i == 0:
        maior = menor = numeros[i]
    else:
        if numeros[i] > maior:
            maior = numeros[i]
        if numeros[i] < menor:
            menor = numeros[i]

print(f'Você digitou os valores {numeros}')

for i in range (0, 5):
    if numeros[i] == maior:
        print(f'O maior valor digitado foi {numeros[i]} na posição {i}')
    if numeros[i] == menor:
        print(f'O menor valor digitado foi {numeros[i]} na posição {i}')
