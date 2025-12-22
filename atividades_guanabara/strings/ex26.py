#Primeira e última ocorrência de uma string

nome = input('Digite uma frase: ')
nome = nome.strip().capitalize().upper()

print(f'A letra "a" aparece {nome.count('A')} vezes na sua frase.')

print(f'O primeiro "a" aparece na posição {nome.find('A') + 1}')

print(f'O último "a" aparece na posição {nome.rfind('A') + 1}')