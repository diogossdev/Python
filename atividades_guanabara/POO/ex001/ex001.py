#Declaração de Classes
class MinhaClasse:
    def __init__(self): #Método Construtor
        #Atributos de Instância
        self.idade = 0
        self.nome = ''

    #Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} tem {self.idade} anos e está estudando POO!"


#Declaração de Objetos

eu = MinhaClasse()
eu.idade = 20
eu.nome = 'Diogo'

resposta = input('Você fez aniversário? (S/N) ')
if resposta == 'S':
    eu.aniversario()
    
print(eu.mensagem())

vivi = MinhaClasse()
vivi.idade = 19
vivi.nome = 'Victória'

vivi.aniversario()
print(vivi.mensagem())