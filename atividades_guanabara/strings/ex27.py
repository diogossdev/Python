#Primeiro e último nome de uma pessoa

nome = input('Digite seu nome completo: ')
nome = nome.strip().title().split()

print(f'Seu primeiro nome é {nome[0]} e seu último nome é {nome[-1]}.')