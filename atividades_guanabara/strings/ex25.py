#Verificar se tem "Silva" no nome

nome = input('Digite seu nome: ')
nome = nome.strip().title().split()
print('Verificando se teu nome tem "Silva"...')
print("Silva" in nome)