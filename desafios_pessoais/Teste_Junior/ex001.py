#Desafio 1

"""
Objetivo: Criar uma função chamada analisar_texto que receba uma frase (string) e retorne um dicionário contendo a contagem de: vogais, consoantes e espaços em branco.

Exemplo de entrada: "Python 3"

Exemplo de saída: {"vogais": 1, "consoantes": 5, "espacos": 1} (números e caracteres especiais devem ser ignorados na contagem de vogais/consoantes).
"""

def analisar_texto(frase:str) -> dict:
    dicionario = {"vogais":0, "consoantes":0, "espacos":0}
    vogais = "aeiou"

    for unidade in frase:

        unidade_minuscula = unidade.lower()

        if unidade_minuscula.isalpha():
            if unidade_minuscula in vogais:
                dicionario["vogais"] += 1
            else:
                dicionario["consoantes"] += 1

        elif unidade == " ":
            dicionario["espacos"] += 1

    return dicionario

def main():
    frase = "Eu amo Python3!"
    print(analisar_texto(frase))


if __name__ == "__main__":
    main()