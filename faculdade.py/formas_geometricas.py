def percentual (qnt_questoes:int, qnt_acertos:int) -> float:
    porcentagem = qnt_acertos*100/qnt_questoes
    return porcentagem

def letragem (porcent:float) -> str:
    if (porcent <= 100) and (porcent >= 90):
        letra_A = 'Nota Letra A'
        return letra_A
    elif (porcent < 90) and (porcent >= 80):
        letra_B = 'Nota Letra B'
        return letra_B
    elif (porcent < 80) and (porcent >= 70):
        letra_C = 'Nota Letra C'
        return letra_C
    elif (porcent < 70) and (porcent >= 60):
        letra_D = 'Nota Letra D'
        return letra_D
    elif (porcent < 60):
        letra_E = 'Nota Letra E'
        return letra_E
    else:
        invalido = 'Digite notas válidas'
        return invalido

def conceito (resumo:float) -> str:
    if resumo == 'Nota Letra A':
        return ('Excelente')
    elif resumo == 'Nota Letra B':
        return ('Bom')
    elif resumo == 'Nota Letra C':
        return ('Regular')
    elif resumo == 'Nota Letra D':
        return ('Ruim')
    elif resumo == 'Nota Letra E':
        return ('Reprovado')

#Programa Principal

nome = input('Digite seu nome: ')
quantidade_questoes = int(input('Digite a quantidade de questões: '))
quantidade_acertos = int(input('Digite a quantidade de acertos: '))

porcentagem = percentual(quantidade_questoes,quantidade_acertos)
letra = letragem(porcentagem)
resumo = conceito(letra)

print(f'Porcentagem: {porcentagem:.2f}%')
print(f'Letra de Conceito: {letra}')
print(f'Conceito: {resumo}')
