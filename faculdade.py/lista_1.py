numeros = []
valor = int(input('Digite um valor: '))
numeros.append(valor)
maior = numeros[0]
menor = numeros[0]
soma = numeros[0]
for i in range(1, 5):
    valor = int(input('Digite um valor: '))
    numeros.append(valor)
    soma += numeros[i]
    if numeros[i] > maior:
        maior = numeros[i]
    if numeros[i] < menor:
        menor = numeros[i]
    
print(f'A média dos valores é {soma/i}')
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')
