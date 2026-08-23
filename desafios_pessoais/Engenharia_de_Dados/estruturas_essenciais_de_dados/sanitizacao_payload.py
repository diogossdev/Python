#função que purifica os dados
def limpar_payload_usuarios(dados:list) -> list:
    payload_limpo = []
    incremento = 0

    for i in range(len(dados)):
        verificador = 0

        if dados[i].get("email") is None: #verificando se existe o campo "email"
            verificador = 1
        elif "@" not in dados[i]["email"]: #verificando se o campo "email" possui @
            verificador = 1

        try: #verificando se o valor pode ser convertido para inteiro
            eh_inteiro = int(dados[i]["idade"])
        except ValueError:
            verificador = 1

        if verificador == 0:
            payload_limpo.append({})

            payload_limpo[incremento]["nome"] = dados[i].get("nome").strip().title()
            payload_limpo[incremento]["email"] = dados[i].get("email")
            payload_limpo[incremento]["idade"] = dados[i].get("idade")

            incremento += 1

    return payload_limpo
    
def main():
    # Dados de entrada para o seu teste:
    payload_bruto = [
        {"nome": "CARLOS SILVA", "email": "carlos@email.com", "idade": "28"},
        {"nome": "ana beatriz", "email": "ana.email.com", "idade": "25"},      # email inválido
        {"nome": "MARCOS SOUZA", "idade": "30"},                              # sem email
        {"nome": "Bia mendes", "email": "bia@email.com", "idade": "trinta"},   # idade inválida
        {"nome": "  joão pedro  ", "email": "joao@email.com", "idade": "42"}  # nome com espaços
    ]

    payload_limpo = limpar_payload_usuarios(payload_bruto)
    print(payload_limpo)

if __name__ == "__main__":
    main()