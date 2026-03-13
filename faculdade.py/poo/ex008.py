class Conta_Corrente:
  def __init__(self, numero:int, saldo:float, nome_titular:str):
    self._numero = numero
    self._saldo = saldo
    self._nome = nome_titular

  def depositar(self, valor:float):
    self._saldo += valor
  def sacar(self, valor:float):
    if self._saldo - valor < 0:
      return False
    else:
      self._saldo -= valor
      return True

  @property
  def saldo(self):
    return self._saldo

  @property
  def numero(self):
    return self._numero

  @property
  def nome(self):
    return self._nome

class Banco:
  def __init__(self, lista_contas):
    self._contas = lista_contas

  @property
  def contas(self):
    return self._contas
  
  def transferir(self, conta_transferidora, num_conta, valor_transferencia):
    user_transferencia = ''
    for i in self._contas:
      if i.numero == num_conta:
        user_transferencia = i
        if conta_transferidora.saldo - valor_transferencia >= 0:
          conta_transferidora.sacar(valor_transferencia)
          user_transferencia.depositar(valor_transferencia)
          return True
        else:
          return False
    return f"ERRO --- Número de conta não encontrada --- "

  def somar_saldos(self):
    saldo_total = 0
    for i in self._contas:
      saldo_total += i.saldo
    return saldo_total


  def adicionar_conta(self, nova_conta):
    for i in self._contas:
      if nova_conta.numero == i.numero:
        return "Não foi possível criar a conta --- Número de banco já usado --- "
      else:
        self._contas.append(nova_conta)
        return f"Conta do usuário(a) {nova_conta.nome} criado com sucesso!"
    

  def remove_conta(self, excluir_numero):
    for i in self._contas:
      if i.numero == excluir_numero:
        self._contas.remove(i)
        return f"Conta removida com sucesso!"
    return "ERRO --- Número de conta não encontrado --- "
    

#Programa Principal
lemuel = Conta_Corrente(123, 2000, 'Lemuel')
diogo = Conta_Corrente(234, 3000, 'Diogo')
ryan = Conta_Corrente(567, 9000, 'Ryan')
renam = Conta_Corrente(890, 10000, 'Renam')
matheus = Conta_Corrente(103, 1, 'Matheus')
listona = [lemuel, diogo, ryan, renam, matheus]

banco = Banco(listona)

number_user = int(input('Digite o número do seu banco: '))
user = ''
for i in listona:
  if i.numero == number_user:
    user = i
print(f'Bem-vindo, usuário(a) {user.nome}!')
while True:
  acao = int(input('''Digite o que você quer fazer:
  1- depositar dinheiro;
  2- sacar dinheiro;
  3- verificar o saldo atualizado do seu banco;
  4- transferir dinheiro para outra conta;
  5- verificar a soma de todos os saldos;
  6- criar nova conta;
  7- excluir conta;
  8- sair.
  '''))
  if acao == 1:
    valor_deposito = float(input('Digite o valor do seu depósito: '))
    user.depositar(valor_deposito)
    print(f"Saldo atualizado! Agora você possui {user.saldo:.2f}R$ de saldo no banco.")

  elif acao == 2:
    valor_saque = float(input('Digite o valor do seu saque: '))
    possibilidade = user.sacar(valor_saque)
    if possibilidade == True:
      print(f'Saque realizado com sucesso! Agora você possui {user.saldo:.2f}R$ de saldo no banco.')
    else:
      print('Saque não concluído --- SALDO INSUFICIENTE ---')

  elif acao == 3:
    print(f"O saldo atual do seu banco é de {user.saldo:.2f}R$.")

  elif acao == 4:
    conta_transferencia = int(input('Digite o valor do número da conta do usuário: '))
    if conta_transferencia == user.numero:
      print('INVÁLIDO --- Não pode selecionar sua própria conta --- ')
    else:
      valor_transferencia = float(input('Digite o valor da transferência: '))
      transferir = banco.transferir(user, conta_transferencia, valor_transferencia)
      if transferir == True:
        print(f'Transferência concluída! Agora você possui {user.saldo:.2f}R$ de saldo no banco.')
      elif transferir == False:
        print('Transferência não concluída --- SALDO INSUFICIENTE ---')
      else:
        print(transferir)

  elif acao == 5:
    print(f"A soma de todos os saldos é de {banco.somar_saldos()}R$.")

  elif acao == 6:
    nome_user = input('Digite o nome da conta do novo usuário: ')
    numero_user = int(input('Digite o número do banco do seu usuário: '))
    novo_usuario = Conta_Corrente(numero_user, 0, nome_user)
    print(banco.adicionar_conta(novo_usuario))

  elif acao == 7:
    excluir_numero = int(input('Digite o número do banco do usuário: '))
    print(banco.remove_conta(excluir_numero))

  elif acao == 8:
    print('Finalizando suas ações...')
    break
  else:
    print('Ação desconhecida. Tente novamente.')
