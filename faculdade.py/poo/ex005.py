class Data:
  def __init__(self, dia, mes, ano):
    self._dia = dia
    self._mes = mes
    self._ano = ano

  def __str__(self):
    if self._dia < 10 and self._mes < 10:
      return f"0{self._dia}/0{self._mes}/{self._ano}"
    elif self._dia < 10:
      return f"0{self._dia}/{self._mes}/{self._ano}"
    elif self._mes < 10:
      return f"{self._dia}/0{self._mes}/{self._ano}"
    else:
      return f"{self._dia}/{self._mes}/{self._ano}"

  @property
  def dia(self):
    return self._dia

  @property
  def mes(self):
    return self._mes

  @property
  def ano(self):
    return self._ano

  @dia.setter
  def dia(self, novo_dia):
    self._dia = novo_dia

  @mes.setter
  def mes(self, novo_mes):
    self._mes = novo_mes

  @ano.setter
  def ano(self, novo_ano):
    self._ano = novo_ano

#PP
data = Data(8, 12, 2005)
print(data)

