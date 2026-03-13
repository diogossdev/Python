# O Carro e a Bomba de Combustível

class Carro:
    def __init__(self, modelo, tanque_atual=0, capacidade_maxima=50):
        self._modelo = modelo
        self._tanque = tanque_atual
        self._capacidade = capacidade_maxima

    def __str__(self):
        return f"O modelo do seu carro é {self._modelo} com tanque atual de {self._tanque} litros e capacidade máxima de {self._capacidade} litros."

    @property
    def tanque(self):
        return self._tanque
    
    def encher_tanque(self, litros):
        if litros + self._tanque > self._capacidade:
            self._tanque = self._capacidade
            return f"Quantidade maior do que a capacidade do tanque. Tanque preenchido com {self.tanque} litros."
        else:
            self._tanque += litros
            return f"Pronto! Agora seu tanque possui {self.tanque} litros de armazenamento!"


class BombaCombustivel:
    def __init__(self):
        pass
    
    def abastecer_veiculo(self, carro, quantidade):
        return carro.encher_tanque(quantidade)

# Programa Principal
carrinho = Carro('Tukson', 20)
print(carrinho)

posto_gasolina = BombaCombustivel()
mensagem_posto = posto_gasolina.abastecer_veiculo(carrinho, 12)
print(mensagem_posto)
