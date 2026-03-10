#Declaração de Classes
class MinhaClasse:
    """
    Essa classe é um teste usado pelo programador Diogo para estudar POO e seus fundamentos!
    
    Para usar essa classe, basta criar uma variável (que será uma pessoa) passando nome e idade da seguinte forma:

    variavel = MinhaClasse(nome, idade)
    """
    def __init__(self, nome = 'vazio', idade = 0): #Método Construtor
        #Atributos de Instância
        self.idade = idade
        self.nome = nome

    def __getstate__(self):
        return f'Estado: nome = {self.nome} // idade = {self.idade}'

    #Método String
    def __str__(self): #Dunder Method
        return f"O(A) {self.nome} tem {self.idade} anos."

    #Métodos de Instância
    def aniversario(self):
        self.idade += 1

#Declaração de Objetos

eu = MinhaClasse('Diogo', 20)

eu.aniversario()
    
print(eu)

vivi = MinhaClasse('Victória', 19)

vivi.aniversario()
print(vivi)

teste = MinhaClasse()
print(teste)

#Documentação da Classe
print(vivi.__doc__) #Dunder Attribute

print(eu.__getstate__()) # Dunder Method