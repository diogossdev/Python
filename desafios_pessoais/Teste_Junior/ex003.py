#Desafio 3

"""
Desafio 3: Algoritmo Clássico (Estrutura de Dados / Pilha)
Objetivo: Criar uma função chamada validador_parenteses que receba uma string contendo apenas os caracteres de fechamento: (), [] e {}. A função deve retornar True se a ordem dos fechamentos estiver correta e False se estiver incorreta. (Muito comum em entrevistas!).

Exemplo True: "{[()]}" ou "()[]{}"

Exemplo False: "(]" ou "([)]"
"""


def validador_parenteses(string):
    if len(string) % 2 != 0:
        return False
    
    contador = -1
    verificador1 = 0
    verificador2 = 0

    for i in range(len(string) // 2):
        if string[i] != string[contador]:
            verificador1+= 1

        if i % 2 == 0 and string[i] != string[i+1]:
            verificador2 += 1
        
        if verificador1 > 0 and verificador2 > 0:
            return False

        contador = contador - 1

    return True

def main():
    print(validador_parenteses("{[(([]))]})")) #False
    print(validador_parenteses("{{[(]}")) #False
    print(validador_parenteses("{[()]}")) #True
    print(validador_parenteses("{(}))")) #False
    print(validador_parenteses("[(){}]")) #False
    print(validador_parenteses("[]{}()")) #True

if __name__ == "__main__":
    main()