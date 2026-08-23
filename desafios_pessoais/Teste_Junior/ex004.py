class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class Pilha:
    def __init__(self):
        self.no = None
        self.tamanho = 0

    @property
    def no(self):
        return self.no
    @no.setter
    def no(self, novo_no):
        self.no = No(novo_no)

    @property
    def tamanho(self):
        return self.tamanho
    

string = "12345"
print(len(string))
        
