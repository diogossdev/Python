def quantidade_cupons(valor_compra:float) -> int:
    cupons = valor_compra // 50
    return cupons

#programa principal

beneficiados = 0
quantos_faltou = 0
cupons = 0
cupons_totais = 0
um = 0

while True:
    valor_compra = float(input('Digite o valor da compra: '))
    cupons = quantidade_cupons(valor_compra)
    if cupons_totais + cupons <= 100:
        cupons_totais += cupons
        if cupons > 0:
            beneficiados += 1
        print(f'O cliente receberá {cupons} cupons!')
    else:
        while True:
            if cupons_totais + 1 <= 100 and valor_compra >= 50:
                valor_compra = valor_compra - 50
                cupons_totais = cupons_totais + 1
                cupons = cupons - 1
                if um == 0:
                    um += 1
                    beneficiados += 1
            else:
                quantos_faltou += cupons
                break
print(f'Tivemos {beneficiados} pessoas beneficiadas')
if quantos_faltou > 0:
    print(f'Ficou devendo {quantos_faltou} cupons para o último cliente.')
