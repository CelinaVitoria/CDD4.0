repeticao = "s"
while repeticao == "s" or repeticao == "S":
    num = float(input("digite um número:"))
    if num > 0:
        print("positivo")
    else:
        print("negativo")
    repeticao = input("Deseja verificar outro número?(s/n)")
