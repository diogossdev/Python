from datetime import date
# Verificar se o ano é bissexto

ano = int(input('Digite o ano e direi se é bissexto (digite 0 se quiser o ano atual): '))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0) :
    print('Esse ano é bissexto!')
else:
    print('Esse ano não é bissexto')