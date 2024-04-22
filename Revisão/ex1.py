soma = 0
for x in range(1,3):
    nota = float(input(f"Digite a nota {x}:"))
    soma = soma + nota
media = soma/2
if media >=7:
    print(f"Sua nota foi {media}, aprovado")
elif media >=4:
    print(f"Sua nota foi {media}, recuperação")
else:
    print(f"Sua nota foi {media}, reprovado")