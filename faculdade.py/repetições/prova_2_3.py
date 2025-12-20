while True:
    numero = int(input('Digite um valor: '))
    if numero % 2 == 0 and numero != 0:
        for i in range (1, 11):
            print(f'{numero} x {i} = {numero*i}')
    elif numero % 2 != 0:
        if numero > 0:
            for j in range(1, numero + 1):
                print(j)
        else:
            for k in range(numero, 2):
                print(k)
    else:
        break

print('Fim do programa!')
    
