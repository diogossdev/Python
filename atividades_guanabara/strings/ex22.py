#Analisador de Textos

nome = input("Digite seu nome completo: ")
nome = nome.strip()
print(f'Seu nome com todas as letras maiúsculas é: {nome.upper()}')

print(f'Seu nome com todas as letras minúsculas é: {nome.lower()}')

comprimento = len(nome)
espaco = nome.count(' ')

print(f'Seu nome tem {comprimento - espaco} letras.')

nome_list = nome.split()
print(f'Seu primeiro nome é {nome_list[0]} e tem {len(nome_list[0])} letras')