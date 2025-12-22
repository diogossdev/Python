#Separador de Dígitos de 0 a 9999

num = int(input('Digite um número de 0 a 9999: '))

if num >= 0 and num < 10:
    num = str(num)
    print(f'unidade: {num[0]}')
elif num >= 10 and num < 100:
    num = str(num)
    print(f'unidade: {num[1]}')
    print(f'dezena: {num[0]}')
elif num >= 100 and num < 1000:
    num = str(num)
    print(f'unidade: {num[2]}')
    print(f'dezena: {num[1]}')
    print(f'centena: {num[0]}')
elif num >= 1000 and num < 10000:
    num = str(num)  
    print(f'unidade: {num[3]}')
    print(f'dezena: {num[2]}')
    print(f'centena: {num[1]}')
    print(f'milhar: {num[0]}')
else:
    print('Valor Inválido.')