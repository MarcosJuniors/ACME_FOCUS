
with open("employee_satisfaction_survey.csv", "r", encoding="utf-8") as arquivo:
    dados = arquivo.read()

lista = dados.splitlines()

respostas = {}

# Guardar somente a resposta mais recente de cada funcionário
for linha in lista[1:]:
    coluna = linha.split(",")

    data = coluna[0].strip()
    email = coluna[1].strip().lower()
    nota = int(coluna[2].strip())

    if email not in respostas:
        respostas[email] = [data, nota]
    elif data > respostas[email][0]:
        respostas[email] = [data, nota]

# Calcular os resultados usando somente as respostas mais recentes
total = 0
quantidade = 0

quantidade_1 = 0
quantidade_2 = 0
quantidade_3 = 0
quantidade_4 = 0
quantidade_5 = 0

for resposta in respostas.values():
    nota = resposta[1]

    total += nota
    quantidade += 1

    if nota == 1:
        quantidade_1 += 1
    elif nota == 2:
        quantidade_2 += 1
    elif nota == 3:
        quantidade_3 += 1
    elif nota == 4:
        quantidade_4 += 1
    elif nota == 5:
        quantidade_5 += 1

if quantidade > 0:
    media = total / quantidade

    porcentagem_1 = quantidade_1 / quantidade * 100
    porcentagem_2 = quantidade_2 / quantidade * 100
    porcentagem_3 = quantidade_3 / quantidade * 100
    porcentagem_4 = quantidade_4 / quantidade * 100
    porcentagem_5 = quantidade_5 / quantidade * 100

    print("\n===== RELATÓRIO DE SATISFAÇÃO =====")
    print(f"Funcionários analisados: {quantidade}")
    print(f"Soma das notas: {total}")
    print(f"Média geral: {media:.2f}")

    print("\n===== DISTRIBUIÇÃO DAS NOTAS =====")
    print(f"Nota 1: {quantidade_1} ({porcentagem_1:.1f}%)")
    print(f"Nota 2: {quantidade_2} ({porcentagem_2:.1f}%)")
    print(f"Nota 3: {quantidade_3} ({porcentagem_3:.1f}%)")
    print(f"Nota 4: {quantidade_4} ({porcentagem_4:.1f}%)")
    print(f"Nota 5: {quantidade_5} ({porcentagem_5:.1f}%)")

    print("\n===== GRÁFICO DE SATISFAÇÃO =====")
    print("Cada * representa uma resposta")

    print(f"Nota 1: {'*' * quantidade_1}")
    print(f"Nota 2: {'*' * quantidade_2}")
    print(f"Nota 3: {'*' * quantidade_3}")
    print(f"Nota 4: {'*' * quantidade_4}")
    print(f"Nota 5: {'*' * quantidade_5}")

else:
    print("Nenhuma resposta encontrada.")
