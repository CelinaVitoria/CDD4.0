media = 0
soma = 0
for x in range(1,11):
    num = float(input(f"Digite o número {x}:"))
    soma = soma + num
    media = soma / 10
print(media)
