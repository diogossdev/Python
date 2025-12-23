# Custo da viagem

numero = int(input('Digite a distância da viagem em km: '))
if numero <= 200:
    valor = numero*0.5
    print(f'O valor a ser pago da viagem será de {valor:.2f} reais!')
else:
    valor = numero*0.45
    print(f'O valor a ser pago da viagem será de {valor:.2f} reais!')