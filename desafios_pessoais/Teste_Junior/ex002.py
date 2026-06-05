#Desafio 2

"""
Objetivo: Criar uma função chamada Contador_palavras que receba um texto longo. Ela deve remover pontuações básicas (., ,, !), transformar tudo para letras minúsculas e retornar um dicionário com a frequência de cada palavra.

Exemplo de entrada: "Python é vida, Python é muito bom!"

Exemplo de saída: {"python": 2, "é": 2, "vida": 1, "muito": 1, "bom": 1}
"""

def contador_palavras(texto):
    dicionario = {}
    pontuacoes = ",.?!"

    lista_palavras = texto.lower().split()
    for i in range(len(lista_palavras)):
        palavra_limpa = lista_palavras[i].strip(pontuacoes)

        dicionario[palavra_limpa] = dicionario.get(palavra_limpa, 0) + 1

    return dicionario

def main():
    texto = "Python é vida,   Python é    muito bom!!!!"
    print(contador_palavras(texto))

if __name__ == "__main__":
    main()
