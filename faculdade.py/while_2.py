soma = 0
contagem = 0
while True:
    contagem = int(input('Digite um número para a soma (zero "0" cancela a contagem): '))
    if contagem == 0:
        break
    else:
        soma = contagem + soma
        contagem = 0

print(f'A soma dos valores digitados é {soma}')
    
