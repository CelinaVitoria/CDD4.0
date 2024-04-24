eleitores = int(input("digite o número de eleitores:"))
brancos = int(input("digite o número de eleitores que votaram branco:"))
nulos = int(input("digite o número de eleitores que votaram nulo:"))
validos = int(input("digite o número de eleitores com voto válido:"))
while brancos + nulos + validos != eleitores:
    validos = int(input("digite o número de eleitores com voto válido:"))
porcBrancos = (100 * brancos)/eleitores
porcNulos = (100 * nulos)/eleitores
porcValidos = (100 * validos)/eleitores
print(f"Brancos: {porcBrancos}% \n Nulos: {porcNulos}% \n Válidos: {porcValidos}%")