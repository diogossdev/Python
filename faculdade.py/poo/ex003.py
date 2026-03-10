class Jogador:
    """
    Essa classe define um jogador com atributos de nome e vida. A vida máxima do jogador é 100 e ele pode se curar usando um relacionamento de objetos com a classe Pocao.
    """
    def __init__(self, nome='', vida=100):
        self._nome = nome
        self._vida = vida

    def __str__(self):
        return f'O jogador {self._nome} possui {self._vida} de vida.'
    
    def receber_cura(self, valor:int):
        if self._vida + valor >= 100:
            self._vida = 100
        else:
            self._vida += valor

    def usar_pocao(self, pocao):
        #self = objeto do jogador
        #pocao = objeto da pocao
        self.receber_cura(pocao._curador)
        
    #Métodos Acessadores
    @property
    def nome(self):
        return self._nome
    @property
    def vida(self):
        return self._vida
    
    #Métodos Alteradores
    @vida.setter
    def vida(self, vida:int):
        if vida <= 0 or vida > 100:
            raise ValueError
        else:
            self._vida = vida

    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    
class Pocao:
    """
    É a classe que permite ao jogador fazer uma cura de acordo com o valor da poção estabelecida por ele.
    """
    def __init__(self, cura=1):
        self._curador = cura
    
    def __str__(self):
        return f'A poção cura {self._curador} de vida'
    
    #Método Acessador
    @property
    def poder_cura(self):
        return self._curador

    #Método Alterador
    @poder_cura.setter
    def poder_cura(self, pocao:int):
        if pocao <= 0:
            raise ValueError
        else:
            self._curador = pocao

#Programa Principal

jogador = Jogador()
pocao = Pocao()

print('Olá, vamos simular um RPG juntos!')
nome_jogador = input('Primeiramente, digite o nome do seu jogador: ')
jogador.nome = nome_jogador
print()
print(f'Perfeito! o nome do seu jogador é {jogador.nome}.')

while True:
    vida_jogador = int(input('Digite a vida do seu jogador (1 a 100): '))

    try:
        jogador.vida = vida_jogador
        print('Vida de jogador concluída. Você está indo muito bem!')
        break

    except ValueError:
        print('Erro na vida do jogador. Só pode de 1 a 100')

print()
print('Agora iremos curar o jogador!')

while True:
    cura = int(input('Digite o valor da poção (maior que 0): '))

    try:
        pocao.poder_cura = cura
        print('Poção atualizada com sucesso!')
        break

    except ValueError:
        print('Erro no valor da poção --- somente válido será a cura maior que 0.')

print()
print(f'Perfeito, jogador(a) {jogador.nome}! Agora vamos ver a situação do seu player!')
print(f'Atualmente ele possui {jogador.vida} de vida, mas com a magia de cura da poção...')

jogador.usar_pocao(pocao)
print(f'Agora ele possui {jogador.vida} pontos de vida!!')
