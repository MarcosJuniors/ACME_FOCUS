with open("employee_satisfaction_survey.csv", "r", encoding="utf-8")as arquivo:
     dados = arquivo.read()

lista = dados.splitlines()

#planilha = dados.splitlines() O splitlines converte string para lista, quando utilizo o len(planilha) ele faz a contagem da quantidade de linhas da planilha que no caso é 901
#planilha = dados.split(",") o split serve para separar elementos de uma linha, ele divide a linha em pedaços e transforma em novos elementos
total = 0
quantidade = 0
for linhas in lista[1:]:
    coluna = linhas.split(",")
    notas = int(coluna[2])
    total = total + notas
    quantidade = quantidade + 1

print(f'A Quantidade de notas processadas : {quantidade} linhas')
print("O Total das notas calculadas é: ", total)
     


#print(int(coluna[2])) transforma string da planilha em numero inteiro
print("Cabeçalho:", lista[0])
print(coluna)
print(f'O Número de elementos da lista da planilha Acme Corp foi de: {len(lista)} linhas')
print(f'O Número de colunas da planilha do cabeçalho, timestamp, email e satisfaction foi: {len(coluna)} colunas')
#print(len(linhas[-1]))
#print(len(linhas))
#print(f'Planilha completa: {len(planilha)}') 
#print(len(planilha))