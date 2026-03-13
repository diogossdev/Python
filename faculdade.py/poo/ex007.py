class AfricaSul:
  def __init__(self, nome:str, capital:str, dimensao:int):
    self._nome = nome
    self._capital = capital
    self._dimensao = dimensao
    self._fronteira = []

  def __str__(self):
    return f"O país se chama {self.nome} com capital {self.capital}, {self.dimensao}km² de dimensão e possui {self.fronteira} como países que fazem fronteira."

  @property
  def nome(self):
    return self._nome

  @property
  def capital(self):
    return self._capital

  @property
  def dimensao(self):
    return self._dimensao

  @property
  def fronteira(self):
    return self._fronteira

  def adicionar_pais(self, pais):
    if pais not in self._fronteira:
      self._fronteira.append(pais)
      return "País adicionado!"
    else:
      return f"{pais} já está adicionado na lista de países que fazem fronteira."

#PP
africa_sul = AfricaSul('África do Sul', 'Pretória', 1220000)
print(africa_sul.adicionar_pais('Lesoto'))
print(africa_sul.adicionar_pais('Botsuana'))
print(africa_sul.adicionar_pais('Namíbia'))
print(africa_sul.adicionar_pais('Namíbia'))
print(africa_sul)