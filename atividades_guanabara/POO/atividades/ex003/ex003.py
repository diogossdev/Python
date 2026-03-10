class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos.
    """
    def __init__(self, id=123456, titular='', saldo=0):
        self.id = id
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        return f'A conta {self.id} do(a) cliente {self.titular} possui {self.saldo:.2f} reais de saldo.'

    def saque(self, saque:float):
        if self.saldo - saque < 0:
            print('Saque inválido.')
        else:
            self.saldo -= saque
            print(f'Saque de R${saque} realizado com sucesso!')

    def deposito(self, deposito:float):
        self.saldo += deposito
        print(f'Depósito de R${deposito} realizado com sucesso!')

## Programa Principal

#Conta do Diogo
diogo = ContaBancaria(132452, 'Diogo', 1000)
print(diogo)
saque = float(input(f'Digite o valor do saque para {diogo.titular}: '))
diogo.saque(saque)
print(f'{diogo.titular} agora possui {diogo.saldo} reais de saldo.')

#Conta da Vivi
vivi = ContaBancaria(456321, 'Victória', 2000)
print(vivi)
deposito = float(input(f'Digite o valor do depósito para {vivi.titular}: '))
vivi.deposito(deposito)
print(f'{vivi.titular} agora possui {vivi.saldo} reais de saldo.')


        