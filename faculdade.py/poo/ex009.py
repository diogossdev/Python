#Classe do Professor
class Professor:
    def __init__(self, nome:str, disciplina:str):
        self.nome = nome
        self.disciplina = disciplina

    def avaliar_aluno(self, aluno:object, nota:float):
        if aluno.adicionar_nota(nota):
            return f"Nota {nota} adicionada com sucesso!"
        else:
            return f"Nota {nota} não pôde ser adicionada --- VALOR INVÁLIDO ---"
#Classe do Aluno
class Aluno:
    def __init__(self, nome:str):
        self.nome = nome
        self._notas = []

    @property
    def notas(self):
        return tuple(self._notas)

    @property
    def media(self):
        contador = 0
        for i in self.notas:
            contador += i
        if not self.notas: #Isso significa: Se a lista estiver vazia...
            return '0.00'
        return f'{contador/len(self.notas):.2f}'

    def adicionar_nota(self, valor:float):
        if valor >= 0 and valor <=10:
            self._notas.append(valor)
            return True
        else:
            return False
        

# Programa Principal
aluno = Aluno('Diogo')
professor = Professor('Thiago', 'AED')
print(professor.avaliar_aluno(aluno, 12))
print(professor.avaliar_aluno(aluno, 8.0))
print(professor.avaliar_aluno(aluno, 9.0))
print(professor.avaliar_aluno(aluno, 10.0))
print(f'A média do aluno, dada as notas válidas, será {aluno.media}.')