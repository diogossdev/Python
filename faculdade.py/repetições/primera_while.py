x = int(input('Digite o número do ínicio da contagem: '))
y = int(input('Digite o número do fim da contagem: '))
if x < y:
    while x <= y:
        print(x)
        x += 1
elif x > y:
    while x >= y:
        print(x)
        x -= 1
else:
    print(x)
        
print('Fim da contagem!')




