infos = {}

infos['nome'] = input('Digite o nome do aluno: ')
infos['média'] = float(input('Digite a média do aluno: '))

if infos['média'] >= 7.0:
    infos['situação'] = 'Aprovado'
else:
    infos['situação'] = 'Reprovado'

for k, v in infos.items():
    print(f'{k} = {v}')