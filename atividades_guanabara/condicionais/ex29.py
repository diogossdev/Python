velocidade = int(input('Digite a velocidade do carro: '))
if velocidade <= 80:
    print('Velocidade permitida.')
else:
    multa = (velocidade - 80) * 7
    print(f'Acima da média. Multa de {multa} reais.')