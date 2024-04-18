nota1 = float(input("digite a nota1:"))
while nota1 < 0 or nota1 > 10:
    nota1 = float(input("digite a nota1 novamente:"))
nota2 = float(input("digite a nota2:"))
while nota2 < 0 or nota2 > 10:
    nota2 = float(input("digite a nota2 novamente:"))
media = (nota1 + nota2) /2
print(media)