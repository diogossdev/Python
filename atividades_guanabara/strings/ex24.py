lugar = input('Digite o lugar que você nasceu: ')
print('Verificando se começa com Santo...')

lugar = lugar.strip().title()
print("Santo " in lugar[0:6])