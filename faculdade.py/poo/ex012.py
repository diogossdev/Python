#Testando criar função com raise
def teste_problema(numero:int):
    if numero == 0:
        raise ZeroDivisionError
    
try:
    numero1 = int(input('Digite um número: '))
    numero2 = int(input('Digite outro número: '))
    teste = teste_problema(numero2)
    print('concluído!')
except:
    print('Deu ruim')