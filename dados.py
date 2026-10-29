
with open("employee_satisfaction_survey.csv", "r", encoding="utf-8") as arquivo:
    dados = arquivo.read()

lista = dados.splitlines()

total = 0
quantidade = 0
quantidade_1 = 0
quantidade_2 = 0
quantidade_3 = 0
quantidade_4 = 0
quantidade_5 = 0

respostas = {}

for linhas in lista[1:]:
    coluna = linhas.split(",")

    data = coluna[0].strip()
    email = coluna[1].strip()
    notas = int(coluna[2])

    if email not in respostas:
        respostas[email] = [data, notas]
    elif data > respostas[email][0]:
        respostas[email] = [data, notas]

# Contar somente as respostas mais recentes
for resposta in respostas.values():
    notas = resposta[1]

    total += notas
    quantidade += 1

    if notas == 1:
        quantidade_1 += 1
    if notas == 2:
        quantidade_2 += 1
    if notas == 3:
        quantidade_3 += 1
    if notas == 4:
        quantidade_4 += 1
    if notas == 5:
        quantidade_5 += 1

if quantidade > 0:
    porcentagem_1 = quantidade_1 / quantidade * 100
    porcentagem_2 = quantidade_2 / quantidade * 100
    porcentagem_3 = quantidade_3 / quantidade * 100
    porcentagem_4 = quantidade_4 / quantidade * 100
    porcentagem_5 = quantidade_5 / quantidade * 100

    media = total / quantidade

    print(f"A média geral das notas foi: {media:.2f}")
    print(f"A porcentagem das notas 1 foi: {porcentagem_1:.0f}%")
    print(f"A porcentagem das notas 2 foi: {porcentagem_2:.0f}%")
    print(f"A porcentagem das notas 3 foi: {porcentagem_3:.0f}%")
    print(f"A porcentagem das notas 4 foi: {porcentagem_4:.0f}%")
    print(f"A porcentagem das notas 5 foi: {porcentagem_5:.0f}%")
    print(f"Quantidade de notas 1: {quantidade_1}")
    print(f"Quantidade de notas 2: {quantidade_2}")
    print(f"Quantidade de notas 3: {quantidade_3}")
    print(f"Quantidade de notas 4: {quantidade_4}")
    print(f"Quantidade de notas 5: {quantidade_5}")
    print(f"Quantidade de funcionários: {quantidade}")
    print(f"Soma das notas: {total}")
else:
    print("Nenhuma resposta encontrada.")
