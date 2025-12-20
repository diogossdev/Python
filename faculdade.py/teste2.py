num1 = float(input('Digite um número maior que 0: '))
if num1 > 0:
    num2 = float(input('Digite outro número maior que 0: '))
    if num2 > 0:
        print(f'A soma desses valores é {num1 + num2}, a subtração é {num1 - num2}, a multiplicação é {num1 * num2:.2f} e a divisão é {num1 / num2:.2f}.')
    else:
        print('Ocorreu um erro. Tente novamente.')
else:
    print('Ocorreu um erro. Tente novamente.')

