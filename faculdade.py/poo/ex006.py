class Aluno:
  def __init__(self, matricula:int, nome:str, notas:list):
    self._matricula = matricula
    self._nome = nome
    self._notas = notas

  @property
  def nome(self):
    return self._nome

  @property
  def notas(self):
    return self._notas

  @nome.setter
  def nome(self, novo_nome):
    self._nome = novo_nome

  @property
  def matricula(self):
    formatacao = str(self._matricula)
    formatacao1 = formatacao[0:4]
    formatacao2 = formatacao[4:5]
    formatacao3 = formatacao[5:]
    return f"{formatacao1}.{formatacao2}.{formatacao3}"

  def media(self):
    media = 0
    for i in self._notas:
      media += i
    quant_notas = len(self._notas)
    return f"{media/quant_notas:.2f}"

  def adiciona_nota(self, nota):
    self._notas.append(nota)


#PP
aluno = Aluno(1234567, 'Diogo', [10, 10, 10])
print(aluno.matricula)
print(aluno.media())

aluno.nome = 'Lemuel'
print(aluno.nome)

aluno.adiciona_nota(8)
print(aluno.notas)
print(aluno.media())