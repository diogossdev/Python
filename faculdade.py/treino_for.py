preco = 0
compra_total = 0
qnt_produtos = 0
maior_preco = 0

# Programa Principal
while True:
    preco = float(input('Digite o preço do produto: '))
    compra_total += preco
    qnt_produtos += 1

    if preco > maior_preco:
        maior_preco = preco

    continuar = input('Você deseja continuar? Digite "S" ou "N": ')
    if continuar == 'N':
        break

print(f'O total gasto na compra foi {compra_total} reais.')
print(f'O número de produtos cadastrados foi {qnt_produtos}.')
print(f'O preço do produto mais caro foi {maior_preco} reais.')
