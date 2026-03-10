class Ponto:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def quadrante(self):
    if self.x > 0 and self.y > 0:
      return 'Primeiro Quadrante.'
    elif self.x > 0 and self.y < 0:
      return 'Quarto Quadrante.'
    elif self.x < 0 and self.y < 0:
      return 'Terceiro Quadrante'
    elif self.x < 0 and self.y > 0:
      return 'Segundo Quadrante'
    else:
      return 'Não está em nenhum dos quadrantes'

class Retangulo:
  def __init__(self, base, altura):
    self.base = base
    self.altura = altura
  def calculaArea(self):
    valor = self.base * self.altura
    return valor
  def ehQuadrado(self):
    if self.base == self.altura:
      return True
    else:
      return False

class Aluno:
  def __init__(self, nome, matricula, notas):
    self.matricula = matricula
    self.nome = nome
    self.notas = notas

class ContaCorrente:
  def __init__(self, saldo, num, cpf):
    self.saldo = saldo
    self.num = num
    self.cpf = cpf

# Usando a classe Ponto
ponto1 = Ponto(0, 0)
print(f'Coordenadas do Ponto1: ({ponto1.x},{ponto1.y})  --- situação: {ponto1.quadrante()}')

ponto2 = Ponto(5, 5)
print(f'Coordenadas do Ponto2: ({ponto2.x},{ponto2.y}) --- situação: {ponto2.quadrante()}')

#Usando a classe Retangulo
lado = int(input('Digite o lado: '))
altura = int(input('Digite a altura: '))
quadrado = Retangulo(lado, altura)
if quadrado.ehQuadrado() == True:
  print('É quadrado!')
else:
  print('Não é quadrado!')

area = Retangulo(lado, altura)
print(f'A área desse retângulo é {area.calculaArea()}.')