# Aumentos Múltiplos

salario = float(input('Digite seu salário: '))
if salario <= 1250.00:
    salario = (salario * 15 / 100) + salario
    print(f'O seu novo salário será {salario:.2f} reais.')
else:
    salario = (salario * 10 / 100) + salario
    print(f'O seu novo salário será {salario:.2f} reais.')