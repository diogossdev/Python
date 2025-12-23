from random import randint
n = randint(0, 5)
print(n)

print('Olá! Sou um computador criado pelo Didi e pensei num número aleatório entre 0 e 5! Você consegue adivinhar qual seria? Tente!')

tentativa = int(input('Digite seu número: '))
if tentativa == n:
    print(f'Eu pensei em {n}... você conseguiu! Parabéns!')
else:
    print(f'Eu pensei em {n}... Quem sabe na próxima?')

