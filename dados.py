with open("employee_satisfaction_survey.csv", "r", encoding="utf-8")as arquivo:
     dados = arquivo.read()

lista = dados.splitlines()

#planilha = dados.splitlines() O splitlines converte string para lista, quando utilizo o len(planilha) ele faz a contagem da quantidade de linhas da planilha que no caso é 901
#planilha = dados.split(",") o split serve para separar elementos de uma linha, ele divide a linha em pedaços e transforma em novos elementos
total = 0
quantidade = 0
quantidade_1 = 0
quantidade_2 = 0
quantidade_3 = 0
quantidade_4 = 0
quantidade_5 = 0
for linhas in lista[1:]:
    coluna = linhas.split(",")
    notas = int(coluna[2])
    total = total + notas
    quantidade = quantidade + 1

    if notas ==1:
         quantidade_1+=1
    if notas ==2:
         quantidade_2+=1
    if notas ==3:
         quantidade_3+=1
    if notas ==4:
        quantidade_4+=1
    if notas ==5:
         quantidade_5+=1

porcentagem_1 = quantidade_1/quantidade * 100
porcentagem_2 = quantidade_2/quantidade * 100
porcentagem_3 = quantidade_3/quantidade * 100
porcentagem_4 = quantidade_4/quantidade * 100
porcentagem_5 = quantidade_5/quantidade * 100
media = total/quantidade
media_1 = total/quantidade_1
media_2 = total/quantidade_2
media_3 = total/quantidade_3
media_4 = total/quantidade_4
media_5 = total/quantidade_5

print(f'A média geral das notas foi: {media}')
print(f'A média das notas 1 foi: {media_1:.2f}')
print(f'A média das notas 2 foi: {media_2:.2f}')
print(f'A média das notas 3 foi: {media_3:.2f}')
print(f'A média das notas 4 foi: {media_4:.2f}')
print(f'A média das notas 5 foi: {media_5:.2f}')
print(f'A Porcentagem das notas foi: {porcentagem_1:.0f}%')
print(f'A Porcentagem das notas foi: {porcentagem_2:.0f}%')
print(f'A Porcentagem das notas foi: {porcentagem_3:.0f}%')
print(f'A Porcentagem das notas foi: {porcentagem_4:.0f}%')
print(f'A Porcentagem das notas foi: {porcentagem_5:.0f}%')
print(f"Quantidade de notas 1: {quantidade_1}")
print(f"Quantidade de notas 2: {quantidade_2}")
print(f"Quantidade de notas 3: {quantidade_3}")
print(f"Quantidade de notas 4: {quantidade_4}")
print(f"Quantidade de notas 5: {quantidade_5}")
print(f"Quantidade de respostas: {quantidade}")
print(f"Soma das notas: {total}")
#print(len(linhas[-1]))
#print(len(linhas))
#print(f'Planilha completa: {len(planilha)}') 
#print(len(planilha))

