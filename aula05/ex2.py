notas = ["","","","",""]
soma = 0
cont = 0
for x in range(5):
    notas[x] = float(input("digite a nota:"))
for z in range(5):
    soma += notas[z]
media = soma/5
for y in range(5):
    if notas[y] >= media:
        cont = cont + 1
print("media da sala:", media,"alunos aprovados:", cont)