# Desigualdade Triangular / Analisando Triângulo v1.0

l1 = float(input('Digite o primeiro lado: '))
l2 = float(input('Digite o terceiro lado: '))
l3 = float(input('Digite o segundo lado: '))

if l1 < l2 + l3 and l2 < l1 + l2 and l3 < l1 + l2:
    print('Esses lados podem formar um triângulo!')
else:
    print('Esses lados não formam um triângulo.')