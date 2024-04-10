x = 0
soma = 0
numAlunos = int(input("Número de alunos:"))
while x < numAlunos:
    x = x + 1
    notas = float(input("Digite a nota dos alunos:"))
    soma = soma + notas
media = soma/numAlunos
print(media)