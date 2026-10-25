with open("employee_satisfaction_survey.csv", "r", encoding="utf-8")as arquivo:
     dados = arquivo.read()

lista = dados.splitlines()
linha = lista[1]
coluna = linha.split(",")

print(int(coluna[2]))
print("Cabeçalho:", lista[0])
print(coluna)
print(f'O Número de elementos da lista da planilha Acme Corp foi de: {len(lista)} linhas')
print(f'O Número de colunas da planilha do cabeçalho, timestamp, email e satisfaction foi: {len(coluna)} colunas')