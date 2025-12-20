empresas = []

for i in range(20):
    nome = input("Digite o nome da empresa: ")
    empresas.append([nome])  

for i in range(100):
    voto = input("Digite o nome da empresa votada: ")
    for j in range(20):
        if voto == empresas[j][0]:
            empresas[j].append(1)   

maior = 1
for grupo in empresas:
    votos = len(grupo) - 1
    if votos > maior:
        maior = votos

vencedoras = []
for grupo in empresas:
    if len(grupo) - 1 == maior:
        vencedoras.append(grupo[0]) 

print("Empresa(s) vencedora(s):")
for v in vencedoras:
    print(v)
